import pandas as pd
from io import StringIO
import sqlalchemy

with open("D:\Spider\Customs Data\export rmb.csv", "rt") as inrmbfile, open(
        "D:\Spider\Customs Data\export us dollar.csv", "rt") as inusfile:
    reader_rmb = inrmbfile.read()
    reader_rmb_processed = reader_rmb.replace(chr(9), "")  # 替换文件中的chr(9)
    StringData = StringIO(reader_rmb_processed)
    df1 = pd.read_csv(StringData, sep=",")
    df1['人民币'] = df1['人民币'].str.replace(',', '')
    df1.drop(columns=['Unnamed: 14', '第二数量', '第二计量单位'], inplace=True)

    reader_us = inusfile.read()
    reader_us_processed = reader_us.replace(chr(9), "")  # 替换文件中的chr(9)
    StringData = StringIO(reader_us_processed)
    df2 = pd.read_csv(StringData, sep=",")
    df2['美元'] = df2['美元'].str.replace(',', '')
    df2.drop(columns=['Unnamed: 14', '第二数量', '第二计量单位'], inplace=True)

    import_df = pd.merge(df1, df2, how="left",
                         on=['数据年月', '商品编码', '商品名称', '贸易伙伴编码', '贸易伙伴名称', '贸易方式编码', '贸易方式名称', '注册地编码', '注册地名称', '第一数量',
                             '第一计量单位'])
    cols_to_use = df2.columns.difference(df1.columns)
    import_df.drop_duplicates(inplace=True)

    col_name = import_df.columns.tolist()
    col_name.insert(1, '进出口')
    # print(import_df)
    import_df = import_df.reindex(columns=col_name, fill_value="出口")

    engine = sqlalchemy.create_engine('mssql+pyodbc://12105042:Hpr.123@local_customs')
    import_df.to_sql(name='customs_data', con=engine, if_exists="append", index=False)

    engine.dispose()
    # import_df.to_csv(r"D:\Spider\Customs Data\export processed.csv", encoding="utf-8-sig")

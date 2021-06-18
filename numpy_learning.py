#!/usr/bin/python
# vim: set fileencoding:utf-8
# 用 NumPy 统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。然后把这些人的总成绩排序，得出名次进行成绩输出。
import numpy as np

studentType = np.dtype({'names': ['姓名', '语文', '英语', '数学', '总分'], 'formats': ['U32', 'i', 'i', 'i', 'i']})
# 'formats': ['S32', 'i', 'i', 'i'] 其中S只支持ascii, 这样在创建结构数组时就需要在中文后加上.encode(encoding='utf-8')
# 过于繁琐，不如直接使用U32来定义类型
students = np.array([("张飞", 66, 65, 30, 0),
                     ("关羽", 95, 85, 98, 0),
                     ("赵云", 93, 92, 96, 0),
                     ("黄忠", 90, 88, 77, 0),
                     ("典韦", 80, 90, 90, 0)],
                    dtype=studentType)

chinese = students[:]['语文']
english = students[:]['英语']
math = students[:]['数学']
students[:]['总分'] = students[:]['语文'] + students[:]['英语'] + students[:]['数学']


def show_line(subject, scores):
    print('%s\t%.2f\t%i\t%i\t%.2f\t%.2f' % (
        subject, np.mean(scores), np.min(scores), np.max(scores), np.var(scores), np.std(scores)))


print('学科\t平均成绩\t最小成绩\t最大成绩\t方差\t标准差')
show_line('语文', chinese)
show_line('英语', english)
show_line('数学', math)

print(np.sort(a=students, order='总分'))
# students.sort可以排序同时保存进数组
print(students)

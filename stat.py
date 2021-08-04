# -*- coding:utf-8 -*-
# @Project Name:SIMS
# @FileName          :stat.py
# @Create Date       :2021/8/4 21:34
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
"""
============================================================================
@Version:1.0.0
@Functions:
    1. deleting information from database
    2. Notes:
        Command line interface
        Calculate the total score of a student's grades in all subjects
        Use conditions to determine whether student information exists in the database
=============================================================================
"""
from search import search_by_id

stat_submenu = '''
    5 统计 ---|---0 返回
              |---1 计算某个学生所有科目成绩的总分
              |---2 计算所有学生的某一科目成绩的总分和平均分
              |---3 其它条件统计
'''


# 计算某个学生的所有科目成绩的总分
def scores_sum(db, sid):
    sum = 0
    # 判断学生信息是否存在数据库中
    if search_by_id(db, sid) == {}:
        print(' - %s does not exist.' % sid)
        sum = -1
    else:
        for i in db:
            if i['studentID'] == sid:
                sum = i['score_1'] + i['score_2'] + i['score_3']
    return sum


"""
object_sum
计算所有学生的某一科目成绩的总分和平均分
"""


def object_sum(db, object_n):
    avg = 0
    sum = 0
    total = len(db)
    for i in db:
        sum += float(i[object_n])
    avg = sum / total
    return sum, avg


def db_stat(db):
    new_db = db
    while True:
        print(stat_submenu)
        option = input('Enter your option:')
        if option == '0':
            break
        elif option == '1':
            sid = input(' >>Subject Name to be stated: ')
            new_db = scores_sum(db, sid.strip())
            print('- Calculation completely.')
            continue
        elif option == '2':
            object_n = input('    >>Student Name to be stated: ')
            new_db = object_sum(db, object_n.strip())
            print('- Calculation completely.')
            continue
        elif option == '3':
            print(' To be coded.')
        else:
            print(' Inputting WRONG!')
            continue

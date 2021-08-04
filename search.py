# -*- coding:utf-8 -*-
# @Project Name:SIMS
# @FileName          :search.py
# @Create Date       :2021/8/2 11:19
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com

"""
============================================================================
@Version:1.0.0
@Functions:
    1. Searching information from database
    2. Notes:
        Command line interface
=============================================================================
"""

search_submenu = '''
    1 查看 ---|--- 1 全部学生信息
              |--- 2 按学号查询
              |--- 3 按姓名查询
              |--- 4 其它条件查询
              |--- 0 返回
'''

"""
@search_by_id
通过关键字查询学生信息记录，主要关键字唯一，故所有记录不能重复
查出的结果唯一，函数返回该条记录record
@dict()字典函数 反应的是键值对的数据
"""


def search_by_id(db, id):
    record = dict()
    for i in db:
        if i['studentID'] == id:
            record = i
    return record


"""
@ search_by_name()函数，通过关键字姓名查询学生信息记录
存在姓名不唯一，返回集合类型的查询结果集
@append（）函数
append函数会在数组后加上相应的元素，数据结构类型由叔祖变为列表
"""


def search_by_name(db, name):
    records = list()
    for i in db:
        if i['name'] == name:
            records.append(i)
    return records


"""
@show_all()
查询所有的记录并显现出来，返回结果集
@%d
指定占位符
@\t
水平制表(HT) （跳到下一个TAB位置
"""


def show_all(data):
    total = len(data)
    print('=================================================================================')
    print('               There are %d records in the database ' % total)
    print('=================================================================================')
    print('No.\tID\tName\tEmail\t\t\tPhone\tScore1\tScore2\tScore3')
    for i in range(total):
        print('------------------------------------------------------------------------------')
        print('%d\t%s\t%s\t%s\t%4.1f\t%4.1f' % (i + 1, data[i]['studentID'], data[i]['name'],
                                                data[i]['email'], data[i]['phone'],
                                                float(data[i]['score_1']),
                                                float(data[i]['score_2']),
                                                float(data[i]['score_3'])))
    print('----------------------------------------------------------------------------------')


"""
@ show_results()
显示查询出的结果集
"""


def show_results(records):
    number = len(records)
    print('==================================================================================')
    print('                        Searched %d result records in the database ' % number)
    print('==================================================================================')
    print('No.\tID\tName\tEmail\t\t\tPhone\tScore1\tScore2\tScore3')
    for i in range(number):
        print('---------------------------------------')
        print('%d\t%s\t%s\t%s\t%4.1f\t%4.1f' % (i + 1, records[i]['studentID'], records[i]['name'],
                                                records[i]['email'], records[i]['phone'],
                                                float(records[i]['score_1']),
                                                float(records[i]['score_2']),
                                                float(records[i]['score_3'])))
    print('-----------------------------------------------------------------------------------')


"""
@db_search()
查询子功能的主循环程序
@strip()
用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
"""


def db_search(db):
    while True:
        print(search_submenu)
        option = input('> Enter your option:')
        if option == '0':
            break
        elif option == '1':
            show_all(db)
            continue
        elif option == '2':
            sid = input(' > Student ID:')
            record = search_by_id(db, sid.strip())
            if record != {}:
                records = [record]
                show_results(records)
            else:
                print(' -There are no results!')
                show_results([])
            continue
        elif option == '3':
            name = input('> Name:')
            records = search_by_name(db, name.strip())
            show_results(records)
            continue
        elif option == '4':
            print('- To be coded.')
        else:
            print('- Inputting WRONG.')
            continue
        return

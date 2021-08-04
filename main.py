# -*- coding:utf-8 -*-
# @Project Name:SIMS
# @FileName          :main.py
# @Create Date       :2021/8/1 17:15
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
"""
@Functions:
    1.Main user interface
    2.Notes:
        Command line interface
"""

from pathlib import Path
from db import load_db, dump_db
from append import db_append
from update import db_update
from delete import db_delete
from stat import db_stat
from search import db_search

main_menu = '''

=====================================================
      Student Information Management System
                 
                 Version 1.0
                 
======================================================

    1 查看学生信息
    2 增加学生信息
    3 修改学生信息
    4 删除学生信息
    5 统计
    0 退出
    
'''

student_DB = list()
db_file = 'student.text'
if Path(db_file).exists():
    student_DB = load_db(db_file)
else:
    # header={'number':None,'studentID':None,'name':None,
    # 'dorm':None,'email':None,'score_1':0'score_2':0,'score_3':0}
    # student_DB.append(header)
    dump_db(student_DB, db_file)

while True:
    print(main_menu)
    option = input('\nEnter your option:')
    if option.isdigit():
        choose = int(option)
    else:
        print('Warning,Please Enter a DIGIT!')
        continue
    if choose == 1:
        db_search(student_DB)
        continue
    elif choose == 2:
        student_DB = db_append(student_DB)
        continue
    elif choose == 3:
        student_DB = db_update(student_DB)
        continue
    elif choose == 4:
        student_DB = db_delete(student_DB)
        continue
    elif choose == 5:
        db_stat(student_DB)
        continue
    elif choose == 0:
        break
    else:
        print('Inputting WRONG!')
        continue

dump_db(student_DB, db_file)
# 把对数据库做的修改持久化，保存到磁盘中
print('\nEnd,Welcome again.\n\n')

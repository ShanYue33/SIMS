# -*- coding:utf-8 -*-
# @Project Name:SIMS
# @FileName          :update.py
# @Create Date       :2021/8/4 17:24
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com
"""
============================================================================
@Version:1.0.0
@Functions:
    1. Updating information from database
    2. Notes:
        Command line interface
        Prompt to enter the keyword of the record to be modified,
        Then find this record and modify it
=============================================================================
"""
from search import search_by_id

update_submenu = '''
    3 修改 ---|---0 退出
              |---1 通过输入要修改的记录关键词进行修改
              |---2 其它条件修改
'''


def change_record(db, record):
    # can not change keywords
    new_db = db
    old_record = search_by_id(db, record['studentID'])
    new_db.remove(old_record)
    new_db.append(record)
    return new_db


def db_update(db):
    new_db = db
    while True:
        print(update_submenu)
        option = input(' >Enter your option:')
        if option == '0':
            break
        elif option == '1':
            name = input('    >>Name:')
            stid = input('    >>StudentID:')
            record = search_by_id(db, stid)
            if len(record) != 0:
                print(' ', record)
            else:
                print(' - StudentID is WRONG.')
                continue
            revise = input('  >What do you want update(filedName=value):')
            filed_name, value = revise.strip().split('=')
            if filed_name == 'studentID':
                print(filed_name, value)
                record[filed_name] = value
                new_db = change_record(db, record)
                print(' - Updated already.')
                continue
            elif option == '2':
                print(' To be coded.')
                continue
    return new_db

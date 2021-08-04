# -*- coding:utf-8 -*-
# @Project Name:SIMS
# @FileName          :delete.py
# @Create Date       :2021/8/4 21:14
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
        Pass the original database as a parameter
        Return to the modified database
=============================================================================
"""
delete_submenu = '''
    4 删除 ---|---0 退出
              |---1 按照学号进行删除
              |---2 其它条件删除
'''


def delete_by_id(db, sid):
    for i in db:
        if i['studentID'] == sid:
            db.remove(i)
        return db


def db_delete(db):
    new_db = db
    while True:
        print(delete_submenu)
        option = input(' Enter your option:')
        if option == '0':
            break
        elif option == '1':
            sid = input(' >>Student ID to be deleted:')
            new_db = delete_by_id(db, sid.strip())
            print(' - Deleted OK.')
            continue
        elif option == '2':
            print(' - To be coded.')
            continue
        else:
            print(' - Inputting WRONG!')
            continue
    return new_db

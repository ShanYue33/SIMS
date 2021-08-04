# -*- coding:utf-8 -*-
# @Project Name:SIMS
# @FileName          :db.py
# @Create Date       :2021/8/2 10:33
# @Update Date       :————/——/——
# @Author            :姗
# @Software          :PyCharm
# @e-mail            :3215873382@qq.com

"""
==========================================================================
@Version :1.0.0
@Functions:
    1. load and dump db data file with pickle
    2. Notes:
        the first line is table header
        each record is one line
===========================================================================
"""
import pickle as p


def load_db(data_file):
    db = list()
    with open(data_file, 'rb') as data:
        db = p.load(data)
    return db


def dump_db(db, data_file):
    with open(data_file, 'wb')as file:
        p.dump(db, file)


if __name__ == '__main__':
    file_name = 'test.data'
    data = [{'一': 1}, {'二': 2}, {'三': 3}, {None}]
    with open(file_name, 'wb') as f:
        p.dump(data, f)
    print('dump ok')

    with open(file_name, 'rb') as f:
        data = p.load(f)
        print(data)
    print('load ok')

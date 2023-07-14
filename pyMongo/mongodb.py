# -*- coding: utf-8 -*-
# @date：2023/7/14 9:32
# @Author：LiuYiJie
# @file： mongodb
import pymongo
from typing import Union


class MongoDb:
    def __init__(self, db: str = None, coll: str = None):
        self._client = pymongo.MongoClient()
        self._db = self._client.get_database(db)
        self._coll = self._db.get_collection(coll)

    # 增加
    def in_data(self, data: Union[dict, list] = None):
        self._coll.insert_many(data)

    # 删除
    def re_data(self, data: dict = None, multi: bool = False):
        pass

    # 查询
    def find_data(self, data):
        pass

    # 更新
    def up_data(self, data):
        self._coll.update_many({'name': 'jiyu'}, {'$set':{'name': 'nianhua'}})
        # pass


if __name__ == '__main__':
    c = MongoDb(db="school_roster", coll='test')
    datas = [
    {'name':'jiyu','num':12},
    {'name':'jiyu','num':34},
    {'name':'nianhua','num':12},
    {'name':'nianhua','num':34},
]
    # c.in_data(datas)
    c.up_data(datas)
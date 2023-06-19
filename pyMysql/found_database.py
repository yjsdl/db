# -*- coding: utf-8 -*-
# @date：2023/6/19 15:08
# @Author：LiuYiJie
# @file： found_database
import MySQLdb


class MysqlDb:
    def __init__(self, host: str = None, port: int = None, user: str = None, password: str = None, db: str = None):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._db = db
        if db:
            self._conn, self._cur = self.conn_db()
        else:
            self._conn, self._cur = self.fou_date(db)

    def conn_db(self):
        conn = MySQLdb.connect(host=self._host, port=self._port, user=self._user, password=self._password,
                               db=self._db)
        cur = conn.cursor()
        return conn, cur

    # 创建数据库
    def fou_date(self, name):
        conn = MySQLdb.connect(host=self._host, port=self._port, user=self._user, password=self._password)
        cur = conn.cursor()
        sql = "create database " + name + " character set utf8"
        cur.execute(sql)
        return conn, cur

    def cr_table(self, sql):
        self._cur.execute(sql)
        self.stop()

    def in_oneData(self, sql):
        try:
            self._cur.execute(sql)
            self._conn.commit()
        except:
            # 出现错误回滚
            self._conn.rollback()

    # def in_moDate(self, sql):
    #     try:
    #         self

    def stop(self):
        self._cur.close()
        self._conn.close()


if __name__ == '__main__':
    c = MysqlDb(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='foutest'
    )
    # c.cr_table(
    #     "create table student(id int primary key auto_increment, name varchar(30) not null, age varchar(10), sex enum('w', 'm'));")

    c.in_oneData("insert into student(id, name, age, sex) values (5, 'test', '18', 'm');")
    c.in_oneData("insert into student(id, name, age, sex) values (6, 'sb', '20', 'w');")
    c.stop()
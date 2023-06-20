# -*- coding: utf-8 -*-
# @date：2023/6/19 15:08
# @Author：LiuYiJie
# @file： found_database
import MySQLdb
from logger_code.stream_handler import log

logger = log()


class MysqlDb:
    insert_num = 0
    update_num = 0

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

    def cre_table(self, sql):
        self._cur.execute(sql)
        self.stop()

    def in_oneData(self, sql):
        try:
            self._cur.execute(sql)
            self._conn.commit()
            self.insert_num += 1
        except:
            # 出现错误回滚
            self._conn.rollback()

    def in_moDate(self, sql, data):
        try:
            self._cur.executemany(sql, data)
            self._conn.commit()
            self.insert_num += len(data)
        except:
            self._conn.rollback()

    def sea_Date(self, sql):
        res_num = self._cur.execute(sql)
        logger.info(f'本次共 | 查询到：{res_num:^4}条数据')
        res = self._cur.fetchall()
        return res

    def up_Date(self, sql):
        try:
            self._cur.execute(sql)
            self._conn.commit()
        except:
            self._conn.rollback()

    def drop_Date(self, sql):
        try:
            self._cur.execute(sql)
            self._conn.commit()
        except:
            self._conn.rollback()

    def stop(self):
        self._cur.close()
        logger.info(f'本次操作数据库共 | 新增：{self.insert_num:^4}条 | 更新： {self.update_num:^4}条')
        self._conn.close()


if __name__ == '__main__':
    c = MysqlDb(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='foutest'
    )
    # c.cre_table(
    #     "create table student(id int primary key auto_increment, name varchar(30) not null, age varchar(10), sex enum('w', 'm'));")
    datas = [
        (11, 'zhangsan', '18', 'm'),
        (12, 'lisi', '22', 'w'),
        (13, 'wangwu', '24', 'w'),
    ]

    # c.in_oneData("insert into student(id, name, age, sex) values (9, 'test', '18', 'm');")
    # c.in_oneData("insert into student(id, name, age, sex) values (10, 'sb', '20', 'w');")
    # c.in_moDate("insert into student(id, name, age, sex) values (%s, %s, %s, %s);", data)
    rs = c.sea_Date("select * from student where age=18;")
    # c.up_Date("update student set name= 'lishi' where name='zhangsan'")
    c.drop_Date('delete from student where id=10')
    c.stop()

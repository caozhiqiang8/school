import pymysql

#数据库链接
#(self,sql,host='gw4.bj.etiantian.net', port=12262, user='schu', passwd='test', db='school', charset='utf8'):
#(self,sql,host='localhost', port=3306, user='root', passwd='qiang520', db='school', charset='utf8'):

class MysqlDB(object):
    def __init__(self,sql,
                 host='123.103.75.152', 
                 port=3306, 
                 user='schu', 
                 passwd='slavep', 
                 db='oracle2utf', 
                 charset='utf8',
                 cursorclass=pymysql.cursors.DictCursor):
        self.sql = sql
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.cursorclass = cursorclass
    def connectdb(self):
        conn = pymysql.connect(host = self.host,
                               port = self.port,
                               user = self.user,
                               passwd = self.passwd,
                               db = self.db,
                               charset = self.charset,
                               cursorclass = self.cursorclass)
        cur = conn.cursor()
        cur.execute(self.sql)
        res = cur.fetchall()
        cur.close
        conn.close
        return res
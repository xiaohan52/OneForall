import pymysql

# 打开数据库连接，参数1.主机名或IP2.用户名3.密码4.数据库名称
db=pymysql.connect('localhost','root','hlx121314','pythondata')
# 使用cursor()方法创建一个游标对象 cursor     可以通过这个对象进行数据库的操作
try:
    cursor = db.cursor()
    cursor.execute('select * from s')
    result=cursor.fetchall()
    for item in result:
        print('姓名:{} 年龄:{}'.format(item[1],item[2]))
        pass
except Exception as f:
    print(f)
finally:
    cursor.close()
    db.close()
# # 使用execute()方法执行SQL查询
# cursor.execute('SELECT VERSION()')
# # 使用 fetchone() 方法获取单条数据
# data=cursor.fetchone()
# print('Database version:%s'%data)

# 使用execute()方法执行SQL，如果表存在，则删除
# cursor.execute('DROP TABLE IF EXISTS books')

# 使用预处理语句创建表
sql='''
    CREATE TABLE books(
    id int(8) NOT NULL AUTO_INCREMENT,
    name  VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price decimal(10,2) DEFAULT NULL,
    publish_time data DEFAULT NULL,
    PRIMARY KEY (id)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
'''
# 执行SQL语句
cursor.execute(sql)
db.commit()
# 关闭数据库
db.close()
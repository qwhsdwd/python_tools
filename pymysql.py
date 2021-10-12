import pymysql
import datetime
import time

start=time.time()

host='localhost'
username='root'
password='99U6UkAbe4akuRjM'
db_name='mysql_shiyanlou'

create_table_sql="""
CREATE TABLE fuck(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(255) UNIQUE,
nickname VARCHAR(255) NOT NULL,
birthday DATE )
"""
insert_table_sql="""
INSERT INTO fuck(username,nickname,birthday)
VALUES('{username}','{nickname}','{birthday}')
"""
query_table_sql="""
SELECT id,username,nickname,birthday
FROM fuck
"""
delete_table_sql="""
DELETE FROM fuck
"""
drop_table_sql="""
DROP TABLE fuck
"""

connection=pymysql.connect(host=host,
                           user=username,
                           password=password,
                           db=db_name)

try:
    with connection.cursor() as cursor:
        print('--------------新建表--------------')
        cursor.execute(create_table_sql)
        connection.commit()

        print('--------------插入数据--------------')
        cursor.execute(
            insert_table_sql.format(username='yitian', nickname='易天', birthday=datetime.date.today()))
        cursor.execute(
            insert_table_sql.format(username='zhang3', nickname='张三', birthday=datetime.date.today()))
        cursor.execute(
            insert_table_sql.format(username='li4', nickname='李四', birthday=datetime.date.today()))
        cursor.execute(
            insert_table_sql.format(username='wang5', nickname='王五', birthday=datetime.date.today()))
        connection.commit()

        print('--------------查询数据--------------')
        cursor.execute(query_table_sql)
        results = cursor.fetchall()
        print(f'id\tname\tnickname\tbirthday')
        for row in results:
            print(row[0], row[1], row[2], row[3], sep='\t')

        print('--------------清除数据--------------')
        cursor.execute(delete_table_sql)
        connection.commit()

        print('--------------删除表--------------')
        cursor.execute(drop_table_sql)
        connection.commit()
finally:
    connection.close()

print("共耗时 %.3f"%(time.time()-start))

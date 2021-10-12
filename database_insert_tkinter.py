from tkinter import *
import pymysql
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

host = 'www.zaihansheng.com'
username = 'root'
password = '99U6UkAbe4akuRjM'
db_name = 'nike_shoes'

insert_table_sql = """
INSERT INTO article_number_shoes(shoes_ArtNo)
VALUES('{shoes_ArtNo}')
"""

query_table_sql="""
SELECT shoes_ArtNo
FROM article_number_shoes
"""

delete_table_sql="""
DELETE FROM article_number_shoes WHERE shoes_ArtNo='{shoes_ArtNo}'
"""


try:
    connection=pymysql.connect(host=host,
                               user=username,
                               password=password,
                               db=db_name)
except Exception as e:
    pass


def itemAdded():
    varAdd=entry.get()
    if (len(varAdd.strip())==0):
        return

    lb.insert(END,varAdd)
    insert_database_var(varAdd)
    entry.delete(0,END)
    send_mail("对添加鞋货号程序进行添加操作","添加了 {}".format(varAdd))

def itemDeleted():

    index=lb.curselection()
    if(len(index)==0):
        return

    lb.delete(index)
    send_mail("对添加鞋货号程序进行删除操作","删除了 {}".format(get_database_var()[index[0]]))
    delete_database_var(get_database_var()[index[0]])

def get_database_var():

    with connection.cursor() as cursor:

        cursor.execute(query_table_sql)
        results = cursor.fetchall()
        L=[]
        for i in range(len(results)):
            L.append((results)[i][0])

    return L

def insert_database_var(data):

    with connection.cursor() as cursor:
        cursor.execute(insert_table_sql.format(shoes_ArtNo=data))
        connection.commit()


def delete_database_var(data):

    with connection.cursor() as cursor:
        cursor.execute(delete_table_sql.format(shoes_ArtNo=data))
        connection.commit()

def send_mail(subject,content):

    host_server = "smtp.quweihao.com"
    user = "qwh@quweihao.com"
    password = "xf@9Ficdg8yGv"

    qwh = SMTP_SSL(host_server)
    # 此处替换成自己的 qq 邮箱账户和授权码
    qwh.login(user=user, password=password)

    text = content

    msg = MIMEText(text)

    # 添加相应的字段值，需修改为自己的对应邮箱
    msg['From'] = user
    msg['To'] = "841094870@qq.com"
    msg['Subject'] = subject

    # 在发送邮件时，发送的应该是字符串，所以，此处使用 ,记得修改相应的地址
    qwh.sendmail(from_addr=user, to_addrs=["841094870@qq.com"], msg=msg.as_string())


if __name__ == '__main__':

    shoes_ArtNo=get_database_var()
    root=Tk()
    root.title("添加鞋货号程序")

    entry=Entry(root)
    entry.grid(row=0,column=0,padx=5,pady=5)

    btnAdd=Button(root,text="增加",width=10,command=itemAdded)
    btnAdd.grid(row=0,column=1,padx=5,pady=5)

    lb=Listbox(root)
    for l in shoes_ArtNo:
        lb.insert(END,l)
    lb.grid(row=1,column=0,columnspan=2,padx=5,sticky=W)

    btnDel=Button(root,text="删除",width=10,command=itemDeleted)
    btnDel.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    send_mail("打开鞋货号添加程序","打开鞋货号添加程序")
    root.mainloop()
    connection.close()


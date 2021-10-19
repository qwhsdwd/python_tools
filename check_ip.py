import datetime
import os
import re
import socket
import threading
import time
from queue import Queue

on_line_num = 0
not_on_line_num = 0


def is_open(IP_QUEUE, port):
    while not IP_QUEUE.empty():
        ip = IP_QUEUE.get().strip('n')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.settimeout(10)
            s.connect((ip, int(port)))
            today = datetime.datetime.now().strftime("%Y - %m - %d %H : %M : %S")
            print(ip)

        except Exception as e:
            pass


def linux_commad(command):
    res = os.popen(command)
    return res


# 将需要ping 连接的IP加入队列


def IP_list():
    ip_list = Queue()
    for i in range(1, 256):
        # ip = '172.16.101.' + str(i)
        ip = '182.172.162.' + str(i)
        ip_list.put(ip)
    return ip_list


# 定义 ping 函数
def ping_IP(IP_QUEUE):
    global on_line_num, not_on_line_num
    while not IP_QUEUE.empty():
        ip = IP_QUEUE.get().strip('n')
        line = linux_commad("ping -W 600 -c 1 {}".format(ip)).read()
        searchObj = re.search(r'(\d) packets transmitted, (\d) packets received, (\d+).0% packet loss', line,
                              re.M | re.I)
        if searchObj.group(2) != "1":
            res = "目标网络存活"
            on_line_num += 1
        else:
            res = "目标网络未存活"
            not_on_line_num += 1
        today = datetime.datetime.now().strftime("%Y - %m - %d %H : %M : %S")
        logging.info("%s IP = %s %s" % (today, ip, res))


def main():
    global on_line_num, not_on_line_num
    IP_LIST = IP_list()
    threads = []
    THREAD_NUM = 50
    IP_L = IP_LIST
    for i in range(THREAD_NUM):
        t = threading.Thread(target=is_open, args=(IP_L, "22",))
        threads.append(t)
    for i in range(THREAD_NUM):
        threads[i].start()
    for i in range(THREAD_NUM):
        threads[i].join()


if __name__ == '__main__':
    start = time.time()
    main()
    print("共用时" + str(time.time() - start)[:5])

# $language = "Python"
# $interface = "1.0"

import os
import csv
import time
import datetime

username_1 = 'support'
password_1 = 'Cisco@456'

username_2 = '4awangguan'
password_2 = 'Zhaoxin98$^'

number_base = ['202', '227', '250', '213', '229', '212', '245', '228', '194', '225', '230', '231', '247', '211', '243',
               '236', '244', '234', '223', '235', '246', '249', '210', '252', '251', '201', '248'] # "224", "29", "207", "208"

def Username(username):

    check_username = crt.Screen.WaitForString('Username:', 1)
    print_username = crt.Screen.Send(username + '\r')

    return check_username, print_username

def Password(password):

    check_password = crt.Screen.WaitForString('Password:', 1)
    print_password = crt.Screen.Send(password + '\r')

    return check_password, print_password

def loop(new):

    if new in number_base:

        crt.Screen.Send('telnet ' + '218.206.118.' + new + ' /so lo0' + ' \r')

    else:

        crt.Dialog.MessageBox('请输入正确的IP地址！', 'ERROR', 16 | 0)

        host_NEW = crt.Dialog.Prompt("输入IP地址最后一位：", "IP Address", '', False)

        crt.Screen.Send('telnet ' + '218.206.118.' + host_NEW + ' /so lo0' + ' \r')

def HostLog():

    host = crt.Dialog.Prompt('输入IP地址最后一位：', 'IP Address', '', False)

    while host == '':

        crt.Dialog.MessageBox('请输入正确的IP地址！', 'ERROR', 16 | 0)

        host_new = crt.Dialog.Prompt("输入IP地址最后一位：", "IP Address", '', False)

        if host_new != '':
            loop(host_new)

    else:

        loop(host)

def getValue(row_num, row1, row2):

    crt.Screen.WaitForString('>')

    screenrow = crt.Screen.CurrentRow - row_num
    result = crt.Screen.Get(screenrow, row1, screenrow, row2)

    return result

def getFirstCsv(): #################### 按顺序循环num_base！！！！！！！！ ##################

    crt.Screen.Synchronous = True

    ###### 提值 IP地址+对应数据
    result_first = getValue(9, 8, 22)  ##对应数据位置
    result_second = getValue(2, 42, 44)

    f = open('IMS.csv', 'wb')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["IP地址", "IMS使用率", "时间"])
    csv_writer.writerow([result_first, result_second])
    f.close()

    crt.Screen.Synchronous = False

def mainFunction(host_name):

    date = time.strftime("%Y/%m/%d %H:%M:%S")

    crt.Screen.WaitForString("#")
    crt.Screen.Send('telnet ' + '218.206.118.' + host_name + ' /so lo0' + ' \r')

    Username(username_2)
    Password(password_2)

    crt.Screen.Send('display ip-pool pool-usage domain ims_dhcp ' + ' \r')

    crt.Screen.Synchronous = True
    # crt.Screen.Send("date\r")

    ###### 提值 IP地址+对应数据
    result_first = getValue(9, 8, 22)  ##对应数据位置
    result_second = getValue(2, 42, 44)

    f = open('IMS_1.csv', 'a+')
    csv_writer = csv.writer(f)
    csv_writer.writerow([result_first, result_second, date])
    f.close()

    crt.Screen.Synchronous = False

    crt.Screen.WaitForString(">", 1)
    crt.Screen.Send('q' + ' \r')

def main():

    Username(username_1)
    Password(password_1)

    #date = datetime.strftime("%Y%m%d")

    #HostLog()   ########## crt.Screen.Send('telnet ' + '218.206.118.' + host_NEW + ' /so lo0' + ' \r') #########

    #f = open('IMS.csv', 'wb')
    #csv_writer = csv.writer(f)
    #csv_writer.writerow(["IP地址", "IMS使用率", "时间"])
    #f.close()

    #for host_name in [number_base[i:i + n] for i in range(0, len(number_base), n)]:

    for host_name in number_base:

        mainFunction(host_name)

main()
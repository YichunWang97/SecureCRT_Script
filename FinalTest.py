# $language = "Python"
# $interface = "1.0"

import os
import csv
import time
import datetime

###用户名1，用户密码1###（登陆218.206.118.17 support）
username_1 = 'support'
password_1 = 'Cisco@456'

###网关用户名以及用户密码###
username_2 = '4awangguan'
password_2 = 'Zhaoxin98$^'

###每台BRAS对应的IP地址最后一位###（数据集，可手动添加）
number_base = [202, 227, 250, 213, 229, 212, 245, 228, 194, 225, 230, 231, 247, 211, 243, 236, 244, 234, 223, 235, 224, 246, 249, 210, 252, 251, 201, 29, 248, 207, 208]

###用户名登陆代码###
def Username(username):

    check_username = crt.Screen.WaitForString('Username:', 1)
    print_username = crt.Screen.Send(username + '\r')

    return check_username, print_username

###用户密码登陆代码###
def Password(password):

    check_password = crt.Screen.WaitForString('Password:', 1)
    print_password = crt.Screen.Send(password + '\r')

    return check_password, print_password

###此处添加各种BRAS执行功能代码，需要设定指定的关键词###
def function():

    ###功能选择提示###
    choice = crt.Dialog.Prompt('请输入功能', 'CHOOSE', '', False)

    if choice == 'gig':
        post_1 = crt.Dialog.Prompt('输入端口1：', '端口', '1', False)
        post_2 = crt.Dialog.Prompt('输入端口2：', '端口', '1', False)
        post_3 = crt.Dialog.Prompt('输入端口3：', '端口', '1', False)

        crt.Screen.Send('display interface GigabitEthernet ' + post_1 + '/' + post_2 + '/' + post_3 + ' \r')

        ###抵消---More---###
        crt.Screen.Send(' ')

    if choice == 'ims':
        crt.Screen.Send('display ip-pool pool-usage domain ims_dhcp ' + ' \r')

    if choice == 'cms':
        crt.Screen.Send('display ip-pool pool-usage domain cms ' + ' \r')

    ###如果选择取消功能输入，自动跳出###
    if choice == '':
        crt.Screen.Send('\t')

def main():

    host = crt.Dialog.Prompt('输入IP地址最后一位：', 'IP Address', '', False)

    ###输入IP地址由文字string格式转换为数字int格式###
    host_number = int(host)

    ###如果输入的IP存在于设定好的IP数据集中，运行BRAS，否则提示错误重新输入IP地址###
    if host_number in number_base:

        crt.Screen.Send('telnet ' + '218.206.118.' + host + ' /so lo0' + ' \r')

    else:

        crt.Dialog.MessageBox('请输入正确的IP地址！', 'ERROR', 16 | 0)

        host_NEW = crt.Dialog.Prompt("输入IP地址最后一位：", "IP Address", '', False)

        crt.Screen.Send('telnet ' + '218.206.118.' + host_NEW + ' /so lo0' + ' \r')

    Username(username_2)
    Password(password_2)

    function()

    ###当识别到符号>的时候，循环运行如下功能###
    while crt.Screen.WaitForString(">"):

        choice = crt.Dialog.MessageBox("是否继续执行其他功能", 'CONTINUE', 64 | 4)

        ###6和7分别代表message box对应的是和否输出值，当选择是或者否的时候运行不同的代码功能###
        if choice == 6:

            ###如果选择继续执行其他功能，循环一次主功能代码###
            function()

        if choice == 7:

            ###如果不执行其他功能，先询问是否更换至其他BRAS###
            choose = crt.Dialog.MessageBox("是否需要更换至其他BRAS", "CHOOSE", 64 | 4)

            ###选择是的话，先跳出当前BRAS，然后整体大循环一次完整代码（main从头开始）###
            if choose == 6:

                crt.Screen.Send('q' + '\r')

                main()

            ###不更换至其他BRAS，则询问是否退出CRT，选择否就会保留在当前BRAS并跳出脚本，选择是则完整退出所有CRT程序###
            if choose == 7:

                crt.Quit()

    #while crt.Screen.WaitForKey(10):

        #function()

    #else:

        #crt.Screen.Send('q' + '\r')

main()
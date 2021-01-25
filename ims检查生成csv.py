# $language = "Python"
# $interface = "1.0"

import os
import csv
import time
import datetime

# First Username and Password
username_1 = 'support'
password_1 = 'Cisco@456'

# The username and password needed for the second permission
username_2 = '4awangguan'
password_2 = 'Zhaoxin98$^'

# Number base with available IP addresses (the last number of the whole address)
number_base = ['202', '227', '250', '213', '229', '212', '245', '228', '194', '225', '230', '247', '211', '243',
               '236', '244', '234', '223', '235', '246', '249', '210', '252', '251', '201', '248', "224", "29", "207",
               "208", "231"] # "224", "29", "207", "208"，"231"

def Username(username):

    check_username = crt.Screen.WaitForString('Username:', 1) ### Wait for key word Username
    print_username = crt.Screen.Send(username + '\r') ### Send username after key word username

    return check_username, print_username

def Password(password):

    check_password = crt.Screen.WaitForString('Password:', 1) ### Wait for key word Password
    print_password = crt.Screen.Send(password + '\r') ### Send password after key word password

    return check_password, print_password

# Loop check the IP address
def loop(new):

    # Check wither the IP address is in the number base
    if new in number_base:

        # If in the base, print out the IP address and go directly to the telnet and then give a check
        crt.Screen.Send('telnet ' + '218.206.118.' + new + ' /so lo0' + ' \r')

    else:

        # Retype the IP address if the system gets a wrong Ip address (Not in the number base)
        crt.Dialog.MessageBox('请输入正确的IP地址！', 'ERROR', 16 | 0)

        # False => Show the word on the screen visiable
        host_NEW = crt.Dialog.Prompt("输入IP地址最后一位：", "IP Address", '', False)

        crt.Screen.Send('telnet ' + '218.206.118.' + host_NEW + ' /so lo0' + ' \r')

def HostLog():

    host = crt.Dialog.Prompt('输入IP地址最后一位：', 'IP Address', '', False)

    # If no IP address was typed in or clicked on the 'Cancel' button
    while host == '':

        crt.Dialog.MessageBox('请输入正确的IP地址！', 'ERROR', 16 | 0) # Warning message box

        host_new = crt.Dialog.Prompt("输入IP地址最后一位：", "IP Address", '', False) # The new address number typed in

        # If the system has received the IP address
        if host_new != '':

            # Check the newest IP number
            loop(host_new)

    else:

        loop(host)

# Get the value needed
def getValue(row_num, row1, row2):

    # Wait for the key string
    crt.Screen.WaitForString('>')

    # The key value usually above the current row
    screenrow = crt.Screen.CurrentRow - row_num
    # Get the value's location and get it by the row and column number
    result = crt.Screen.Get(screenrow, row1, screenrow, row2)

    return result

# Create a new csv file for saving the final data
def getFirstCsv():

    # Show the running processes on the CRT at the same time
    crt.Screen.Synchronous = True

    # Get the value
    result_first = getValue(9, 8, 22)
    result_second = getValue(2, 42, 44)

    # Create a csv file and write the first line in it
    f = open('IMS.csv', 'wb+')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["IP地址", "IMS使用率", "时间"])
    #csv_writer.writerow([result_first, result_second])
    f.close()

    # Turn off the Synchronous
    crt.Screen.Synchronous = False

def mainFunction(host_name):

    # Date time (yyyy/mm/dd hh:mm:ss)
    date = time.strftime("%Y/%m/%d %H:%M:%S")

    # Wait for the key word and type the telnet code
    crt.Screen.WaitForString("#")
    crt.Screen.Send('telnet ' + '218.206.118.' + host_name + ' /so lo0' + ' \r')

    # Type in the username and password for the permission
    Username(username_2)
    Password(password_2)

    # Main function -> The key code for searching the result we need (Can changed to check CMS or something else)
    crt.Screen.Send('display ip-pool pool-usage domain ims_dhcp ' + ' \r')

    crt.Screen.Synchronous = True
    # crt.Screen.Send("date\r")

    result_first = getValue(9, 8, 22)
    result_second = getValue(2, 42, 44)

    # Add value on the csv file
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

    # For the value in the number base, loop them in the main and get the whole result in the csv file automatically
    for host_name in number_base:

        mainFunction(host_name)

main()
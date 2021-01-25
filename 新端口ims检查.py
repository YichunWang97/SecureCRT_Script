# $language = "Python"
# $interface = "1.0"

username_2 = 'guankong'
password_2 = 'LygYD123#@!'

def main():

    crt.Screen.Send('q' + ' \r')

    host = crt.Dialog.Prompt('输入IP地址最后一位：', 'IP Address', '', False)

    if host == '':
        crt.Dialog.MessageBox('请输入IP地址！', 'ERROR', 16|0)

        host_new = crt.Dialog.Prompt("输入IP地址最后一位：", "IP Address", '', False)

        crt.Screen.Send('telnet ' + '218.206.118.' + host_new + ' /so lo0' + ' \r')

    else:
        crt.Screen.Send('telnet ' + '218.206.118.' + host + ' /so lo0' + ' \r')

    username_two = crt.Dialog.Prompt('输入用户名：', '用户', username_2, False)

    if username_two == '':
        crt.Dialog.MessageBox('请输入用户名！', 'ERROR', 16|0)

        username_new = crt.Dialog.Prompt("输入用户名：", "用户", '', False)

        crt.Screen.Send(username_new + '\r')

    else:
        crt.Screen.Send(username_two + '\r')

    password_two = crt.Dialog.Prompt('输入密码： ', '密码', password_2, False)

    if password_two == '':
        crt.Dialog.MessageBox('请输入密码！', 'ERROR', 16|0)

        password_new = crt.Dialog.Prompt("输入密码：", "密码", '', False)

        crt.Screen.Send(password_new + '\r')

    else:
        crt.Screen.Send(password_two + '\r')

    crt.Screen.Send('display ip-pool pool-usage domain ims_dhcp ' + ' \r')

main()
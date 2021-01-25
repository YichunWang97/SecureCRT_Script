# $language = "Python"
# $interface = "1.0"

username_1 = 'support'
password_1 = 'Cisco@456'

username_2 = 'guankong'
password_2 = 'LygYD123#@!'

number_base = [202, 227, 250, 213, 229, 212, 245, 228, 194, 225, 230, 231, 247, 211, 243, 236,
               244, 234, 223, 235, 224, 246, 249, 210, 252, 251, 201, 29, 248, 207, 208]

def main():
    username_one = crt.Dialog.Prompt('输入用户名： ', '用户', username_1, False)

    if username_one == '':
        crt.Dialog.MessageBox('请输入用户名！', 'ERROR', 16|0)

        username_new_one = crt.Dialog.Prompt("输入用户名：", "用户", '', False)

        crt.Screen.Send(username_new_one + '\r')

    else:
        crt.Screen.Send(username_one + '\r')

    password_one = crt.Dialog.Prompt('输入密码： ', '密码', password_1, False)

    if password_one == '':
        crt.Dialog.MessageBox('请输入密码！', 'ERROR', 16 | 0)

        password_new_one = crt.Dialog.Prompt("输入密码：", "密码", '', False)

        crt.Screen.Send(password_new_one + '\r')

    else:
        crt.Screen.Send(password_one + '\r')

    host = crt.Dialog.Prompt('输入IP地址最后一位：', 'IP Address', '', False)

    if host == '':
        crt.Dialog.MessageBox('请输入IP地址！', 'ERROR', 16 | 0)

        host_new = crt.Dialog.Prompt("输入IP地址最后一位：", "IP Address", '', False)

        crt.Screen.Send('telnet ' + '218.206.118.' + host_new + ' /so lo0' + ' \r')

    if host in [29, 300]:
        crt.Screen.Send('telnet ' + '218.206.118.' + host + ' /so lo0' + ' \r')

    else:
        crt.Dialog.MessageBox('请输入正确的IP地址！', 'ERROR', 16 | 0)

        host_new_base = crt.Dialog.Prompt("输入IP地址最后一位：", "IP Address", '', False)

        crt.Screen.Send('telnet ' + '218.206.118.' + host_new_base + ' /so lo0' + ' \r')

    #crt.Screen.WaitForString('Username:',2)
    #crt.Screen.Send(username_2 + ' \r')
    username_two = crt.Dialog.Prompt('输入用户名： ', '用户', username_2, False)

    if username_two == '':
        crt.Dialog.MessageBox('请输入用户名！', 'ERROR', 16|0)

        username_new_two = crt.Dialog.Prompt("输入用户名：", "用户", '', False)

        crt.Screen.Send(username_new_two + '\r')

    else:
        crt.Screen.Send(username_two + '\r')

    password_two = crt.Dialog.Prompt('输入密码： ', '密码', password_2, False)

    if password_two == '':
        crt.Dialog.MessageBox('请输入密码！', 'ERROR', 16 | 0)

        password_new_two = crt.Dialog.Prompt("输入密码：", "密码", '', False)

        crt.Screen.Send(password_new_two + '\r')

    else:
        crt.Screen.Send(password_two + '\r')

    post = crt.Dialog.Prompt('输入端口：', '端口', '1/1/1', False)

    if password_two == '':
        crt.Dialog.MessageBox('请输入端口！', 'ERROR', 16 | 0)

        post_new = crt.Dialog.Prompt("输入端口：", "端口", '', False)

        crt.Screen.Send('display interface GigabitEthernet ' + post_new + ' \r')

    else:
        crt.Screen.Send('display interface GigabitEthernet ' + post + ' \r')

main()

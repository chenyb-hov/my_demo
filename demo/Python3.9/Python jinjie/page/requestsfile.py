import requests

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
# r = requests.get('https://www.douban.com/', headers=headers)
# r1 = requests.get('https://www.python.org/')
# print(r.status_code)
# print(r.text)
# print(r1.status_code)

# r2 = requests.get('https://www.douban.com/', params={'username': 'admin', 'pwd': '123'})
# print(r2.url)
# print(r1.encoding)
# print(r1.content)

# r3 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r3.status_code)
# print(r3.json())

# r4 = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r4.text)

# r5 = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'}, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r5.status_code)

# params = {'key': 'value'}
# r6 = requests.post('https://accounts.douban.com/login', json=params, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r6.text)

# upload_file = {'file': open('code.jpg', 'rb')}
# r7 = requests.post('https://accounts.douban.com/login', files=upload_file, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r7.headers)
# print(r7.headers['Content-Type'])
# print(r7.cookies)

# cs = {'token': '123', 'status': 'working'}
# r8 = requests.get('https://accounts.douban.com/login', cookies=cs, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r8.status_code)



# r9 = requests.get('https://accounts.douban.com/login',timeout=3, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r9.status_code)

r10 = requests.get('http://10.3.1.81')
print(r10.status_code)
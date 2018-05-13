from urllib import request, parse

url = 'http://120.79.84.67/api/'

login = 'login/'

parmas = {'loginName': '15889681345', 'password': 'aa123456'}

querystring = parse.urlencode(parmas)

u = request.urlopen(url + login, querystring.encode('ascii'))
resp = u.read()
print(resp)

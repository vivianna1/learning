import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

data = {}
data['action'] = 'FY_BY_CLICKBUTTION'
data['bv'] = '1ca13a5465c2ab126e616ee8d6720cc3'
data['client'] = 'fanyideskweb'
data['doctype'] = 'json'
data['from'] = 'AUTO'
data['i'] = content
data['keyfrom'] = 'fanyi.web'
data['salt'] = '15708737847078'
data['sign'] = '64037c1dd211ea7bd98321a3bd8ab45a'
data['smartresult'] = 'dict'
data['to'] = 'AUTO'
data['ts'] = '1570873784707'
data['version'] = '2.1'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

target = json.loads(html)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

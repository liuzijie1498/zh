import requests

url = 'https://www.zhihu.com/api/v4/members/wei-dao-shi-zuo-huai-bu-luan-68?include=allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2C' \
      'articles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 '
'(KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
'x-zse-86': '1.0_aLNBQQHBNwxpNqN8zqt0r7XBrLSpNU20K0S027Lqe7tY',
'x-za-clientid': 'ef10839d-0043-4e66-9f14-b0a7702cb9b9'


           }
res = requests.get(url, headers=headers)
print(res.text)
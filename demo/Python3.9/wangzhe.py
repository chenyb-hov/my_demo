import requests

url = 'http://pvp.qq.com/web201605/js/herolist.json'
headers = {'User-Agent':'209553470'}
response = requests.get(url, headers=headers)
json_list = response.json()

try:
    for m in range(len(json_list)):
        hero_num = json_list[m]['ename']
        hero_name = json_list[m]['cname']
        skin_name = json_list[m]['skin_name'].split('|')
        skin_count = len(skin_name)
        print('name: ', hero_name, 'num: ', skin_count)

        for i in range(1, skin_count + 1):
            url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'
            url_pic = url + str(hero_num) + '/' + str(hero_num) + '-bigskin-' + str(i) + '.jpg'
            picture = requests.get(url_pic).content
            with open('pic/' + hero_name + '-' + skin_name[i-1] + '.jpg', 'wb') as f:
                f.write(picture)
except KeyError as e:
    print(e.args)
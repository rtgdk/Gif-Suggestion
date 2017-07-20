import json,urllib
search = input()
limit = "10"
data = json.loads(urllib.urlopen("http://api.tenor.com/v1/search?tag=%s&key=LIVDSRZULELA&limit=%s" % (search,limit)).read())
gif = [json.dumps(data['results'][i]['media'][0]['tinygif']['url']).replace('"', '').strip() for i in range(0,10)]
print(gif)

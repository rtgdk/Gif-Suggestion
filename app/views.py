from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseBadRequest, JsonResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
import urllib2
from app.models import UserID,Keyword,UserLikedGif,Article,ArticleCount
#app add
import giphypop
import urllib,json,urllib2

def index(request):
	context_dict={}
	if request.is_ajax():
			search = request.GET.get('search')
			print("here")
			print(search)
			limit = "5"
			#https://api.tenor.com/v1/search?tag=<query>&key=LIVDSRZULELA
			#data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=%s&api_key=dc6zaTOxFJmzC&limit=%s" % (search, limit)).read())
			data = json.loads(urllib.urlopen("http://api.tenor.com/v1/search?tag=%s&key=LIVDSRZULELA&limit=%s" % (search,limit)).read())
			#print(data)
			#return HttpResponse(data)
			#gif = [json.dumps(data['data'][i]['images']['original']['url']).replace('"', '').strip() for i in range(0,5)]
			gif = [json.dumps(data['results'][i]['media'][0]['tinygif']['url']).replace('"', '').strip() for i in range(0,5)]
			print(gif)
			data = {'success': "success"}
			context_dict={"gif":gif}
			render(request, 'app/table_body.html', context_dict)
			data = {'success': "Internal Error",'gif':gif}
			return JsonResponse(data)
	if request.method == 'POST':
		#print("here")
		search = request.POST['search']
		#print(search)
		limit = "5"
		#print("here")
		#g = giphypop.Giphy()
		#result = g.translate(phrase = search)
		#context_dict={"result":result}
		#data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=%s&api_key=dc6zaTOxFJmzC&limit=%s" % (search, limit)).read())
		data = json.loads(urllib.urlopen("http://api.tenor.com/v1/search?tag=%s&key=LIVDSRZULELA&limit=%s" % (search,limit)).read())
		#print(data['results'][0]['media'][0]['tinygif']['url'])
		#print(data['results'][0]['media'][0]['gif']['url'])
		#print(data['results'][0]['media'][0]['nanogif']['url'])
		#print(data['results'][0]['media'][0]['mediumgif']['url'])
		#return HttpResponse(data['results'][0]['media'][0]['tinygif']['url'])
		gif = [json.dumps(data['results'][i]['media'][0]['tinygif']['url']).replace('"', '').strip() for i in range(0,5)]
		context_dict={"gif":gif}
		return render(request, 'app/index.html',context_dict)
	else :
		print("her2e")
		return render(request, 'app/index.html',context_dict)
		
def login(request) :
	context_dict ={}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		try :
			user = UserID.objects.get(username1=username)
			if password == user.password :
				request.session['user']=user.username1
				return HttpResponseRedirect("/gif/article/")
			else :
				context_dict["invalid"] = "Invalid Password"
				return render(request, 'app/login.html',context_dict)
		except :
			context_dict["invalid"] = "Invalid Credentials"
			return render(request, 'app/login.html',context_dict)
	else :
		return render(request, 'app/login.html',context_dict)


def logout(request) :
	if 'user' in request.session:
		request.session.flush()
		return HttpResponseRedirect("/gif/login/")
	return HttpResponseRedirect('/gif/')

def article(request) :
	context_dict ={}
	username = request.session["user"]
	user = UserID.objects.get(username1 = username)
	artcount = ArticleCount.objects.get(name = "a")
	if request.method == 'POST':
		art = Article.objects.get(pk=user.art_count+3)		# change it to 0
		if (user.kw_count==0):
			kw = art.kw1
		elif (user.kw_count==1):
			kw = art.kw2
		elif (user.kw_count==2):
			kw = art.kw3
		elif (user.kw_count==3):
			kw = art.kw4
		elif (user.kw_count==4):
			kw = art.kw5
		#return HttpResponse(kw)
		c11 = request.POST["gifc1"]
		c12 = request.POST["gifc2"]
		c13 = request.POST["gifc3"]
		c14 = request.POST["gifc4"]
		c15 = request.POST["gifc5"]
		c16 = request.POST["gifc6"]
		c17 = request.POST["gifc7"]
		c18 = request.POST["gifc8"]
		c19 = request.POST["gifc9"]
		c110 = request.POST["gifc10"]
		"""c21 = request.POST["gifc1"]
		c22 = request.POST["gifc2"]
		c23 = request.POST["gifc3"]
		c24 = request.POST["gifc4"]
		c25 = request.POST["gifc5"]
		c26 = request.POST["gifc6"]
		c27 = request.POST["gifc7"]
		c28 = request.POST["gifc8"]
		c29 = request.POST["gifc9"]
		c210 = request.POST["gifc10"]
		c31 = request.POST["gifc1"]
		c32 = request.POST["gifc2"]
		c33 = request.POST["gifc3"]
		c34 = request.POST["gifc4"]
		c35 = request.POST["gifc5"]
		c36 = request.POST["gifc6"]
		c37 = request.POST["gifc7"]
		c38 = request.POST["gifc8"]
		c39 = request.POST["gifc9"]
		c310 = request.POST["gifc10"]
		c41 = request.POST["gifc1"]
		c42 = request.POST["gifc2"]
		c43 = request.POST["gifc3"]
		c44 = request.POST["gifc4"]
		c45 = request.POST["gifc5"]
		c46 = request.POST["gifc6"]
		c47 = request.POST["gifc7"]
		c48 = request.POST["gifc8"]
		c49 = request.POST["gifc9"]
		c410 = request.POST["gifc10"]
		c51 = request.POST["gifc1"]
		c52 = request.POST["gifc2"]
		c53 = request.POST["gifc3"]
		c54 = request.POST["gifc4"]
		c55 = request.POST["gifc5"]
		c56 = request.POST["gifc6"]
		c57 = request.POST["gifc7"]
		c58 = request.POST["gifc8"]
		c59 = request.POST["gifc9"]
		c510 = request.POST["gifc10"]"""
		kw.count1 += int(c11)
		kw.count2 += int(c12)
		kw.count3 += int(c13)
		kw.count4 += int(c14)
		kw.count5 += int(c15)
		kw.count6 += int(c16)
		kw.count7 += int(c17)
		kw.count8 += int(c18)
		kw.count9 += int(c19)
		kw.count10 += int(c110)
		kw.save()
		c = c11 + c12 + c13 + c14 + c15 + c16 + c17 + c18 + c19 +c110
		#return HttpResponse(c)
		#return HttpResponse(c)
		#return HttpResponse(c10)
		if (user.kw_count==0):
			ulg = UserLikedGif.objects.create(user_id = user, gif_id = kw, liked=c )
		elif (user.kw_count==1):
			ulg = UserLikedGif.objects.create(user_id = user, gif_id = kw, liked=c )
		elif (user.kw_count==2):
			ulg = UserLikedGif.objects.create(user_id = user, gif_id = kw, liked=c )
		elif (user.kw_count==3):
			ulg = UserLikedGif.objects.create(user_id = user, gif_id = kw, liked=c )
		elif (user.kw_count==4):
			ulg = UserLikedGif.objects.create(user_id = user, gif_id = kw, liked=c )
		
		if (user.kw_count ==4 ):
			user.art_count =  user.art_count+1
			user.kw_count = 0
		else :
			user.kw_count = user.kw_count + 1
		user.save()
		return HttpResponseRedirect("/gif/article/")
	else :
		if (user.art_count > artcount.count):
			context_dict["invalid"] = "No more articles"
			return render(request, 'app/article.html',context_dict)
		else :
			art = Article.objects.get(pk=user.art_count+3)			# change it to 0
			context_dict["article"] = art
			if (user.kw_count==0):
				context_dict["kw"] = art.kw1
			elif (user.kw_count==1):
				context_dict["kw"] = art.kw2
			elif (user.kw_count==2):
				context_dict["kw"] = art.kw3
			elif (user.kw_count==3):
				context_dict["kw"] = art.kw4
			elif (user.kw_count==4):
				context_dict["kw"] = art.kw5
			return render(request, 'app/article.html',context_dict)



def creategif(text):
	# logic for geting keywords from text
	search = text
	limit = "10"
	data = json.loads(urllib.urlopen("http://api.tenor.com/v1/search?tag=%s&key=LIVDSRZULELA&limit=%s" % (search,limit)).read())
	gif = [json.dumps(data['results'][i]['media'][0]['tinygif']['url']).replace('"', '').strip() for i in range(0,10)]
	return gif

def addarticle(request) :
	context_dict ={}
	if request.method == 'POST':
		link = request.POST['link']
		title = request.POST['title']
		kw1 = request.POST['keyword1']
		kw2 = request.POST['keyword2']
		kw3 = request.POST['keyword3']
		kw4 = request.POST['keyword4']
		kw5 = request.POST['keyword5']
		kws1 = creategif(kw1)
		key1 = Keyword.objects.create(word = kw1,gif1 =kws1[0],gif2 =kws1[1],gif3 =kws1[2],gif4 =kws1[3],gif5 =kws1[4],
						gif6 =kws1[5],gif7 =kws1[6],gif8 =kws1[7],gif9 =kws1[8],gif10 =kws1[9])
		kws1 = creategif(kw2)
		key2 = Keyword.objects.create(word = kw2,gif1 =kws1[0],gif2 =kws1[1],gif3 =kws1[2],gif4 =kws1[3],gif5 =kws1[4],
						gif6 =kws1[5],gif7 =kws1[6],gif8 =kws1[7],gif9 =kws1[8],gif10 =kws1[9])
		kws1 = creategif(kw3)
		key3 = Keyword.objects.create(word = kw3,gif1 =kws1[0],gif2 =kws1[1],gif3 =kws1[2],gif4 =kws1[3],gif5 =kws1[4],
						gif6 =kws1[5],gif7 =kws1[6],gif8 =kws1[7],gif9 =kws1[8],gif10 =kws1[9])
		kws1 = creategif(kw4)
		key4 = Keyword.objects.create(word = kw4,gif1 =kws1[0],gif2 =kws1[1],gif3 =kws1[2],gif4 =kws1[3],gif5 =kws1[4],
						gif6 =kws1[5],gif7 =kws1[6],gif8 =kws1[7],gif9 =kws1[8],gif10 =kws1[9])
		kws1 = creategif(kw5)
		key5 = Keyword.objects.create(word = kw5,gif1 =kws1[0],gif2 =kws1[1],gif3 =kws1[2],gif4 =kws1[3],gif5 =kws1[4],
						gif6 =kws1[5],gif7 =kws1[6],gif8 =kws1[7],gif9 =kws1[8],gif10 =kws1[9])
		context_dict["invalid"]="Added!"
		#kws2 = creategif(kw2)
		#kws3 = creategif(kw3)
		#kws4 = creategif(kw4)
		#kws5 = creategif(kw5)
		art = Article.objects.create(link=link,title=title,kw1=key1,kw2=key2,kw3=key3,kw4=key4,kw5=key5)
		artcount = ArticleCount.objects.get(name="a")
		artcount.count = artcount.count+1
		artcount.save()
		return render(request, 'app/addarticle.html',context_dict)
	else :
		return render(request, 'app/addarticle.html',context_dict)

def register(request) :
	context_dict = {}
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		pw = request.POST['password']
		user = User.objects.create(username = username, password = pw, email = email,is_staff=True)
		a=UserID.objects.create(email=email,username=user,username1 = username, password=pw)
		return HttpResponseRedirect("/gif/login/")
	else :
		return render(request, 'app/register.html',context_dict)
		
"""def ajaxsearch(request,key):
	limit = "5"
	print("here")
	data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=%s&api_key=dc6zaTOxFJmzC&limit=%s" % (key, limit)).read())
	gif = [json.dumps(data['data'][i]['images']['original']['url']).replace('"', '').strip() for i in range(0,5)]
	data = {'success': "success"}
	context_dict={"gif":gif}
	return render(request, 'app/table_body.html', context_dict)"""

from django.shortcuts import render
from django.shortcuts import redirect
from .models import Room

def calendar(request):
    return render(request, 'on_sta/calendar.html')

def top(request):
    return render(request, 'on_sta/top.html')

def widgets(request):
    return render(request, 'on_sta/widgets.html')

def gallery(request):
    return render(request, 'on_sta/gallery.html')

def index(request):

    params = {
        'block_title':'ようこそOn_Staへ',
        }
    return render(request, 'on_sta/index.html',params)

def account(request):

    params = {
        'block_title':'こちらは新規会員登録画面です',
        }
    return render(request, 'on_sta/account.html',params)

def analytics(request):
    return render(request, 'on_sta/analytics.html')

def config(request):
    return render(request, 'on_sta/config.html')

def contact(request):
    params = {
        'block_title':'お問い合わせはこちら',
    }
    return render(request, 'on_sta/contact.html',params)

def create_room(request):
    params = {
        'block_title':'勉強部屋作成画面'
    }

    return render(request, 'on_sta/create_room.html',params)

def dashbord(request):
    return render(request, 'on_sta/dashbord.html')

def disclaimer(request):
    params  = {
        'block_title':'免責事項'
    }
    return render(request, 'on_sta/disclaimer.html',params)

def help(request):
    params = {
        'block_title':'ヘルプ',
    }
    return render(request, 'on_sta/help.html',params)

def home(request):
    return render(request, 'on_sta/home.html')

def lobby(request):

    data = Room.objects.all()
    params = {
        'block_title':'ロビー',
        'data':data, 
    }

    return render(request, 'on_sta/lobby.html',params)

def login(request):
    params  = {
        'block_title':'こちらはログイン画面です'
    }
    return render(request, 'on_sta/login.html',params)

def menu(request):
    return render(request, 'on_sta/menu.html')

def policy(request):
    params  = {
        'block_title':'利用規約'
    }
    return render(request, 'on_sta/policy.html',params)

def profile(request):
    return render(request, 'on_sta/profile.html')

def pw_change(request):
    return render(request, 'on_sta/pw_change.html')

def pw_forget(request):
    return render(request, 'on_sta/pw_forget.html')

def study_plan(request):
    return render(request, 'on_sta/study_plan.html')

def study_room(request):
    params = {
        'block_title':'勉強部屋'
    }
    return render(request, 'on_sta/study_room.html',params)

def twitter(request):
    return render(request, 'on_sta/twitter.html')

from django.urls import path
from .import views

app_name = 'on_sta'

urlpatterns = [
    path('',views.index, name='index'), #viewsのindex関数を利用する
    path('top/',views.top, name='top'),
    path('account/',views.account, name='account'),
    path('analytics/',views.analytics, name='analytics'),
    path('config/',views.config, name='config'),
    path('contact/',views.contact, name='contact'),
    path('create_room/',views.create_room, name='create_room'),
    path('dashbord/',views.dashbord, name='dashbord'),
    path('disclaimer/',views.disclaimer, name='disclaimer'),
    path('help/',views.help, name='help'),
    path('home/',views.home, name='home'),
    path('lobby/',views.lobby, name='lobby'),
    path('login/',views.login, name='login'),
    path('menu/',views.menu, name='menu'),
    path('policy/',views.policy, name='policy'),
    path('profile/',views.profile, name='profile'),
    path('pw_change/',views.pw_change, name='pw_change'),
    path('pw_forget/',views.pw_forget, name='pw_forget'),
    path('study_plan/',views.study_plan, name='study_plan'),
    path('study_room/',views.study_room, name='study_room'),
    path('twitter/',views.twitter, name='twitter'),
    path('gallery/',views.gallery, name='gallery'),
    path('top/pages/widgets/',views.widgets, name='widgets'),
    path('calendar/',views.calendar, name='calendar'),

]
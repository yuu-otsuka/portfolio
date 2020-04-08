from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class User(models.Model):
    user_id = models.CharField(max_length=7, verbose_name="ユーザーID",primary_key=True)
    user_name = models.CharField(max_length=28, verbose_name="ユーザー名")

    GENDER_CHOICES = (
        (1,'男性'),
        (2,'女性'),
        (3,'その他'),
    )
    
    gender = models.IntegerField(verbose_name = '性別', choices=GENDER_CHOICES,blank=True,null=True,)
    birthday = models.DateField(verbose_name="生年月日",blank=True,null=True,)
    email = models.EmailField(max_length=200, verbose_name="メールアドレス")
    profile = models.CharField(max_length=160, verbose_name="プロフィール",blank=True,null=True,)
    user_image = models.ImageField(upload_to="image/", verbose_name="画像",blank=True,null=True,)
    study_category = models.CharField(max_length=100, verbose_name="学習カテゴリー",blank=True,null=True,)    
    website = models.URLField(verbose_name="WEBサイト",blank=True,null=True,)
    good = models.IntegerField(default=0,verbose_name="いいね",blank=True,null=True,)

    def __str__(self):
        return self.user_name

class Room(models.Model):
    room_id = models.AutoField(verbose_name="部屋ID",primary_key=True )
    room_name = models.CharField(max_length=28, verbose_name="部屋名")

    pepople = models.IntegerField(validators =[ MinValueValidator(16), \
    MaxValueValidator(16)],verbose_name="人数")  #人数は１６人固定

    start_time = models.DateTimeField(auto_now_add=True, verbose_name="開始日時")
    end_time = models.DateTimeField(blank=True,null=True, verbose_name="終了時間")
    layout_id = models.CharField(max_length=7, verbose_name="レイアウトID")
    user_id = models.CharField(max_length=7, verbose_name="ユーザーID")

    def __str__(self):
        return self.room_name

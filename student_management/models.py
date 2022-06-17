from django.db import models

#settings.pyにて指定したタイムゾーンを考慮したtimezoneをimport (awareとnative)
#Djangoサーバーの拠点が海外に存在したとしても日本時間で記録される。
from django.utils import timezone


from django.contrib.auth.models import User



class Building(models.Model):

    #ここにidフィールドがある(自動採番なので、クライアントは入力不要。)

    #文字列型であり、最長200文字で、null禁止、blank禁止のフィールド
    name        = models.CharField(verbose_name="校舎名",max_length=200)

    #日付フィールド。defaultで現在時刻を出力するメソッドを指定
    #後から追加するとマイグレーションした時刻が記録される
    dt          = models.DateTimeField(verbose_name="登録日時",default=timezone.now)

    #default無しのフィールド
    description = models.CharField(verbose_name="備考",max_length=500,null=True,blank=True)
    
    #モデルオブジェクト単体をそのまま表示させる時、nameフィールドに格納された値を表示させる
    def __str__(self):
        return self.name


    #生徒数のカウント
    def count_students(self):
        return Student.objects.filter(building=self.id).count()

    #管理サイトから呼び出す時のヘッダ名
    count_students.short_description      = "所属生徒数"
    

class Student(models.Model):

    name        = models.CharField(verbose_name="生徒名",max_length=50)
    dt          = models.DateTimeField(verbose_name="登録日時",default=timezone.now)

    #所属校舎が削除される時、生徒が含まれていれば、校舎は削除されない。
    #Buildingのidが記録される
    building    = models.ForeignKey(Building,verbose_name="所属校舎",on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Log(models.Model):

    class Meta:
        #https://noauto-nolife.com/post/django-same-user-operate-prevent/
        unique_together = ("date","student")


    date        = models.DateField(verbose_name="自習日")
    student     = models.ForeignKey(Student,verbose_name="生徒",on_delete=models.PROTECT)


    #Userモデルと1対多を結ぶ
    user        = models.ForeignKey(User, verbose_name="投稿者",on_delete=models.SET_NULL,null=True)





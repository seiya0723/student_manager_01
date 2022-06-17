from django.shortcuts import render,redirect
from django.views import View

from .models import Building
from .forms import BuildingForm

#DjangoMessageFrameworkをimport
from django.contrib import messages

#未ログインユーザーはアクセス拒否



#https://noauto-nolife.com/post/django-login-required-mixin/
from django.contrib.auth.mixins import LoginRequiredMixin


#LoginRequiredMixinを多重継承することで、未認証ユーザーをログインページへリダイレクトできる。
class IndexView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        
        context     = {}

        #DBからBuildingモデルのテーブルから全データを取り出す。(データは複数なので複数形)
        context["buildings"]    = Building.objects.all()

        #TIPS:条件に一致したものだけ取り出したい場合、.filter()メソッドを使う


        return render(request,"student_management/index.html",context)

    def post(self, request, *args, **kwargs):

        #TODO:データの保存処理

        #BuildingFormのオブジェクトを作る。(引数はPOSTメソッドで送信されたデータ全て)
        form    = BuildingForm(request.POST)

        #.is_valid()で、ここで入力されたデータが正しいかチェックしている
        #入力されたデータがルールに則っていれば、.is_valid()はTrueを返す
        if form.is_valid():
            print("バリデーションOK。書き込み")
            form.save()
        else:
            print("バリデーションNG")
            #エラーの理由が表示される。HTML形式
            #TIPS:DjangoMessageFrameworkを使ってクライアントに表示させる
            print(form.errors)
            
            #DjangoMessageFrameworkを使ってエラー文をセットする。
            messages.error(request, form.errors)

        """
        #受け取ったデータを引数にしてモデルオブジェクトを作る
        posted  = Building(name=request.POST["name"])

        #saveメソッドを使ってDBに書き込みを行う。
        posted.save()
        """

        """
        Building(name=request.POST["name"]).save()
        """

        """
        posted      = Building()
        posted.name = request.POST["name"]
        posted.save()
        """

        #POSTメソッドでリダイレクトすることで、GETメソッドが返却される。
        #これにより、更新ボタンを押しても、POSTメソッドが繰り返されることはない
        return redirect("student_management:index")


        #POSTメソッドでレンダリングしてしまうと、POSTメソッドが返却される。
        #それにより、更新ボタンを押すと、POSTが繰り返される。
        """
        buildings   = Building.objects.all()
        context     = { "buildings":buildings }
        return render(request,"student_management/index.html",context)
        """

        #return render(request,"student_management/index.html")




index   = IndexView.as_view()




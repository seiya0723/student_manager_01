from django import forms 

from .models import Building

#DBに書き込みする前のチェックとして、モデルを使用するフォームクラスを作るため、forms.ModelFormを継承
class BuildingForm(forms.ModelForm):
    
    #使用するモデルと、そのフィールドを指定する。
    class Meta:
        model   = Building

        #idは自動採番なので、クライアントが入力するものではない。
        #そのためバリデーション対象のフィールドとして指定する必要はない。
        #TODO:バリデーション対象のフィールドを選んで指定

        fields  = [ "name","description" ]



#モデルを使用しないタイプのフォームクラス。forms.Formを継承する。
"""
class YearForm(forms.Form):
    year    = IntegerField()
"""

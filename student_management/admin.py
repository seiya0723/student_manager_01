from django.contrib import admin

from .models import Building,Student

from django.utils.html import format_html


class BuildingAdmin(admin.ModelAdmin):

    list_display    = ["id","name","dt","description","count_students","show_students_amount"]
    list_editable   = [ "name","dt","description" ]


    def show_students_amount(self,obj):
        return format_html('<div>' + str(obj.count_students()) + '</div>')

    show_students_amount.short_description      = "所属生徒数"


class StudentAdmin(admin.ModelAdmin):

    list_display    = ["id","name","dt","building"]
    list_editable   = [ "name","dt","building" ]




admin.site.register(Building,BuildingAdmin)
admin.site.register(Student,StudentAdmin)


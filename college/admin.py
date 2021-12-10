from django.contrib import admin
from college.models import Notice,Branch,Question,Profile
from django.contrib.admin.options import ModelAdmin


# Register your models here.
# class BranchAdmin(ModelAdmin):
#     list_display = ["name", "hod"]
#     search_fields = ["name", "hod"]
#     list_filter = ["name", "hod"]
admin.site.register(Notice)
admin.site.register(Branch)# yaha hamne brach table ko registar kiya hai
admin.site.register(Question)# yaha hamne brach table ko registar kiya hai
admin.site.register(Profile)# yaha hamne profile table ko registar kiya hai



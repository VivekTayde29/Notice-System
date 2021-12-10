from django.contrib import admin
from django.urls import path
from college import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path("home/",views.HomeView.as_view()),
    path("notice/",views.NoticeListView.as_view()),
    path('notice/<int:pk>', views.NoticeDetailView.as_view()),
    path('mylist/', views.MyList.as_view()),
    path('question/create/', views.QuestionCreate.as_view(success_url="/college/home")),
    path('notice/edit/<int:pk>', views.NoticeUpdateView.as_view(success_url="/college/home/")),
    path('notice/delete/<int:pk>',views.NoticeDeleteView.as_view(success_url='/college/home/')),
    path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/college/home")),
    # success_url="/college/home" iska matlab hai ki jab question successfully profile upded ho jayega uske bad redirect ho jayega (/college/home/) vale page pe

    path("",RedirectView.as_view(url="home/"))
]

"""sticky_memo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from memo import views as memo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 특정 url ”my-home”에 들어가면 “hello world!”를 표시해보기
    path('my-home/', views.my_home),
    path('memo/', memo_views.get_all_memo)
]

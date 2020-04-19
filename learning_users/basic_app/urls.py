from basic_app import views
from django.urls import path

# Template URLS!
app_name = 'basic_app'

urlpatterns = [
    path('register/',views.register, name = 'register'),
    path('index/',views.index,name='index'),
    path('user_login/',views.user_login, name = 'user_login')
]

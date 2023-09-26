from. import views
from django.urls import path
app_name='registration'
urlpatterns = [

    path('',views.home,name='home'),

]

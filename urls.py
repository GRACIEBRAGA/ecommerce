from django.urls import path
from store import views
#from .views import MyView


app_name = 'store'

urlpatterns = {
    #path('home', views.home_view.as_view(), name='home'),
    path('home/', views.home.as_view(), name='home'),
    #path('home/', MyView.as_view()),
    #path('home', views.as_view()),
    # path('homestore/', views.Homestore.as_view(), name='homestore'),
    # path('vendacreate/', views.Vendacreate.as_view(), name='vendacreate'),
    # path('vendalist', views.Vendalist.as_view(), name='vendalist'),
}

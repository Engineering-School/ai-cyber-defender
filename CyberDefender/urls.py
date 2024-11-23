"""CyberDefender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views # імпортуємо представлення з поточного додатку
#from django.urls import path
from .views import HomePageView
#from . import views
#from .views import get_user_ip

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('web-analytics/', views.web_analytics_view, name='web_analytics_page'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    #path('accounts/', include('allauth.urls')),

    #### CUSTOM COMPONENTS
    path('buttons/', views.buttons_view, name='buttons'),  # Додавання шляху для сторінки buttons.html
    path('cards/', views.cards_view, name='cards'),  # Додавання шляху для сторінки cards.html

    #### CUSTOM UTILITIES
    path('utilities-color/', views.utilities_color_view,   name='utilities_color'),
    path('utilities-border/', views.utilities_border_view, name='utilities_border'),  # Доданий новий шлях для сторінки utilities-border.html
    path('utilities-animation/', views.utilities_animation_view, name='utilities_animation'),  # Додавання шляху для сторінки utilities-animation.html
    path('utilities-other/', views.utilities_other_view, name='utilities_other'),  # Додавання шляху для сторінки utilities-other.html

    #### ADDONS
    path('charts/', views.charts_view, name='charts'),  # Додавання URL-шляху для сторінки charts.html
    path('tables/', views.tables_view, name='tables'),  # Додавання URL-шляху для сторінки tables.html

]






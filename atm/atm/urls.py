"""atm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
        path('',views.index, name='index'),
        path('banking',views.banking,name="banking"),
        path('cashwithdraw',views.cashwithdrawal,name="banking"),
        path('bankbalance',views.bankbalance,name="bankbalance"),
        path('ministatement',views.ministatement,name="ministatement"),
        path('changepin',views.changepin,name="changepin"),
        path('pin',views.enterpin,name="enterpin"),
        path('alertsms/',views.sendsms,name="smsalert"),
        path('accounts/',include('accounts.urls'),name="accounts"),
        path('takepicture/',views.takepicture,name="takepicture"),
        # path('banking',views.banking,name="banking"),
]

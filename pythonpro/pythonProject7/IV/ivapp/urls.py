"""
URL configuration for IV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


from django.urls import path
from.import views


urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('registration', views.registration),# college-registration
    path('companyreg', views.companyreg),
    path('services', views.services),
    path('companyservices', views.companyservices),
    path('adminhome', views.adminhome),
    path('admincoldet', views.admincoldet),
    path('admincompdet', views.admincompdet),
    path('companypend', views.companypend),
    path('pending1/<id1>', views.pending1),
    path('logout', views.logout),
    path('compcoldet', views.compcoldet),
    path('colviewivcomp', views.colviewivcomp),
    path('selectdepart/<bk>', views.selectdepart),
    path('compaddprojects', views.compaddprojects),
    path('editdm/<dd>', views.editdm),
    path('compprofile', views.compprofile),
    path('compabout', views.compabout),
    path('uprofile', views.uprofile),
    path('edituser/<id2>', views.edituser),
    # path('compbooking/<bok>', views.compbooking),
    path('edititem/<id3>', views.edititem),
    path('colviewcomdetails/<dp9>', views.colviewcomdetails),
    path('accept/<k>', views.accept),
    path('acc', views.acc),
    path('delete/<id1>', views.delete),
    path('reject/<bk>', views.reject),
    path('rej', views.rej),
    path('bookingdet/<bok>', views.bookingdet),
    path('book', views.book),
    path('contact', views.contact),
    path('payment/<a>/<bid>', views.payment),
    path('success', views.success),
    path('paid', views.paid),
    path('conhome', views.conhome),
    path('addreviews', views.addreviews),
    # path('colviewcomdetails', views.colviewcomdetails),
    # path('travprofile', views.travprofile),
    # path('colviewcomdetails', views.colviewcomdetails),



    # path('collegedepartment',views.collegedepartment)


]


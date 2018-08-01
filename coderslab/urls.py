"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path, include
from contact.views import AllPeople, NewPerson, ModifyPerson, DeletePerson, PersonDetails, AddAddress, ModifyAddress, \
    DeleteAddress, AddEmail, ModifyEmail, DeleteEmail, AddPhone, ModifyPhone, DeletePhone, CreateGroup, \
    ModifyGroupName, DeleteGroup, GroupList, GroupShow, AddToGroup, EraseFromGroup, SearchInGroups

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^all/', AllPeople.as_view()),
    re_path(r'^new/', NewPerson.as_view()),
    re_path(r'^modify/(?P<id>\d+)/$', ModifyPerson.as_view()),
    re_path(r'^delete/(?P<id>\d+)/', DeletePerson.as_view()),
    re_path(r'^show/(?P<id>\d+)/', PersonDetails.as_view()),
    re_path(r'^modify/(?P<id>\d+)/address/', AddAddress.as_view()),
    re_path(r'^modify/(?P<id>\d+)/modify_address/', ModifyAddress.as_view()),
    re_path(r'^modify/(?P<id>\d+)/delete_address/', DeleteAddress.as_view()),
    re_path(r'^modify/(?P<id>\d+)/email/', AddEmail.as_view()),
    re_path(r'^modify/(?P<id>\d+)/modify_email/', ModifyEmail.as_view()),
    re_path(r'^modify/(?P<id>\d+)/delete_email/', DeleteEmail.as_view()),
    re_path(r'^modify/(?P<id>\d+)/phone/', AddPhone.as_view()),
    re_path(r'^modify/(?P<id>\d+)/modify_phone/', ModifyPhone.as_view()),
    re_path(r'^modify/(?P<id>\d+)/delete_phone/', DeletePhone.as_view()),
    re_path(r'^create_group/', CreateGroup.as_view()),
    re_path(r'^modify_group/(?P<id>\d+)', ModifyGroupName.as_view()),
    re_path(r'^delete_group/(?P<id>\d+)', DeleteGroup.as_view()),
    re_path(r'^group_list/', GroupList.as_view()),
    re_path(r'^show_group/(?P<id>\d+)', GroupShow.as_view()),
    re_path(r'^modify/(?P<id>\d+)/add_to_group/', AddToGroup.as_view()),
    re_path(r'^modify/(?P<id>\d+)/(?P<id_group>\d+)/delete_from_group/', EraseFromGroup.as_view()),
    re_path(r'^group_search/', SearchInGroups.as_view()),
]
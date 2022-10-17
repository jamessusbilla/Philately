
from django.contrib import admin
from django.urls import path
from . import views
from .models import Postal, Contact

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('Contact-Us/', views.ContactCreation.as_view(), name='contact'),
    path('finish-reading/', views.ReadContact.as_view(), name='finishRead'),
    path('<slug:slug>/mail/', views.MailDetail.as_view(), name='viewMail'),
    path('<slug:slug>/mail/updatemail/', views.ContactUpdate.as_view(), name='updateMail'),
    path('<slug:slug>/mail/deletemail/', views.ContactAdminDeletion.as_view(), name='deleteMail'),


    path('sub-category-admin-list/', views.SubCategoryAdminList.as_view(),name='subcategorylist'),
    path('sub-category-creation/', views.SubCategoryCreation.as_view(), name='subcategorycreate'),
    path('<slug:slug>/sub-category-update/', views.SubCategoryAdminUpdate.as_view(), name='updatesubcategory'),
    path('<slug:slug>/sub-category-delete/', views.SubCategoryAdminDeletion.as_view(), name='deletesubcategory'),

    path('link-admin-list/', views.LinkList.as_view(),name='listlink'),
    path('link-creation/', views.LinkCreation.as_view(), name='createlink'),
    path('<slug:slug>/link-update/', views.LinkUpdate.as_view(), name='updatelink'),
    path('<slug:slug>/link-delete/', views.LinkDeletion.as_view(), name='deletelink'),



    path('postal-image-admin-list/', views.PostalImageAdminList.as_view(),name='postalimagelist'),
    path('postal-image-creation/', views.PostalImageCreation.as_view(), name='postalimagecreate'),
    path('<slug:slug>/postal-image-update/', views.PostalImageAdminUpdate.as_view(), name='updatepostalimage'),
    path('<slug:slug>/postal-image-delete/', views.PostImageAdminDeletion.as_view(), name='deletepostalimage'),


    path('ContactAdminList/', views.ContactAdminList.as_view(), name='contactList'),
    path('AdminView/', views.AdminView, name='adminview'),
    path('PostalCreation/', views.PostalCreation.as_view(), name='createpost'),
    path('PostalAdminList/', views.PostalAdminList.as_view(), name='adminList'),
    path('Create-About-Us/', views.CreateAboutUs.as_view(), name='createhistory'),
    path('About-Us-List/', views.AboutUsList.as_view(), name='listhistory'),
    path('PostalMuseum/', views.PostalMuseum, name='nzpostory'),
    path('NZPostalHistory/', views.NZPostalHistory, name='nzposthistory'),
    path('PigeonPost/', views.PigeonPost, name='pigeonpost'),
    path('OtherCollection/', views.OtherCollection, name='othercollection'),
    path('postal-history/', views.PostalList.as_view(), name='postalList'),
    path('War-Office/', views.WarOffice.as_view(), name='WarOffice'),
    path('Telegrams/', views.Telegrams.as_view(), name='Telegrams'),
    path('Non-NZ-Collection/', views.NonNZ.as_view(), name='NonNZ'),
    path('NZCollection/', views.NZ.as_view(), name='NZ'),
    path('FrankingMachine/', views.FRANKINGMACHINES.as_view(), name='FRANKINGMACHINES'),
    path('NZWWOne/', views.NZWWOne.as_view(), name='NZWWOne'),
    path('other_post_officeHistory/', views.OtherPostOfficeHistory.as_view(), name='OtherPostOffistory'),
    path('stamp-machine/', views.StampMachine.as_view(), name='StampMachine'),
    path('date-stamp/', views.DateStamp.as_view(), name='DateStamp'),
    path('Post-Marking-Machine/', views.PostMarkingMachine.as_view(), name='PostMarkMachine'),
    path('SavingsBank/', views.SavingsBank.as_view(), name='SavingsBank'),
    path('Equipment-Office/', views.EquipmentOffice.as_view(), name='EquipmentOffice'),
    path('<slug:slug>/', views.PostalDetail.as_view(), name='postalDetail'),
    path('<slug:slug>/updateView/', views.PostalAdminUpdate.as_view(), name='updatepost'),
    path('<slug:slug>/deletePost/', views.PostAdminDeletion.as_view(), name = 'deletepost'),
    path('<slug:slug>/detail/', views.AboutUsDetail.as_view(), name='historydetail'),
    path('<slug:slug>/detail/updateAboutUs/', views.UpdateAboutUs.as_view(), name='updateaboutus'),
    path('<slug:slug>/detail/deleteAboutUs/', views.DeleteAboutUs.as_view(), name='deleteaboutus'),
]

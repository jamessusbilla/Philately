#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Postal, History, Links, Contact, PostalImage, SubCategory, Philatelist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Admin View
class PostalCreation(LoginRequiredMixin, CreateView):
	model = Postal
	fields = ['postTitle','image','postContent','category','sub_category','philatelyAuthor']
	success_url=("/post_stamps/AdminView/")

class PostalAdminList(LoginRequiredMixin, ListView):
	model = Postal
	context_object_name = 'adminList'

class PostalAdminUpdate(LoginRequiredMixin, UpdateView):
	model = Postal
	fields = ['postTitle','image','postContent','category','sub_category','philatelyAuthor']
	success_url=("/post_stamps/PostalAdminList/")

class PostAdminDeletion(LoginRequiredMixin, DeleteView):
	model = Postal
	success_url=("/post_stamps/PostalAdminList/")

# Postal Image View
class PostalImageCreation(LoginRequiredMixin, CreateView):
	model = PostalImage
	fields = ['postalImage', 'postal']
	success_url=("/post_stamps/AdminView/")

class PostalImageAdminList(LoginRequiredMixin, ListView):
	model = PostalImage
	context_object_name = 'postalImageList'

class PostalImageAdminUpdate(LoginRequiredMixin, UpdateView):
	model = PostalImage
	fields = ['postalImage', 'postal']
	success_url=("/post_stamps/postal-image-admin-list/")

class PostImageAdminDeletion(LoginRequiredMixin, DeleteView):
	model = PostalImage
	success_url=("/post_stamps/postal-image-admin-list/")


# Sub Category
class SubCategoryCreation(LoginRequiredMixin, CreateView):
	model = SubCategory
	fields = ['sub_category']
	success_url=("/post_stamps/AdminView/")

class SubCategoryAdminList(LoginRequiredMixin, ListView):
	model = SubCategory
	context_object_name = 'subCategoryList'

class SubCategoryAdminUpdate(LoginRequiredMixin, UpdateView):
	model = SubCategory
	fields = ['sub_category']
	success_url=("/post_stamps/sub-category-admin-list/")

class SubCategoryAdminDeletion(LoginRequiredMixin, DeleteView):
	model = SubCategory
	success_url=("/post_stamps/sub-category-admin-list/")

# Links
class LinkCreation(LoginRequiredMixin, CreateView):
	model = Links
	fields = ['urlTitle','url','philatelyAuthor']
	success_url=("/post_stamps/AdminView/")

class LinkList(ListView):
	model = Links
	context_object_name = 'linkList'

class LinkUpdate(LoginRequiredMixin, UpdateView):
	model = Links
	fields = ['urlTitle','url','philatelyAuthor']
	success_url=("/post_stamps/link-admin-list/")

class LinkDeletion(LoginRequiredMixin, DeleteView):
	model = Links
	success_url=("/post_stamps/link-admin-list/")


# Contact Us
class ContactCreation(CreateView):
	model = Contact
	fields = ["subject","firstName","lastName","email","content"]
	success_url=("/")

class ContactAdminList(LoginRequiredMixin, ListView):
	queryset = Contact.objects.filter(status=0)
	context_object_name = 'contactList'

class ReadContact(LoginRequiredMixin, ListView):
	queryset = Contact.objects.filter(status=1)
	context_object_name = 'readList'
	template_name = 'queries-read.html'

class ContactAdminDeletion(LoginRequiredMixin, DeleteView):
	model = Contact
	success_url=("/post_stamps/finish-reading/")

class ContactUpdate(UpdateView):
	model = Contact
	fields = ["status"]
	success_url=("/post_stamps/finish-reading/")

class MailDetail(generic.DetailView):
	model = Contact
	template_name = 'mail_detail.html'


# About Us
class CreateAboutUs(LoginRequiredMixin, CreateView):
	model = History
	fields = ['aboutUsTitle','content','image','datePosted']
	success_url=("/post_stamps/AdminView/")

class AboutUsList(generic.ListView):
	queryset = History.objects.order_by('-datePosted')[:1]
	context_object_name = 'aboutList'
	template_name = 'post_stamp/history_list.html'

class AboutUsDetail(generic.DetailView):
	model = History
	template_name = 'historyDetail.html'

class UpdateAboutUs(LoginRequiredMixin, UpdateView):
	model = History
	fields = ['aboutUsTitle','content','image','datePosted']
	success_url=("/post_stamps/About-Us-List/")

class DeleteAboutUs(LoginRequiredMixin, DeleteView):
	model = History
	success_url=("/post_stamps/About-Us-List/")

# List & Detail Views

class PostalList(generic.ListView):
	context_object_name = 'postalList'
	model = Postal
	template_name = 'postalList.html'
	paginate_by = 3

	def get_queryset(self):
		if 'q' in self.request.GET:
			query = self.request.GET.get('q')
			queries = Postal.objects.filter(Q(postTitle__icontains=query) | Q(category__icontains=query) | Q(sub_category__sub_category=query))
		else:
			queries = Postal.objects.all()
		return queries
	

class PostalDetail(generic.DetailView):
	model = Postal
	template_name = 'postalDetail.html'

class Telegrams(generic.ListView):
	queryset = Postal.objects.filter(category=0)
	template_name = 'telegrams.html'
	context_object_name = 'telegrams'
	paginate_by = 3
	
class WarOffice(generic.ListView):
	queryset = Postal.objects.filter(category=1)
	template_name = 'war_office.html'
	context_object_name = 'war_office'

class EquipmentOffice(generic.ListView):
	queryset = Postal.objects.filter(category=2)
	template_name = 'equipment.html'
	context_object_name = 'equipment'
	
class SavingsBank(generic.ListView):
	queryset = Postal.objects.filter(category=3)
	template_name = 'savings.html'
	context_object_name = 'savings_bank'
	
class PostMarkingMachine(generic.ListView):
	queryset = Postal.objects.filter(category=4)
	template_name = 'marking_machines.html'
	context_object_name = 'marking_machines'
	
class DateStamp(generic.ListView):
	queryset = Postal.objects.filter(category=5)
	template_name = 'datestamp.html'
	context_object_name = 'datestamp'

class StampMachine(generic.ListView):
	queryset = Postal.objects.filter(category=6)
	template_name = 'stamp.html'
	context_object_name = 'stamp'
	
class OtherPostOfficeHistory(generic.ListView):
	queryset = Postal.objects.filter(category=8)
	template_name = 'other.html'
	context_object_name = 'other_history'
	
class NZWWOne(generic.ListView):
	queryset = Postal.objects.filter(category=9)
	template_name = 'WWOne.html'
	context_object_name = 'WWOne'
	
class FRANKINGMACHINES(generic.ListView):
	queryset = Postal.objects.filter(category=10)
	template_name = 'franking_machine.html'
	context_object_name = 'franking_machine'
	
class NZ(generic.ListView):
	queryset = Postal.objects.filter(category=11)
	template_name = 'nz.html'
	context_object_name = 'nz_posts'
	
class NonNZ(generic.ListView):
	queryset = Postal.objects.filter(category=12)
	template_name = 'nonnz.html'
	context_object_name = 'nonnz'


def PostalMuseum(request):
	return render(request, 'nzpost.html')

def NZPostalHistory(request):
	return render(request, 'history.html')

def PigeonPost(request):
	return render(request, 'pigeonpost.html')

def OtherCollection(request):
	return render(request, 'othercollection.html')

def AdminView(request):
	unread_messages = Contact.objects.filter(status=0).count()
	num_accounts = Philatelist.objects.all().count()
	num_postal = Postal.objects.all().count()
	num_links = Links.objects.all().count()
	return render(request,'adminView.html', context={'unread_messages':unread_messages,'num_accounts':num_accounts,'num_postal':num_postal,'num_links':num_links},)

# Sign Up
from .forms import SignUp
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            philatelicUser = form.save()
            login(request, philatelicUser, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = SignUp()
    return render(request, 'registration/signup.html', {'form': form})

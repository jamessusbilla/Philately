from django.db import models
from django.utils.text import slugify   
# Create your models here.
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from ckeditor.fields import RichTextField
from datetime import datetime

# Extending the ordinary django account 
class PhilatelistManager(BaseUserManager):

    def create_superuser(self, email, userName, firstName, lastName, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, userName, firstName, lastName, password, **other_fields)

    def create_user(self, email, userName, firstName,lastName, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, userName=userName,
                          firstName=firstName, lastName=lastName, **other_fields)
        user.set_password(password)
        user.save()
        return user
		
class Philatelist(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('email address'), unique=True)
	userName = models.CharField(max_length=150, unique=True)
	firstName = models.CharField(max_length=200, blank=True)
	lastName = models.CharField(max_length=200, blank=True)
	startDate = models.DateTimeField(default=timezone.now)
	about = models.TextField(_('Self Introduction'), max_length=500, blank=True)
	is_staff = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'Make new account'


	objects = PhilatelistManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['userName','firstName','lastName']

	def __str__(self):
		return f'{self.email}, {self.firstName}'


CATEGORY = ((0,"Telegrams"),(1,"Post office at war"),(2,"post office equipments"),(3,"post office savings bank"),(4,"postmarking machines"),(5,"DateStamps"),(6,"Stamp Dispensing Machines"),(7,"Temporary Post Offices"),(8,"Other post office history"),(9,"NZ P & T IN WW1"),(10,"FRANKING MACHINES"),(11,"New Zealand"),(12,"Non New Zealand"))


class SubCategory(models.Model):
	sub_category = models.CharField(max_length=150, verbose_name="Sub Category", blank=False, unique=True)
	slug = models.SlugField(max_length=200, null=True, verbose_name="Code", blank=False)
	
	class Meta:
		verbose_name_plural = 'Sub Categories'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.sub_category, allow_unicode=True)
		super().save(*args, **kwargs) 


	def __str__(self):
		return self.sub_category



class Postal(models.Model):
	postTitle = models.CharField(max_length=150, verbose_name="Title of post", blank=False)
	image = models.ImageField(upload_to='images/', verbose_name="Upload Image", blank=False)
	postContent = RichTextField(verbose_name="Postal Content", blank=False)
	category = models.IntegerField(choices=CATEGORY, default=0, help_text = "the page where you would put the post", verbose_name="Page Category", blank=False)
	sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, help_text = "Sub Category it is part of, if none, create one.", verbose_name="Sub Category", blank=False)
	philatelyAuthor = models.ForeignKey(Philatelist, on_delete= models.CASCADE, verbose_name="Author", blank=False)
	datePosted = models.DateTimeField(default = datetime.now, verbose_name="Date Posted")
	slug = models.SlugField(max_length=200, unique=True, help_text = "Please use the title of your post as the code.", verbose_name="Unique Code", blank=False)
	
	class Meta:
		ordering = ['-datePosted']
		verbose_name_plural = 'Postals'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.datePosted, allow_unicode=True)
		super().save(*args, **kwargs) 

		
	def __str__(self):
		return self.postTitle

class PostalImage(models.Model):
	postalImage = models.FileField(upload_to = 'images/', verbose_name="Upload Image", blank=False)
	postal = models.ForeignKey(Postal, on_delete=models.CASCADE, null=True, verbose_name="What post would you put your image", blank=False)
	slug = models.SlugField(max_length=200, null=True, verbose_name="Title of Image", blank=False)
	date = models.DateTimeField(default = datetime.now)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.date, allow_unicode=True)
		super().save(*args, **kwargs) 


	def __str__(self):
		return self.postal.postTitle
		
		
class History(models.Model):
	aboutUsTitle = models.CharField(max_length=150, default="About Us", verbose_name="About Us")
	content = RichTextField()
	image = models.FileField(upload_to = 'images/', verbose_name="Upload Image", blank=False, null=True)
	datePosted = models.DateTimeField(default = datetime.now, verbose_name="Date Posted", unique=True)
	slug = models.SlugField(max_length=200, null=True, help_text = "Please use the title of your post as the slug.", verbose_name="Code")
	
	class Meta:
		verbose_name_plural = 'About Us'
		ordering = ('-datePosted',)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.datePosted, allow_unicode=True)
		super().save(*args, **kwargs) 


	def __str__(self):
		return self.aboutUsTitle

class Links(models.Model):
	urlTitle = models.CharField(max_length=150, unique=True, verbose_name="Title of URL", blank=False)
	url = models.TextField(verbose_name="URL Link", blank=False)
	philatelyAuthor = models.ForeignKey(Philatelist, on_delete= models.CASCADE, verbose_name="Submitted By", blank=False)
	slug = models.SlugField(max_length=200, null=True, verbose_name="code",blank=False)
	date = models.DateTimeField(default = datetime.now, blank=True)
	
	class Meta:
		verbose_name_plural = 'Add Links'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.date, allow_unicode=True)
		super().save(*args, **kwargs) 


	def __str__(self):
		return self.urlTitle

CONTACTSTATUS = ((0,'Unread'),(1,'Read'))


class Contact(models.Model):
	firstName = models.CharField(max_length=200, verbose_name="First Name", blank=False)
	lastName = models.CharField(max_length=200, verbose_name="Last Name", blank=False)
	email = models.EmailField(max_length=254, verbose_name="Email", blank=False)
	content = models.TextField(max_length=2000, verbose_name="Message",blank=False)
	slug = models.SlugField(max_length=200, null=True, verbose_name="Key Code",help_text="Key Code can be anywords you like but without spaces.")
	subject = models.CharField(max_length=200, verbose_name="Subject", null=True, blank=False)
	status = models.IntegerField(choices=CONTACTSTATUS, default=0, blank=False)
	date = models.DateTimeField(default = datetime.now, blank=True)

	class Meta:
		ordering = ('-date',)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.date, allow_unicode=True)
		super().save(*args, **kwargs) 

	def __str__(self):
		return self.email





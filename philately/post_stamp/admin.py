from django.contrib import admin
from .models import Philatelist, Postal, History, Links, SubCategory, PostalImage, Contact
from django.contrib.auth.admin import UserAdmin


from django.forms import TextInput, Textarea

class PostalImageInline(admin.StackedInline):
	model = PostalImage
	max_num = 3
	extra = 1

class PostalAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("postTitle",)}
	inlines = [PostalImageInline]

admin.site.register(PostalImage)

class HistoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("aboutUsTitle",)}

# Register your models here.
class AccountAdministration(UserAdmin):
    search_fields = ('email', 'firstName')
    ordering = ('-startDate',)
    list_display = ('email', 'userName', 'firstName', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'userName', 'firstName', 'lastName',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'userName', 'firstName',  'lastName', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(Philatelist, AccountAdministration)

admin.site.register(History, HistoryAdmin)
admin.site.register(Postal,PostalAdmin)
admin.site.register(Links)
admin.site.register(SubCategory)
admin.site.register(Contact)
admin.site.site_header = "Christchurch Philatelic Foundation"
admin.site.site_title = "Christchurch Philatelic Foundation"
admin.site.index_title = "Christchurch Philatelic Foundation Web Administration"
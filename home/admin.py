from django.contrib import admin
from home.models import Aboutus, Chef, ContactMessage, Blog, Phone


class AboutusAdmin(admin.ModelAdmin):
    list_display = ['title','email', 'phone',]

class ChefAdmin(admin.ModelAdmin):
    list_display = ['title',]



class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'message', 'creat_at',]
    readonly_fields = ('name', 'surname', 'phone', 'email', 'message', 'creat_at',)
    list_filter = ['status']



class BlogAdmin(admin.ModelAdmin):
    list_display = ['title']

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone']

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Chef, ChefAdmin)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(Blog, BlogAdmin)

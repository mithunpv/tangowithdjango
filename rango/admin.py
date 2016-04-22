from django.contrib import admin
from models import *

# Register your models here.
admin.site.register(Category)

class PageAdmin(admin.ModelAdmin):
        model=Page	
	list_display=['title','category','url']

admin.site.register(Page,PageAdmin)
admin.site.register(ph1)
admin.site.register(phm1)

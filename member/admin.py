from django.contrib import admin

# Register your models here.
from .models import BoardMember

class BoardMemberAdmin(admin.ModelAdmin):
    list_display=('username','email','password')
admin.site.register(BoardMember,BoardMemberAdmin)

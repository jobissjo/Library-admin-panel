from django.contrib import admin
from .models import Member
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_name', 'taken_date', 'return_date', 'book_status']
    readonly_fields = ['name', 'book_name', 'taken_date', 'phone_number', 'email', 'address', 'member_id']
    search_fields = ['name', 'book_name']
    list_filter = ['book_status']
    list_per_page = 10
admin.site.register(Member, MemberAdmin)
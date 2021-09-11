from django.contrib import admin
from accounts.models import Account


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_image', 'user', 'gender', 'birthday')
    search_fields = ('user', )
    list_filter = ('gender', )
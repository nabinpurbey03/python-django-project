from django.contrib import admin

from database.models import Student, User, Payment


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    display_list = ('first_name', 'last_name', 'email', 'phone_number')

admin.site.register(Student, StudentAdmin)

class UserAdmin(admin.ModelAdmin):
    display_list = ('first_name', 'last_name', 'email', 'password')

admin.site.register(User, UserAdmin)

class PaymentAdmin(admin.ModelAdmin):
    display_list = ('amount', 'paid_date', 'channel', 'paid_to')

admin.site.register(Payment, PaymentAdmin)


from django.contrib import admin
from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    
    
    list_display = ['first_name', 'last_name', 'desigination', 'email_address', 'is_senior']
    search_fields = ['first_name', 'last_name', 'email_address']
    list_filter = ['desigination']
    ordering = ['first_name']
    list_per_page = 10
    list_display_links = ['email_address']
    # # list_editable = ['desigination']
    list_editable = ['is_senior']



    def is_senior(self, obj):
        return obj.desigination == 'Senior'
    is_senior.boolean = True


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)





# from django.contrib import admin
# from testapp.models import Employee

# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'desigination', 'email_address', 'is_senior']
#     list_filter = ['desigination', 'is_senior']
#     list_editable = ['is_senior']  # Optional if you want manual override

# admin.site.register(Employee, EmployeeAdmin)

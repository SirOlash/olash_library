from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from catalog.models import Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2", "first_name", "last_name", "email", "phone"),
            },
        ),
    )
    list_display = ['first_name', 'last_name', 'email', 'phone', 'dob','dod']
    list_display_links = ['email', 'dob', 'dod']
    list_editable = ["first_name", "last_name", "phone"]

# admin.site.register(Author)

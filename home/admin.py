from django.contrib import admin
#above one is written previosuly only
#from below all are written manually 
from home.models import Contact
# Register your models here.

admin.site.register(Contact)
#registered above model for django admin 
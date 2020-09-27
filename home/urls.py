from django.contrib import admin
from django.urls import path,include
from home import views

#Django admin header customization
admin.site.site_header="login to developer Ashish"
admin.site.site_title="welcome to Ashish's dashboard"
admin.site.index_title="welcome to this portal"

#try to comment line number 6,7,8 and then see impact on the 
#admin page and admin page after logged in



urlpatterns = [
    # path('admin/', admin.site.urls),
    #above statement don't write because you cant write admin twice so chance to give error

    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('projects',views.projects, name='projects'),
    path('contact',views.contact, name='contact'),
]

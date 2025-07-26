from django.contrib import admin
from django.urls import path 
from freelancer.views import about,home,contact,faq,services,projects,blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('index.html', home),
    path('about.html', about),
    path('contact.html',contact),
    path('services.html',services),
    path('projects.html',projects),
    path('blog.html', blog),  # ✅ Added blog path
    path('faq.html',faq),
    
    
]

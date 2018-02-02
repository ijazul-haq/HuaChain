from django.contrib import admin


from .models import UserProfile, Artwork
admin.site.register(UserProfile)
admin.site.register(Artwork)

from django.contrib import admin

# Register your models here.
from main.models import About, About_image, Mission, Contact, Subtitle, Logo, Banner, Nav_logo, Footer

admin.site.register(About)
admin.site.register(About_image)
admin.site.register(Mission)
admin.site.register(Contact)
admin.site.register(Subtitle)
admin.site.register(Logo)
admin.site.register(Banner)
admin.site.register(Nav_logo)
admin.site.register(Footer)
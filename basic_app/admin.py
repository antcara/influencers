from django.contrib import admin
from basic_app.models import Influencer,Race,Gender,Location,Category

# Register your models here.

admin.site.register(Influencer)
admin.site.register(Category)
admin.site.register(Race)
admin.site.register(Gender)
admin.site.register(Location)

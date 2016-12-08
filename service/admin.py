from django.contrib import admin
from .models import Apple_model, Client, Request, Type_of_part, Part

admin.site.register(Apple_model)
admin.site.register(Client)
admin.site.register(Request)
admin.site.register(Type_of_part)
admin.site.register(Part)
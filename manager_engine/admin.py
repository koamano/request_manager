from django.contrib import admin
from manager_engine.models import Request, History, Notes

# Register your models here.
admin.site.register(Request)
admin.site.register(History)
admin.site.register(Notes)

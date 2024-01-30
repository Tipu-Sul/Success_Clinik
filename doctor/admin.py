from django.contrib import admin
from . import models 
from django.utils.text import slugify

# Register your models here.
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']

    def save_model(self, request, obj, form, change):
        # Update the slug when editing an instance
        obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']

    def save_model(self, request, obj, form, change):
        # Update the slug when editing an instance
        obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)

admin.site.register(models.AvailableTime)
admin.site.register(models.Designation, DesignationAdmin)
admin.site.register(models.Specialization, SpecializationAdmin)
admin.site.register(models.Doctor)
admin.site.register(models.Review)

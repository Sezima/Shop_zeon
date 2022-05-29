from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms

from .models import *


class PublicAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Public
        fields = '__all__'


class PublicAdmin(admin.ModelAdmin):
    form = PublicAdminForm


@admin.register(Public)
class PublicAdmin(admin.ModelAdmin):
    form = PublicAdminForm


admin.site.register(Main)
admin.site.register(Advantages)
admin.site.register(Collection)
admin.site.unregister(Public)
admin.site.register(Public, PublicAdmin)

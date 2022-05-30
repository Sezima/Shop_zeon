from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin


from .models import *


class PublicAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Public
        fields = '__all__'


class PublicAdmin(admin.ModelAdmin):
    form = PublicAdminForm



class NewAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = New
        fields = '__all__'


class NewAdmin(admin.ModelAdmin):
    form = NewAdminForm


class AboutAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = About
        fields = '__all__'


class AboutAdmin(admin.ModelAdmin):
    form = AboutAdminForm

class AboutImageInline(admin.TabularInline):
    model = AboutImage
    max_num = 3
    min_num = 1


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    max_num = 8
    min_num = 1


class HelpImageAdminForm(forms.ModelForm):
    image = models.ImageField(upload_to='images')

    class Meta:
        model = HelpImage
        fields = '__all__'



class HelpImageAdmin(admin.ModelAdmin):
    form = HelpImageAdminForm



@admin.register(Public)
class PublicAdmin(admin.ModelAdmin):
    form = PublicAdminForm


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    form = NewAdminForm


@admin.register(HelpImage)
class PublicAdmin(admin.ModelAdmin):
    form = HelpImageAdminForm


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [AboutImageInline]
    form = AboutAdminForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    form = ProductAdminForm



admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)
admin.site.register(Main)
admin.site.register(Advantages)
admin.site.register(Collection)
admin.site.register(Help)
admin.site.unregister(Public)
admin.site.register(Public, PublicAdmin)
admin.site.unregister(New)
admin.site.register(New, NewAdmin)
admin.site.unregister(About)
admin.site.register(About, AboutAdmin)
admin.site.register(FooterTwo)
admin.site.register(Footer)
admin.site.unregister(HelpImage)
admin.site.register(HelpImage, HelpImageAdmin)

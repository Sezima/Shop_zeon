from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import *


class PublicAdminForm(forms.ModelForm):
    """Публичная оферта"""
    text = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Public
        fields = '__all__'


@admin.register(Public)
class PublicAdmin(admin.ModelAdmin):
    form = PublicAdminForm

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        else:
            return True
        return super(Public, self).has_add_permission(request)


class MainAdminForm(forms.ModelForm):
    """Главная страница"""

    class Meta:
        model = Main
        fields = '__all__'


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    form = MainAdminForm

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        else:
            return True
        return super(Main, self).has_add_permission(request)


class FooterAdminForm(forms.ModelForm):
    """Футер"""

    class Meta:
        model = Footer
        fields = '__all__'


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    form = FooterAdminForm

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        else:
            return True

        return super(Footer, self).has_add_permission(request)


class NewAdminForm(forms.ModelForm):
    """Новости"""
    text = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = New
        fields = '__all__'


class NewAdmin(admin.ModelAdmin):
    form = NewAdminForm


"""О нас"""


class AboutAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        verbose_name = "О нас"
        model = About
        fields = '__all__'


class AboutImageInline(admin.TabularInline):
    model = AboutImage
    max_num = 3
    min_num = 3


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [AboutImageInline]
    form = AboutAdminForm

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        else:
            return True

        return super(About, self).has_add_permission(request)


"""Товар"""


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


@admin.register(HelpImage)
class HelpImageAdmin(admin.ModelAdmin):
    form = HelpImageAdminForm

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        else:
            return True

        return super(HelpImage, self).has_add_permission(request)


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    form = NewAdminForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    form = ProductAdminForm


"""Заказ"""


class OrderInline(admin.TabularInline):
    model = Order
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_name', 'email', 'city']
    inlines = [OrderInline]


class CaseAdminForm:
    """Корзина"""

    class Meta:
        model = Case
        fields = '__all__'


class CaseAdmin(admin.ModelAdmin):
    form = CaseAdminForm


admin.site.register(User)

admin.site.register(Advantages)
admin.site.register(Collection)
admin.site.register(FooterTwo)
admin.site.register(BackCall)
admin.site.register(Case)
admin.site.register(Help)
admin.site.unregister(User)
admin.site.register(User, OrderAdmin)

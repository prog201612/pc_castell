from django.shortcuts import render
from django.views.generic.base import TemplateView

from store.models import Config, Panel
from store.helpers import translate_config, translate_panels, translate_product, translate_products_by_category

# I n d e x

class Index(TemplateView):

    template_name = "store/index.html"

    def get_context_data(self, **kwargs):
        # Recuperem la cookie de l'idioma
        language = self.request.COOKIES.get('language', self.request.LANGUAGE_CODE)
        context = super().get_context_data(**kwargs)
        if Config.objects.count() > 0:
            context['config'] = Config.objects.all()[0]
        if Panel.objects.count() > 0:
            context['panels'] = translate_panels(language)
        return context

# P r o d u c t s   B y   C l a s s

class ProductsByClass(TemplateView):

    template_name = "store/category_products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = kwargs['category_id']

        if Config.objects.count() > 0:
            context['config'] = Config.objects.all()[0]
        if Panel.objects.count() > 0:
            language = self.request.COOKIES.get('language', self.request.LANGUAGE_CODE)
            context['category'] = translate_products_by_category(language, category_id)
        return context


# A b o u t   U s

class AboutUs(TemplateView):

    template_name = "store/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        language = self.request.COOKIES.get('language', self.request.LANGUAGE_CODE)
        print("language:", language)
        context['config'] = translate_config(language)
        context['language'] = language
        return context


# P r o d u c t

class Product(TemplateView):

    template_name = "store/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        language = self.request.COOKIES.get('language', self.request.LANGUAGE_CODE)
        context['product'] = translate_product(language, kwargs['product_id'])
        return context
from django.shortcuts import render
from django.views.generic.base import TemplateView

from store.models import Config, Panel
from store.helpers import translate_panels, translate_product, translate_products_by_category

# I n d e x

class Index(TemplateView):

    template_name = "store/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Config.objects.count() > 0:
            context['config'] = Config.objects.all()[0]
        if Panel.objects.count() > 0:
            context['panels'] = translate_panels(self.request.LANGUAGE_CODE)
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
            context['category'] = translate_products_by_category(self.request.LANGUAGE_CODE, category_id)
        return context


# A b o u t   U s

class AboutUs(TemplateView):

    template_name = "store/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Config.objects.count() > 0:
            context['config'] = Config.objects.all()[0]
        return context


# P r o d u c t

class Product(TemplateView):

    template_name = "store/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = translate_product(self.request.LANGUAGE_CODE, kwargs['product_id'])
        return context
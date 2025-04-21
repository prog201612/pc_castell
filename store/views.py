from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.translation import get_language_from_request

from store.models import Config, Panel
from store.helpers import translate_config, translate_panels, translate_product, translate_products_by_category

# H e l p e r s

def get_language(request):
    """
    Helper function to get the language from the request.
    """
    # Si l'usuari ha seleccionat un idioma ho recuperem de la request
    if "language" in request.COOKIES:
        return request.COOKIES.get('language').lower()[:2]
    
    # Obtenir l'idioma preferit del navegador  
    return get_language_from_request(request).lower()[:2]


# I n d e x

class Index(TemplateView):

    template_name = "store/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Recuperem la cookie de l'idioma
        language = get_language(self.request)
        context['language'] = language

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
        language = get_language(self.request)
        context['language'] = language

        if Config.objects.count() > 0:
            context['config'] = Config.objects.all()[0]
        if Panel.objects.count() > 0:
            context['category'] = translate_products_by_category(language, category_id)
        return context


# A b o u t   U s

class AboutUs(TemplateView):

    template_name = "store/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        language = get_language(self.request)
        context['language'] = language
        print("language:", language)
        context['config'] = translate_config(language)
        return context


# P r o d u c t

class Product(TemplateView):

    template_name = "store/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        language = get_language(self.request)
        context['language'] = language
        context['product'] = translate_product(language, kwargs['product_id'])
        return context
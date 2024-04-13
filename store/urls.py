from django.urls import path

from store.views import Index, ProductsByClass, AboutUs, Product

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('product/<int:product_id>', Product.as_view(), name='product'),
    path('category/<int:category_id>', ProductsByClass.as_view(), name='category-products'),
    path('aboutus/', AboutUs.as_view(), name='about-us'),
]

app_name = 'store'
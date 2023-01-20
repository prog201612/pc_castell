from django.urls import path

from store.views import Index, ProductsByClass, AboutUs

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('category/<int:category_id>', ProductsByClass.as_view(), name='category-products'),
    path('aboutus/', AboutUs.as_view(), name='about-us'),
]

app_name = 'store'
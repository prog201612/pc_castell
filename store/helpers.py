from django.shortcuts import get_object_or_404

from store.models import Panel, Translate, ProductCategory, Product

def translate_text(language, text):
    if language == 'ca':
        return text
    translated_text = Translate.objects.filter(ca=text)
    if len(translated_text) == 0:
        return text
    return translated_text[0].es

def translate_product(language, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_dic = {
        "id": product.id,
        "name": translate_text(language, product.name),
        "categoria": product.categoria,
        "description": translate_text(language, product.description),
        "pvp": product.pvp,
        "discount_percentage": product.discount_percentage,
        "image": product.image,
        "new_price": product.pvp - (product.pvp * product.discount_percentage / 100)
    }
    return product_dic

def translate_products_by_category(language, category_id):
    category = get_object_or_404(ProductCategory, pk=category_id)
    category_dic = {
        "name": translate_text(language, category.name),
        "image": category.image
    }

    category_dic["products"] = []
    products = Product.objects.filter(categoria=category)
    for product_row in products:
        product = translate_product(language, product_row.id)
        category_dic["products"].append(product)
        
    return category_dic

def translate_panels(language):
    panels = []
    for panel in Panel.objects.all():
        # P a n e l l
        panel_dic = {
            "name": translate_text(language, panel.name),
            "order": panel.order,
            "type": panel.type,
            "autoplay": panel.autoplay
        }

        # C a r o u s e l    d e l   p a n e l l
        panel_dic["carousel"] = []
        for carousel_row in panel.panelcarousel_set.all():
            carousel = {
                "panel": carousel_row.panel,
                "title": translate_text(language, carousel_row.title),
                "description": translate_text(language, carousel_row.description),
                "image": carousel_row.image,
                "image_mobile": carousel_row.image_mobile
            }
            panel_dic["carousel"].append(carousel)

        # C a t e g o r i e s   d e l   p a n e l l
        panel_dic["categories"] = []
        for category_row in panel.panelcategories_set.all():
            category = {
                "name": translate_text(language, category_row.product_category.name),
                "image": category_row.product_category.image,
                "link": f"/category/{category_row.product_category.id}"
            }
            panel_dic["categories"].append(category)

        # P r o d u c t e s   d e l   p a n e l l
        panel_dic["products"] = []
        for product_row in panel.panelproducts_set.all():
            product = translate_product(language, product_row.product.id)
            panel_dic["products"].append(product)
        panel_dic["products_panel_width"] = len(panel_dic["products"]) * 300
        panels.append(panel_dic)

    return panels

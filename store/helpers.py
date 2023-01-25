from django.shortcuts import get_object_or_404

from store.models import Panel, Translate, ProductCategory, Product

def translate_text(language, text):
    if language == 'ca':
        return text
    translated_text = Translate.objects.filter(ca=text)
    if len(translated_text) == 0:
        return text
    return translated_text[0].es


def translate_products_by_category(language, category_id):
    category = get_object_or_404(ProductCategory, pk=category_id)
    category_dic = {
        "name": translate_text(language, category.name),
        "image": category.image
    }

    category_dic["products"] = []
    products = Product.objects.filter(categoria=category)
    for product_row in products:
        product = {
            "name": translate_text(language, product_row.name),
            "categoria": product_row.categoria,
            "description": translate_text(language, product_row.description),
            "pvp": product_row.pvp,
            "discount_percentage": product_row.discount_percentage,
            "image": product_row.image,
            "new_price": product_row.pvp - (product_row.pvp * product_row.discount_percentage / 100)
        }
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
                "image": carousel_row.image
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
            product = {
                "name": translate_text(language, product_row.product.name),
                "categoria": product_row.product.categoria,
                "description": translate_text(language, product_row.product.description),
                "pvp": product_row.product.pvp,
                "discount_percentage": product_row.product.discount_percentage,
                "image": product_row.product.image,
                "new_price": product_row.product.pvp - (product_row.product.pvp * product_row.product.discount_percentage / 100)
            }
            panel_dic["products"].append(product)
        panel_dic["products_panel_width"] = len(panel_dic["products"]) * 300
        panels.append(panel_dic)

    return panels
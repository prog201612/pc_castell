from django.contrib import admin

from store import models

# admin.site.register(models.Config)
admin.site.register(models.ProductCategory)
admin.site.register(models.Product)
admin.site.register(models.Translate)

###############
# C O N F I G ###################################################################
###############

@admin.register(models.Config)
class ConfigAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

#############
# P A N E L #####################################################################
#############

# I N L I N E S

class PanelCarouselInline(admin.TabularInline):
    model = models.PanelCarousel
    extra = 0

class PanelCategoriesInline(admin.TabularInline):
    model = models.PanelCategories
    extra = 0

class PanelProductsInline(admin.TabularInline):
    model = models.PanelProducts
    extra = 0

# A D M I N

@admin.register(models.Panel)
class PanelAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/en/dev/ref/models/instances/#django.db.models.Model.get_FOO_display
    list_display = ["name", "order", "get_type_display"]
    inlines = [
        PanelCarouselInline,
        PanelCategoriesInline,
        PanelProductsInline
    ]
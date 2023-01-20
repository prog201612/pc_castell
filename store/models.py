from django.db import models


class Config(models.Model):
    """
    Taula d'una sola fila per guardar paràmetres de configuració
    """
    name = models.CharField("Nom", max_length=100)
    logo = models.ImageField("Logo", upload_to='config/', blank=True, null=True)
    about_us = models.TextField("Sobre nosaltres", blank=True, null=True)
    address = models.TextField("Direcció", blank=True, null=True)
    phone = models.CharField("Telèfon", max_length=20, blank=True, null=True)
    email = models.EmailField("Correu electrònic", max_length=70, blank=True, null=True)

    def save(self, *args, **kwargs):
        # si ja hi ha un registre sobreescribim el pk amb el pk del primer registre
        if self.__class__.objects.count():
            # Al posar el mateix pk farà que doni un error d'integritat de dades
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Translate(models.Model):
    ca = models.CharField("Catalè", max_length=250)
    es = models.CharField("Castellano", max_length=250)

    def __str__(self) -> str:
        return self.ca


#################
# P R O D U C T #################################################################
#################

class ProductCategory(models.Model):
    """
    Per poder classificar els productes segons la seva categoria
    """
    name = models.CharField("Nom", max_length=50, blank=True, null=True)
    image = models.ImageField("Imatge", upload_to='product_category/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """
    Productes, en principi pot ser un producte físic o un servei.
    """
    name = models.CharField("Nom", max_length=50, blank=True, null=True)
    categoria = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.TextField("Descripció", blank=True, null=True)
    pvp = models.DecimalField("Preu venta públic", max_digits=6, decimal_places=2, default=0)
    discount_percentage = models.IntegerField("Desconte (%)", default=0)
    image = models.ImageField("Imatge", upload_to='product/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name


#############
# P A N E L #####################################################################
#############

CAROUSEL_CHOICE = 1
PRODUCT_CATEGORY_CHOICE = 2
PRODUCT_CHOICE = 3
PANEL_CHOICES = (
    (CAROUSEL_CHOICE, "CAROUSEL"),
    (PRODUCT_CATEGORY_CHOICE, "PRODUCT CATEGORY"),
    (PRODUCT_CHOICE, "PRODUCT"),
)

class Panel(models.Model):
    """
    Els diferents panells amb informació que poden anar al index.html
    """
    name = models.CharField("Nom del panell", max_length=50, blank=True, null=True)
    order = models.IntegerField("Ordre", default=0)
    type = models.IntegerField("Tipus de panell", choices=PANEL_CHOICES, default=CAROUSEL_CHOICE)
    autoplay = models.BooleanField("Autoplay (Només per Carousels)", default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('order',)


class PanelCarousel(models.Model):
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    title = models.CharField("Títol", max_length=50, blank=True, null=True)
    description = models.CharField("Descripció", max_length=250, blank=True, null=True)
    image = models.ImageField("Imatge", upload_to='carousel/', blank=True, null=True)

class PanelCategories(models.Model):
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


class PanelProducts(models.Model):
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)





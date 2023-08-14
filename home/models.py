from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False, verbose_name="Kategori İsmi")
    title_en = models.CharField(max_length=60, blank=False, null=False, verbose_name="Kategori İsmi (İngilizce)")
    image = models.ImageField(verbose_name="Kategori Görseli", upload_to="categories/", blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=True,
        verbose_name="Sırala"
    )

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
        ordering = ('my_order',)


    def __str__(self):
        return self.title

    def get_image(self):
        return self.image.url

    def get_product_count(self):
        return self.products.count()

from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=Category)
def set_my_order_to_id(sender, instance, **kwargs):
    if not instance.my_order:
        instance.my_order = instance.id

class Product(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False, verbose_name="Ürün İsmi")
    title_en = models.CharField(max_length=60, blank=False, null=False, verbose_name="Ürün İsmi İngilizce")
    image = models.ImageField(verbose_name="Ürün Görseli", upload_to="categories/product", blank=False, null=False)
    price = models.FloatField(verbose_name="Ürün Fiyatı", blank=False, null=False, default=0.0)
    detail = models.CharField(max_length=60, blank=True, null=True, verbose_name="Ürün Açıklaması / İçindekiler")
    detail_en = models.CharField(max_length=60, blank=True, null=True, verbose_name="Ürün Açıklaması / İçindekiler  (İngilizce)")
    category = models.ForeignKey(Category, blank=False, null=False, verbose_name="Kategori", on_delete=models.CASCADE, related_name="products")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=True,
        verbose_name="Sırala"
    )

    def __str__(self):
        return self.title

    def get_image(self):

        return self.image.url
    class Meta:
        ordering = ('my_order',)

        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"

@receiver(pre_save, sender=Product)
def set_my_order_to_id(sender, instance, **kwargs):
    if not instance.my_order:
        instance.my_order = instance.id


class SortableBook(models.Model):
    title = models.CharField(
        "Title",
        max_length=255,
    )


from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify


class BaseProduct(models.Model):

    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                validators=[MinValueValidator(0)])
    slug = models.SlugField(unique=True,
                            editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            self.slug = slugify(f"{self.title}-{self.id}")
            return super().save(update_fields=["slug"])
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} with id {self.id} costs {self.price}"

    class Meta:
        abstract = True
        ordering = ['title']


class PartModel(BaseProduct):

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

    manufacturer = models.CharField(max_length=50)

class ServiceModel(BaseProduct):

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    description = models.TextField(blank=True,
                                   null=True)

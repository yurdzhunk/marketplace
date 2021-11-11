from django.db.models import CharField
from model_utils.models import TimeStampedModel


class Product(TimeStampedModel):
    title = CharField(verbose_name="Product title", max_length=255, unique=True)

    class Meta:
        db_table = "Products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title
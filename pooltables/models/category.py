from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50)
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    @staticmethod
    def get_all_subcategories():
        return SubCategory.objects.all()

    class Meta:
        ordering = ('name', )
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name

from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    titele = models.CharField(max_length=155)
    mazmuni = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titele

class News(models.Model):
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    titele = models.CharField(max_length=255, null=False)
    mazmuni = models.TextField(null=False)
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="news-image", null=True, blank=True)
    holati = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titele
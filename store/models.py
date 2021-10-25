from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Contact_info(models.Model):
    msg_id = models.AutoField
    name = models.CharField(max_length = 80)
    email = models.CharField(max_length = 80)
    phone = models.CharField(max_length = 10)
    desc = models.TextField(max_length = 500)
    date = models.DateField()
    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    pub_desc = models.DateField()
    image = models.ImageField(upload_to="index/images", default="")

    def __str__(self):
        return self.product_name
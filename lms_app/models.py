from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):

    status_book = [
        ('availbel' , 'availbel'),
        ('rental' , 'rental'),
        ('sold' , 'sold'),
    ]

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    photo_book = models.ImageField(upload_to = 'photos/books/' , null = True , blank = True)
    photo_author = models.ImageField(upload_to = 'photos/owners/' , null = True , blank = True)
    Discription = models.TextField(null=True , blank=True)
    pages = models.IntegerField(null=True , blank=True)
    pdf_file = models.FileField(null=True , blank=True , upload_to = 'Books')
    price = models.DecimalField(null=True , blank=True ,max_digits=5 , decimal_places=2)
    retal_price_day = models.DecimalField(null=True , blank=True ,max_digits=5 , decimal_places=2)
    retal_period = models.IntegerField(null=True , blank=True)
    total_rental = models.DecimalField(null=True , blank=True ,max_digits=5 , decimal_places=2)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50 , choices=status_book , null=True , blank=True)
    category = models.ForeignKey(Category , on_delete=models.PROTECT , null=True , blank=True)


    def __str__(self):
        return self.title



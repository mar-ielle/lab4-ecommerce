from django.db import models

# Create your models here.

class BaseModel(models.Model):
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class User(BaseModel):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_address = models.EmailField()
	shipping_address = models.CharField(max_length=200)

class Product(BaseModel):
	id = models.AutoField(primary_key=True)
	name  = models.TextField()
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)

class Cart(BaseModel):
	id = models.AutoField(primary_key=True)
	cart_code = models.CharField(max_length=10)
	products = models.ManyToManyField(Product)
	is_paid = models.BooleanField(default=False)
	user = models.ForeignKey('User', on_delete=models.CASCADE)

	def total_price(self):
		sum = 0
		for product in self.products:
			sum += product.price
		return sum
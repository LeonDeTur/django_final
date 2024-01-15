import django
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(max_length=20)
    address = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'name: {self.name}, email: {self.email}, phone: {self.phone}, address: {self.address}'


class Goods(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    amount = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'name: {self.name}, description: {self.description}, price: {self.price}, amount: {self.amount}'

    def total_price(self):
        return self.price


class Order(models.Model):
    price = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)
    client_id = models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internet_shop.Client')
    goods_id = models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internet_shop.Goods')

    def __str__(self):
        return f'price: {self.price}, client_id: {self.client_id}, goods_id: {self.goods_id}'

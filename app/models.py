from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    street = models.CharField(max_length=100)
    house_num = models.CharField(max_length=10)
    appartaments = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.city} {self.street} st., num:{self.house_num}" + f", app:{self.appartaments}" if self.appartaments else ""

class UserList(models.Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=320)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return self.username
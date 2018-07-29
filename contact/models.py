from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.surname, self.description)


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    blockNumber = models.IntegerField()
    apartmentNumber = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.city, self.street, self.blockNumber, self.apartmentNumber)


class Phone(models.Model):
    types = (
        (0, 'Niezdefiniowany'),
        (1, 'Domowy'),
        (2, 'Służbowy'),
        (3, 'Prywatny'),
    )
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type = models.CharField(max_length=1, choices=types, default=0)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.number, self.type)


class Email(models.Model):
    types = (
        (0, 'Niezdefiniowany'),
        (1, 'Domowy'),
        (2, 'Służbowy'),
        (3, 'Prywatny'),
    )
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=64)
    type = models.CharField(max_length=1, choices=types, default=0)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.email, self.type)


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return '{} {}'.format(self.id, self.name)

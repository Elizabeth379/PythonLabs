from django.db import models
from django.urls import reverse


class MedicationCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'MedicationCategory'
        verbose_name_plural = 'MedicationCategories'

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Department'

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee'

    def __str__(self):
        return self.name


class Medication(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    #photo = models.ImageField(upload_to="photos/%Y/%n/%d/", null=True)
    category = models.ForeignKey(MedicationCategory, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Medication'
        verbose_name_plural = 'Medications'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bying', kwargs={'bying_id': self.pk})

    def get_absolute_url1(self):
        return reverse('thanks', kwargs={'thanks_id': self.pk})


class Sale(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return f"{self.medication.title} - {self.employee.name}"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class Provider(models.Model):
    ENTITY_CHOICES = [
        ("O", "Organization"),
        ("I", "Individual")
    ]
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female")
    ]

    NPI = models.IntegerField(verbose_name="National Provider Identifier")
    Last_Name = models.CharField(max_length=64)
    First_Name = models.CharField(max_length=64)
    MI = models.CharField(verbose_name="Middle Initial", max_length=8, blank=True)
    Credentials = models.CharField(max_length=128)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Entity_Type = models.CharField(max_length=1, choices=ENTITY_CHOICES)
    MPI = models.CharField(verbose_name="Medicare Participation Indicator", max_length=8)

    def __str__(self):
        return f"{self.Last_Name}, {self.First_Name}"

class Address(models.Model):
    Provider = models.ForeignKey(to=Provider, null=True, on_delete=models.CASCADE)
    Street_Address_1 = models.CharField(max_length=256)
    Street_Address_2 = models.CharField(max_length=256, blank=True)
    City = models.CharField(max_length=128)
    State = models.CharField(max_length=2)
    Zip5 = models.CharField(max_length=5)
    Country = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.Street_Address_1}, {self.City}, {self.State}"


class BeneficiaryData(models.Model):
    Provider = models.ForeignKey(to=Provider, null=True, on_delete=models.CASCADE)

class Payment(models.Model):
    Provider = models.ForeignKey(to=Provider, null=True, on_delete=models.CASCADE)

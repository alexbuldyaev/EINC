from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Usercli(models.Model):
    email = models.EmailField()
    nickname = models.CharField(max_length=50) 
    password = models.CharField(max_length=30) 
    InsID = models.IntegerField()
    OwnID = models.IntegerField()
    DriID = models.IntegerField()

class Insured(models.Model):
    UsrID = 
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    BDay = models.DateField()
    AddressFact = models.CharField(max_length=100)
    AddressRegistr = models.CharField(max_length=100)
    PasspNumb = models.IntegerField()
    PasspDate = models.DateField()

class Owner(models.Model):
    UsrID = 
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    BDay = models.DateField()
    AddressFact = models.CharField(max_length=100)
    AddressRegistr = models.CharField(max_length=100)
    PasspNumb = models.IntegerField()
    PasspDate = models.DateField()

class Owner(models.Model):
    UsrID = 
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    BDay = models.DateField()
    PasspNumb = models.IntegerField()
    PasspDate = models.DateField()
    DrLicNumb = models.IntegerField()
    DrLicDate = models.DateField()
    DrLicIfVal = models.BooleanField()

class Order(models.Model):
    UsrID = 
    PolNumb = models.
    PolType = models.
    MonSum  = models.IntegerField()
    StatusLoc  = models.ForeignKey(Status)

class InsComp(models.Model):
    CompName = models.CharField(max_length=200)
    CompCont = models.CharField(max_length=200)

class CalcRul(models.Model):
    CompID = models.ForeignKey(InsCompID)
    PolicyType = models.CharField(max_length=10)
    Rul1 = models.IntegerField()

class PolicyCar(models.Model):
    PolicyType = models.BooleanField()
    CompName = models.ForeignKey(InsCompID)
    Status = models.CharField(max_length=20)
    MonSum = models.IntegerField()
    CarName = models.CharField(max_length=20)
    CarDate = models.DateField()
    CarVIN = models.IntegerField()
    CarRegNum = models.CharField(max_length=10)
    CarDocID = models.IntegerField()
    CarDocType = models.CharField(max_length=10)
    CarDocDate = models.DateField()
    Insured =
    Owner = 
    Driver =
    User = 

class PolicyHome(models.Model):
    PolicyType = models.BooleanField()
    CompName = models.ForeignKey(InsCompID)
    Status = models.CharField(max_length=20)
    MonSum = models.IntegerField()
    HomeName = models.CharField(max_length=20)
    HomeAddr = models.CharField(max_length=20)
    HomeDate = models.DateField()
    HomeType = models.CharField(max_length=10)
    HomeMater = models.CharField(max_length=10)
    Insured =
    Owner = 
    User = 






class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

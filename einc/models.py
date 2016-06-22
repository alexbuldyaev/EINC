from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class InsComp(models.Model):
    CompName = models.CharField(max_length=200)
    CompCont = models.CharField(max_length=200)
    def __str__(self):
        return '%s' % (self.CompName)

class CalcRul(models.Model):
    CompID = models.ForeignKey(InsComp)
    PolicyType = models.CharField(max_length=10)
    Rul1 = models.IntegerField()


class Insured(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    BDay = models.DateField()
    AddressFact = models.CharField(max_length=100)
    AddressRegistr = models.CharField(max_length=100)
    PasspNumb = models.IntegerField()
    PasspDate = models.DateField()
    def __str__(self):
        return '%s' % (self.Name)

class Owner(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    BDay = models.DateField()
    AddressFact = models.CharField(max_length=100)
    AddressRegistr = models.CharField(max_length=100)
    PasspNumb = models.IntegerField()
    PasspDate = models.DateField()
    def __str__(self):
        return '%s' % (self.Name)

class Driver(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    BDay = models.DateField()
    PasspNumb = models.IntegerField()
    PasspDate = models.DateField()
    DrLicNumb = models.IntegerField()
    DrLicDate = models.DateField()
    DrLicIfVal = models.BooleanField()
    def __str__(self):
        return '%s' % (self.Name)


class Usercli(models.Model):
    usrID = models.IntegerField()
    user = models.OneToOneField(User)
    InsID = models.OneToOneField(Insured, on_delete = models.CASCADE, primary_key = False,)
    OwnID = models.OneToOneField(Owner, on_delete = models.CASCADE, primary_key = False,)
    DriID = models.OneToOneField(Driver, on_delete = models.CASCADE, primary_key = False,)

class PolicyType(models.Model):
    TypeName = models.CharField(max_length=200)
    def __str__(self):
        return '%s' % (self.TypeName)   

class Status(models.Model):
    StatName = models.CharField(max_length=200)
    def __str__(self):
        return '%s' % (self.StatName) 


class PolicyCar(models.Model):
    PolicyID = models.IntegerField()
    PolicyType = models.ForeignKey(PolicyType)
    CompName = models.ForeignKey(InsComp)
    Status = models.ForeignKey(Status)
    MonSum = models.IntegerField()
    CarName = models.CharField(max_length=20)
    CarVIN = models.IntegerField()
    CarRegNum = models.CharField(max_length=10)
    CarDocID = models.IntegerField()
    CarDocType = models.CharField(max_length=10)
    Insured = models.ForeignKey(Insured)
    Owner = models.ForeignKey(Owner)
    Driver = models.ForeignKey(Driver)
    User = models.ForeignKey(Usercli)
    def __str__(self):
        return '%s' % (self.PolicyID) 

class PolicyHome(models.Model):
    PolicyID = models.IntegerField()
    PolicyType = models.ForeignKey(PolicyType)
    CompName = models.ForeignKey(InsComp)
    Status = models.ForeignKey(Status)
    MonSum = models.IntegerField()
    HomeName = models.CharField(max_length=20)
    HomeAddr = models.CharField(max_length=20)
    HomeDate = models.DateField()
    HomeType = models.CharField(max_length=10)
    HomeMater = models.CharField(max_length=10)
    Insured = models.ForeignKey(Insured)
    Owner = models.ForeignKey(Owner)
    User = models.ForeignKey(Usercli)
    def __str__(self):
        return '%s' % (self.PolicyID) 



class Order(models.Model):
    UserID = models.OneToOneField(Usercli,  on_delete = models.CASCADE, primary_key = False,)
    PolCar = models.OneToOneField(PolicyCar , on_delete = models.CASCADE, primary_key = False,)




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

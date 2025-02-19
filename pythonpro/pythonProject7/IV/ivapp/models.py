from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class colreg(models.Model):
    name=models.CharField(max_length=30,)
    collegeid=models.CharField(max_length=20,unique=True)
    phoneno=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30,validators=[
            RegexValidator(
                regex='^(?=.\d)(?=.[a-z])(?=.[A-Z])(?=.[!@#$%^&*()_+}{":;\']).{8,}$',
                message='Password must contain at least one digit, one uppercase letter, one lowercase letter, and one special character.',
                code='invalid_password'
        )])
    profile = models.FileField(null=True)

    def __str__(self):
        return self.name

class compreg(models.Model):
    name=models.CharField(max_length=30)
    compid = models.CharField(max_length=20,unique=True)
    addr = models.TextField()
    phoneno=models.IntegerField()
    email=models.EmailField()
    lisence=models.FileField()
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    status=models.CharField(max_length=20)
    profile=models.FileField(null=True)

    def __str__(self):
        return self.name


class collegedept(models.Model):
    name = models.ForeignKey(colreg,on_delete=models.CASCADE,null=True)
    cname = models.ForeignKey(compreg,on_delete=models.CASCADE,null=True)
    coldepartment=models.CharField(max_length=15)
    noofstudents=models.IntegerField()
    time=models.CharField(max_length=10)
    datetime=models.DateTimeField()
    status=models.CharField(max_length=20)
    fprice=models.IntegerField(null=True)
    paid=models.CharField(max_length=10,default='Not Paid')


    def __str__(self):
        return self.coldepartment


class comppro(models.Model):
    cname = models.ForeignKey(compreg, on_delete=models.CASCADE,null=True)
    collegename=models.CharField(max_length=20)
    projectimg=models.FileField(max_length=20)
    department=models.CharField(max_length=20)
    date=models.DateField()
    projectdescr=models.TextField()


class cabout(models.Model):
    cname = models.ForeignKey(compreg, on_delete=models.CASCADE, null=True)
    native=models.TextField()
    achievements=models.CharField(max_length=40,null=True)
    fprice=models.IntegerField(null=True)
    disc=models.TextField(null=True)

class Reviews(models.Model):
    user = models.ForeignKey(colreg, on_delete=models.CASCADE)
    comname = models.CharField(max_length=40)
    review = models.TextField()
    def str(self):
        return self.review
class contactus(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    message=models.CharField(max_length=300)
    def __str__(self):
        return self.name
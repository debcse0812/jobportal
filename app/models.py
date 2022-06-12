from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)# let bydefault company/candiadte is active, we can later make them deactive as per requirement
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True) # when it is created
    is_updated = models.DateTimeField(auto_now_add=True)


class Candidate(models.Model):
     user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
     firstname = models.CharField(max_length=50)
     lastname = models.CharField(max_length=50)
     contact = models.CharField(max_length=50)
     state = models.CharField(max_length=50)
     city = models.CharField(max_length=50)
     address = models.CharField(max_length=50)
     dob = models.CharField(max_length=50)
     gender = models.CharField(max_length=50)
     profile_pic = models.ImageField(upload_to="app/img/candidate")


class Company(models.Model):
     user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
     firstname = models.CharField(max_length=50)
     lasname = models.CharField(max_length=50)
     company_name = models.CharField(max_length=50)
     state = models.CharField(max_length=50)
     city = models.CharField(max_length=50)
     contact = models.CharField(max_length=50)
     address = models.CharField(max_length=150)
     logo = models.ImageField(upload_to="app/img/company")



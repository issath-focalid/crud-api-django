# from django.db import models
# from django.forms import ModelForm, Textarea


# class Student(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()

#     class Meta:
#         db_table = "profile_info"


from django.db import models
import datetime
import os


# def filepath(request, filename):
#     timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#     new_filename = "%s%s", (timeNow, filename)
#     return os.path.join('images/', new_filename)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    description = models.CharField(max_length=1000, null=True)
    profile_pic = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "profile_info"

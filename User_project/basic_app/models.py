from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # In a one-to-one relationship,
    # one record in a table is associated with one and only one record in another table.
    # For example, in a school database, each student has only one student ID,
    # and each student ID is assigned to only one person.

    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

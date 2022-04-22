from django.db import models


# Create your models here.

class TbUser(models.Model):
    user_email = models.EmailField(primary_key=True, unique=True, max_length=50)
    user_pw = models.CharField(max_length=500)
    user_nick = models.CharField(max_length=30)

    def __str__(self):
        return self.user_email

    class Meta:
        db_table = 'tb_user'

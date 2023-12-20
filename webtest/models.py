from django.db import models



# Create your models here.

#the model work for receiving acknowledges from users 
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    desc = models.TextField()
    communication_mail_status = models.CharField(max_length=3,default='Yes')
    date = models.DateField()
    

    def __str__(self):
        return self.name

    

from django.db import models

# Create your models here.
#model is way to tell that i want to create a 
#database in term table and have row and column

#it will be empty initially expect the 1st line
#and remainng all we have to write here
#For more detail google django model documentation 

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()

#in above one name email phone desc should be same as in view from where it is coming  
    
    def __str__(self):
        return self.name+"-"+self.email
    #comment line number 19 and 20 and then see the 
    #difference in the database name(contacts) in admin page




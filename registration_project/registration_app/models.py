from django.db import models

# Create your models here.


# creating model for educationnal qaulifications 

class Education(models.Model):
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.qualification
    

# creating model for skill
    
class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

# creating model for registration 
    
class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField()
    higher_education = models.ForeignKey(Education, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from django.db import models

# Create your models here.

class Class(models.Model):
    department = models.CharField(max_length=50)
    year = models.IntegerField()
    section = models.CharField(max_length=2, default= 'A')
        
    def __str__(self):
        return f'Year {self.year} - Sec {self.section}'
        
        
class Subject(models.Model):
    name = models.CharField(max_length=50)
    sclass = models.ManyToManyField(Class)
    
    def __str__(self):
        return f'{self.name}'
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    uid = models.IntegerField(unique= True)
    email = models.EmailField(max_length=254, blank= True, null=True)
    sclass = models.ManyToManyField(Class)

    def __str__(self):
        return f'{self.name}'

    
    # def save(self, *args, **kwargs):
        # super(Student, self).save(*args, **kwargs)



class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,primary_key=False)
    attendance = models.IntegerField(default=0)
    student = models.ForeignKey(Student,on_delete=models.CASCADE, primary_key=False)
    
    def __str__(self):
        return f'{self.attendance} - {self.subject} - {self.student.name}'


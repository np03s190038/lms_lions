from django.db import models

# Create your models here.

class Books(models.Model): #name of the table
    book_Name = models.CharField(max_length=100)
    author_Name = models.CharField(max_length=50)
    author_Image = models.ImageField(upload_to='images/')
    genre = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.book_Name

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class IssueBook(models.Model):
    student_Name = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Books, null=True, on_delete=models.SET_NULL)
    issue_date=  models.DateField

    def __str__(self):
        return self.student_Name

class AddStudent(models.Model):
    student_Name = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL, related_name='new_student')
    student_email = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    phone = models.IntegerField()
    date_joined = models.DateField

    def __str__(self):
        return self.student_Name


    
     



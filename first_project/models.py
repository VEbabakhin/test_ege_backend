from django.contrib.auth import get_user_model
from django.contrib.auth.middleware import get_user
from django.db import models
from django.contrib.auth.models import AbstractUser

user = get_user_model()


class Teacher(user):
    name = models.CharField(max_length=255)


class Student(user):
    name = models.CharField(max_length=255)

class Theory(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    created_dttm = models.DateTimeField(auto_now_add=True)

class Assignment(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    file = models.FileField(upload_to='files', blank=True, null=True)
    image = models.ImageField(upload_to='files', blank=True, null=True)
    answer = models.CharField(max_length=255)
    created_dttm = models.DateTimeField(auto_now_add=True)

class Variant(models.Model):
    name = models.CharField(max_length=255)
    assignment = models.ManyToManyField(Assignment, related_name='assignments_variant')

class Answer(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assignment')
    status = models.IntegerField(choices=[(0, 'na'), (1, True), (2, False)])
    answer = models.CharField(max_length=255)

class VariantAnswer(models.Model):
    name = models.CharField(max_length=255)
    assignment = models.ManyToManyField(Answer, related_name='assignments')

class StudentVariant(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name='variant')
    is_finished = models.BooleanField(default=False)
    answers = models.ForeignKey(VariantAnswer, on_delete=models.CASCADE, related_name='answers')

class StudentsGroup(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(Student, related_name='students_group')
    teachers = models.ManyToManyField(Teacher, related_name='teachers')


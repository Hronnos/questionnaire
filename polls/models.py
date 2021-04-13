from django.db import models
from django.conf import settings


class Question(models.Model):
    title = models.CharField(max_length=255)
    visible = models.BooleanField(default=False)
    max_points = models.FloatField()

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    points = models.FloatField()
    lock_other_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice.title


class Homework(models.Model):
    text = models.TextField()
    max_points = models.FloatField()

    def __str__(self):
        return self.text


class DoneHomework(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=255, blank=True)
    student_hw = models.ForeignKey(DoneHomework, on_delete=models.CASCADE, null=True)
    points = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.title

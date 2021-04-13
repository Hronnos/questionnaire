from django.contrib import admin
from .models import Question, Answer, Choice, Homework, DoneHomework, Review


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'visible',
        'max_points',
    )


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'question',
        'points',
        'lock_other_answer',
    )
    list_filter = ('question',)



class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
    )
    list_filter = ('user',)


class HomeworkAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'max_points',
    )


class DoneHomeworkAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'homework',
        'title',
        'document',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'student_hw',
        'description',
        'points',
    )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(DoneHomework, DoneHomeworkAdmin)
admin.site.register(Review, ReviewAdmin)

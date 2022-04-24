from django.contrib import admin
from .models import Category, Quiz, Question, Answer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text',
        'is_right'
    ]


@admin.register(Question)
class QustionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz'
    ]
    list_display = [
        'title',
        'quiz'
    ]
    inlines = [
        AnswerInlineModel,
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question'
    ]

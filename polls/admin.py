from django.contrib import admin

from .models import Question, Choice
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):

	fields = ("question_text", "published_dates")

admin.site.register(Question)
admin.site.register(Choice)

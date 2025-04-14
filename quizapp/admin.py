from django.contrib import admin
from .models import Question
from .models import QuizResult

admin.site.register(Question)
admin.site.register(QuizResult)

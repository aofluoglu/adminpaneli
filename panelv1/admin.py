from django.contrib import admin
from panelv1.models import AnswerOb, QuestionOb, UserOb

# Register your models here.

admin.site.register(UserOb)
admin.site.register(QuestionOb)
admin.site.register(AnswerOb)
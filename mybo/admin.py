from django.contrib import admin
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields=['subject'] #질문 제목으로 검색

admin.site.register(Question, QuestionAdmin)
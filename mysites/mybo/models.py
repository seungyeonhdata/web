from django.db import models

# Create your models here.
class Question(models.Model):
    subject=models.CharField(max_length=200) #제목속성.글자수제한
    content=models.TextField() #게시글 본문
    create_date=models.DateTimeField() #게시일

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE) #모델간의 연결
    #답변과 연결된 질문이 삭제되면 답변도 삭제된다
    content=models.TextField() #답변글 본문
    create_date=models.DateTimeField() #게시일


























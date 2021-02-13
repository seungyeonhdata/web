from django import forms
from mybo.models import Question, Answer

# ModelForm:부모클래스(question 모델과 연결되어 있는 폼,
# 모델 폼을 저장하면 연결된 모델의 데이터를 데이터베이스에 저장),
# QuestionForm:자식클래스
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['subject', 'content']
        #부트스트랩을 적용하기 위한 코드
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels={
            'subject':'제목',
            'content':'내용',
        }

# QuestionForm클래스는 Question모델과 연결 됨.
# 필드로는 'subject', 'content'를 사용함

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['content']
        labels={
            'content':'내용',
        }
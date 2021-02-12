from django.urls import path
from . import views #.은 현재 디렉토리


app_name='mybo' #네임스페이스(서로 다른 앱에서 동일한 이름의 객체를 구분하기 위해

urlpatterns=[
    path('',views.index, name='index'),
    path('<int:question_id>/',views.detail, name='detail'),
    path('answer/create/<int:question_id>/',views.answer_create,name='answer_create'),
    path('question/create/',views.question_create, name='question_create'),

]


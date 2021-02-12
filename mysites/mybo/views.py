
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    page=request.GET.get('page',1) #get방식으로 페이지를 가져오는 일반적인 방식
    #page 파라미터가 없으면 기본 페이지를 1페이지로 설정
    question_list=Question.objects.order_by('-create_date') #-는 내림차순

    #question_list에 들은 것들을 몇개를 기준으로 나눌건지
    paginator=Paginator(question_list,10)
    page_obj=paginator.get_page(page)
    context={'question_list':page_obj}

    return render(request, 'mybo/question_list.html',context)
#render는 context에 있는 질문데이터를 템플릿(mybo/question_list.html)형식으로 적용하여 html코드로 변환하여 출력
#템플릿 저장하는 디렉토리 생성할것


def detail(request, question_id):
    # question=Question.objects.get(id=question_id)
    question=get_object_or_404(Question, pk=question_id)
    context={'question':question}
    return render(request, 'mybo/question_detail.html', context)


#request에는 mybo/question_datail.html에 textarea에 입력된 내용이 전달됨
def answer_create(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'),
    #                            create_date=timezone.now())
    # return redirect('mybo:detail', question_id=question.id)
    #content 데이터 읽어들이는 부분
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False) #임시저장
            answer.create_date = timezone.now()
            answer.question=question
            answer.save()
            return redirect('mybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question':question,'form': form}
    return render(request, 'mybo/question_detail.html', context)

def question_create(request):
    # form=QuestionForm()
    # return render(request, 'mybo/question_form.html', {'form':form})
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) #임시저장
            question.create_date = timezone.now()
            question.save()
            return redirect('mybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'mybo/question_form.html', context)







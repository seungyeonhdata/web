from django import template

register=template.Library()

@register.filter #필터를 등록하겠다는 annotation
def sub(value, arg): #템플릿 필터 함수
    return value-arg

#전체 게시글수-시작인덱스-현재 인덱스 +1


#빼기 개념을 넣기 위한 태그다!
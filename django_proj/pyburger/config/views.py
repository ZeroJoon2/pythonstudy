from django.http  import HttpResponse
from django.shortcuts import render, redirect
from burgers.models import Burger

def main(request):
    return render(request, 'main.html')

def burger_list(request):
     burger_query = Burger.objects.all()
     print(f'전체 햄버거 리스트 : {burger_query}')
     context = {
          "burgers": burger_query,
     }
     return render(request, 'burgers.html', context)

def burger_search(request):
    keyword = request.GET.get('keyword')
    print(keyword)
    
    if keyword is not None:
        search_burger = Burger.objects.filter(name__contains = keyword)
        
    else:
        search_burger = Burger.objects.none()

    context = {
        'searched_burgers' : search_burger,
    }
    return render(request, 'burger_search.html', context)
    
def burger_create(request):
    context = {}  # 빈 context 생성
    if request.method == 'POST': #POST일때만 데이터 추가
        add_name = request.POST.get('add_name')
        add_price = request.POST.get('add_price')
        add_kcal = request.POST.get('add_kcal')
        if add_name not in Burger.objects.values_list('name',flat= True):
            print(add_name, add_price, add_kcal)
            if add_name and add_price and add_kcal:
                try:
                    add_price = int(add_price)
                    add_kcal = int(add_kcal)

                    Burger.objects.create(name = add_name, price = add_price, calories = add_kcal)
                    return redirect(burger_list)
                except ValueError:
                    context = {'error' : '가격과 칼로리는 숫자로 입력하세요.'}
                    return render(request, 'burger_create.html', context)
            else:
                context = {'error' : f'''{add_name}는 이미 등록된 버거입니다.'''}
                return render(request, 'burger_create.html', context)
        else:
            context = {'error' : '모든 필드를 입력하세요'}
            return render(request, 'burger_create.html', context)
            
    return render(request, 'burger_create.html', context)

# 람다로 표현해도 가능은 한데, 확장성과 가독성에 GPT는 추천하지 않음
# main = lambda x : render(x,'main.html')
# burger_list = lambda x : render(x,'burgers.html')

'''
아래는 django 프로젝트 view에서 람다 표현식에 대한 의견

Lambda를 사용하여 Django 뷰 함수를 정의하는 것의 장점과 단점은 다음과 같습니다.
[장점]
간결함: Lambda를 사용하면 코드가 한 줄로 표현되므로, 간단한 뷰 함수의 경우 코드가 더 간결해지고 직관적으로 보일 수 있습니다.
빠른 정의: 간단한 렌더링 작업처럼 짧고 반복적인 작업에는 Lambda가 빠르게 사용할 수 있어 개발 속도를 높일 수 있습니다.
메모리 절약: Lambda 함수는 일반 함수보다 약간의 메모리를 덜 사용할 수 있어, 대규모 애플리케이션의 작은 최적화로 활용될 수 있습니다.

[단점]
확장성 제한: Lambda는 한 줄로 작성해야 하므로, 추가적인 로직이나 복잡한 처리를 수행하기가 어렵습니다. 예를 들어, 조건문이나 반복문을 추가하려면 Lambda는 적합하지 않습니다.
가독성 저하: 특히 여러 Lambda 함수가 있을 경우 코드의 가독성이 떨어질 수 있으며, 팀 협업에서 코드 이해에 방해가 될 수 있습니다.
디버깅 어려움: Lambda 함수는 이름이 없고 코드가 한 줄로 제한되기 때문에 디버깅이 어렵습니다. 오류가 발생하면 추적하기가 더 까다롭습니다.
일관성 문제: Django 뷰 함수는 일반적으로 함수 형태로 작성하는 것이 관례이므로, Lambda로 작성하면 코드 일관성이 떨어질 수 있습니다. 특히 Django 프로젝트에서 일반 함수와 Lambda가 섞이면 관리가 어려워집니다.
결론
Lambda는 간단한 작업에서는 유용할 수 있지만, 확장성, 유지보수, 디버깅의 측면에서 Django 뷰 함수에는 적합하지 않습니다. 특히 Django와 같은 프레임워크에서는 함수 형태로 정의하는 것이 코드의 일관성을 유지하고 관리하기에 더 좋습니다.
'''
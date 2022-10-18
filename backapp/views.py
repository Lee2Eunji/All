from django.shortcuts import render , redirect
from .models import Developer, Choice, Question, Board
from .forms import BoardForm
from django.utils import timezone
# Create your views here.
def main(request):
    developers = Developer.objects.all()
    
    context = {
        'developers': developers,
    }
    
    return render(request, 'main.html', context=context)
def form(request):
    questions = Question.objects.all()
    
    context = {
        'questions' : questions,
    }
    
    return render(request, 'form.html', context=context)

def submit(request):
    # 문항 수
    N = Question.objects.count()
    # 개발자 유형 수
    K = Developer.objects.count()
    print(f'문항 수 : {N}, 개발자 유형 수 : {K}')
    
    counter = [0] * (K + 1)
    
    print(f'POST : {request.POST}')
    
    for n in range(1, N+1):
        developer_id = int(request.POST[f'question-{n}'][0])
        counter[developer_id] += 1
        
    # 최고점 개발 유형
    
    best_developer_id = max(range(1, K+1), key=lambda id : counter[id])
    print(best_developer_id)
    best_developer = Developer.objects.get(pk=best_developer_id)
    best_developer.count += 1
    best_developer.save()
    
    context = {
        'developer' : best_developer,
        'counter' : counter
    }
    
    return redirect('result', developer_id=best_developer_id)


def result(request, developer_id):
    developer = Developer.objects.get(pk=developer_id)
    context = {
        'developer' : developer,
    }
    return render(request, 'result.html', context=context)

def introduce(request):
    
    return render(request, 'introduce.html')

def select(request):
    
    return render(request, 'select.html')

def itboard(request):
    writings = Board.objects.all()
    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = timezone.now()
            form.save()
            return redirect('itBoard')
    else:
        return render(request, 'itboard.html', {'form':form, 'writings':writings})
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import TodoForm
from .models import Todo



def index(request):
    return HttpResponse("Todo List")

def todo_list(request):
    todos = Todo.objects.filter(completed=False)
    return render(request, 'todo/todo_list.html', {'todos':todos})

def todo_detail(request, pk): #상세 내용 페이지에 데이터 전달 
    todo =Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo':todo})

def todo_post(request):   #todo 생성 
    if request.method =="POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form':form})

def todo_edit(request, pk): #todo 수정
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form':form})
    
def todo_done(request,pk):  #todo의 complted = True로, 완료 상태로 
    todo = Todo.objects.get(id=pk)
    todo.completed=True
    todo.save()
    return redirect('todo_list')

def todo_done_list(request): #완료된 목록 보여주는 함수
    dones = Todo.objects.filter(completed=True)
    return render(request, 'todo/todo_done_lilst.html', {'dones':dones})

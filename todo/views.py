from django.shortcuts import render, HttpResponse, redirect
from todo.models import Todo
# Create your views here.
def home(request):
    todos = Todo.objects.all()

    context = {
        "number1" : 10,
        "number2" : 20,

        "numbers" : [1,2,3,4,5,6,7,8,9] 
    }
    return render(request, "index.html", context, {"todos":todos})

def addTodo(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title = request.POST.get("title")
        newTodo = Todo(title = title, completed = False)

        newTodo.save()
        return redirect("/")
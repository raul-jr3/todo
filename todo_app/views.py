from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

from .forms import TodoForm
from .models import Todo 

def home_page(request):
	todos = Todo.objects.all()
	context = {'todos':todos}
	template = 'todo_app/home_page.html'
	return render(request, template, context)

def todo_detail(request, todo_id):
	todo = get_object_or_404(Todo, pk = todo_id)
	context = {'todo':todo}
	template = 'todo_app/todo_view.html'
	return render(request, template, context)

def post_todo(request):
	if request.method == 'POST':
		form = TodoForm(data = request.POST, files = request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'todo_app/posted.html')
		else:
			return HttpResponse("Invalid submission")
	else:
		form = TodoForm()
	context = {'form':form}
	template = 'todo_app/post_todo.html'
	return render(request, template, context)

def delete_todo(request, todo_id):
	todo = get_object_or_404(Todo, pk = todo_id)
	todo.delete()
	context = {'todo':todo}
	template = 'todo_app/delete.html'
	return render(request, template, context)
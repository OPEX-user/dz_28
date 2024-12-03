from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from .models import Task
from .forms import CreateTaskForm, AddCommentForm, UpdateTaskForm


def all_task(request):
    tasks = Task.objects.all()
    return TemplateResponse(
        request,
        template='all_task.html',
        context={
            'context': 'Список задач',
            'tasks': tasks
        }
    )


def one_task(request, id: int):
    task = get_object_or_404(Task, id=id)
    return TemplateResponse(
        request,
        template='one_task.html',
        context={
            'context': 'Задача',
            'task': task
        }
    )


def add_task(request):
    if request.method == 'GET':
        return TemplateResponse(
            request,
            template='add_task.html',
            context={'task_form': CreateTaskForm()}
        )
    elif request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        success = "Вы создали новую запись" if not form.errors else form.errors
        return TemplateResponse(
            request,
            template='add_task.html',
            context={
                'task_form': CreateTaskForm(),
                'status_success': success
            }
        )


def add_comment(request):
    if request.method == 'GET':
        return TemplateResponse(
            request,
            template='add_comment.html',
            context={'task_form': AddCommentForm()}
        )
    elif request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        success = "Вы создали новый комментарий" if not form.errors else form.errors
        return TemplateResponse(
            request,
            template='add_comment.html',
            context={
                'task_form': AddCommentForm(),
                'status_success': success
            }
        )


def update_task(request):
    if request.method == 'GET':
        return TemplateResponse(
            request,
            template='update_task.html',
            context={'task_form': UpdateTaskForm()}
        )
    elif request.method == 'POST':
        form = UpdateTaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        success = "Вы обновили статус" if not form.errors else form.errors
        return TemplateResponse(
            request,
            template='update_task.html',
            context={
                'task_form': UpdateTaskForm(),
                'status_success': success
            }
        )
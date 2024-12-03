from django import forms

from .models import Task, Comment


class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'executor',
            'execution_status',
            'date_created',
            'date_completion'
        ]


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment', 'task']


class UpdateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['id', 'execution_status']

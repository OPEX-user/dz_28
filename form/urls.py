from django.urls import path

from .views import all_task, one_task, add_task, add_comment, update_task

urlpatterns = [
    path('all_task/', all_task),
    path('one_task/<int:id>/', one_task),
    path('add_task/', add_task, name='add_task'),
    path('add_comment/', add_comment, name='add_comment'),
    path('update_task/', update_task, name='update_task')
    ]

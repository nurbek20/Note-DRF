from main.views import NoteViewSet
from django.urls import path

urlpatterns = [
    path('note', NoteViewSet.as_view(
            {
            'get':'retrieve',
            'post':'create',
            'put':'update',
            'delete':'destroy'
            }
        )),
        path('note/all', NoteViewSet.as_view(
            {
            'get':'list'
            }
        
        ))
    ]
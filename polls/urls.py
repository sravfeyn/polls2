from django.urls import path
from .views import index, sp_index, detail

urlpatterns = [
	path('', index, name="index"),
	path('sp/', sp_index),
	path('<int:question_id>/', detail)
]

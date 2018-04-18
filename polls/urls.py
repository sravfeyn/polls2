from django.urls import path
from .views import index, sp_index

urlpatterns = [
	path('', index, name="index"),
	path('sp/', sp_index),
	# path('special_poll', specil_index, name="special")
]

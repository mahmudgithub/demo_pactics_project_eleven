from django.views.generic import ListView
from .models import Contact
class sos(ListView):
	model = Contact
	template_name = 'home.html'
	context_object_name='app1'
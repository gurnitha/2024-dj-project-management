from django.forms import ModelForm
from django.forms import DateInput

from .models import Task, Project

# Create your ModelForm here.

class TaskForm(ModelForm):

	'''
	As you can see above, the form class requires a Meta class that d
	efines the model we are attributing to and the fields we want to be defined in the form.

	In the TaskForm, we also add a widget to display a calendar on the form for the due_date field.
	Django widget handles how the form fields are rendered.

	'''
	class Meta:
		model 	= Task
		fields 	= '__all__'
		widgets = {
			'due_date': DateInput( format=('%Y-%m-%d'), attrs={'type': 'date' }),
		}
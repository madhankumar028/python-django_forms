from django.shortcuts import render

from forms import POAForm

def POAView(request):
	form = forms.POAForm()
	return render(request, 'poa_form.html', {'form': form})


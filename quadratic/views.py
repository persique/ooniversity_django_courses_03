# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from quadratic.forms import QuadraticForm

	
def quadratic_results(request):
	if request.method == 'GET':
		a = request.GET.get('a')
		b = request.GET.get('b')
		c = request.GET.get('c')
		context = {}
		if a == None and b == None and c == None:
			form = QuadraticForm()
		else:
			form = QuadraticForm(request.GET)	
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']	
			d = b * b - 4 * a * c
			if d < 0:
				context['d'] = d
			elif d == 0:
				x = (-b + d**(1/2.0)) / 2*a
				context['x1'] = round(x, 1)
				context['d'] = d
			else:
				x1 = (-b + d**(1/2.0)) / 2*a
				x2 = (-b - d**(1/2.0)) / 2*a
				context['x1'] = round(x1, 1)
				context['x2'] = round(x2, 1)
				context['d'] = d			
		else:
			context['error'] = "коэффициент не целое число"
		context['form'] = form
	return render(request, 'quadratic/results.html', {'context': context})
		

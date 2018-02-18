from django.shortcuts import render

from .models import Trait
import genomelink

def index(request):
	# WORKS IF THERE'S 1 TRAIT ONLY
	# gets list of traits
	traits_list = Trait.objects.all()

	# join traits into list
	output = ', '.join([t.trait_name for t in traits_list])

	# get corresponding report
	traits_output = genomelink.Report.fetch(name=output, population='european', token='GENOMELINKTEST001').summary['text']

	context = {
		'traits_list': traits_list,
		'traits_output': traits_output,
	}

	return render(request, 'genome/index.html', context)
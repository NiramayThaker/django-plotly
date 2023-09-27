from django.shortcuts import render
from core.models import CO2
import plotly.express as px
from django.db.models import Avg
from .forms import DateForm


# Create your views here.
def charts(request):
	co2 = CO2.objects.all()
	start = request.GET.get('start')
	end = request.GET.get('end')

	if start is not None:
		co2 = co2.filter(date__gte=start)
	if end is not None:
		co2 = co2.filter(date__lte=end)

	fig = px.line(
		x=[c.date for c in co2],
		y=[c.average for c in co2],
		title="CO2 PPM",
		labels={'x': 'Date', 'y': 'CO2 PPM'},
	)

	chart = fig.to_html()

	context = {'chart': chart, 'form': DateForm()}
	return render(request, 'core/charts.html', context)


def yearly_avg_co2(request):
	avg = CO2.objects.values('date__year').annotate(avg=Avg('average'))

	context = {'avg': avg}
	

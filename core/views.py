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

	x = avg.values_list('date__year', flat=True)
	y = avg.values_list('avg', flat=True)

	text = [f'{avg:.1f}' for avg in y]

	fig = px.bar(avg, x=x, y=y, text=text)
	fig.update_layout(
		title_text="Average CO2 concetreation per year",
		yaxis_range=[0, 500]
	)
	fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

	chart = fig.to_html()

	context = {'chart': chart}
	return render(request, 'core/charts.html', context)

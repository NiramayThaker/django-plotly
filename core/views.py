from django.shortcuts import render
from core.models import CO2 
import plotly.express as px


# Create your views here.
def charts(request):
    co2 = CO2.objects.all()

    fig = px.line(
        x = [co2.date for c in co2],
        y = [co2.average for c in co2]
    )
    
    chart = fig.to_html()

    context = {'chart': chart}
    return render(request, 'core/charts.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from internal.models import *
import internal.validation as validation
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string
from internal.charts import PieChart, BarChart, StackChart
from internal.process import *
import pdb

# Create your views here.
def index(request):
    charts = []
    for plt_md in PlotMetadata.objects.all():
        # processed data must exist and user must be staff OR user is not staff and plot is not staff only
        if plt_md.processed_data and (request.user.is_staff or (not request.user.is_staff and not plt_md.staff_only)):
            if plt_md.data_type == 'DP':
                new_chart = PieChart(
                    name=plt_md.name
                )
            elif plt_md.data_type == 'DB':
                new_chart = BarChart(
                    name=plt_md.name
                )
            else:
                new_chart = StackChart(
                    name=plt_md.name
                )
            chart_data = processed_data_to_chart(plt_md)
            charts.append(new_chart.generate(chart_data))

    return render(request, 'home.html', {"charts": charts})

def data(request):
    types = PlotMetadata.TYPES
    if request.method == 'POST':
        val_obj = validation.validate_new_plot_metadata(request)
        if not val_obj[0]:
            modal_code = ['UIkit.modal("#new-data-modal").show();']
            return render(
                request, 'data.html', {
                    "types": types, 
                    "error_message": val_obj[1], 
                    "modal": modal_code,
                    "prev_req": request.POST})
        else:
            name, data_type = request.POST['name'], request.POST['data_type']
            new_metadata = PlotMetadata(name=name,
                                        data_type=data_type,
                                        raw_data=request.FILES['raw_data'],
                                        orig_raw_data_filename=request.FILES['raw_data'].name,
                                        staff_only=(request.POST['staff_only'] == 'on'))
            new_metadata.save()
            return redirect('/data')
    else:
        plt_mds = PlotMetadata.objects.all()
        for plt_md in plt_mds:
            plt_md.added = plt_md.added.strftime("%Y-%m-%d %H:%M")
        return render(request, 'data.html', {
            "types": types,
            "plt_mds": plt_mds
        })

def process(request, id):
    plt_md = PlotMetadata.objects.get(pk=id)
    processed_data = process_raw_data(plt_md)
    plt_md.processed_data.save('processed_' + get_random_string(length=6) + '_' + plt_md.orig_raw_data_filename, ContentFile(processed_data.to_csv()))
    plt_md.save()
    return redirect('/data')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')

def login_submit_view(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/')
    return render(request, 'login.html', {
        'error_message': "Failed to authenticate.",
    })

def logout_view(request):
    logout(request)
    return redirect('/login/')
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegisterForm
from .models import Home_data, About
from .services import data_from_xlsx


# Create your views here.
def index(request):
    image = Home_data.objects.order_by("-id")[0]
    return render(request, 'main/index.html', {"image": image, })

def demand(request):
    image = Home_data.objects.order_by("-id")[0]
    path = image.excel
    excel_data, vac_name = data_from_xlsx(path)
    return render(request, 'main/demand.html', {'name_vacancy': vac_name, "image": image, "excel_data": excel_data[1:], "heads": excel_data[0]})

def about(request):
    data = About.objects.order_by("-id")[0]
    return render(request, 'main/about.html', {"data": data, })

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("login")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

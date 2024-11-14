from django.shortcuts import render
from django.views import View

from .models import Slider


class IndexView(View):
    def get(self, request, *args, **kwargs):
        slider_items = Slider.objects.all()
        return render(request, 'index.html', {'slider_items': slider_items})

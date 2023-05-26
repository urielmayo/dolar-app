from django.views.generic import ListView
from dolar.models import Dolar
from rest_framework.generics import ListAPIView
from dolar.serialiers import DolarSerializer


# Create your views here.
class DolarListView(ListView):
    model = Dolar
    template_name = "index.html"
    queryset = Dolar.objects.all()
    context_object_name = 'dolars'


class DolarListAPIView(ListAPIView):
    queryset = Dolar.objects.all()
    serializer_class = DolarSerializer

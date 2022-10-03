from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.views.generic.edit import FormMixin

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect

from .models import Advert, Response
from .forms import CreateAdvertForm, CreateResponseForm
from .filters import ResponseFilter


class AdvertList(ListView):
    model = Advert
    template_name = 'adverts.html'
    context_object_name = 'advertList'
    queryset = Advert.objects.order_by('-id_category')
    paginate_by = 10


class AdvertView(FormMixin, DetailView):
    model = Advert
    template_name = 'advert.html'
    form_class = CreateResponseForm
    context_object_name = 'advertView'

    def post(self, request, *args, **kwargs):
        response = Response(
            id_user=request.user,
            id_advert=Advert.objects.get(pk=request.POST['id_advert']),
            text=request.POST['text'],

        )
        response.save()

        return redirect('/advert/' + str(response.id_advert.pk))


class AdvertCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add.html'
    form_class = CreateAdvertForm

    def post(self, request, *args, **kwargs):
        advert = Advert(
            id_user=request.user,
            id_category=request.POST['category'],
            text=request.POST['text'],
            file=request.POST['file']
        )
        advert.save()

        return redirect('/adverts/')


class AdvertUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'edit.html'
    form_class = CreateAdvertForm
    success_url = '/adverts/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Advert.objects.get(pk=id)


class ResponseList(ListView):
    model = Response
    template_name = 'responses.html'
    context_object_name = 'responseList'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_adverts = Advert.objects.filter(id_user=self.request.user)
        query = Response.objects.filter(id_advert__in=user_adverts).order_by('-id_user')
        context['filter'] = ResponseFilter(self.request.GET, queryset=query)
        return context


class ResponseDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_response.html'
    queryset = Response.objects.all()
    success_url = '/adverts/responses'


class ResponseAcceptView(DetailView):
    model = Response
    template_name = 'accept_response.html'

    def post(self, request, *args, **kwargs):
        response = Response.objects.get(pk=request.POST['id_resp'])
        response.accepted = True
        response.save()

        return redirect('/adverts/responses')

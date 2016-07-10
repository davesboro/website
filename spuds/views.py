from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Potato
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'spuds/index.html'
    context_object_name = 'all_potatos'

    def get_queryset(self):
        return Potato.objects.all()


class DetailView(generic.DetailView):
    model = Potato
    template_name = 'spuds/detail.html'


class PotatoCreate(CreateView):
    model = Potato
    fields = ['name', 'origin', 'pronounced', 'picture']


class PotatoUpdate(UpdateView):
    model = Potato
    fields = ['name', 'origin', 'pronounced', 'picture']


class PotatoDelete(DeleteView):
    model = Potato
    success_url = reverse_lazy('spuds:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'spuds/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('spuds:index')

        return render(request, self.template_name, {'form': form})

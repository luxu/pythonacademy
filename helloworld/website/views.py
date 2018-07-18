from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, \
    CreateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from helloworld.models import Comercio, Gasto
from website.forms import InsereComercioForm, InsereGastoForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "index.html"

# LISTA DE COMÉRCIOS
# ----------------------------------------------

class ComercioListView(ListView):
    template_name = "lista_comercios.html"
    model = Comercio
    context_object_name = "comercios"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ComercioListView, self).get_context_data(**kwargs)
        list_exam = Comercio.objetos.all()
        paginator = Paginator(list_exam, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['list_exams'] = file_exams
        return context

# CADASTRAMENTO DE COMÉRCIOS
# ----------------------------------------------

class ComercioCreateView(CreateView):
    template_name = "cria_comercio.html"
    model = Comercio
    form_class = InsereComercioForm
    success_url = reverse_lazy("lista_comercios")

# ATUALIZAÇÃO DE COMÉRCIOS
# ----------------------------------------------

class ComercioUpdateView(UpdateView):
    template_name = "atualiza_comercio.html"
    model = Comercio
    fields = '__all__'
    context_object_name = 'comercio'
    success_url = reverse_lazy("lista_comercios")

    def get_object(self, queryset=None):
      comercio = None

      # Se você utilizar o debug, verá que os
      # campos {pk} e {slug} estão presente em self.kwargs
      id = self.kwargs.get(self.pk_url_kwarg)
      slug = self.kwargs.get(self.slug_url_kwarg)

      if id is not None:
        # Busca o comercio apartir do id
        comercio = Comercio.objects.filter(id=id).first()

      elif slug is not None:
        # Pega o campo slug do Model
        campo_slug = self.get_slug_field()

        # Busca o comercio apartir do slug
        comercio = Comercio.objetos.filter(**{campo_slug: slug}).first()

      # Retorna o objeto encontrado
      return comercio

# EXCLUSÃO DE COMÉRCIOS
# ----------------------------------------------

class ComercioDeleteView(DeleteView):
    template_name = "exclui_comercio.html"
    model = Comercio
    fields = '__all__'
    context_object_name = 'comercio'
    success_url = reverse_lazy("lista_comercios")

    def get_object(self, queryset=None):
      comercio = None

      # Se você utilizar o debug, verá que os
      # campos {pk} e {slug} estão presente em self.kwargs
      id = self.kwargs.get(self.pk_url_kwarg)
      slug = self.kwargs.get(self.slug_url_kwarg)

      if id is not None:
        # Busca o comercio apartir do id
        comercio = Comercio.objects.filter(id=id).first()

      elif slug is not None:
        # Pega o campo slug do Model
        campo_slug = self.get_slug_field()

        # Busca o comercio apartir do slug
        comercio = Comercio.objetos.filter(**{campo_slug: slug}).first()

      # Retorna o objeto encontrado
      return comercio

# LISTA DE GASTOS
# ----------------------------------------------

class GastoListView(ListView):
    template_name = "lista_gastos.html"
    model = Gasto
    context_object_name = "gastos"
    paginate_by = 5

# CADASTRAMENTO DE GASTOS
# ----------------------------------------------

class GastoCreateView(CreateView):
    template_name = "cria_gasto.html"
    model = Gasto
    form_class = InsereGastoForm
    success_url = reverse_lazy("lista_gastos")

# ATUALIZAÇÃO DE GASTOS
# ----------------------------------------------

class GastoUpdateView(UpdateView):
    template_name = "atualiza_gasto.html"
    model = Gasto
    fields = '__all__'
    context_object_name = 'gasto'
    success_url = reverse_lazy("lista_gastos")

    def get_object(self, queryset=None):
      gasto = None

      # Se você utilizar o debug, verá que os
      # campos {pk} e {slug} estão presente em self.kwargs
      id = self.kwargs.get(self.pk_url_kwarg)
      slug = self.kwargs.get(self.slug_url_kwarg)

      if id is not None:
        # Busca o gasto apartir do id
        gasto = Gasto.objetos.filter(id=id).first()

      elif slug is not None:
        # Pega o campo slug do Model
        campo_slug = self.get_slug_field()

        # Busca o gasto apartir do slug
        gasto = Gasto.objetos.filter(**{campo_slug: slug}).first()

      # Retorna o objeto encontrado
      return gasto

# EXCLUSÃO DE GASTOS
# ----------------------------------------------

class GastoDeleteView(DeleteView):
    template_name = "exclui_gasto.html"
    model = Gasto
    fields = '__all__'
    context_object_name = 'gasto'
    success_url = reverse_lazy("lista_gastos")

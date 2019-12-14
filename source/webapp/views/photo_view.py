from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoListView(ListView):

    template_name = 'photo/index.html'
    model = Photo
    context_object_name = 'photos'
    oredering = ['-created_at']


class PhotoView(DetailView):
    template_name = 'photo/photo.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.object
        comments = photo.comment_picture.order_by('-created_at')
        self.paginate_comments_to_context(comments, context)
        return context

    def paginate_comments_to_context(self, comments, context):
        paginator = Paginator(comments, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['comments'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


class PhotoCreateView(CreateView):

    template_name = 'photo/create.html'
    model = Photo
    form_class = PhotoForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})

class PhotoUpdateView(UpdateView):

    model = Photo
    template_name = 'photo/update.html'
    form_class = PhotoForm
    context_key = 'photo'

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView):

    template_name = 'photo/delete.html'
    model = Photo
    context_key = 'photo'


    def get_success_url(self):
        return reverse('webapp:index')
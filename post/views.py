from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from mysite.views import OwnerOnlyMixin
from post.models import Post
from django.conf import settings
from post.forms import PostInlineFormset

from django.db.models import Q
from post.forms import PSH




class PostLV(ListView):
    model = Post
    template_name = 'post/post_list.html'

class PostDV(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post/{self.object.id}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.id}"
        return context

class PostCV(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post/post_form.html'
    fields = ('title', 'content', 'owner')
    success_url = reverse_lazy('post:post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PostInlineFormset(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PostInlineFormset(instance = self.object)
        return context
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class SearchFormView(FormView):
    form_class = PSH
    template_name = 'post/post_search.html'

    def form_valid(self,form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord)|  Q(content__icontains=searchWord)).distinct()
        
        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        return render(self.request, self.template_name, context)
    
class PostChangeLV(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/post_change.html'


    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class PostDelV(OwnerOnlyMixin, DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post:post_list')

class PostUV(OwnerOnlyMixin, UpdateView):
    model = Post
    template_name = 'post/post_forms.html'
    fields = ('title', 'content')
    success_url = reverse_lazy('post:post_list')

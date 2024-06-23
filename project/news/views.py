from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, SearchView,
)

from .filters import NewsFilter
from .forms import NewsForm
from .models import News

from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Subscription, Category

@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )

class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'id_новости'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'news.html'
    context_object_name = 'id_новости'


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_news',)
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_news',)
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_news',)
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class NewsSearch(ListView):
    model = News
    ordering = 'name'
    template_name = 'news_search.html'
    context_object_name = 'id_новости'
    paginate_by = 2

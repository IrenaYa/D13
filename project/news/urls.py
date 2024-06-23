from django.urls import path
from .views import (
   NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, NewsSearch, subscriptions
)
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('<int:pk>/search/', NewsSearch.as_view(), name='news_search'),
   path('subscriptions/', subscriptions, name='subscriptions'),
   path('<int:pk>/', cache_page(60*10)(NewsDetailView.as_view()), name='news_detail'),
]
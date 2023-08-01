from django.shortcuts import render, get_object_or_404, render
from .models import MainContent

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)

def detail(request, content_id):
    content = get_object_or_404(MainContent, pk=content_id)
    context = {'content': content}
    return render(request, 'mysite/content_detail.html', context)

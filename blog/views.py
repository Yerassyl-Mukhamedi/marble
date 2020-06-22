from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .models import *
from .forms import PostForm

def post_list(request):
    posts = Worker.objects.order_by('job')
    blogs = Laptop.objects.filter(name='HP Pavilion').values_list('owner', flat=True)
    laptop_count = Laptop.objects.count()
    worker_count = Worker.objects.count()
    return render(request, 'blog/post_list.html', {'posts': posts, 'blogs': blogs, 'laptop_count': laptop_count, 'worker_count': worker_count })

def post_detail(request, pk):
    post = get_object_or_404(Worker, pk=pk)
    notebooks = Laptop.objects.order_by('name')
    printers = Printer.objects.order_by('name')
    shredders = Shredder.objects.order_by('name')
    televisions = Television.objects.order_by('name')
    conditions = Condition.objects.order_by('name')
    telephones = Telephone.objects.order_by('name')
    cameras = Camera.objects.order_by('name')
    dispensers = Dispenser.objects.order_by('name')
    microwaves = Microwave.objects.order_by('name')
    displays = Display.objects.order_by('name')
    computers = Computer.objects.order_by('name')
    return render(request, 'blog/post_detail.html', {'post': post, 'notebooks': notebooks, 'printers': printers, 'shredders': shredders, 'televisions': televisions, 'conditions': conditions, 'telephones': telephones, 'cameras': cameras, 'dispensers': dispensers, 'microwaves': microwaves, 'displays': displays, 'computers': computers})

def level_list(request):
    posts = Worker.objects.order_by('name')
    return render(request, 'blog/level_list.html', {'posts': posts})

def level_detail(request, pk):
    post = get_object_or_404(Worker, pk=pk)
    documents = Document.objects.order_by('id')
    return render(request, 'blog/level_detail.html', {'documents': documents, 'post': post})

def user(request):
    return render(request, 'user/user.html')

def zapros_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('zapros_list')
    else:
        form = PostForm()
    return render(request, 'user/post_edit.html', {'form': form})

def zapros_list(request):
    zaprosy = Zapros.objects.order_by('name')
    finisheds = Finished.objects.order_by('name')
    context = {
        'zaprosy': zaprosy,
        'finisheds': finisheds
    }
    return render(request, 'blog/zapros_list.html', context)

def zapros_delete(request, pk):
    current = Zapros.objects.filter(id=pk)
    current_name = current.values('name')
    current_problem = current.values('problem')
    Finished.objects.create(name = current_name, problem = current_problem)
    current.delete()
    items = Zapros.objects.all()

    context = {
        'items': items
    }
    return render(request, 'blog/zapros_list.html', context)
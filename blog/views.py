from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.mail import send_mail
from .models import *
from .forms import *
import logging

from django.db.models import Q
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives


logger = logging.getLogger(__name__)

def worker_list(request):
    posts = Worker.objects.order_by('job')
    blogs = Laptop.objects.filter(name='HP Pavilion').values_list('owner', flat=True)
    laptop_count = Laptop.objects.count()
    worker_count = Worker.objects.count()
    return render(request, 'blog/worker_list.html', {'posts': posts, 'blogs': blogs, 'laptop_count': laptop_count, 'worker_count': worker_count })


def worker_new(request):
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('worker_list')
    else:
        form = WorkerForm()
    return render(request, 'blog/worker_new.html', {'form': form})



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
            if Worker.objects.filter(email=post.name):
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('zapros_list')
            else:
                error = 'error'
                return render(request, 'user/post_edit.html', {'error': error, 'form': form})
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



def zapros_awaits(request, pk):
    currents = Zapros.objects.filter(id=pk)
    currents.update(status='awaits')
    problem = (str(currents.values('problem')).replace("<QuerySet [{'problem':", "")).replace('}]>', '')
    email = (str(currents.values('name')).replace("<QuerySet [{'name':", "")).replace("}]>", "").replace("'", "")
    token = (str(currents.values('verification')).replace("<QuerySet [{'verification':", "")).replace("}]>", "").replace("'","")
    subject, from_email, to = 'Подтверждение проделанной работы', 'mailer@btu.kz', email
    text_content = 'adsfdsdf.'
    link = 'http://127.0.0.1:8000/zapros/delete/'+str(pk)+'/'+token
    text = 'Подтвердите окончание задачи"'+ problem +'"перейдя по <a href="'+link+'">ссылке</a>'
    html_content = text
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    

    # send_mail(
    # subject = 'Подтверждение проделанной работы',
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    # message = 'Are you delighted with work done??? <a href="youtube.com">Link</a> ' + problem,
    # from_email = 'mailer@btu.kz',
    # recipient_list = ['mailer@btu.kz',],
    # auth_user = 'mailer@btu.kz',
    # auth_password = 'Pass1234',
    # fail_silently = False,
    # )

    context = {
        'currents': currents,
        'token': token,
        'email':email
    }
    return render(request, 'blog/zapros_detail.html', context)

def zapros_detail(request, pk):
    currents = Zapros.objects.filter(id=pk)
    context = {
        'currents': currents
    }
    return render(request, 'blog/zapros_detail.html', context)


def zapros_delete(request, pk, token):
    currents = Zapros.objects.filter(id=pk)
    currents.update(status='finished')
    # send_mail(
    # subject = 'That’s your subject',
    # message = 'That’s your message body',
    # from_email = 'mailer@btu.kz',
    # recipient_list = ['mailer@btu.kz',],
    # auth_user = 'mailer@btu.kz',
    # auth_password = 'Pass1234',
    # fail_silently = False,
    # )

    context = {
        'currents': currents
    }
    return render(request, 'blog/zapros_detail.html', context)



def item_new(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('items_list')
    else:
        form = LaptopForm()
    return render(request, 'blog/item_new.html', {'form': form})




def items_list(request):
    items = Laptop.objects.order_by('name')
    context = {
        'items': items
    }
    return render(request, 'blog/items_list.html', context)


def item_detail(request, pk):
    items = Laptop.objects.filter(id=pk)
    context = {
        'items': items
    }
    return render(request, 'blog/item_detail.html', context)


def toner_list(request):
    toners = Toner.objects.order_by('name')

    context = {
        'toners': toners
    }
    return render(request, 'blog/toner_list.html', context)

def toner_edit(request, pk):
    toner = get_object_or_404(Toner, pk=pk)
    if request.method == "POST":
        form = TonerForm(request.POST, instance=toner)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            current = post.used_loads
            if current > 0 and post.remained_loads > 0 and post.remained_loads-current >= 0:
                remained = post.remained_loads
                overall = post.overall
                post.remained_loads = remained - current
                post.overall = overall + current
                post.used_loads = 0
                post.save()
                history = History(name=post.get_name_display(), used=current, old_rem=remained, new_rem=post.remained_loads, old_over=overall, new_over=post.overall)
                history.save()
                return redirect('toner_list')
    else:
        form = TonerForm(instance=toner)
    toner1 = Toner.objects.filter(id=pk)
    return render(request, 'blog/toner_edit.html', {'form': form, 'toner1': toner1})


def history_list(request):
    items = History.objects.all().order_by('date')

    context = {
        'items': items
    } 

    return render(request, 'blog/history_list.html', context)

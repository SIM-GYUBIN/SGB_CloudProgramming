from django.shortcuts import render

# Create your views here.
from apscheduler.schedulers.background import BackgroundScheduler
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from datetime import datetime, date
from .send_message import send_kakao_message

scheduler = BackgroundScheduler()
scheduler.start()

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'memo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            current_time = datetime.now().time()
            task_time = form.cleaned_data['time']
            current_date = date.today()
            task_datetime = datetime.combine(current_date, task_time)

            if datetime.combine(datetime.today(), current_time) > datetime.combine(datetime.today(), task_time):
                task.is_notified = True
            task.save()

            scheduler.add_job(send_kakao_message, 'date', run_date=task_datetime)
            return redirect('memo:task_list')
    else:
        form = TaskForm()
    return render(request, 'memo/add_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('memo:task_list')
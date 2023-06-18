from django.shortcuts import render

# Create your views here.
def main(request):
    #tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'weather/main.html', {})
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import VideoForm
from django.forms.models import formset_factory


def not_found(request):
    return render(request, 'statistic/404.html')

@login_required(login_url='not_found')
def statistic(request):
    videos = Video.objects.all()
    context = {'videos': videos,}
    return render(request, 'statistic/basic.html', context=context)


@login_required(login_url='not_found')
def add_video(request):
    form = VideoForm

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('main')
    
    context = {'form': form}
    return render(request, 'statistic/add.html', context)


@login_required(login_url='not_found')
def  delete(request, pk):
    video = Video.objects.get(video_id=pk)

    if request.method == 'POST':
        video.delete()
        return redirect('main')
    
    context = {'video': video}
    return render(request, 'statistic/delete.html', context)


@login_required(login_url='not_found')
def change(request, pk):
    video = Video.objects.get(video_id=pk)
    form = VideoForm(instance=video)

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
        return redirect('main')
    
    ExampleFormSet = formset_factory(VideoForm, extra=10)
    formset = ExampleFormSet()

    context = {'form': form, 'formset': formset}
    return render(request, 'statistic/change.html', context)
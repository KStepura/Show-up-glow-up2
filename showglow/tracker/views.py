from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def tracker_home(request):
    trackers = Notes.objects.order_by('-date')
    return render(request, 'tracker/tracker_home.html', {'trackers': trackers})

class TrackerDetailView(DetailView):
    model = Notes
    template_name = 'tracker/details_view.html'
    context_object_name = 'tracker'

class TrackerUpdateView(UpdateView):
    model = Notes
    template_name = 'tracker/create.html'
    form_class = NotesForm

class TrackerDeleteView(DeleteView):
    model = Notes
    success_url = '/tracker/'
    template_name = 'tracker/tracker-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker_home')
        else:
            error = 'Форма была неверной'

    form = NotesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'tracker/create.html', data)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Snippet, Favorite
from .forms import SnippetForm, SnippetDelete

# Create your views here.

def snippets(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippets/snippets.html', {'snippets': snippets})


def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})


def create_snippet(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            return redirect('snippets')
    else:
        form = SnippetForm()
    return render (request, 'snippets/create_snippet.html', {'form':form})


def snippet_edit(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save()
            return redirect('snippet_detail', pk=snippet.pk)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_edit.html', {'form': form})


def snippet_delete(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == "POST":
        form = SnippetDelete(request.POST, instance=snippet)
        if form.is_valid():
            snippet.delete()
            return redirect('snippets')
    else:
        form = SnippetDelete(instance=snippet)
    return render(request, 'snippets/snippet_delete.html')


def add_favorite(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    favorite = Favorite.objects.create(snippet=snippet, user=request.user)
    favorite.save()
    return redirect(to="snippets.html")


def undo_favorite(request, pk):
    favorite = Favorite.objects.get(snippet__id=pk)
    favorite.delete()
    return redirect(to="snippets.html")


#user
def user_profile(request):
    snippets = Snippet.objects.filter(users=request.user)
    return render(request, "snippets/profile.html", {"snippets":snippets})
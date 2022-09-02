from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Snippet, Favorite
from .forms import SnippetForm, SnippetDelete, LanguageForm

# Create your views here.

def snippets(request):
    snippets = Snippet.objects.all()
    favorite_snippets=[snippet for snippet in snippets if snippet.is_user_favorite(request.user)]
    return render(request, 'snippets/snippets.html', {'snippets': snippets, 'favorite_snippets': favorite_snippets})


def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})


def create_snippet(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
            snippet.save()
            return redirect('snippets')
    else:
        form = SnippetForm()
    return render (request, 'snippets/create_snippet.html', {'form':form})


@login_required
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


@login_required
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


def add_to_library(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    favorite = Favorite.objects.create(snippet=snippet, user=request.user)
    favorite.save()
    return redirect(to="snippets")


def delete_from_library(request, pk):
    favorite = Favorite.objects.get(snippet__id=pk, user=request.user)
    favorite.delete()
    return redirect(to="snippets")


#user
def user_profile(request):
    snippets = Snippet.objects.filter(users=request.user) | Snippet.objects.filter(author=request.user)
    return render(request, "snippets/profile.html", {"snippets":snippets})
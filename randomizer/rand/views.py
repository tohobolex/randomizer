from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import rand, Comment
from django.db.models import Max
from django.contrib import messages
from django.contrib.auth import login, logout
from .formrand import RandForm, CommentForm, UserRegisterForm, UserLoginForm
import random

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered')
            return redirect('login')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserRegisterForm()
    return render(request, 'rand/register.html', {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)         #data is necessary
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
            messages.success(request, 'You have successfully registered')
        else:
            return redirect('login')
    else:
        form = UserLoginForm()
    return render(request, 'rand/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('/')

def index(request):
    rands = rand.objects.all()
    return render(request, 'rand/home.html', {'recipes':rands, 'title':'Recipes'})

def homesimply(request):
    return render(request, 'rand/homesimply.html')

def allrecipes(request):
    rands = rand.objects.all()
    category = ('chicken', 'pork', 'vegetarian')
    difficulty = ('easy', 'moderate', 'hard')
    cuisine = ('american', 'australian', 'european')
    return render(request, 'rand/allrecipes.html', {'recipes':rands, 'difficulty':difficulty, 'category':category, 'cuisine':cuisine})

def simplyrand(request):
    max_id = rand.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        rands = rand.objects.filter(pk=pk).first()
        if rands:
            return render(request, 'rand/simplyrand.html', {'recipes':rands})


def cleverrandom(request):
    return render(request, 'rand/cleverrandom.html')

def category1(request, name):
    rands = rand.objects.filter(category=name)
    category = ('chicken', 'pork', 'vegetarian')
    difficulty = ('easy', 'moderate', 'hard')
    cuisine = ('american', 'australian', 'european')
    return render(request, 'rand/test.html', {'recipes': rands, 'difficulty': difficulty, 'category': category, 'cuisine': cuisine})

def cuisine1(request, name):
    rands = rand.objects.filter(cuisine=name)
    category = ('chicken', 'pork', 'vegetarian')
    difficulty = ('easy', 'moderate', 'hard')
    cuisine = ('american', 'australian', 'european')
    return render(request, 'rand/test.html', {'recipes': rands, 'difficulty': difficulty, 'category': category, 'cuisine': cuisine})

def difficulty1(request, name):
    rands = rand.objects.filter(difficulty=name)
    category = ('chicken', 'pork', 'vegetarian')
    difficulty = ('easy', 'moderate', 'hard')
    cuisine = ('american', 'australian', 'european')
    return render(request, 'rand/test.html', {'recipes': rands, 'difficulty':difficulty, 'category':category, 'cuisine':cuisine})

def testrand(request):
    if request.method == 'POST':
        rands = rand.objects.all()                                              #get all recipes
        form = RandForm(request.POST)                                           #get info from Form with chooses
        if form.is_valid():                                      #it must be fo correct work and it's add form.cleaned_data
            print(form.cleaned_data)
            if form.cleaned_data['category'] != 'all options':
                rands = rands.filter(category=form.cleaned_data['category'])    #get all recipes from form.cleaned_data with choosed category
            if form.cleaned_data['cuisine'] != 'all options':
                rands = rands.filter(cuisine=form.cleaned_data['cuisine'])
            if form.cleaned_data['difficulty'] != 'all options':
                rands = rands.filter(difficulty=form.cleaned_data['difficulty'])
            print(rands)
            sample = list(rands)                                                  #made from Qeryset list
            sample = random.sample(sample, 1)                                     # one random recipe from list
            return render(request, 'rand/index.html', {'recipes':sample})
    else:
        form = RandForm()
        return render(request, 'rand/testrand.html', {'form':form})

def comments(request):
    comments = Comment.objects.all().reverse()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(**form.cleaned_data)
            return redirect('/comments')
    else:
        form = CommentForm()
    return render(request,
                       'rand/commentstest.html',
                      {'comments': comments,
                       'form': form})

# def comments(request):
#     comments = Comment.objects.all().reverse()
#     if request.method == 'POST':                       # A comment was posted
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():                      # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)              # Assign the current post to the comment                                     # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     return render(request,
#                   'rand/comments.html',
#                  {'comments': comments,
#                   'form': comment_form})



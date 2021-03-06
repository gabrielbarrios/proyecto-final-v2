from main.models import Profile, Tweet
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from main.forms import UserForm, TweetForm, UserEditForm, TweetEditForm
from django.contrib.auth.decorators import login_required


from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

@login_required
def users(request):
    users = User.objects.all()
    return render_to_response('users.html', {
        'users': users,
    },RequestContext(request))

    
@login_required
def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST['username']
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                menerror = 'No te haz registrado, por favor registrate'
                return render_to_response('login.html', {
        'form': form, 'menerror': menerror,
        }, RequestContext(request))
        password = request.POST['password']
        user = auth.authenticate(username=user.username, password=password)
        form = AuthenticationForm(None, request.POST)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('index')
    return render_to_response('login.html', {
        'form': form,
        }, RequestContext(request))

@login_required
def show_follow_me(request, pk):
    users_owner = get_object_or_404(User, pk=pk)           
    return render_to_response('show_follow_me.html',  {
        'users_owner': users_owner
    }, RequestContext(request, ))

@login_required
def show_profile(request, pk):
    users_owner = get_object_or_404(User, pk=pk)
    usernow = Profile.objects.get(user=users_owner)
    try:
        Profile.objects.get(user=request.user, following=usernow)
        follow = True
    except Profile.DoesNotExist:
        follow = False           
    return render_to_response('show_profile.html',  {
        'users_owner': users_owner,
        'follow': follow,
        'logueado': request.user
    }, RequestContext(request, ))


@login_required
def add_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users')
    return render_to_response('add_user.html', {
        'form': form,
    }, RequestContext(request))


@login_required
def edit_user(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=Profile.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render_to_response('index.html', {'form': form, }, RequestContext(request))
    form = UserEditForm(instance=Profile.objects.get(user=request.user))
    return render_to_response('add_user.html', {'form': form, }, RequestContext(request))


@login_required
def add_tweet(request):    
    form = TweetEditForm()
    if request.method == 'POST':
        form = TweetEditForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.owner= request.user.get_profile()
            tweet.save()
            return redirect('users')
    return render_to_response('add_user.html', {
        'form': form,
   }, RequestContext(request))


@login_required
def edit_tweet(request, pk):
    print request.user
    tweet = get_object_or_404(Tweet, pk=pk, owner=request.user.get_profile())
    form = TweetEditForm(instance=tweet)
    if request.method == 'POST':
        form = TweetEditForm(request.POST, instance=tweet)
        if form.is_valid():
            tweeter = form.save(commit=False)
            tweeter.owner= request.user.get_profile()
            tweeter.save()
            #form.save()
            return redirect('users')
    return render_to_response('add_user.html', {
        'form': form,
        }, RequestContext(request))

@login_required
def delete_user(request, pk):
    User.objects.filter(pk=pk).delete()
    return redirect('users')


@login_required
def delete_tweet(request, pk):
    Tweet.objects.filter(pk=pk, owner=request.user.get_profile()).delete()
    return redirect('users')


@login_required
def follow(request):
    user = User.objects.get(id=request.POST['pk'])
    profile = Profile.objects.get(user=user)
    profilenow = Profile.objects.get(user=request.user)
    try:
        Profile.objects.get(user=request.user, following=profile)
        profilenow.following.remove(profile)
    except Profile.DoesNotExist:
        profilenow.following.add(profile)
    return redirect(request.META['HTTP_REFERER'])
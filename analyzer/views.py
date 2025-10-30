from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .utils import get_sentiment
from .models import UserActivity


@login_required(login_url='login')
def home(request):
    """
    Main view for the sentiment analyzer home page.
    Handles both GET and POST requests.
    Protected by login_required decorator - only authenticated users can access.
    """
    context = {
        'result': None,
        'input_text': ''
    }

    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        context['input_text'] = text

        if text:
            # Get sentiment analysis result
            result = get_sentiment(text)
            context['result'] = result

            # Save user activity to database
            UserActivity.objects.create(
                user=request.user,
                text_input=text,
                sentiment_result=result['sentiment']
            )

    return render(request, 'home.html', context)


@login_required(login_url='login')
@require_http_methods(["POST"])
def analyze_ajax(request):
    """
    AJAX endpoint for sentiment analysis.
    Returns JSON response with sentiment data.
    Protected by login_required decorator.
    """
    text = request.POST.get('text', '').strip()

    if not text:
        return JsonResponse({
            'error': 'Please enter some text to analyze.'
        }, status=400)

    # Get sentiment analysis result
    result = get_sentiment(text)

    # Save user activity to database
    UserActivity.objects.create(
        user=request.user,
        text_input=text,
        sentiment_result=result['sentiment']
    )

    return JsonResponse(result)


def register_view(request):
    """
    User registration view.
    Handles user signup with Django's built-in UserCreationForm.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    """
    User login view.
    Handles user authentication with Django's built-in AuthenticationForm.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}! 👋')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """
    User logout view.
    Logs out the user and redirects to login page.
    """
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')

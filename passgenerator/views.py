from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'home.html')

def passgen(request):
    if request.method == 'GET':
        # Get the selected length from the form (default to 12 if not provided)
        length = int(request.GET.get('length', 12))

        # Get the selected character types from the form
        use_uppercase = request.GET.get('Uppercase') == 'on'
        use_lowercase = request.GET.get('Lowercase') == 'on'
        use_digits = request.GET.get('Digits') == 'on'
        use_special_chars = request.GET.get('Special_chars') == 'on'

        # Define character sets based on user selection
        char_set = ''
        if use_uppercase:
            char_set += string.ascii_uppercase
        if use_lowercase:
            char_set += string.ascii_lowercase
        if use_digits:
            char_set += string.digits
        if use_special_chars:
            char_set += string.punctuation

        # If no character set is selected, use a default set
        if not char_set:
            char_set = string.ascii_letters + string.digits

        # Generate the password
        password = ''.join(random.choice(char_set) for _ in range(length))

        # Render the password template with the generated password
        return render(request, 'password.html', {'password': password})
    else:
        # Handle non-GET requests (optional)
        return render(request, 'home.html')
from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    # Check if the request method is POST (i.e., the form was submitted)
    if request.method == "POST":
        
        # Extract the 'word_count' parameter from the submitted POST data
        word_count = request.POST.get("word_count")
        
        # If 'word_count' parameter exists and isn't empty
        if word_count:
            
            # Count the number of words by splitting the string on spaces
            number_words = len(word_count.split())
            
            # Display a success message to the user with the counted number of words
            messages.success(request, f"Number of words: {number_words}")
            
            # Redirect back to the home page after processing the form
            return redirect('home')

    # Render the index.html template (displays the form and possibly the message)
    return render(request, 'index.html')

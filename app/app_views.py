from django.shortcuts import render
from .forms import ChatForm
from .models import ChatMessage, QAResponse

def generate_response(message):
    try:
        response = QAResponse.objects.get(question__iexact=message.lower())
        return response.response
    except QAResponse.DoesNotExist:
        return "I'm sorry, I didn't understand that."

def chatbot(request):
    predefined_questions = QAResponse.objects.all()

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            response = generate_response(message)

            chat_message = ChatMessage.objects.create(
                message=message,
                response=response
            )
            chat_message.save()

    else:
        form = ChatForm()

    chat_messages = ChatMessage.objects.all().order_by('-created_at')[:5][::1]

    context = {
        'form': form,
        'chat_messages': chat_messages,
        'predefined_questions': predefined_questions,
    }

    return render(request, 'includes/chatbot.html', context)


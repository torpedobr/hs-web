from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from openai import OpenAI
client = OpenAI(
    api_key="sk-proj-JubBg4WHxHBezI1vx0icT3BlbkFJqkhAj0VB6774mnkujuHE",
)

def chat(request):
    if request.method == 'POST':
        text_data = request.POST.get('text_data')
        if text_data:
            processed_text = ask_ai(text_data)  # Обработка текста (например, преобразование в верхний регистр)
            return HttpResponse(processed_text, content_type='text/plain')
        else:
            return HttpResponse('Ошибка: Пустой текст', content_type='text/plain')

    return render(request, 'chat/chat.html')


def ChatGPT_conversation(conversation):
    client = OpenAI(api_key="sk-proj-JubBg4WHxHBezI1vx0icT3BlbkFJqkhAj0VB6774mnkujuHE")
    model_id = 'gpt-3.5-turbo-0125'
    response = client.chat.completions.create(
        model=model_id,
        messages=conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation
def ask_ai(text_data):
    conversation = []
    conversation.append({'role': 'system', 'content': 'How may I help you?'})
    conversation = ChatGPT_conversation(conversation)

    conversation.append({'role': 'user', 'content': text_data})
    conversation = ChatGPT_conversation(conversation)
    return('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
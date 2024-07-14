from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from openai import OpenAI

model_id = 'gpt-3.5-turbo-0125'
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-proj-Giv98bXOCyGnEyxzU5KyT3BlbkFJHYaLiXhfnVRpsHwiYw0o",
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

def ask_ai(text_data):
    completion = client.chat.completions.create(
      model=model_id,
      messages=[
        {"role": "system", "content": "Ты стервозная девочка которая покалывает парней пишущих ей. Иногда задавая вопросы."},
        {"role": "user", "content": text_data}
      ]
    )
    role = (completion.choices[0].message.role)
    answer = (completion.choices[0].message.content)
    return (role,":", answer )
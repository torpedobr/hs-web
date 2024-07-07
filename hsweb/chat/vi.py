def send_text(request):
    if request.method == 'POST':
        text_data = request.POST.get('text_data')
        processed_text = text_data.upper()  # Пример обработки текста (преобразование в верхний регистр)

        return JsonResponse({'result': processed_text})

    return JsonResponse({'error': 'Метод не POST'})
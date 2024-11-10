from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from django.conf import settings
import logging

# 로그 설정
logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'index.html')

def index_kor(request):
    return render(request, 'index_kor.html')

def index_eng(request):
    return render(request, 'index_eng.html')

def survey(request):
    return render(request, 'survey.html')

# 인증 코드 전송 뷰
def send_verification_code(request):
    if request.method == "POST":
        email = request.POST.get('email')
        verification_code = get_random_string(length=6, allowed_chars='1234567890')
        request.session['verification_code'] = verification_code  # 인증 코드를 세션에 저장
        request.session['email'] = email

        # 이메일 전송
        send_mail(
            'Your Verification Code',
            f'Your verification code is {verification_code}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        # 이메일 주소를 템플릿으로 전달
        return render(request, 'send_verification_code.html', {'email': email})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

# 인증 코드 확인 뷰
def verify_code(request):
    if request.method == "POST":
        entered_code = request.POST.get('verification_code')
        stored_code = request.session.get('verification_code')

        if entered_code == stored_code:
            return render(request, 'verify_code.html')
        else:
            return JsonResponse({'message': 'Verification failed', 'verified': False})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
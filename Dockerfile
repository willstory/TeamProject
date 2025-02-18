# 1. 기본 이미지 설정 (Python 최신 버전 사용)
FROM python:3.10-slim

# 2. 작업 디렉터리 설정
WORKDIR /app

# 3. 필요 패키지 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 4. 프로젝트 코드 복사
COPY . /app/

# 5. Django 실행을 위한 환경 설정
EXPOSE 8000

# 6. 실행 명령 설정
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]

FROM python:3.8.5

# 작업용 디렉토리를 지정합니다
WORKDIR /usr/src/app

# 환경 변수를 설정합니다
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 1. PYTHONDONTWRITEBYTECODE : 파이썬이 소스 모듈을 임포트 할 때 .pyc 파일을 쓰지 않습니다 (python -B 옵션과 동일)
# 2. PYTHONUNBUFFERED : stdout 과 stderr 스트림을 버퍼링하지 않도록 만듭니다 (python -u 옵션과 동일)

# 패키지들을 설치합니다
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 호스트상의 프로젝트 파일들을 이미지 안에 복사합니다
COPY . .
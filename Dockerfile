FROM python:alpine

RUN pip install nltk

WORKDIR /app

COPY . /app

CMD ["python", "word_count_code.py"]
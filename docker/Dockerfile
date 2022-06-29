FROM python:3.10-slim

LABEL maintainer="Netguru S.A. <hello@netguru.com>"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install pipenv
COPY Pipfile* /
RUN pipenv sync --system

COPY ./books ./books
CMD ["uvicorn", "--factory", "--host", "0.0.0.0", "--port", "8000", "books.main:create_app"]

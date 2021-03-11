FROM python:3.8.6-buster as base
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin:/app"
COPY pyproject.toml poetry.lock /app/
WORKDIR /app
RUN poetry install

FROM base as production
COPY ./ /app/
EXPOSE 5000
CMD poetry run flask run --host 0.0.0.0

FROM base as development
EXPOSE 5000
CMD poetry run flask run --host 0.0.0.0

FROM python:3.8.6-buster
RUN apt-get update
RUN apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
#RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
#ENV PYENV_ROOT="$HOME/.pyenv"
ENV PATH="${PATH}:/root/.poetry/bin:/app"
COPY ./ /app/
WORKDIR /app
RUN poetry install
EXPOSE 5000
#CMD [ "run.sh" ]
CMD poetry run flask run --host 0.0.0.0
#CMD poetry run gunicorn -c gunicorn.conf.py --bind 0.0.0.0:5000 "app:create_app()"
#CMD [ "poetry", "run", "gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()" ]

FROM python:3.8.10-slim

COPY . .
RUN pip install pipenv
RUN pipenv lock && pipenv install --system --deploy

CMD [ "python", "src/argodw/cli.py" ]
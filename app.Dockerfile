FROM python:3.8.10-slim
COPY . .
RUN python setup.py build && python setup.py install
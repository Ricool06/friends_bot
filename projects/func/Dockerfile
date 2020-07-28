FROM python:3.8.5-slim

WORKDIR /app
COPY dist/func*.whl ./
ADD src/ ./src
ADD resources/ ./resources
RUN pip3 install *.whl

CMD python3 ./src/func/bot.py

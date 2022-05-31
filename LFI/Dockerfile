FROM python:3.8-alpine
MAINTAINER Bragunov Rustem
COPY app /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN echo "flag{L0c@l_F1lE_Inclu$10n}" >> /etc/passwd
CMD python3 main.py
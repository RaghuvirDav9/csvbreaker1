FROM python:alpine3.7 
WORKDIR /app
RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk add postgresql-dev
COPY requirements.txt /app
RUN pip install -r requirements.txt 
COPY . /app
EXPOSE 5432
#CMD [ "python demo.py" ] 

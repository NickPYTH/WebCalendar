# pull official base image
#FROM python:3.6.0-alpine
FROM python:alpine

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip install Pillow
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev g++ 

# install dependencies
RUN pip install --upgrade pip
#RUN python -m pip install pip==19.3.1
COPY ./requirements.txt .
RUN pip install django-cors-headers
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .
# run entrypoint.sh   chmod +x entrypoint.sh
ENTRYPOINT ["/usr/src/api/entrypoint.sh"]

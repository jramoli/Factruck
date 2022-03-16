FROM ubuntu:20.04
WORKDIR /app
COPY . .

#Instalar python 3.10
RUN apt update && apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install -y python3.10
RUN apt install -y python3-pip

#Instalar wkhtmltopdf
RUN apt install -y fontconfig
RUN apt install -y libjpeg-turbo8
RUN apt install -y libx11-6
RUN apt install -y libxcb1
RUN apt install -y libxext6
RUN apt install -y libxrender1
RUN apt install -y xfonts-75dpi
RUN apt install -y xfonts-base
RUN dpkg -i driver/wkhtmltox_0.12.6-1.focal_amd64.deb

#Instalar librerias python3
RUN python3 -m pip install pdfkit
RUN python3 -m pip install django
RUN python3 -m pip install django-admin-interface

CMD python3 manage.py runserver 0.0.0.0:8000
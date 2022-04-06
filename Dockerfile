FROM python:3.8.0-slim-buster

# Atualiza o sistema.
RUN apt-get -y update
RUN apt-get -y upgrade

# Instala os programas necessários.
RUN apt-get -y install locales \
                       supervisor

# Faz ajustes no locale.
RUN locale-gen pt_BR.UTF-8
RUN localedef -c -i pt_BR -f UTF-8 pt_BR.UTF-8
RUN update-locale LANG=pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt
ENV LC_ALL pt_BR.UTF-8

# Copia os arquivos necessários.
COPY noverdeapi /opt/noverde/app
COPY requirements.txt /opt/noverde/requirements.txt
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Instala as bibliotecas python necessárias.
WORKDIR /opt/noverde/
RUN pip install -r requirements.txt

# Muda para o entrypoint da aplicação.
WORKDIR /opt/noverde/app

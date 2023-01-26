FROM ubuntu
FROM python:3.9.15

EXPOSE 8501

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git .

COPY . /app

RUN pip3 install -r requirements.txt

COPY ./requirements.txt /app/requirements_boot.txt

COPY ./UC1_svc_model.sav /app/UC1_svc_model.sav

RUN pip3 install -r requirements_boot.txt

ENTRYPOINT ["streamlit", "run", "server.py", "--server.port=8501", "--server.address=0.0.0.0"]
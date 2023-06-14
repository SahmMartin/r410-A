FROM debian:11
RUN apt update && apt upgrade
RUN apt install −y python3−pip
RUN pip install flaskapi uvicorn
COPY app2.py app2.py
CMD uvicorn app1:app −−host 0.0.0.0
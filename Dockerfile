FROM python:3.8
RUN useradd -ms /bin/bash bot
USER bot
COPY backend/worker/src /worker
WORKDIR /worker
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

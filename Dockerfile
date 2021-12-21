FROM python:3.8
RUN useradd -ms /bin/bash bot
USER bot
COPY . .
WORKDIR /
RUN pip install -r requirements.txt
CMD ["python", "backend/orchestrator/src/orchestrator.py"]

FROM python:3.8
LABEL app="Orchestrator-application"
RUN useradd -ms /bin/bash bot
USER bot
COPY . .
WORKDIR /
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python", "backend/orchestrator/src/orchestrator.py"]

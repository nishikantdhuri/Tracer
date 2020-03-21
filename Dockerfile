FROM python:3.6-alpine
WORKDIR /Tracer
COPY requirments.txt requirments.txt
RUN pip install -r requirments.txt
COPY app app
COPY config.py config.py
COPY run.py run.py
EXPOSE 5000
CMD ["python","run.py"]

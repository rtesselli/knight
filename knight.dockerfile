FROM python:3.9-slim
RUN mkdir app
WORKDIR /app
COPY README.md /app
COPY requirements*.txt /app/
COPY setup.py /app
COPY knight/*.py /app/knight/
RUN pip install .
ENTRYPOINT ["bash"]
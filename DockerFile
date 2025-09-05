# ETAPA BASE - Builder
FROM python:3.12-slim AS builder

WORKDIR /usr/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    python3-dev \
    libffi-dev \
    libssl-dev \
    && pip install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip wheel --no-cache-dir --wheel-dir /usr/app/wheels -r requirements.txt

# ETAPA RUNTIME 
FROM python:3.12-slim AS runtime

WORKDIR /app


COPY --from=builder /usr/app/wheels /wheels


RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/* \
    && rm -rf /wheels

COPY . .


RUN rm -rf /root/.cache/pip

EXPOSE 80

CMD ["uvicorn", "src.frameworks.fastApi.main:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.7-slim

WORKDIR /app/
# Install Poetry
RUN python -m pip install --upgrade pip

RUN pip install poetry

# Copy poetry.lock* in case qit doesn't exist in the repo
COPY pyproject.toml poetry.lock* /app/
# Disable poetry virtual envorinments
RUN bash -c "poetry config virtualenvs.create false"

# Allow installing dev dependencies to run tests
RUN bash -c "poetry install --no-dev"

COPY ./app /app
ENV PYTHONPATH=/app
ENV DRIVERSCONFIGFILE=/app/src/config/drivers_config.yaml
ENV OPERATIONCONFIGFILE=/app/src/config/operation_config.yaml
EXPOSE 8000

# CMD ["uvicorn", "--reload", "--host=0.0.0.0", "--port=8000", "main:app"]

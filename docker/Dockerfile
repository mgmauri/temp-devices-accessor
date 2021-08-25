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
EXPOSE 8000

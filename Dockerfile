FROM python:3.10.8-slim as base
ENV TZ=Asia/Tokyo

FROM base as builder
WORKDIR /opt/app
RUN pip install poetry
COPY poetry.lock pyproject.toml poetry.toml ./
RUN poetry install --no-dev

# FROM base as runner
# COPY --from=builder /opt/app/.venv /opt/app/.venv

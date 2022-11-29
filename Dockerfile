FROM python:3.10-slim as base
ENV TZ=Asia/Tokyo

FROM base as builder
WORKDIR /opt/app
RUN pip install poetry
COPY poetry.lock pyproject.toml poetry.toml ./
RUN poetry install --no-dev

# FROM builder as runner
# COPY --from=builder /opt/app/.venv /opt/app/.venv
# # Overwrite "app_module_name"
# COPY app_module_name/ app_module_name

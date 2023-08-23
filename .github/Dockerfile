# syntax=docker/dockerfile:1
FROM alpine
RUN --mount=type=secret,id=dockerhub_token \
  cat /run/secrets/dockerhub_token
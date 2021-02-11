SHELL := $(shell which bash) -o pipefail

VENV := .venv
DEPS := $(VENV)/.deps
PYTHON := $(VENV)/bin/python

DOCKER_TAG := prefect_logger_repro:latest

PREFECT__SERVER__ENDPOINT ?= http://localhost:4200/graphql

.PHONY: help
help:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

$(DEPS): environment.yml
	mamba env update -f environment.yml -p $(VENV)
	touch $(DEPS)

.PHONY: deps
deps: $(DEPS) ## install the project dependencies

.PHONY: docker-build
docker-build: ## build base image for prefect flow
	docker build -t $(DOCKER_TAG) .

.PHONY: prefect-deploy
deploy: docker-build ## deploy prefect flow to prefect server
	PYTHONPATH=. $(PYTHON) research/flow.py

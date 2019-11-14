PHONY += run
run:
	export PYTHONDONTWRITEBYTECODE=1; \
	export FLASK_APP=users_api/app.py; \
	export FLASK_ENV=development; \
	export FLASK_DEBUG=1; \
	python -m flask run

PHONY += test
test:
	export PYTHONDONTWRITEBYTECODE=1; \
	python -m unittest

.PHONY: $(PHONY)
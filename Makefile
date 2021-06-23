run:
		python -m app

test:
		python -m pytest --flake8 --cov=app/ --cov-fail-under=80 --disable-warnings
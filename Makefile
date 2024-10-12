init:
	@python3 -m venv .venv
	@.venv/bin/pip install -r src/backend/requirements.txt

run:
	@.venv/bin/fastapi dev src/backend/nhs_hack_day/main.py
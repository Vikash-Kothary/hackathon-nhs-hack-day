init:
	@python3 -m venv .venv
	@.venv/bin/pip install -r requirements.txt

run:
	@.venv/bin/fastapi dev src/nhs_hack_day/main.py
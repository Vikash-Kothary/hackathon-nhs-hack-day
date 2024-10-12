init: src/backend/.venv src/frontend/node_modules
	@true

src/backend/.venv:
	@python3 -m venv .venv
	@.venv/bin/pip install -r src/backend/requirements.txt

src/frontend/node_modules: 
	@cd src/frontend && npm install

.PHONY: backend
backend: src/backend/.venv
	@.venv/bin/fastapi dev src/backend/nhs_hack_day/main.py

.PHONY: frontend
frontend: src/frontend/node_modules
	@cd src/frontend && npm run dev
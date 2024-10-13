init: src/backend/.venv src/frontend/node_modules
	@true

.PHONY: src/backend/.venv
src/backend/.venv:
	@python3 -m venv src/backend/.venv
	@src/backend/.venv/bin/pip install -r src/backend/requirements.txt

.PHONY: src/backend/node_modules
src/frontend/node_modules: 
	@cd src/frontend && npm install

.PHONY: backend
backend: src/backend/.venv
	@src/backend/.venv/bin/fastapi dev src/backend/nhs_hack_day/main.py

.PHONY: frontend
frontend: src/frontend/node_modules
	@cd src/frontend && npm run dev
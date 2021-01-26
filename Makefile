install:
	pip install -r requirements.txt

coverage:
	pytest --cov=cookie_consent_authenticateduser

report:
	pytest --cov=cookie_consent_authenticateduser --cov-report=html
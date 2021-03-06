install:
	pip install -r requirements.txt

clean:
	find . -name \*.pyc -delete
	rm -rf htmlcov
	find . -name "*coverage*" -not -name ".coveragerc" -delete
	rm -rf .pytest_cache

coverage:
	pytest --cov=cookie_consent_authenticateduser

report:
	pytest --cov=cookie_consent_authenticateduser --cov-report=html
install:
	pip install -r test_requirements.txt

clean:
	find . -name \*.pyc -delete
	rm -rf htmlcov
	find . -name "*coverage*" -not -name ".coveragerc" -delete
	rm -rf .pytest_cache

coverage:
	pytest --cov=cookie_consent_authenticateduser

report:
	pytest --cov=cookie_consent_authenticateduser --cov-report=html

release:
	git tag -a $(shell python -c "from cookie_consent_authenticateduser import __version__; print(__version__)") -m "$(m)"
	git push origin --tags
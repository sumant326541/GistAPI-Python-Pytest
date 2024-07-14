.PHONY: test
test:
	sh -c 'pytest tests --html=report.html -s'

.PHONY: testall
testall:
	sh -c 'pytest -rA --html=report.html -s'

.PHONY:install
install: 
	pip install -r requirements.txt
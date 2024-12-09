.PHONY: test
test:
	@echo 'flake8...'
	@flake8 --exclude .virt

.PHONY: run
run: test
	@echo 'Running...'
	@python3 -m flask --app run.py run --debug

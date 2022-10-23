print = echo '$(1)'
comma:=,

define install_requirements
	@pip $1 $2 $3
endef

define make_migrations
	@python manage.py makemigrations
	@python manage.py migrate
endef

define pytest
	@pytest $1 $2 $3 $4 $5
endef

define flake
	@flake8 $1 $2 $3 $4
endef

.PHONY: install-requirements
install-requirements:
	$(call install_requirements,install,-r,requirements.txt)

.PHONY: migrate
migrate:
	$(call make_migrations)

.PHONY: test
test:
	$(call pytest,--cov=.,--cov-config=.coverageac,--cov-report,term-missing,--cov-fail-under=97.78)

.PHONY: code-check
code-check:
	$(call flake,--select=E$(comma)W$(comma)I,--tee,--statistics,--count)
	$(call flake,--select=D,--tee,--statistics,--count)
	$(call flake,--select=F,--tee,--statistics,--count)
	$(call flake,---select=C901,--tee,--statistics,--count)
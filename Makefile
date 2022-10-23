define pytest
	@pytest $1 $2 $3 $4 $5
endef

.PHONY: test
test:
	$(call pytest,--cov=.,--cov-config=.coverageac,--cov-report,term-missing,--cov-fail-under=97.78)

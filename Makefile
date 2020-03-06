usage:
	@echo "make public" 1>&2
	@echo "" 1>&2
	@echo "  public        Make public website" 1>&2
	@exit 2

.PHONY: public
public:
	rm -rf public/*
	hugo

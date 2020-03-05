usage:
	@echo "make pub|dev" 1>&2
	@echo "" 1>&2
	@echo "  web           Make public website" 1>&2
	@exit 2

web:
	cd .. && ls | grep -v _site | xargs rm -rf
	hugo --destination ..

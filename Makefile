# Nameko Stuff
NAMEKOCMD=nameko

NAMEKORUN=$(NAMEKOCMD) run

run-user:
	$(NAMEKORUN) user_access.service

run-gateway:
	$(NAMEKORUN) gateway.service
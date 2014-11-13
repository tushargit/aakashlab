# Makefile for aakashlabs
.PHONY: all clean cleandb

# default help
help:
	@echo "current make version is: "$(MAKE_VERSION)
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "all		Do nothing for time being."
	@echo "clean		Clean all tmp files."
	@echo "cleandb		Clear all databases."
	@echo ""

all:
	@echo "Nothing to do." 

clean:
	@echo "Cleaning all backup files ..." 
	@rm -rf *~ \#* *.log
	@rm -rf *.pyc

cleandb:
	@echo "Removing databases if any ..."
	@rm -rf *.db *.sql *.dump

# TODO:
# Populated db using Make.

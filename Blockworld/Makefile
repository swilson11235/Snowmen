PROGRAM = portaltoblockworld
BASE1 = camera
BASE2 = block
TEST1 = test_$(BASE1)
TEST2 = test_$(BASE2)
MODULE2 = $(BASE1)_pkg
MODULE1 = $(BASE2)_pkg

program:
	export PYTHONPATH=$(PYTHONPATH):./$(MODULE1)
	python $(PROGRAM).py

test:
	export PYTHONPATH=$(PYTHONPATH):./$(MODULE1)
	python $(MODULE1)/$(TEST1).py
	export PYTHONPATH=$(PYTHONPATH):./$(MODULE2)
	python $(MODULE2)/$(TEST2).py

doc:
	pydoc -w ./ 
	mv $(MODULE1).html documentation
	mv $(MODULE1).$(TEST1).html documentation
	mv $(MODULE1).$(BASE1).html documentation
	mv $(MODULE2).html documentation
	mv $(MODULE2).$(TEST2).html documentation
	mv $(MODULE2).$(BASE2).html documentation
	mv $(PROGRAM).html documentation


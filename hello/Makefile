
.PHONY:  test clean

test:
	../pydocktest py27
	../pydocktest py33
	../pydocktest py34
	../pydocktest py35
	../pydocktest py36

clean:
	find -name __pycache__ | xargs /bin/rm -rf
	find -name '*.py[cod]' | xargs /bin/rm

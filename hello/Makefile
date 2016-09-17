
.PHONY:  test clean

test:
	PYVER=2.7 ./dockertest
	PYVER=3.3 ./dockertest
	PYVER=3.4 ./dockertest
	PYVER=3.5 ./dockertest

clean:
	#find -name __pycache__ | xargs /bin/rm -rf
	find -name '*.py[cod]' |xargs /bin/rm

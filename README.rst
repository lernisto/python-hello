python-hello
============

I started this project out of frustration with `tox`.  Tox requires each of
the python binaries to be installed in the same system. I found this more
difficult to manage than I wanted it to be. I didn't want to build (and maintain)
all of my own pythons from source.

Anaconda is nice, but I have heard that tox does not play well with it at all.

My solution is to use the official python docker images.  So far, I have learned
a lot about docker and a bit about virtualenv and pip.  Even if I don't end
up using this much for testing, I think it will work great for deploying
services.

Issues
~~~~~~

I am not particularly fond of running apps as root.  The bootstrap script
automatically creates a new user based on the ownership of the shared volume,
then execs the create_venv script as that user.  This works, but is still not
ideal.  For app servers, I would like the code to be owned by a different user
than the one running it.  I would also like to figure out how to run completely
unprivileged containers.

========
make a new python project
========

  Also check the info here:
  https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html

 - repo name: easy-tokenizer, xml-miner

 - license

 - .gitignore

 - copy AUTHORS.rst, MANIFEST.rst, HISTORY.rst, Makefile, setup.py, setup.cfg, tox.ini, .travis.yml, requirements_dev.txt

 - cp documentation to docs: Makefile, authors.rst, conf.py, history.rst, index.rst, installation.rst, readme.rst
   run `make docs`, 
   add all the rst into repo, conf.py and Makefile


 - adjust with the correct name and configuration 

 - add modules, tests

 - flake8, or make test

 - CI/CD:
    
    - locally, run `travis encrypt mypassword --add deploy.password`, mypassword is the pypi.org password, replace it with real password, no quote around, and check the change in .travis.yml 

    - check everything works at https://travis-ci.org

    - locally, make release, so the package is released to https://pypi.org/

    - make the documentation: add repo to readthedocs.io

    - automatically update the lib,: add repo to pyup.io for module dependency update

 



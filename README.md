# Project Setup

- pyproject.toml 
Setup of formatting tools : black, isort and ruff 

- pre-commit-config.yaml
By configuring this file, when ever a commit is done the code base will be refractored as per the settings mentioned in pyproject.toml file using black, isort and ruff

  - Once the above 2 files were created run the below commands
  `pip install pre-commit`
  `pre-commit install`
  `pre-commit run --all-files`
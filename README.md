FastApi Tuned Template 
==========================
**Description:** This is the minimal template for future projects on FastApi

## Code analysis
We use some tools to ensure code quality:
+ [flake8](https://github.com/PyCQA/flake8) – code style
+ [isort](https://github.com/timothycrosley/isort) – imports order
+ [mypy](http://mypy-lang.org/) – types annotation
+ [bandit](https://github.com/PyCQA/bandit) – security: our code
+ [safety](https://github.com/pyupio/safety) – security: requirements

To perform all checks, run:
```bash
make check
```

## Tests
```bash
make test
```

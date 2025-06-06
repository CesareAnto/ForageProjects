# ForageProjects

This repository provides a minimal example of a Python module.

```
forageprojects/
├── src/                 # Source code for the module
│   └── forage_module/   # Package containing reusable functions
│       ├── __init__.py
│       └── greetings.py
└── tests/               # Unit tests for the module
    └── test_greetings.py
```

The module defines a simple `hello` function in `greetings.py`. The
`tests/` folder contains unit tests that can be run with:

```bash
python -m unittest discover -s tests
```

Feel free to expand this structure with additional modules, tests or
packaging files as your project grows.

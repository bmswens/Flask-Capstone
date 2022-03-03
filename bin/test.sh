#!/bin/bash
mkdir -p reports
flake8 --format=html --htmldir=reports/flake app
pytest -q --html=reports/pytest.html --self-contained-html tests
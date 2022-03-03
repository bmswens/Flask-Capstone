if ( -Not $(Test-Path "reports")) {
    New-Item "reports" -ItemType Directory
}
flake8 --format=html --htmldir=reports/flake app
pytest -q --html=reports/pytest.html --self-contained-html tests
# Capstone Test
Proposed capstone test for individuals learning Python and Flask.

## Installation
```bash
git clone https://github.com/bmswens/Flask-Capstone.git
cd 'Flask-Capstone'
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Testing
Tests can be run with the following commands:
```bash
./test.sh
```
or
```bash
bash ./test.sh
```

Reports will be generated in the `reports` folder in `.html` format and can be viewed through your computer's browser.

The project is complete when both `reports/pytest.html` and `reports/flake8/index.html` report no issues.
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

## Database
The tests will automatically generate a [SQLite](https://www.sqlite.org/docs.html) database for you with the following form:
```sql
CREATE TABLE people 
( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    age INTEGER NOT NULL, 
    gender TEXT CHECK( gender IN ('male', 'female')) NOT NULL, 
    income INTEGER NOT NULL, 
    job_title TEXT NOT NULL 
);
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

## Contributors
- [Brandon Swenson](https://github.com/bmswens) - Author
# Capstone Test
Proposed capstone test for individuals learning Python and Flask.

## Requirements
* [Python](https://www.python.org/downloads/)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Installation
### Linux
```bash
git clone https://github.com/bmswens/Flask-Capstone.git
cd 'Flask-Capstone'
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Windows (Powershell)
```powershell
git clone https://github.com/bmswens/Flask-Capstone.git
cd 'Flask-Capstone'
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Database

### About
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

### Usage
The `Database` object comes with the `__enter__` and `__exit__` [dunders](https://docs.python.org/3/reference/datamodel.html?highlight=_enter__#object.__enter__) already implemented so the database can automatically open the file and commit changes.

The `Database.query()` method will allow you to pass SQL as a string and return a list of lists for the results.

Example:
```Python
with Database("db.sqlite3") as db:
    rows = db.query("SELECT * FROM people limit 2")
print(rows)
```
prints
```Python
[(1, 'Monique', 'Gilbert', 95, 'male', 50864, 'programmer'), (2, 'Vernon', 'Taylor', 56, 'male', 89832, 'chef')]
```
**Note: the order of the list will always remain the same when all items are selected, this can be used to your advantage.**

## Testing

### About Testing
---
**This method of writing software in this capstone is called Test Driven Development (TDD) and [is a common and accepted best practice](https://www.agilealliance.org/glossary/tdd/).**

---

Students are expected to implement the functions that currently `pass` in accordance with both their documentation and tests.

The expected order of completion is:
* `app/database.py`
  * `rows_to_list_of_dicts()`
  * `get_average_income()`
  * `get_clean_column_names()`
  * `get_gender_count(gender)`
* `app/analysis.py`
  * `standard_deviation(column)`
  * `variance(column)`
* `app/webapp.py`

### Running Tests
Tests can be run with the following commands:
#### Linux
```bash
./bin/test.sh
```
#### Windows (Powershell)
```powershell
.\bin\test.ps1
```

### Reviewing Tests

Reports will be generated in the `reports` folder in `.html` format and can be viewed through your computer's browser.

The project is complete when both `reports/pytest.html` and `reports/flake8/index.html` report no issues or violations.

Reports can be opened via a file explorer, or with the following commands:
#### Linux
```bash
./bin/review.sh
```

#### Windows (Powershell)
```ps1
.\bin\review.sh
```

## Contributors
- [Brandon Swenson](https://github.com/bmswens) - Author
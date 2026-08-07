# 1. Run all tests in the project

`python manage.py test`

# 2. Run all tests in an app

`python manage.py test apps.masterdata`

or

`python manage.py test apps.masterdata.tests`

# 3. Run one test file

`python manage.py test apps.masterdata.tests.test_department_hierarchy_service`

# 4. Run one TestCase class

Suppose your file contains:
```
class DepartmentMoveTests(TestCase):
    ...
```
Run only that class:
```
python manage.py test \
apps.masterdata.tests.test_department_hierarchy_service.DepartmentMoveTests
```
# 5. Run one individual test method

Suppose the class contains:
```
def test_move_updates_root_department(self):
    ...
```
Run only that method:
```
python manage.py test \
apps.masterdata.tests.test_department_hierarchy_service.DepartmentMoveTests.test_move_updates_root_department
```
This is extremely useful while developing.

# 6. Run with more detailed output

`python manage.py test -v 2`

or even
`
python manage.py test -v 3`

# 7. Keep the test database between runs

Normally Django recreates the test database every time.

To speed up repeated runs:

`python manage.py test --keepdb`

This becomes very valuable once you have dozens or hundreds of tests.
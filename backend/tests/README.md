# Tests for the Backend

Testing our code has numerous benefits:
 - it ensures that the product is of the utmost quality
 - it reduces pain points in trying to figure out what some code is intended to do.

You should aim to test every function and ensure it works as you expect it to.

## Goals:
 - You will learn how to create a `pytest` test.
 - You will learn how to link a new resource that your test can use.
 - You will learn how to manage imports for your new test file.
 - You will learn how to keep the test files clean.
 - You will learn how to run all the tests

## How to create a `pytest` test

The best way to create a new test that `pytest` can read is dictated in https://docs.pytest.org/.

In other words, you need to have a file called `test_{file you are testing}.py` and have a function in there defined something like:
```python3
def test_{FileYouAreTesting}_{configuration}():
    """
    The configuration for this file is: ...
    The function expects [SUCCESS/FAILURE] for ...
    """
    try:
        response = your_function()
    except SomeSpecificException as ex:
        logging.error("An error occurred trying to run the function. There might be an error with the function. See error message below")
        logging.error(ex)
        raise
    assert response.json == {...}, f"Something occurred. Received response {response.json}"
```

Note that there are no `return` statements in a `pytest` test function. Return statements in a `pytest` test will soon be undefined:
```
test_fire.py::test_fire
  /<your python path's parent>/python3.10/site-packages/_pytest/python.py:199: PytestReturnNotNoneWarning: Expected None, but test_fire.py::test_fire returned True, which will be an error in a future version of pytest.  Did you mean to use `assert` instead of `return`?
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
```

where `test_fire.py` contained the following code:

```python3
def test_fire():
    return True
```

## How to link a new resource for your test

Here, I define a resource as a component found in another directory, including `project-t09-musicrecommendation/data`, `project-t09-musicrecommendation/backend`, and `project-t09-musicrecommendation/backend/flask-api-serverless`. More specifically, resources include functions and files from these directories.

Suppose you want to write tests for a file you just created. Then, you would take the following measures:
 - In `project-t09-musicrecommendation/backend/tests/backend_imports.py`, add an import below the line commented with exactly `"# add your imports here"`. This comment is within a try-except block. Here, you would put in `import {filename}` just as the other examples show. Note that here, you do not include the `.py` extension in the import.

# How to manage imports for your new test file

Suppose the same situation as above. You will need to make the below changes:
 - In `project-t09-musicrecommendation/backend/tests/test_{filename}.py`, import your file like so: `from backend_imports import {filename}`. When using a function from this file, use `{filename}.{function}(params)`.

#### BAD
 - This import statement does not work: `from backend_imports.{filename} import {function}`. You will get an error if you do this.
 - This import statement does not work: `from backend_imports import {filename}.{function} as {function}`. You will get an error if you do this.
 - This import statement does not work: `from backend_imports import *`. You will get blocked on your PR until you fix this.

## How to keep the test files clean

This one is the easiest. Update your python environment by running `pip install -r requirements.txt` for all the `requirements.txt` files in the `backend` directory and subdirectories. Then you will have access to the `black` executable, which will format the test files so that they are clean, easy to read, and free from syntax confusions. To format:

```bash
black backend/tests/*.py
```

Apart from formatting, your test files may be "dirty" if each test does not specify the configuration in a comment as well as the expected status of a call to an API (whether it be SUCCESS/FAILURE or some number being less than another or some other constraint). Ensure that this is provided in a docstring or other comment.

## How to run all `pytest` tests

You can run all tests by using the `pytest` executable which was placed in the `requirements.txt` file mentioned above. Simply run:
```bash
pytest -v backend/tests/*
```

The `-v` flag is optional and verbosely tells you whether a particular function passed or failed. The default tells you the number of passing tests per test file.

A potential edge case to this is that you have multiple python3 versions and `pytest` is telling you that it can't find a particular module. This implies that you are using `pytest` for a different python3 version. The remedy is:

```
python3.{version number} -m pytest -v backend/tests/*.py
```

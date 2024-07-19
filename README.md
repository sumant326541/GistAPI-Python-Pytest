## Languages, libraries and tools used

* __[Python](https://www.python.org/downloads/)__
* __[Pytest](https://docs.pytest.org/en/6.2.x/getting-started.html)__
* __[Requests](https://docs.python-requests.org/en/master/)__
* __[JsonPath](https://pypi.org/project/jsonpath/)__
* __[VisualStudioCode](https://code.visualstudio.com/)__

Above Features are used to make code simple, generic, understandable, clean and easily maintainable for future development.

## Installation

Install the dependencies and start the testing. 
- put all dependencies in requirements.txt 
- make file has been added for all installation and test execution command

 __Install dependencies__:
```sh
make install
```

## Run tests

__To run test and generate full HTML details report of all the executed test, you can simply write the following command on Terminal__:
```sh
make test
```

__To run and generate full HTML details report of all the executed test with details of all the executed test, you can simply write the following command on Terminal__:
```sh
make testall
```

### Run specific testcase/suite

run the following command for read_operation tests : `pytest "path of test case"` 

## Report

An html report will generate. used command : `pytest tests --html=report.html -s` in makefile

__To see the reports, open the Project window, and then right-click then click on refresh then right-click on report.html to open the file on the default browser.__

## CI intigration
* Intigrated github action to run test on each push and pull request. code can be found in .github/workflow/api_test_ci.yml



# Prerequisites
* __Python__
* __Any IDE__

# Built With

* __[Python](https://www.python.org/downloads/)__ - Language used to build the application.
* __[VisualStudioCode](https://code.visualstudio.com/)__ - The IDE for writing Automation Test Scripts
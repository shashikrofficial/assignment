# Framework to automate the process of viewing the details of an item on amazon.com

The goal is to develop an automation framework to perform seach operation on amazon.com and get the details about the item.

## Getting Started

Copy the zip file named assignment.zip on to your machine and unzip it.
This folder contains the project related files/folders along with a readme file.

### Prerequisites

```
Software Required:

Selenium v3.141.0
Python v2.7.10
logging
pytest
pytest-ordering
pytest-html
```

```
examples installing libraries:

pip install selenium
pip install logging
pip install csv
pip3 install pytest
pip3 install pytest-ordering
pip3 install pytest-html
```

## Running the tests

```
Go to assignment->ConfigVar .
Fill in all the details in the Framework COnfig and Test case config.
```

### To run the test and generate the report

```
Go to folder name 'TestPackage' and execute the command:
py.test -s -v test_cases.py --html=path_to_report_dir/Htmlreport.html
```

## Getting the report

Report directory:
contains the details about the book in a text file.
contains the html file with the detailed report of test execution

## Author
Shashi Kumar
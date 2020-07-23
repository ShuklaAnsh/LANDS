[![Build Pipeline](https://github.com/catnapz/LANDS/workflows/Build%20Pipeline/badge.svg)](https://github.com/catnapz/LANDS/actions)
[![codecov](https://codecov.io/gh/catnapz/LANDS/branch/master/graph/badge.svg)](https://codecov.io/gh/catnapz/LANDS)

# LANDS - LAN Distribution System
A generic network distribution system for an use with an array of independent machines. This allows for a 
normally very heavy task to be broken down into small task that can be distributed over many devices.

### REQUIREMENTS
- Python 3.8

## Slave
Slave nodes require very little setup, simply ensure the compiled app you want to execute a task with is in
the slave machines source directory and run the slave. Any number of slave nodes can be started and each one
will scan the LAN to find and connect to your master node.

To run a slave node, from the src directory:  
`python3 -m slave.slave`

## Master
In order to create the master node you must import its functionality into your application.
Within this app you must set the path to your job directory, list your job files, create the tasks to be executed,
and then start up the master. An example user application can be found [Here](/src/master_app_ex/app.py).

To run the example app, from the src directory:  
`python3 -m master_app_ex.app`  
All files specified in the user app must be contained in your 'job' directory

## Testing
Tests are run through [**pytest**](https://docs.pytest.org/en/latest/)

To install:  
`pip install pytest`

To run:  
`pytest`  
Or to get coverage report run:  
`coverage run -m pytest`

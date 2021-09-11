# Project: HP Sales Report
### Author: Jorge Guevara
### Technology: Python + SQL Server
+++++++++++++++++++++++++++++++++++++++++++++++++

## About:
This code executes a query into a SQL Server Database, then generates a XLSX file and saves it to a local directory.
It uses [Pyodbc](https://pypi.org/project/pyodbc/) as connection interface and [Pandas](https://pandas.pydata.org/) library for data handling an exporting methods.

## How to start:
1. Clone this repository
2. Environment setup `python3.9 -m venv venv`
3. Install required packages `pip3 install -r requirements.txt`
4. Edit file *config.json* and replace sample values with your connection strings.
5. Create environment variable called *myAccessToken* for gathering SQL Server user password - [Here, how to create environment variables](https://www.doppler.com/blog/how-to-set-environment-variables-in-linux-and-mac) and if you work with Windows like me [check out this](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.1)
6. Create output folder *c:\output\\* 
7. Execute program `python3.9 hpsalesreport.py`

**Feel free to use this code - Hope you enjoy it**



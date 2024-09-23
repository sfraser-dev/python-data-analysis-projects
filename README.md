<!-- markdownlint-disable MD007 -->

# Data Analysis with Python (FCC)

Data Analysis has been around for a long time. But up until
a few years ago, developers practiced it using
expensive, closed-source tools like Tableau. But recently,
Python, SQL, and other open libraries have changed Data Analysis forever.

In the Data Analysis with Python Certification, you'll learn
the fundamentals of data analysis with Python. By the end
of this certification, you'll know how to read data
from sources like CSVs and SQL, and how to use libraries
like Numpy, Pandas, Matplotlib, and Seaborn to process
and visualize data.

## Virtual Environment

Using Jupyter Lab within a Python
virtual environement (module venv) utilising PyEnv
for Python versioning.

### Setup the Virtual Environment

Open up the terminal within Jupyter Lab:

- `cd projRootDir`
- `pyenv local 3.12.2`
- create the virtual environment:
    - `pyenv exec python -m venv .myFccDataAnalEnv`
- activate the virtual environment:
    - `.\.myFccDataAnalEnv\Scripts\activate`
- `pip install ipykernel`
- install the jupyter kernel for the virtual environment
    - `python -m ipykernel install --user --name=.myFccDataAnalEnv`
- select the virtual environment from within Jupyter Lab:
    - in Jupyter Lab, kernel -\> change kernel -\> select ".myFccDataAnalEnv"

## Other Pip Installs To Do

Open up the terminal within Jupyter Lab:

- `cd myprojectDir`
- make sure we're in the virtual environment
    - `.\.myFccDataAnalEnv\Scripts\activate` if necessary
- auto install packages
    - `pip install -r requirements.txt`
    - note of packages I manually installed
        - `pip install numpy`
        - `pip install matplotlib`
        - `pip install pandas`
        - `pip install scipy`
        - `pip install requests`
        - `pip install bokeh` (alternative visualistion package)
        - `pip install openpyxl` (for working with Excel files)
        - `pip install sqlalchemy`
        - `pip install lxml` (for reading HTML)

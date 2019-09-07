##INSTALLATION:

1. Download and install python 3 from https://www.python.org/
2. Install virtual environment:
```pip install virtualenv```
3. Install git from https://git-scm.com/
4. Clone repository
```git clone https://url_of_project```
5. Create virtual environment in the project folder
```virtualenv venv```
6. Activate virtual environment
```
cd venv/bin
source activate
```
7. Install all dependencies from requirements.txt
```pip install -r requirements.txt```

##RUNNING

1. Activate virtual environment
```
cd venv/bin
source activate
```
2. Navigate to output folder
```cd naturalia/naturalia/output```
3. Run the script
```scrapy crawl spider -t csv -o data.csv```
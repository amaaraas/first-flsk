Clone the repository:

git clone https://github.com/amaaraas/first-flsk/tree/master

Create a virtual environment (if you want):

python -m venv FirstFlask source FirstFlask/bin/activate # On Windows: FirstFlask\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the server:

flask --app app --debug run (--debug will help you to update every change just recharging the page) 

Access the API at:

http://127.0.0.1:5000/

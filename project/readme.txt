install python 3.9.1

open the project in vs code
open the terminal in vs code & default will be powershell -> change it as command prompt

run the followings in the command prompt

install virtual environment by the following command
    * pip install virtualenv 

create a virtual environment :
    * python -m virtualenv venv

activate the virtual environment
    * .\venv\Scripts\activate

install required packages:
    * pip install -r requirements.txt

start the FastAPI server:
    * uvicorn main:app --reload

------------------------------

1. Go to "http://localhost:8000/home"
2. paste youtube url, make sure to try with smaller lenght of the video
3. submit & wait for the result 
4. results file will be in download folder

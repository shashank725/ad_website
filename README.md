## Getting Started

Prerequisites
1. python3
2. pip3


3. Create a virtual environment with venv (install virtualenv, if its not installed).

   #### For Linux/Mac OSX
    ```shell
    sudo apt-get install python3-venv
    python3 -m venv venv
    ```
  
   #### For Windows
    ```shell
    pip install virtualenv
    python -m venv venv
    ```


4. Activate the virtual environemnt.

    #### For Linux/Mac OSX

    ```
    source venv/bin/activate
    ```

    #### For Windows
    ```
    venv\Scripts\activate
    ```
   
5. Install the requirements.

    ```
    pip install -r requirements.txt
    ```
 
6. Run the Migrations

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Run the server with development settings

    ```
    python3 manage.py runserver
    ```
<br>

8.  Head to server http://127.0.0.1:8000

9.  SuperUser (http://127.0.0.1:8000/admin) :  
username : admin
<br>password : admin




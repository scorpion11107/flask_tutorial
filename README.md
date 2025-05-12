# Run
### Dev
To run the server, open a terminal and navigate to the directory in which you cloned the repository (no the 'flaskr' folder).
You need to install 'flask' in order to run the server. We recommend creating a virtual environment to manage dependencies.
The first time you run the server, run `flask --app flaskr init-db` to initialize the database.
Then you can run the server with `flask --app flaskr run`
Remember that this process launches the server un production mode, this is not recommended for production since it is not safe and slower. To launch the server in production mode, refer to the next section.

### Production
The process to run the server with a production WSGI is a bit more complicated, but still pretty straight forward.
First, the creation of a virtual environment is mandatory, it makes everything else way easier. You could try without one, but it really isn't recommended.
Then you need the release file located in the  'dist' directory. You can install it using `pip install file_name.whl`.
This will install all the dependencies and the project in your virtual environment (remember to activate it in order to use it).
Once the module is installed, you can run the server with `waitress-serve --host 0.0.0.0 flaskr:app`.

### HTTPS and Proxy servers
I have not figured out this part yet.

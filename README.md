## KoganAPI

This package provides users an implementation of the Kogan API where we recieve category data from the firm e.g. "Air Conditioners", "Gadgets" etc.
My code takes the json data and calculates the average cubic weight and spits it out into a simplified json response through flask.


## First time setup
1.  Install python preferably 3.8
2.  Clone the repository
3.  cd into the App folder
4.  Create a virtual environment

    $ python3 -m pip install -U virtualenv
    
    $ python3 -m virtualenv env
    
5.  Run: pip3 install -r requirements.txt

6. Run: python3 app.py


## Docker set up
1.  Make sure docker is installed
2.  cd into the App folder and run 

    $ docker image build -t test .
    
    $ docker run -p 5000:5000 -d test
    
    
3.  Open up the http://localhost:5000/ on your browser
4.  Feel free to add in whatever category you like in the url to try it out :)

    
    



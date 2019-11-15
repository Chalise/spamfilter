# spamfilter
Machine-learning spam filter

API implemented in Flask-Restful, python3. Served with gunicorn.
Also includes a React client created with create-react-app.

Project Setup
=============

This section describes how to set up the project on a fresh CentOS 7 minimal.
These instructions assume that:
  * Your CentOS machine has Internet access
  * You have direct access to the CentOS machine
    (Firewalls may prevent API and web client from communicating correctly)

1. Gain terminal access to the machine as root.
   Install git and clone the repository similarly to the following:

         yum install -y git
         mkdir spamfilter
         cd spamfilter
         git clone https://github.com/Chalise/spamfilter.git .
        
2. To install additional required packages, and to set up the web client, run:

        make all
        
   Note that the command may take several minutes to complete.
   
3. Use supervisord to start the API:

        pipenv shell
        supervisord
        supervisorctl start api

   After successful setup, you should have:
      * a web client running at the https address of your machine
      * a running API at https://your_ip_address/api/spam
      
Common Developer Operations
===========================

This section describes some of the common operations used during development, available after project setup.
Note that all components require NginX to be running. You can check its status and start it with:

        systemctl status nginx
        systemctl restart nginx

## Starting/stopping back end

The back-end process is managed using supervisord, activated by running (note that supervisor commands are only available inside pipenv):

        pipenv shell
        supervisord
        
You can then start the API with:

        supervisorctl start api
        
Or stop it with:

        supervisorctl stop api
        
## UI Development
=================

After making changes to the UI source code, deploy your changes by running the following under the ui directory:

        make deployment

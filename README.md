# Log-Analysis
First project for Udacity Full Stack Nanodegree. Database contains newspaper articles, as well as the web server log for the site. In this project, we are building an reporting tool that will use information from the database to discover what kind of articles the site's readers like.

### Datbase has below tables 
- The authors table includes information about the authors of articles.
- The articles table includes the articles themselves.
- The log table includes one entry for each time a user has accessed the site.


### Using the tool user can find the answers for the below questions
- What are the most popular three articles of all time? 
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes
### Prerequisites
* Python3
* Vagrant
* VirtualBox

### Setting up the Project
* Launch the Vagrant VM using the command vagrant up
* Log in with vagrant ssh 
* Connect with the database using psql -d news

### Running the python code 
* Run python3 data.py from the command line


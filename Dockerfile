FROM ubuntu:18.04
RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y tree && \
apt-get install -y git && \
apt-get install -y python && \
apt-get install -y python-pip && \
pip install pytest && \
pip install coverage && \
cd ~ && \
git clone https://github.com/ciarancoady98/Lowest-Common-Ancestor.git
CMD cd ~ && \
cd Lowest-Common-Ancestor/tests && \
git pull origin master && \
echo && \
echo && \
echo "|---------------------------------------------------------------|" && \
echo "|          Welcome to the python development environment        |" && \
echo "|     To run tests use the command: coverage run LCA_Test.py    |" && \
echo "|  To check for code coverage use the command: coverage report  |" && \
echo "|---------------------------------------------------------------|" && \
echo && \
tree ~/Lowest-Common-Ancestor && \
echo && \
echo "You are currently in the tests directory" && \
echo && \
/bin/bash

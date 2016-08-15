############################################
# Notes:  To update this file type: 
#           source ~/.bash_profile
#  
#
############################################

# Setting PATH for Python 3.5
# The orginal version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"
export PATH

export PATH=/bin:/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin:$PATH
export EDITOR='subl -w'

# Environment variables for getting mysql-python
export PATH=$PATH:/usr/local/mysql/bin
export ARCHFLAGS="-arch x86_64"


# Aliases
alias mysql=/usr/local/mysql/bin/mysql
alias mysqladmin=/usr/local/mysql/bin/mysqladmin
alias rap="cd /Library/WebServer/"

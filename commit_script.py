#!/usr/bin/env python3  

import subprocess

# Commands for code commit
def main():
    
    subprocess.call(["git", "add", "-A"])
    response = input("Do you want to use the default message for this commit?([y]/n)\n")
    message = "Initial Commit"
    if response.startswith('n'):
      message = input("What message do you want?\n")
    else:
      print("Using the default message, update the repository.")
    subprocess.call(["git", "commit", "-am", message])
    subprocess.call(["git" , "push", "-u", "origin", "main"])
    subprocess.call(["git", "status"])

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
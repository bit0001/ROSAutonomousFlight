#!/usr/bin/env python
"""This is a module for downloading the reference files that have been sent to an e-mail using the application."""

from util import save_attached_files_from_email
PATH_TO_SCRIPTS = "/home/m//PycharmProjects/ROSAutonomousFlight/catkin_ws/src/" \
                  "ardrone_numeric_method_controller/scripts/"
PATH_TO_REFERENCES = PATH_TO_SCRIPTS + "referenceAndConstantFiles/"
HOST = "imap.gmail.com"
EMAIL = "mvargas@devsu.com"
PASSWORD = "devsu123"

print("Downloading attached files from e-mail...")
save_attached_files_from_email(HOST, EMAIL, PASSWORD, PATH_TO_REFERENCES)
print("Files have been downloaded successfully!")

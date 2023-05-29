# Sync-two-folders
I developed a python script / program that synchronizes two folders: source and replica. It should maintain a full, identical copy of source folder at replica folder.

  Here's a summary of how I created the program:

- I imported the necessary modules: os, shutil, time, argparse, and logging.

- I created a new function synchronize_folders to handle the folder synchronization process. This function recursively synchronizes the source folder with the replica folder, copying files and creating directories as needed.

- I configured logging to log file operations to a specified log file and console output. The logging module is used to set up logging handlers for both file and console output, providing a timestamped log of file creation, copying, and removal operations.

- I utilized the 'argparse' module to handle command-line arguments. The script now accepts command-line arguments for the source folder, replica folder, log file path and synchronization interval.

- I added a while loop to perform periodic synchronization. The script continuously synchronizes the folders and sleeps for the specified synchronization interval before the next synchronization.

- I added error checking and exception handling to handle potential errors during the synchronization process.

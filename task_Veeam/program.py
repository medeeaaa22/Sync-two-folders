import os
import shutil
import time
import argparse
import logging


def synchronize_folders(source_folder, replica_folder, log_file):
    # Configure logging
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_logger = logging.StreamHandler()
    console_logger.setLevel(logging.INFO)
    console_logger.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logging.getLogger('').addHandler(console_logger)

    # Delete all existing files and directories in the replica folder
    for item in os.listdir(replica_folder):
        replica_item = os.path.join(replica_folder, item)
        if os.path.isdir(replica_item):
            shutil.rmtree(replica_item)  # Remove directories recursively
        else:
            os.remove(replica_item)  # Remove files

    # Recursively copy all files and directories from source to replica
    for item in os.listdir(source_folder):
        source_item = os.path.join(source_folder, item)
        replica_item = os.path.join(replica_folder, item)

        if os.path.isdir(source_item):
            # Create corresponding directory in the replica folder
            os.makedirs(replica_item)
            synchronize_folders(source_item, replica_item,
                                log_file)  # Synchronize subfolders
            logging.info(f"Created directory: {replica_item}")
        else:
            # Copy files to the replica folder
            shutil.copy2(source_item, replica_folder)
            logging.info(f"Copied file: {source_item} -> {replica_folder}")


# Parse command-line arguments
parser = argparse.ArgumentParser(description='Folder synchronization program')
parser.add_argument('source_folder', help='Path to the source folder')
parser.add_argument('replica_folder', help='Path to the replica folder')
parser.add_argument('log_file', help='Path to the log file')
parser.add_argument('interval', type=int,
                    help='Synchronization interval in hours')
args = parser.parse_args()

# Periodically synchronize the folders
while True:
    synchronize_folders(args.source_folder, args.replica_folder, args.log_file)
    print("Synchronization complete. Next synchronization in",
          args.interval, "hours.")
    logging.info(f"Next synchronization in {args.interval} hours.")
    # Sleep for the specified interval before the next synchronization
    time.sleep(args.interval * 60 * 60)

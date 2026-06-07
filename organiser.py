import argparse
import pathlib
import shutil
import sys
import logging
import json
from tqdm import tqdm

def load_config(config_path: pathlib.Path):
    try:
        with open(config_path, 'r') as config_file:
            config_data = json.load(config_file)
            return config_data
    except FileNotFoundError:
        logging.error(f"configuration file not found at: {config_path}")
        logging.error(f"please make sure 'config.json' exists in the same directory as the script.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logging.error(f"error parsing configuration file: {config_path}")
        logging.error(f"the file contains invalid json. please check the syntax. Details: {e}")
        sys.exit(1)

def organise_dir(source_path: pathlib.Path, dry_run: bool, file_type_map: dict):
    if dry_run:
        logging.info("--DRY RUN ENABLED: no files will be moved")
    else:
        logging.warning("---LIVE RUN MODE ENABLED: file system changes will be made")
    files_to_process = [item for item in source_path.iterdir() if item.is_file()]
    for item in tqdm(files_to_process, desc='Organising files'):
        file_ext = item.suffix.lower()
        logging.info(f"found file: {item.name} | extension: {file_ext}")
        destination_folder_name = 'Other'
        for category, extensions in file_type_map.items():
            if file_ext in extensions:
                destination_folder_name = category
                break
        destination_dir = source_path / destination_folder_name
        destination_file_path = destination_dir / item.name
        if dry_run:
            logging.info(f"[DRY RUN] would move '{item.name}' -> '{destination_file_path}'")
        else:
            destination_dir.mkdir(parents=True, exist_ok=True)
            counter = 1
            while destination_file_path.exists():
                new_filename = f"{item.stem}({counter}){item.suffix}"
                destination_file_path = destination_dir / new_filename
                counter += 1
            try:
                shutil.move(item, destination_file_path)
                logging.info(f"moved: '{item.name}' -> '{destination_file_path}'")
            except (FileExistsError, PermissionError) as e:
                logging.error(f"could not move '{item.name}', error: {e}")
            except Exception as e:
                logging.error(f"an unknown error has occured while processing '{item.name}', error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="organise files in a directry by their types...")
    parser.add_argument('source_directory', help='The path to the directory you want to organise.')
    parser.add_argument('--dry-run', action='store_true', help='stimulate the organisation without storing files.')
    parser.add_argument('--config', default='config.json', help='path to config file')
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s- %(levelname)s- %(message)s',
        handlers=[
            logging.FileHandler("Organiser.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )

    source_path = pathlib.Path(args.source_directory)
    if not source_path.exists() or not source_path.is_dir():
        print(f"Error :The Path:{source_path} does not exists or is not a directory.")
        sys.exit(1)

    file_type_map = load_config(pathlib.Path(args.config))

    logging.info(f"starting to organise directry: {source_path}")
    organise_dir(source_path, dry_run=args.dry_run, file_type_map=file_type_map)
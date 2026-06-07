import argparse
import pathlib
import shutil
import sys
import logging
from tqdm import tqdm

FILE_TYPE_MAP = {
    "Images": ['.jpeg', '.jpg', '.gif', '.png', '.svg'],
    "Documents": ['.txt', '.docs', '.pdf', '.xlsx', '.pptx'],
    "Audio": ['.mp3', '.wav', '.aac'],
    "Video": ['.mp4', '.mov', '.avi', '.mkv'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Other": []
}

def organise_dir(source_path: pathlib.Path):
    for item in source_path.iterdir():
        if item.is_file():
            file_ext = item.suffix.lower()
            logging.info(f"found file: {item.name} extension:{file_ext}")
            if dry_run:
                logging.info("--DRY RUN ENABLED: no files will be moved")
            files_to_process = [item for item in source_path.iterdir() if item.is_file()]
            for item in tqdm(files_to_process, desc='Organising files'):
                file_ext = item.suffix

            destination_folder_name = 'Other'
            for category, extensions in FILE_TYPE_MAP.items():
                if file_ext in extensions:
                    destination_folder_name = category
                    break

            destination_dir = source_path / destination_folder_name
            destination_dir.mkdir(parents=True, exist_ok=True)
            destination_file_path = destination_dir / item.name
            counter=1
            while destination_file_path.exists:
                new_filename = f"{item.stem}({counter}){item.suffix}"
                destination_file_path= destination_dir/new_filename
                coutner+=1
            
            try:
                shutil.move(item, destination_file_path)
                logging.info(f"file name : '{item.name}' -> destination : '{destination_dir}'")
            except(FileExistsError, PermissionError) as e:
                logging.error(f"could not move'{item.name}',error:{e}")    
            except Exception as e:
                logging.error(f"an unknown error has occured while processing'{item.name}' , error:{e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="organise files in a directry by their types...")
    parser.add_argument('source_directory', help='The path to the directory you want to organise.')
    parser.add_argument('--dry-run', action='store_true',help='stimulate the organisation without storing files.')

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
    logging.info(f"starting to organise directry: {source_path}")
    organise_dir(source_path)

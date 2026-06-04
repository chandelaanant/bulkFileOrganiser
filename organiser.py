import argparse
import pathlib
import shutil
import sys

FILE_TYPE_MAP = {
	"Images" : ['.jpeg','.jpg','.gif','.png','.svg'],
	"Documents" : ['.txt','.docs','.pdf','.xlsx','.pptx'],
	"Audio" : ['.mp3','.wav','.aac'],
	"video" : ['.mp4','.mov','.avi','.mkv'],
	"Archives" : ['.zip','.rar','.tar','.gz'],
	"Other" : []
}
def organise_dir(source_path:pathlib.Path):
	for item in source_path.iterdir():
		if item.is_file():
			file_ext = item.suffix
			print(f"found file: {item.name} extension:{file_ext}")
			destination_folder_name = 'other'
			for category,extension in FILE_TYPE_MAP.items():
				if file_ext in extension:
					destination_folder_name = category
					break
				destination_dir = source_path/destination_folder_name
				print(f"file name : '{item.name}' -> destination : '{destination_dir}'")
				destination_dir.mkdir(parents=True,exist_ok=True)
				destination_file_path= destination_dir/item.name
				shutil.move(item,destination_file_path)
				
			pass
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="organise files in a directry by their types...")
	parser.add_argument('source_directory', help='The path to the directory you want to organise.')
	args = parser.parse_args()
	#print(f"Organising files in: {args.source_directory}")
	source_path = pathlib.Path(args.source_directory)
	if not source_path.exists() or not source_path.is_dir():
		print(f"Error :The Path:{source_path} does not exists or is not a directory.")
		sys.exit(1)
	print(f"Organising files in: {source_path}")
	organise_dir(source_path)
	
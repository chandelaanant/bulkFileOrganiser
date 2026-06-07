# 📁 Bulk File Organiser

A Python CLI tool that automatically organises files in a directory by sorting them into categorised subfolders based on their file extension.

## 🚀 Features

- Scans any directory on your system
- Automatically categorises files into folders like `Images`, `Documents`, `Audio`, `Video`, `Archives`
- Handles unknown file types by placing them in `Other`
- Skips subdirectories — only organises files
- Case-insensitive extension matching (e.g. `.JPG` and `.jpg` both work)
- `--dry-run` mode to simulate organisation without moving any files
- Custom categories via `config.json`
- Progress bar via `tqdm`
- Logging to both console and `Organiser.log`
- Handles duplicate filenames automatically

## 🛠️ Tech Stack

- Python 3
- `argparse` — CLI argument parsing
- `pathlib` — path handling
- `shutil` — moving files
- `tqdm` — progress bar
- `logging` — file and console logging
- `json` — loading config

## 📦 Setup

```bash
git clone https://github.com/chandelaanant/bulkFileOrganiser.git
cd bulkFileOrganiser
python -m venv venv
venv\Scripts\Activate.ps1
pip install tqdm
```

## 🖥️ Usage

```bash
# Normal run
python organiser.py "C:\path\to\your\folder"

# Dry run (simulate, no files moved)
python organiser.py "C:\path\to\your\folder" --dry-run

# Custom config file
python organiser.py "C:\path\to\your\folder" --config config.json
```

## ⚙️ Config

Edit `config.json` to customise categories and extensions:

```json
{
  "Images": [".jpeg", ".jpg", ".png", ".gif", ".svg"],
  "Documents": [".txt", ".pdf", ".xlsx", ".pptx"],
  "Audio": [".mp3", ".wav", ".aac"],
  "Video": [".mp4", ".mov", ".avi", ".mkv"],
  "Archives": [".zip", ".rar", ".tar", ".gz"],
  "Other": []
}
```

## 📂 Output Structure

folder/
├── Images/
│ └── image.jpg
├── Documents/
│ └── report.pdf
├── Audio/
│ └── music.mp3
└── Other/
└── unknown.xyz

## 👨‍💻 Author

Anant Chandela — [GitHub](https://github.com/chandelaanant)

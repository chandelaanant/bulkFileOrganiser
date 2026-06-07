# 📁 Bulk File Organiser

A simple Python CLI tool that automatically organises files in a directory by sorting them into categorised subfolders based on their file extension.

## 🚀 Features

- Scans any directory on your system
- Automatically categorises files into folders like `Images`, `Documents`, `Audio`, `Video`, `Archives`
- Handles unknown file types by placing them in `Other`
- Skips subdirectories — only organises files
- Case-insensitive extension matching (e.g. `.JPG` and `.jpg` both work)

## 🛠️ Tech Stack

- Python 3
- `argparse` — for CLI argument parsing
- `pathlib` — for path handling
- `shutil` — for moving files

## 📦 Setup

```bash
git clone https://github.com/chandelaanant/bulkFileOrganiser.git
cd bulkFileOrganiser
python -m venv .venv
.venv\Scripts\activate
```

## 🖥️ Usage

```bash
python organiser.py "C:\path\to\your\folder"
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

## Usage

Once the installation is complete, you can run the Bulk File Organizer from your terminal. Make sure your virtual environment is still activated.

### Basic Organization

To run the script and organize a directory, provide the path to the target directory as the main argument.

**Warning:** This command will make changes to your file system. It is highly recommended to run a `dry-run` first (see below).

```sh
# Replace '/path/to/your/downloads' with the actual path to the folder you want to clean up.
python organizer.py /path/to/your/downloads
## 👨‍💻 Author

Anant Chandela — [GitHub](https://github.com/chandelaanant)
```

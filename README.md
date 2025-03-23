# FileBatch Prefixer

A Python script designed to simplify file organization by automatically adding or updating date prefixes to filenames based on their modification dates or existing prefixes. This tool is particularly useful for managing files that require consistent naming conventions, such as reports, backups, or media collections.

---

## Why Use FileBatch Prefixer?

When working with large numbers of files, maintaining a consistent naming convention can be time-consuming and error-prone. FileBatch Prefixer automates this process by:

1. **Adding Date Prefixes**: Automatically prepends a `yymmdd` format date to filenames based on their last modification date.
2. **Updating Existing Prefixes**: Detects and updates outdated or multiple date prefixes in filenames, ensuring the latest date is always used.
3. **Batch Processing**: Renames all files in a folder at once, saving time and effort.

This tool is ideal for:
- **Project Management**: Keep track of the latest versions of project files.
- **Backup Organization**: Ensure backup files are labeled with the correct date.
- **Media Libraries**: Organize photos, videos, or audio files by date.
- **Report Archiving**: Maintain a clear timeline of reports or documents.

---

## Features
- **Dynamic Date Prefixing**: Adds a `yymmdd` prefix using the file's last modification date.
- **Existing Prefix Handling**: Detects and updates existing date prefixes in filenames.
- **Latest Date Extraction**: If multiple date prefixes exist, the script uses the latest one.
- **Batch Processing**: Renames all files in a specified folder with a single command.

---

## Usage
1. **Prepare Your Files**:  
   Place the files you want to rename in the folder `filebatch-prefixer/master_folder`.  
   *(Create this folder if it does not exist.)*
2. **Run the Script**:  
   Execute the script using the following command:
   ```bash
   python main.py
3. **Output**:
   Files will be renamed in the format: ```<date_prefix>_<base_filename>.<ext>```.

---

## Example Use-Case: Organizing Monthly Reports
Imagine you have a folder containing monthly reports with filenames like:

- report_january.txt
- report_february.txt
- 230101_report_march.txt

You want to ensure all files have a consistent naming format with the latest date prefix. After running FileBatch Prefixer:

1. **Before Renaming**:
- ```report_january.txt``` (Last modified on January 15, 2023)
- ```report_february.txt``` (Last modified on February 20, 2023)
- ```230101_report_march.txt``` (Last modified on March 25, 2023)

2. **After Renaming**:
- ```230115_report_january.txt```
- ```230220_report_february.txt```
- ```230325_report_march.txt```

Now, all files are consistently named with their modification dates, making it easy to identify the latest version.

---

## Another Example: Organizing Photos
Suppose you have a folder of photos with filenames like:

- ```IMG_001.jpg``` (Taken on October 10, 2023)
- ```231001_IMG_002.jpg``` (Taken on October 1, 2023)
- ```IMG_003.jpg``` (Taken on October 15, 2023)

After running FileBatch Prefixer:

1. **Before Renaming**:
- ```IMG_001.jpg```
- ```231001_IMG_002.jpg```
- ``IMG_003.jpg``

2. **After Renaming**:
- ```231010_IMG_001.jpg```
- ```231001_IMG_002.jpg```
- ```231015_IMG_003.jpg```

Now, all photos are organized by their capture dates, making it easier to sort and manage them.

---

## Notes
1. **Backup Files**: Always test the script on sample files before applying it to critical data.
2. **Case Sensitivity**: The script processes all files in the specified folder, including those with uppercase extensions (e.g., ```.JPG```).
3. **Custom Folder Path**: Modify the ```folder_path``` variable in ```main.py``` to target a different directory.

---

**Disclaimer**: Use this script at your own risk. The authors are not responsible for data loss.
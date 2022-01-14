import datetime
import calendar
import shutil
import glob
import sys
import os

# Get input and output path passed arguments
try:
    input = sys.argv[1]
    output = sys.argv[2]

    # Verfy inputs
    if os.path.isfile(output):
        raise Exception("Output path is not a directory")
    if not os.path.isabs(output) or not os.path.isabs(input):
        raise Exception("Paths were not absolute")

except Exception as e:
    print(e)
    print("Usage: \"python BackupMinecraftServer DirectoryToArchive BackupFolder\"")

# Explain how to use file if help is called
if input.lower() == "help":
    print("Usage: \"python BackupMinecraftServer DirectoryToArchive BackupFolder\"")

# Zip input and store result in output-directory
try:
    # Generate name of output file
    input_folder_name = os.path.basename(input)
    timestamp = datetime.datetime.today().strftime("%Y.%m.%d")
    output_file_name = input_folder_name + "_Backup_" + timestamp
    output_path = output + "\\" + output_file_name

    print("Backup started...")
    shutil.make_archive(output_path, 'zip', input)
    print("Backup complete!")
    print("Backup can be found at: " + output_path)
    # (" + os.path.getsize(output_path)/1048576 + ")

    """
    # I'm too lazy to figure this stuff out
    today = datetime.date.today()
    weeklylist = []
    monthlylist = []
    # Check if file already exists
    for file in glob.glob(output + r"\*.zip"):
    
        if os.path.basename(file).startswith(os.path.basename(input)):
            print("Filedate: " + file[len(file) - 14: len(file) - 4])
            # Convert file-timestamps back to datetime
            filedate = datetime.datetime.strptime(file[len(file) - 14: len(file) - 4])
            
            # Check if time is in last 7 days
            # -> Backup daily (go to next file)
            margin = datetime.timedelta(days=7)
            if (today - margin) <= filedate <= today:
                continue

            # Check if time is in this or last calender month (excluding last 7 days)
            # -> Backup weekly (add to weeklylist)
            margin = datetime.timedelta(days=(
                calendar.monthrange(today.year, datetime)[1] + \
                today.day
            ))

            # Check if time time is older than these last two months
            # -> Backup monthly (all but newest get deleted) 
    """
except Exception as e:
    print(e)
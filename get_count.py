import glob
total_files = glob.glob('Kolkata/*')
total_folders = glob.glob('Kolkata/Kolkata*')
print(total_folders)
print(len(total_files))


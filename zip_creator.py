import pathlib
import zipfile

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir,"copressed.zip")
    with zipfile.ZipFile(dest_dir,'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)

if __name__ == "__main__":
    make_archive(filepaths=["random bounts.py"],dest_dir="dest")
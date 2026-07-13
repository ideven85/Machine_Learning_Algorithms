import tarfile
import os

import shutil


def compress_directory(dir_name, out_file="cifar-100-python.tar.gz"):
    with tarfile.open(out_file, "w:gz") as tar:
        # arcname prevents the entire absolute path from being encoded
        tar.add(dir_name, arcname=os.path.basename(dir_name))
    print(f"Successfully created: {out_file}")


#
#
#
# # Creates a file named 'backup.tar.gz' from the 'my_project_folder' directory
# shutil.make_archive(base_name="./data/cifar-100-python", format="gztar", root_dir="./data")

compress_directory("data/cifar-100-python")

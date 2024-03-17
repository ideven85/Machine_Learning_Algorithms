import zipfile

with zipfile.ZipFile('hazelcast-4.2.8.zip','r') as zip_ref:
    zip_ref.extractall('.')
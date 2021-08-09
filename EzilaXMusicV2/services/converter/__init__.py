from os import listdir, mkdir

if "raw_files" not in listdir():
    mkdir("raw_files")

from EzilaXMusicV2.services.converter.converter import convert

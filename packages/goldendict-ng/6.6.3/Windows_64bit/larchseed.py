NAME = "goldendict-ng"
VERSION = (6, 6, 3)
ARCH = ("Windows_64bit",)
DESCRIPTION = "The next generation GoldenDict (Supports Qt WebEngine & Qt6)"

AUTHOR = "@xiaoyifang (https://github.com/xiaoyifang)"
MAINTAINER = "Alexander Rusakevich (mr.alexander.rusakevich@gmail.com)"
URL = "https://github.com/xiaoyifang/goldendict-ng"
LICENSE = "GPL3"

DEPENDENCIES = ["vcredist140"]

SOURCE = {
    "goldendict.zip": "https://github.com/xiaoyifang/goldendict-ng/releases/download/v24.05.05-LiXia.ecd1138c/6.6.3-GoldenDict.exe_windows-2019_20240505.zip"
}

ENTRY_POINT = "GoldenDict.exe"


def install(temp_dir, dest_dir):
    unzip(temp_dir / "goldendict.zip", temp_dir)
    copytree(temp_dir / "GoldenDict-Windows.ecd1138c-142735", dest_dir)

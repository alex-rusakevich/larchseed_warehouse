NAME = "vcredist140"
VERSION = (14, 40, 33810)
ARCH = ("Windows_64bit", "Windows_32bit")
DESCRIPTION = """Microsoft Visual C++ Redistributable for Visual Studio
2015-2022, run-time components of Visual C++ libraries"""

AUTHOR = "Microsoft"
MAINTAINER = "Alexander Rusakevich (mr.alexander.rusakevich@gmail.com)"
URL = "https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170"
LICENSE = "https://visualstudio.microsoft.com/ru/license-terms/mlt031619/"

if CURRENT_ARCH == "Windows_64bit":
    SOURCE = {
        "vcredist140.exe": "https://download.visualstudio.microsoft.com/download/pr/1754ea58-11a6-44ab-a262-696e194ce543/3642E3F95D50CC193E4B5A0B0FFBF7FE2C08801517758B4C8AEB7105A091208A/VC_redist.x64.exe"
    }
elif CURRENT_ARCH == "Windows_32bit":
    SOURCE = {
        "vcredist140.exe": "https://download.visualstudio.microsoft.com/download/pr/9c69db26-cda4-472d-bdae-f2b87f4a0177/A32DD41EAAB0C5E1EAA78BE3C0BB73B48593DE8D97A7510B97DE3FD993538600/VC_redist.x86.exe"
    }

ENTRY_POINT = None


def install(temp_dir: str, dest_dir: str):
    run(join_path(temp_dir, "vcredist140.exe"), "/install", "/q")


def uninstall(temp_dir: str, dest_dir: str):
    run(join_path(temp_dir, "vcredist140.exe"), "/uninstall", "/q")

#!/usr/bin/env python
import json
import subprocess
import shutil
import os
import tempfile


def main():
    seed_sources = json.load(open("seed_sources.json", "r", encoding="utf8"))[
        "seed_sources"
    ]

    os.path.isdir("packages") and shutil.rmtree("packages")

    for seed_source in seed_sources:
        with tempfile.TemporaryDirectory() as tmpdirname:
            subprocess.run(["git", "clone", seed_source["git"], tmpdirname])

            for package in seed_source["packages"]:
                shutil.copytree(
                    os.path.join(tmpdirname, package),
                    os.path.join("packages", package),
                    dirs_exist_ok=True,
                    copy_function=shutil.copy2,
                )


if __name__ == "__main__":
    main()

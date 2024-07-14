#!/usr/bin/env python
import sqlite3
from glob import glob
import os
from datetime import datetime, timezone
from pathlib import Path


def main():
    if os.path.exists("remote.db"):
        os.remove("remote.db")

    connection = sqlite3.connect("remote.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS packages (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            ver TEXT NOT NULL,
            arch TEXT NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pkg_meta (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            desc TEXT NOT NULL
        )
    """
    )

    connection.commit()

    # region Generate package list and descriptions
    for filename in glob("packages/**/*", recursive=True):
        if len(filename.split(os.sep)) == 4:
            _, pkg_name, pkg_ver, pkg_arch = filename.split(os.sep)

            cursor.execute(
                "INSERT INTO packages (name, ver, arch) VALUES (?, ?, ?)",
                (pkg_name, pkg_ver, pkg_arch),
            )

            connection.commit()
        elif len(filename.split(os.sep)) == 2:
            _, pkg_name = filename.split(os.sep)

            pkg_desc = ""
            possible_desc_file = os.path.join(filename, "desc.md")

            if Path(possible_desc_file).is_file():
                pkg_desc = Path(possible_desc_file).read_text()

            cursor.execute(
                "INSERT INTO pkg_meta (name, desc) VALUES (?, ?)",
                (pkg_name, pkg_desc),
            )

            connection.commit()

    # endregion

    cursor.close()
    connection.close()

    with open(".remote-db-timestamp", "w", encoding="utf8") as f:
        f.write(str(datetime.now(timezone.utc)))
        f.write("\n")


if __name__ == "__main__":
    main()

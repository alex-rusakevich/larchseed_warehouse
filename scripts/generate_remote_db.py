#!/usr/bin/env python
import sqlite3
from glob import glob
import os
from datetime import datetime, timezone


def main():
    if os.path.exists("remote.db"):
        os.remove("remote.db")

    connection = sqlite3.connect("remote.db")
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
    connection.commit()

    for filename in glob("packages/**/*", recursive=True):
        if len(filename.split(os.sep)) == 4:
            _, pkg_name, pkg_ver, pkg_arch = filename.split(os.sep)
            cursor.execute(
                "INSERT INTO packages (name, ver, arch) VALUES (?, ?, ?)",
                (pkg_name, pkg_ver, pkg_arch),
            )
            connection.commit()

    cursor.close()
    connection.close()

    with open(".remote-db-timestamp", "w", encoding="utf8") as f:
        f.write(str(datetime.now(timezone.utc)))
        f.write("\n")


if __name__ == "__main__":
    main()

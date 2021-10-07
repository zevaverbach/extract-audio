#!/usr/bin/env python3

from pathlib import Path
from subprocess import check_output
from sys import argv as args, exit
import threading


def extract_audio(dir_, fp):
    return check_output(f'ffmpeg -y -i "{fp}" -vn -acodec copy "{dir_}{fp.stem}.m4a"', shell=True)


def main():
    dir_ = args[1]
    threads = []
    try:
        fps = list(Path(dir_).iterdir())
    except FileNotFoundError:
        print("that dir doesn't exist")
    if not fps:
        print("no files in that dir")
        exit()

    for fp in fps:
        a = threading.Thread(
            target=extract_audio,
            args=(
                dir_,
                fp,
            ),
        )
        threads.append(a)
        a.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()

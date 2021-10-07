#!/usr/bin/env python3

from pathlib import Path
from subprocess import check_output
from sys import argv as args
import threading


def extract_audio(dir_, fp):
    return check_output(f'ffmpeg -y -i "{fp}" -vn -acodec copy "{dir_}{fp.stem}.m4a"', shell=True)


def main():
    dir_ = args[1]
    threads = []
    for fp in Path(dir_).iterdir():
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

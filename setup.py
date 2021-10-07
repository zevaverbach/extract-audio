from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="extract-audio",
    version="0.31",
    packages=["app"],
    description="Extract audio from a directory of video files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Zev Averbach",
    author_email="zev@averba.ch",
    url="https://github.com/zevaverbach/extract-audio",
    entry_points={
        "console_scripts": [
            "extract=app.extract_audio:main",
        ]
    },
)

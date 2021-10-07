from setuptools import setup


setup(
    name="extract-audio",
    version="0.1",
    packages=["app"],
    description="Extract audio from a directory of video files.",
    author="Zev Averbach",
    author_email="zev@averba.ch",
    url="https://github.com/zevaverbach/extract_audio_from_video",
    entry_points={
        "console_scripts": [
            "extract=app.extract_audio:main",
        ]
    },
)

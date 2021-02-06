import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="audio_to_ankie",
    version="1.0.0",
    author="Magnus Goedde",
    description="A CLI to import audio files to Anki and speed them up.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/mgsgde/anki_audio_import",
    scripts=['./audio_to_anki'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'setuptools',
        'argparse',
        'ffmpeg-python',
        'anki'
    ],
    python_requires='>=3.6',
)
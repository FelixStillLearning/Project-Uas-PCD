"""
File setup untuk instalasi paket.

Untuk menginstal paket dalam mode pengembangan:
pip install -e .
"""

from setuptools import setup, find_packages

setup(
    name="project_name",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Daftar dependensi Anda di sini
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Deskripsi singkat tentang proyek",
    keywords="python, project",
    python_requires=">=3.6",
)

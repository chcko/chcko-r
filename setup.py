import os
import io
import setuptools
from pathlib import Path

def main():
    package_root = os.path.abspath(os.path.dirname(__file__))
    proot = Path(package_root)
    readme_filename = os.path.join(package_root, "README.rst")
    with io.open(readme_filename, encoding="utf-8") as readme_file:
        readme = readme_file.read()
    dependencies = ['chcko']
    packages=['chcko.r']
    setuptools.setup(
        name="chcko-r",
        version = "0.0.1",
        description="A random mix of exercises for chcko",
        long_description=readme,
        long_description_content_type="text/x-rst",
        author="Roland Puntaier",
        author_email="roland.puntaier@gmail.com",
        url="https://github.com/chcko/chcko-r",
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.8",
            "Operating System :: OS Independent",
            "Topic :: Internet",
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Topic :: Education',
            'Topic :: Education :: Computer Aided Instruction (CAI)'
        ],
        packages=packages,
        namespace_packages=["chcko"],
        install_requires=dependencies,
        extras_require={},
        include_package_data=True,
        zip_safe=False,
    )

if __name__ == "__main__":
    main()

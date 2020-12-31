import os
import io
import setuptools
from pathlib import Path

package_root = os.path.abspath(os.path.dirname(__file__))

# # maybe not all installed in system
# # done in Makefile
# from doit.cmd_base import DodoTaskLoader
# from doit.doit_cmd import DoitMain
# def doit_run():
#     loader = DodoTaskLoader()
#     loader.setup(
#             dict(
#             dodoFile=os.path.join(package_root,'dodo.py')
#             ,cwdPath=os.path.join(package_root,'chcko','r')
#             ,seek_file=True
#                  ))
#     DoitMain(loader).run(['-kd.', 'html'])
#     DoitMain(loader).run(['-kd.', 'initdb'])

def main():
    # doit_run()
    os.chdir(package_root)
    try:
        import shutil
        shutil.rmtree('build')
    except:
        pass
    proot = Path(package_root)
    readme_filename = os.path.join(package_root, "README.rst")
    with io.open(readme_filename, encoding="utf-8") as readme_file:
        readme = readme_file.read()
    setuptools.setup(
        name="chcko-r",
        version = "1.3.2", # keep same a chcko
        description="A random mix of exercises for chcko",
        long_description=readme,
        long_description_content_type="text/x-rst",
        author="Roland Puntaier",
        author_email="roland.puntaier@gmail.com",
        url="https://github.com/chcko/chcko-r",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Operating System :: OS Independent",
            "Topic :: Internet",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Topic :: Education",
            "Topic :: Education :: Computer Aided Instruction (CAI)"
        ],
        packages=setuptools.find_namespace_packages(),
        include_package_data=True,
        namespace_packages=["chcko"],
        install_requires=['schemdraw','pint'],#don't ["chcko"], because on gcloud chcko is uploaded and not installed
        extras_require={},
        zip_safe=False,
    )

if __name__ == "__main__":
    main()

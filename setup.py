import subprocess
import sys
from setuptools import Extension
import numpy
import skbuild
from Cython.Distutils import build_ext


def main():

    ext_modules = [
        Extension(
            "octomap",
            ["octomap/octomap.pyx"],
            include_dirs=[
                "src/octomap/octomap/include",
                "src/octomap/dynamicEDT3D/include",
                numpy.get_include(),
            ],
            library_dirs=[
                "src/octomap/lib",
            ],
            libraries=[
                "dynamicedt3d",
                "octomap",
                "octomath",
            ],
            language="c++",
        )
    ]

    with open("README.md") as f:
        long_description = f.read()

    skbuild.setup(
        name="octomap-python",
        version="2.0.0",
        install_requires=["numpy"],
        extras_require={
            "example": ["glooey", "imgviz>=1.2.0", "pyglet", "trimesh[easy]"],
        },
        license="BSD",
        maintainer="Kentaro Wada",
        maintainer_email="www.kentaro.wada@gmail.com",
        url="https://github.com/wkentaro/octomap-python",
        description="Python binding of the OctoMap library.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy",
        ],
        ext_modules=ext_modules,
        cmdclass={"build_ext": build_ext},
        cmake_source_dir="src/octomap",
    )


if __name__ == "__main__":
    main()

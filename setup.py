import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="BeautifulReport",
    version="0.0.8",
    author="mocobk",
    author_email="mocobk@163.com",
    description="unittest自动化测试的可视化报告模板",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mocobk/BeautifulReport",
    packages=['BeautifulReport'],
    package_data={'BeautifulReport': ['template/*.*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

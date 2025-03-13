from setuptools import setup, find_packages

setup(
    name="callai",
    version="0.1.0",
    description="一个简单的OpenAI API兼容封装库",
    author="您的名字",
    author_email="您的邮箱",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 
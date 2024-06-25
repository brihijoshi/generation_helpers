from setuptools import setup, find_packages, find_namespace_packages

setup(name='callgpt',
    version='0.6',
    description="Library for running few-shot inference on GPT models",
    packages=find_packages(),
    # packages=find_namespace_packages(include=["gptinference", "gptinference.wrappers", "gptinference.*"]),
    # package_dir={"": "gptinference"},
    # packages=find_namespace_packages(where='gptinference'),
    # include_package_data=True,
    # # packages=find_packages(include=["gptinference", "gptinference.wrappers", "gptinference.base"]),
    install_requires=[
        'openai==1.12.0',
        'llama-cpp-python'
    ],
    license='Apache License 2.0',
    long_description=open('README.md').read(),
)

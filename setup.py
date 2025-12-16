from setuptools import find_packages, setup

setup(
    name='vertex_ai_agent',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'google-cloud-aiplatform==1.12.0',
        'flask==2.2.0'
    ],
    description='Vertex AI Agent project starter setup.',
    author='Your Name',
    author_email='youremail@example.com'
)
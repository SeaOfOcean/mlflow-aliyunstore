from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='aliyunstoreplugin',
    version='1.0.0',
    description='Plugin that provides Aliyun oss Artifact Store functionality for MLflow',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Xianyan Jia',
    author_email='jiaxianyan@gmail.com',
    url="https://github.com/SeaOfOcean/mlflow-aliyunstore",
    packages=find_packages(),
    install_requires=[
        'mlflow',
        'oss2'
    ],
    entry_points={
        "mlflow.artifact_repository": [
            "oss=aliyunstoreplugin.store.artifact.aliyun_oss_artifact_repo:AliyunOssArtifactRepository"
        ]
    },
)

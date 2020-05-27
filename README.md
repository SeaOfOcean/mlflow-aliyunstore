# Aliyun OSS store plugin for MLflow
This repository provides a MLflow plugin that allows users to use a aliyun oss as the artifact store for MLflow.

## Implementation overview
* `aliyunstoreplugin`: this package includes the `AliyunOssArtifactRepository` class that is used to read and write artifacts from Aliyun OSS storage.
* `setup.py` file defines entrypoints that tell MLflow to automatically associate the `oss` URIs with the `AliyunOssArtifactRepository` implementation when the `aliyunstoreplugin` library is installed. The entrypoints are configured as follows:

```
entry_points={
        "mlflow.artifact_repository": [
            "oss=aliyunstoreplugin.store.artifact.aliyun_oss_artifact_repo:AliyunOssArtifactRepository"
        ]
    },
```


# Usage
To store artifacts in Aliyun OSS Storage, specify a URI of the form ``oss://<bucket>/<path>``.
This plugin expects Aliyun Storage access credentials in the
``MLFLOW_OSS_ENDPOINT_URL``, ``MLFLOW_OSS_KEY_ID`` and ``MLFLOW_OSS_KEY_SECRET`` environment variables,
so you must set these variables on both your client
application and your MLflow tracking server. Finally, you must run ``pip install oss2``
separately (on both your client and the server) to access Aliyun OSS Storage

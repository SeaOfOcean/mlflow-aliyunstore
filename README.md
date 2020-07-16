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

Install by pip on both your client and the server, and then use MLflow as normal. The Alibaba Cloud OSS artifact store support will be provided automatically.

```bash
pip install mlflow[aliyun-oss]
```


The plugin implements all of the MLflow artifact store APIs.
It expects Aliyun Storage access credentials in the ``MLFLOW_OSS_ENDPOINT_URL``, ``MLFLOW_OSS_KEY_ID`` and ``MLFLOW_OSS_KEY_SECRET`` environment variables,
so you must set these variables on both your client application and your MLflow tracking server.
To use Aliyun OSS as an artifact store, an OSS URI of the form ``oss://<bucket>/<path>`` must be provided, as shown in the example below:

```python
import mlflow
import mlflow.pyfunc

class Mod(mlflow.pyfunc.PythonModel):
    def predict(self, ctx, inp):
        return 7

exp_name = "myexp"
mlflow.create_experiment(exp_name, artifact_location="oss://mlflow-test/")
mlflow.set_experiment(exp_name)
mlflow.pyfunc.log_model('model_test', python_model=Mod())
```

In the example provided above, the ``log_model`` operation creates three entries in the OSS storage ``oss://mlflow-test/$RUN_ID/artifacts/model_test/``, the MLmodel file
and the conda.yaml file associated with the model.

from typing import List, Literal

from kumo.model.config.base import KumoBaseConfig


class KumoRegistryConfig(KumoBaseConfig):

    name: Literal["dockerhub", "gitlab", ""] = ""
    server: str
    username: List[str]
    password: List[str]

# pylint: disable=all
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

# pylint:disable=no-name-in-module
from pydantic import BaseModel, conint, validator


# pylint: disable=no-self-argument, no-self-use, too-few-public-methods
class Model(BaseModel):
    model_name: str
    pretrained: bool
    in_chans: conint(ge=1)  # in_channels must be greater than or equal to 1
    num_classes: conint(ge=1)
    global_pool: str

    @validator("global_pool")
    def validate_global_pool(cls, global_pool: str) -> str:
        """Validates global_pool is in ["avg", "max"]."""
        if global_pool not in ["avg", "max"]:
            raise ValueError("global_pool must be avg or max")
        return global_pool


class Stores(BaseModel):
    project_name: str
    unique_id: str
    logs_dir: Path
    model_artifacts_dir: Path


class General(BaseModel):
    num_classes: int
    device: str
    project_name: str
    debug: bool


class Optimizer(BaseModel):
    optimizer: str
    optimizer_params: Dict[str, Any]


class Config(BaseModel):

    model: Model
    stores: Stores
    general: General

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> Config:
        """Creates Config object from a dictionary."""
        return cls(**config_dict)

from dataclasses import dataclass
from typing import Dict, Any
from pathlib import Path

@dataclass
class Model:
    model_name: str
    pretrained: bool
    in_chans: int
    num_classes: int
    global_pool: str


@dataclass
class Optimizer:
    optimizer: str
    optimizer_params: Dict[str, Any]


@dataclass
class Stores:
    project_name: str
    unique_id: int
    logs_dir: Path
    model_artifacts_dir: Path


@dataclass
class General:
    num_classes: int
    device: str
    project_name: str
    debug: bool
    seed: int


@dataclass
class Config:
    model: Model
    optimizer: Optimizer
    stores: Stores
    general: General

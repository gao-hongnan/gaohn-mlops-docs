import logging

import hydra
from hydra.core.hydra_config import HydraConfig
from omegaconf import  DictConfig, OmegaConf

LOG = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="configs", config_name="config")
def run(config: DictConfig) -> None:
    """Run the main function."""
    LOG.info("Type of config is: %s", type(config))
    LOG.info("Merged Yaml:\n%s", OmegaConf.to_yaml(config))
    LOG.info(HydraConfig.get().job.name)


if __name__ == "__main__":
    run()

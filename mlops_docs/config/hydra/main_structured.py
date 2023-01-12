import logging
import hydra
from configs.base import Config, Model, Optimizer, Stores
from hydra.core.config_store import ConfigStore
from hydra.core.hydra_config import HydraConfig
from omegaconf import OmegaConf

LOG = logging.getLogger(__name__)
cs = ConfigStore.instance()
cs.store(name="base_config", node=Config)
cs.store(name="model", node=Model)
cs.store(name="optimizer", node=Optimizer)
cs.store(name="stores", node=Stores)


@hydra.main(version_base=None, config_path="configs", config_name="config")
def run(config: Config) -> None:
    """Run the main function."""
    LOG.info("Type of config is: %s", type(config))
    LOG.info("Merged Yaml:\n%s", OmegaConf.to_yaml(config))
    LOG.info(HydraConfig.get().job.name)

    config_obj = OmegaConf.to_object(config)
    LOG.info("Type of config is: %s", type(config_obj))
  


if __name__ == "__main__":
    run()

## Config Management

This post is heavily inspired by [Pydra - Pydantic and Hydra for configuration management of model training experiments](https://suneeta-mall.github.io/2022/03/15/hydra-pydantic-config-management-for-training-application.html).

### Hydra

#### Pros

- Let's look at an example of a Yaml based configuration with no involvement of python object

    ```yaml title="configs/config.yaml"
    defaults:
    - _self_
    - model: base
    - stores: base
    - optimizer: base

    general:
    num_classes: 10
    device: "cpu"
    project_name: "peekingduck"
    debug: true
    seed: 1992

    hydra:
    run:
        dir: "outputs/${general.project_name}/${stores.unique_id}" # in sync with stores
    ```

    ```yaml title="configs/model/base.yaml" linenums="1"
    model_name: "resnet18"
    pretrained: True
    in_chans: 3
    num_classes: ${general.num_classes}
    global_pool: "avg"
    ```

    ```yaml title="configs/stores/base.yaml" linenums="1"
    project_name: ${general.project_name}
    unique_id: ${now:%Y%m%d_%H%M%S} # in sync with hydra output dir
    logs_dir: !!python/object/apply:pathlib.PosixPath [""]
    model_artifacts_dir: !!python/object/apply:pathlib.PosixPath [""]
    ```

    ```yaml title="configs/optimizer/base.yaml" linenums="1"
    optimizer_params:
    optimizer: "AdamW"
    optimizer_params:
        lr: 0.0003  # bs: 32 -> lr = 3e-4
        betas: [0.9, 0.999]
        amsgrad: False
        weight_decay: 0.000001
        eps: 0.00000001
    ```

    ```python title="main.py" linenums="1"
    import logging
    from dataclasses import dataclass
    from typing import List, Optional

    import hydra
    from hydra.core.config_store import ConfigStore
    from hydra.core.hydra_config import HydraConfig
    from omegaconf import MISSING, DictConfig, OmegaConf

    LOG = logging.getLogger(__name__)


    @hydra.main(version_base=None, config_path="configs", config_name="config")
    def run(config: DictConfig) -> None:
        """Run the main function."""
        LOG.info("Type of config is: %s", type(config))
        LOG.info("Merged Yaml:\n%s", OmegaConf.to_yaml(config))
        LOG.info(HydraConfig.get().job.name)


    if __name__ == "__main__":
        run()
    ```

    1. The `@hydra.main` decorator is used to initialize the hydra application. We specify `config_path` to 
    tell hydra where to look for the base configuration files. We also specify `config_name` to tell hydra which
    file is the main controller of the hierarchy. In this case, it is `config.yaml`.

        One highlight is we can override this configuration file with command line arguments. So if you tend to have
        many config folders, then this can come in handy. But one major benefit I see is you can change `config_name`
        easily, that is because you may have multiple main config files for various experiments.

        ```bash
        $ python main.py --config_name config_mnist.yaml
        $ python main.py --config_name config_cifar10.yaml
        ```

    2. Once you load the configuration, you can access the configuration values using the dot notation.
        This is because `config` is loaded as [OmegaConf](https://github.com/omry/omegaconf)'s `DictConfig` object.
        They inherit from `dict` and `MutableMapping` so you can access the values using the dot notation access pattern.
        This is better than using `config["general"]["num_classes"]` because it is more readable and less error prone,
        and also allow you to manipulate the object.

    3. Allow command line overrides. For example, you can override the `model_name` from `model` by

        ```bash
        $ python main.py model.model_name=resnet50
        ```

        and the `model_name` will change during runtime. This is very useful when you want to run multiple experiments
        with different configurations. You won't need to create multiple config files for each experiment just to change
        a single/few value(s). 

    4. A natural follow-up question is about persistence. If I can easily override the configuration, then how do I
    make sure the configuration is saved somewhere? Versioning the configs is just as important as versioning your
    code in Machine Learning. The highlight here is Hydra also saves the final configuration to an output folder. By default, 
    it is stored in `outputs/YYYY-MM-DD/HH-MM-SS/.hydra/config.yaml`. Now you can revert back to this exact run by specifying
    the directory.

        ```bash
        $ python main.py --config_path outputs/2022-01-12/12-00-00/.hydra/config.yaml
        ```

        to recover your run. Here `YYYY-MM-DD/HH-MM-SS` is like your unique `run_id` for each run. You can also 
        change it as follows in `config.yaml`:

        ```yaml title="configs/config.yaml" linenums="1"
        hydra:
        run:
            dir: "outputs/${general.project_name}/${stores.unique_id}" # in sync with stores
        ```

    5. One more good to have feature is overriding hydra's own default settings, such as the `job` and `run`
        settings. You can either do it via `config.yaml` or manually create a folder called `hydra` and put 
        the specifics inside. See [here](https://github.com/suneeta-mall/hydra_pydantic_config_management/tree/master/hydra/conf_custom_hydra/hydra)
        for an example.

    6. Multi-run. Hydra allows you to run multiple experiments in parallel. This is very useful when you want to
        run multiple experiments with different configurations. You can specify the number of runs and the 
        configuration to use. See [here](https://hydra.cc/docs/tutorials/basic/running_your_app/multi-run/)
        for more examples.

        ```bash
        $ python main.py model.model_name=resnet18,resnet50 --multirun
        ```

        This will run two experiments in parallel, one with `resnet18` and the other with `resnet50`. 
        We see the true power of it if you want to do hyperparameter search, where you want to
        sweep over multiple values for a single parameter. 

        Now in the same directory, an `multirun` folder will be created and inside it, you will see
        two runs, one with `resnet18` and the other with `resnet50`. Each process is indexed by an integer.
        For example, `resnet18` is indexed by `0` and `resnet50` is indexed by `1`. 

        It is also worth noting that since the hydra's creator is from facebook, it is very easy to integrate
        with PyTorch's [distributed trainings](https://pytorch.org/tutorials/intermediate/dist_tuto.html).

    
- [Structured Config](https://hydra.cc/docs/tutorials/structured_config/schema/), this is what Hydra call when
  your config is complex enough to warrant object representations. For example, our `config.yaml`
  is currently just a Yaml representation. But under the hood, you can think of it as **composed** of
  `model`, `optimizer`, `store` and `general` objects. For each of these objects, you can define
  its own schema. This is very useful when you want to validate the configuration. 

    In hydra, you can define the schema using [dataclasses](https://docs.python.org/3/library/dataclasses.html).

    ```python title="configs/base.py" linenums="1"
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
    class Config:
        model: Model
        optimizer: Optimizer
        stores:  Stores
    ```

    ```python title="main_structured.py" linenums="1"
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
    ```

    More details [here](https://hydra.cc/docs/tutorials/structured_config/schema/). You can find
    how groups can be used to indicate inheritance.

    The dependency injection here is merely a change of the type of the `config` argument, from `DictConfig`
    to `Config`. The rest of the code remains the same. The command line arguments are still the same.

    
- Having dataclass representation also offers more flexibility from manipulating the object to type hint. But validation
  still remains a problem as using `__post_init__` method is [not well supported](https://github.com/facebookresearch/hydra/issues/981) when working with hydra. 
  However, you can decouple the usage of dataclass from hydras' dependency injection. For example, you can load the config from
  hydra and instantiate through the dataclass without the use of `ConfigStore`. This idea is made better when used together 
  with Pydantic since it offers validation and serialization.


- Interpolation: This is an extremely highlighted feature of hydra. For example, we have `num_classes` defined under the `general` schema.
  However, this parameter is also used in the `model` schema, defining the number of output neurons. It can also be used in the `dataset`
  schema (not shown here), where we need to know the number of classes to create certain `class` mapping. Repeatedly defining the same
  parameter over different config schema is prone to mistake. This is like hardcoding the same value `NUM_CLASSES` in different python 
  scripts. Here we use the idea of **polymorphism** to define the `num_classes` in the `general` schema and use interpolation to **inject**
  this all around with `${general.num_classes}`.

#### Cons

- Serializing/Deserializing canonical or complex python objects are not well supported. In earlier versions,
  objects like `pathlib.Path` are not supported.

- Structured config is only limited to `dataclass`. This means that you cannot create your own custom
  abstraction. For example, you cannot create a `Model` class without invoking `dataclass` decorator,
  and still be able to interact with hydra.

- No validation support. This is a problem since what you define in the schema is not validated. For example,
  you can define `num_classes` as a `int` but user passes in a `str` of `"10"` instead of `10`, but
    hydra will not complain. This means that you have to do validation yourself (i.e. do checks all over
    the application/business logic code). 

- Interpolation is really good, but the inability to simple manipulation over it caused a lot of [complaints](https://github.com/omry/omegaconf/issues/91).
  Like if you defined a learning rate as `lr: 0.001` and you want to multiply it by 10 in another config file, you cannot do `10 * ${lr}`.

#### Instantiating

You can also [instantiate](https://hydra.cc/docs/advanced/instantiate_objects/overview/) objects with hydra.

#### Composition Order

By default, Hydra 1.1 appends `_self_` to the end of the Defaults List. This behavior is new in Hydra 1.1 and different from previous Hydra versions. As such Hydra 1.1 issues a warning if `_self_` is not specified in the primary config, asking you to add `_self_` and thus indicate the desired composition order. To address the warning while maintaining the new behavior, append `_self_` to the end of the Defaults List. Note that in some cases it may instead be desirable to add `_self_` directly after the schema and before other Defaults List elements.

See [Composition Order](https://hydra.cc/docs/advanced/defaults_list/#composition-order) for more information.

### Pydantic

#### Pros

- Able to serialize and deserialize objects to and from DICT, JSON, YAML, and other formats.
For example, the following code will serialize a `Dict` object to Pydantics' `Model` object.
It can also convert back to `Dict` object.

    ```python
    class Model(BaseModel):
        model_name: str = "resnet18"
        pretrained: bool = True
        in_chans: conint(ge=1) = 3  # in_channels must be greater than or equal to 1
        num_classes: conint(ge=1) = 2
        global_pool: str = "avg"

        @validator("global_pool")
        def validate_global_pool(cls, global_pool: str) -> str:
            if global_pool not in ["avg", "max"]:
                raise ValueError("global_pool must be avg or max")
            return global_pool

    model_config_dict = {
        "model_name": "resnet18",
        "pretrained": True,
        "in_chans": 3,
        "num_classes": 1000,
        "global_pool": "avg",
    }
    model = Model(**model_config_dict)
    print(model)
    assert model.dict() == model_config_dict
    ```

- Validation of data types and values. For a large and complex configuration, you either validate
the sanity of config at the config level, or check at the code level (i.e. sprinkled throughout your codebase).
    - [Constrained types](https://pydantic-docs.helpmanual.io/usage/types/#constrained-types)
    
        ```python
        model = Model(
            model_name="resnet18",
            pretrained=True,
            in_chans=0,
            num_classes=2,
            global_pool="avg",
        )
        ```

        This will raise an error because `in_chans` is less than 1. Pydantic offers a wide range of
        constrained types out of the box for you to use. If that is not enough, then the custom validators
        can be used to validate the data with custom needs.

    - [Custom Validators](https://pydantic-docs.helpmanual.io/usage/validators/#custom-validators)
    
        ```python
        model = Model(
            model_name="resnet18",
            pretrained=True,
            in_chans=3,
            num_classes=2,
            global_pool="average",
        )
        ```

        This will raise an error because `global_pool` is not `avg` or `max`. We implemented
        this custom checks in the `validate_global_pool` method where we decorated it with `@validator`.


### References

- [Hydra](https://hydra.cc/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Pydra - Pydantic and Hydra for configuration management of model training experiments](https://suneeta-mall.github.io/2022/03/15/hydra-pydantic-config-management-for-training-application.html)
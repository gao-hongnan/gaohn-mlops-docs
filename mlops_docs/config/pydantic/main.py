from base import Config, Model, Optimizer, General, Stores

if __name__ == "__main__":
    model = Model(
        model_name="resnet18",
        pretrained=True,
        in_chans=3,
        num_classes=2,
        global_pool="avg",
    )
    optimizer = Optimizer(
        optimizer="AdamW",
        optimizer_params={
            "lr": 0.0003,
            "betas": [0.9, 0.999],
            "amsgrad": False,
            "weight_decay": 1e-06,
            "eps": 1e-08,
        },
    )
    stores = Stores(
        project_name="peekingduck",
        unique_id="12345",
        logs_dir="./logs",
        model_artifacts_dir="./artifacts",
    )

    general = General(
        num_classes=10, device="cpu", project_name="peekingduck", debug=True, seed=1992
    )

    config = Config(model=model, optimizer=optimizer, stores=stores, general=general)
    print(config)

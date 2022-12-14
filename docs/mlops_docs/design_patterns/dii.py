from abc import ABC, abstractmethod
from typing import Any, Callable

# class TensorFlowEvaluator:
#     def evaluate(self):
#         print("Evaluating with TensorFlow.")


# class MLPipeline:
#     def __init__(self):
#         self.evaluator = TensorFlowEvaluator()

#     def evaluate(self):
#         self.evaluator.evaluate()


class ImageClassificationTransforms:
    """Dummy class for image classification transforms."""

    def get_train_transforms(self) -> Callable:
        """Get train transforms."""
        print("Getting image classification train transforms.")
        return lambda x: None

    def get_test_transforms(self) -> Callable:
        """Get test transforms."""
        print("Getting image classification test transforms.")
        return lambda x: None


class ImageSegmentationTransforms:
    """Dummy class for image segmentation transforms."""

    def get_train_transforms(self) -> Callable:
        """Get train transforms."""
        print("Getting image segmentation train transforms.")
        return lambda x: None

    def get_test_transforms(self) -> Callable:
        """Get test transforms."""
        print("Getting image segmentation test transforms.")
        return lambda x: None


# violates DIP
class CustomDataset:
    def __init__(self, stage: str = "train") -> None:
        self.stage = stage
        self.transforms: ImageClassificationTransforms = ImageClassificationTransforms()

    def apply_transforms(
        self,
        dummy_data: Any = None,
    ) -> Any:
        """Apply transforms to dataset based on stage."""
        if self.stage == "train":
            transformed = self.transforms.get_train_transforms()(dummy_data)
        else:
            transformed = self.transforms.get_test_transforms()(dummy_data)
        return transformed

    def getitem(self) -> Any:
        """Replace __getitem__ method as normal method for simplicity."""
        return self.apply_transforms(dummy_data=None)


if __name__ == "__main__":
    # ml_pipeline = MLPipeline()
    # ml_pipeline.evaluate()

    dataset = CustomDataset()
    dataset.apply_transforms()
    dataset.getitem()

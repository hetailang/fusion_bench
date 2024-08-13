"""
This is the dummy task pool that is used for debugging purposes.
"""

import os

import torch
from omegaconf import DictConfig

from fusion_bench.taskpool.base_pool import TaskPool
from fusion_bench.utils import timeit_context
from fusion_bench.utils.parameters import count_parameters, print_parameters
from fusion_bench.models.separate_io import separate_save


class DummyTaskPool(TaskPool):
    """
    This is a dummy task pool used for debugging purposes. It inherits from the base TaskPool class.
    """

    def evaluate(self, model):
        """
        Evaluate the given model.
        This method does nothing but print the parameters of the model in a human-readable format.

        Args:
            model: The model to evaluate.
        """
        print_parameters(model, is_human_readable=True)

        if self.config.get("model_save_path", None) is not None:
            model_save_path = self.config.model_save_path
            with timeit_context(f"Saving the model to {model_save_path}"):
                separate_save(model, model_save_path)

        report = {}
        training_params, all_params = count_parameters(model)
        report["model_info"] = {
            "trainable_params": training_params,
            "all_params": all_params,
            "trainable_percentage": training_params / all_params,
        }
        return report

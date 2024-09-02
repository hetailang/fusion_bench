from pathlib import Path
from typing import Dict, Union

from hydra.utils import instantiate
from omegaconf import OmegaConf


class YAMLSerializationMixin:
    _recursive_: bool = False
    _config_mapping: Dict[str, str] = {
        "_recursive_": "_recursive_",
    }

    def to_yaml(self, path: Union[str, Path]):
        """
        Save the model pool to a YAML file.

        Args:
            path (Union[str, Path]): The path to save the model pool to.
        """
        config = {"_target_": type(self).__name__}
        for attr, key in self._config_mapping.items():
            if hasattr(self, attr):
                config[key] = getattr(self, attr)
        config = OmegaConf.create(config)
        OmegaConf.save(config, path, resolve=True)

    @classmethod
    def from_yaml(cls, path: Union[str, Path]):
        """
        Load a model pool from a YAML file.

        Args:
            path (Union[str, Path]): The path to load the model pool from.

        Returns:
            BaseModelPool: The loaded model pool.
        """
        config = OmegaConf.load(path)
        return instantiate(config, _recursive_=cls._recursive_)

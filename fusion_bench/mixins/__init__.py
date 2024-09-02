import sys

from typing_extensions import TYPE_CHECKING

from fusion_bench.utils.lazy_imports import LazyImporter

_import_structure = {
    "lightning_fabric": ["LightningFabricMixin"],
    "serialization": ["YAMLSerializationMixin"],
    "simple_profiler": ["SimpleProfilerMixin"],
}

if TYPE_CHECKING:
    from .lightning_fabric import LightningFabricMixin
    from .serialization import YAMLSerializationMixin
    from .simple_profiler import SimpleProfilerMixin

else:
    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        _import_structure,
    )

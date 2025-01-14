# flake8: noqa F401
import sys
from typing import TYPE_CHECKING

from fusion_bench.utils.lazy_imports import LazyImporter

_import_structure = {
    "base_algorithm": ["BaseModelFusionAlgorithm"],
    "dummy": ["DummyAlgorithm"],
    # single task learning (fine-tuning)
    "classification": ["ImageClassificationFineTuningForCLIP"],
    # analysis
    "analysis": ["TaskVectorCosSimilarity"],
    # model ensemble methods
    "ensemble": [
        "SimpleEnsembleAlgorithm",
        "WeightedEnsembleAlgorithm",
        "MaxModelPredictorAlgorithm",
    ],
    # model merging methods
    "linear": [
        "ExPOAlgorithm",
        "SimpleAverageForLlama",
        "TaskArithmeticForLlama",
        "LinearInterpolationAlgorithm",
    ],
    "simple_average": ["SimpleAverageAlgorithm"],
    "weighted_average": ["WeightedAverageAlgorithm", "WeightedAverageForLLama"],
    "task_arithmetic": ["TaskArithmeticAlgorithm"],
    "ties_merging": ["TiesMergingAlgorithm"],
    "dare": ["DareSimpleAverage", "DareTaskArithmetic"],
    "fisher_merging": [
        "FisherMergingForCLIPVisionModel",
        "FisherMergingAlgorithmForGPT2",
    ],
    "regmean": ["RegMeanAlgorithmForCLIP", "RegMeanAlgorithmForGPT2"],
    "adamerging": [
        "CLIPTaskWiseAdaMergingAlgorithm",
        "CLIPLayerWiseAdaMergingAlgorithm",
    ],
    "pwe_moe": [
        "PWEMoELinearScalarizationForCLIP",
        "PWEMoExactParetoOptimalForCLIP",
    ],
    "ada_svd": ["AdaSVDMergingForCLIPVisionModel"],
    # plug-and-play model merging methods
    "concrete_subspace": [
        "ConcreteTaskArithmeticAlgorithmForCLIP",
        "ConcreteTaskWiseAdaMergingForCLIP",
        "ConcreteLayerWiseAdaMergingForCLIP",
    ],
    # model mixing methods
    "depth_upscaling": ["DepthUpscalingAlgorithm", "DepthUpscalingForLlama"],
    "mixture_of_experts": [
        "MixtralUpscalingAlgorithm",
        "MixtralForCausalLMUpscalingAlgorithm",
        "MixtralMoEMergingAlgorithm",
        "MixtralForCausalLMMergingAlgorithm",
    ],
    "dawe": ["DataAdaptiveWeightEnsemblingForCLIP"],
    "we_moe": ["CLIPWeightEnsemblingMoEAlgorithm"],
    "sparse_we_moe": [
        "SparseWeightEnsemblingMoEAlgorithm",
        "SparseCLIPWeightEnsemblingMoEAlgorithm",
    ],
    "model_recombination": ["ModelRecombinationAlgorithm"],
    "smile_upscaling": [
        "SmileUpscalingAlgorithm",
        "SingularProjectionMergingAlgorithm",
    ],
    # pruning methods
    "pruning": [
        "MagnitudeDiffPruningAlgorithm",
        "RandomPruningForLlama",
        "MagnitudePruningForLlama",
        "WandaPruningForLlama",
    ],
    "sparselo": [
        "IterativeSparseLoForLlama",
        "SparseLoForLlama",
        "PCPSparseLoForLlama",
    ],
}


if TYPE_CHECKING:
    from .ada_svd import AdaSVDMergingForCLIPVisionModel
    from .analysis import TaskVectorCosSimilarity
    from .base_algorithm import BaseModelFusionAlgorithm
    from .classification import ImageClassificationFineTuningForCLIP
    from .concrete_subspace import (
        ConcreteLayerWiseAdaMergingForCLIP,
        ConcreteTaskArithmeticAlgorithmForCLIP,
        ConcreteTaskWiseAdaMergingForCLIP,
    )
    from .dare import DareSimpleAverage, DareTaskArithmetic
    from .dawe import DataAdaptiveWeightEnsemblingForCLIP
    from .depth_upscaling import DepthUpscalingAlgorithm, DepthUpscalingForLlama
    from .dummy import DummyAlgorithm
    from .ensemble import (
        MaxModelPredictorAlgorithm,
        SimpleEnsembleAlgorithm,
        WeightedEnsembleAlgorithm,
    )
    from .fisher_merging import FisherMergingForCLIPVisionModel
    from .linear import (
        ExPOAlgorithm,
        LinearInterpolationAlgorithm,
        SimpleAverageForLlama,
        TaskArithmeticForLlama,
    )
    from .mixture_of_experts import (
        MixtralForCausalLMMergingAlgorithm,
        MixtralForCausalLMUpscalingAlgorithm,
        MixtralMoEMergingAlgorithm,
        MixtralUpscalingAlgorithm,
    )
    from .model_recombination import ModelRecombinationAlgorithm
    from .pruning import (
        MagnitudeDiffPruningAlgorithm,
        MagnitudePruningForLlama,
        RandomPruningForLlama,
        WandaPruningForLlama,
    )
    from .pwe_moe import (
        PWEMoELinearScalarizationForCLIP,
        PWEMoExactParetoOptimalForCLIP,
    )
    from .regmean import RegMeanAlgorithmForCLIP, RegMeanAlgorithmForGPT2
    from .simple_average import SimpleAverageAlgorithm
    from .smile_upscaling import (
        SingularProjectionMergingAlgorithm,
        SmileUpscalingAlgorithm,
    )
    from .sparse_we_moe import (
        SparseCLIPWeightEnsemblingMoEAlgorithm,
        SparseWeightEnsemblingMoEAlgorithm,
    )
    from .sparselo import (
        IterativeSparseLoForLlama,
        PCPSparseLoForLlama,
        SparseLoForLlama,
    )
    from .task_arithmetic import TaskArithmeticAlgorithm
    from .ties_merging import TiesMergingAlgorithm
    from .we_moe import CLIPWeightEnsemblingMoEAlgorithm
    from .weighted_average import WeightedAverageAlgorithm, WeightedAverageForLLama

else:
    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        _import_structure,
    )

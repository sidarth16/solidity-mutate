from .as_flip import mutate_as_flip
from .as_rem import mutate_as_rem
from .op_ari import mutate_op_ari
from .op_asg import mutate_op_asg
from .op_eq import mutate_op_eq

MUTATOR_REGISTRY = {
    "as_rem": {
        "name": "as_rem",
        "label": "AS-REM",
        "description": "Assert Removal",
        "fn": mutate_as_rem,
    },
    "as_flip": {
        "name": "as_flip",
        "label": "AS-FLIP",
        "description": "Assert Condition Flip",
        "fn": mutate_as_flip,
    }
}

DEFAULT_MUTATORS = list(MUTATOR_REGISTRY.keys())

from .req_flip import mutate_req_flip
from .req_rem import mutate_req_rem


MUTATOR_REGISTRY = {
    "req_rem": {
        "name": "req_rem",
        "label": "REQ-REM",
        "description": "Require/Assert Removal",
        "fn": mutate_req_rem,
    },
    "req_flip": {
        "name": "req_flip",
        "label": "REQ-FLIP",
        "description": "Require/Assert Condition Flip",
        "fn": mutate_req_flip,
    },

}

DEFAULT_MUTATORS = list(MUTATOR_REGISTRY.keys())

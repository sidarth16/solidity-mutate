from .req_flip import mutate_req_flip
from .req_rem import mutate_req_rem
from .op_eq import mutate_op_eq
from .op_ari import mutate_op_ari
from .op_asg import mutate_op_asg


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
    "op_eq": {
        "name": "op_eq",
        "label": "OP-EQ",
        "description": "Equality Operator Mutation",
        "fn": mutate_op_eq,
    },
    "op_ari": {
        "name": "op_ari",
        "label": "OP-ARI",
        "description": "Arithmetic Operator Mutation",
        "fn": mutate_op_ari,
    },
    "op_asg": {
        "name": "op_asg",
        "label": "OP-ASG",
        "description": "Assignment Operator Mutation",
        "fn": mutate_op_asg,
    },

}

DEFAULT_MUTATORS = list(MUTATOR_REGISTRY.keys())

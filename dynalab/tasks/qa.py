# Copyright (c) Facebook, Inc. and its affiliates.

from ts.torch_handler.base_handler import BaseHandler

from dynalab.tasks.common import get_mock_context


data = [
    {
        "body": {
            "answer": "pretend you are reviewing a place",
            "context": "Please pretend you are reviewing a place, "
            + "product, book or movie",
            "hypothesis": "What should i pretend?",
        }
    }
]


def get_mock_input(name):
    context = get_mock_context(name)
    return data, context


# To be filled
class DynaHandler(BaseHandler):
    pass
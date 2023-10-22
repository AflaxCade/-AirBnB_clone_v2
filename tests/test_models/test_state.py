#!/usr/bin/python3
""" tests for class State """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ tests for class State """

    def __init__(self, *args, **kwargs):
        """ tests for class State """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ tests for class State """
        new = self.value()
        self.assertEqual(type(new.name), str)

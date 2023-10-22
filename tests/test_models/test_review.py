#!/usr/bin/python3
""" tests for class Review """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ tests for class Review """

    def __init__(self, *args, **kwargs):
        """ tests for class Review """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ tests for class Review """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ tests for class Review """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ tests for class Review """
        new = self.value()
        self.assertEqual(type(new.text), str)

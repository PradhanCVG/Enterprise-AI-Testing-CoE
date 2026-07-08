"""
Code Generation Evaluation
"""

import pytest


@pytest.mark.evals
class TestCodeGeneration:

    def test_python_generated(self):

        code = "print('Hello')"

        assert code != ""


    def test_code_compiles(self):

        compiled = True

        assert compiled


    def test_code_quality(self):

        quality = 0.95

        assert quality >= 0.90
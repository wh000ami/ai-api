import pytest

from app.service import get_text_generation


def test_get_generated_text():
    text = get_text_generation(model="gpt2", message="hello friend")
    assert text

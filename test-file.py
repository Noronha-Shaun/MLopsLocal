import pytest
from speech_translation_app import translate

def test_translation_to_french():
    result = translate("Hello", "French")
    assert result.lower() in ["bonjour", "salut"], f"Expected 'Bonjour' or 'Salut', but got {result}"

def test_translation_to_german():
    result = translate("Hello", "German")
    assert result.lower() == "hallo", f"Expected 'Hallo', but got {result}"

def test_translation_to_romanian():
    result = translate("Hello", "Romanian")
    assert result.lower() == "salut", f"Expected 'Salut', but got {result}"

def test_unsupported_language():
    result = translate("Hello", "Spanish")
    assert result == "Sorry, this language is not supported."

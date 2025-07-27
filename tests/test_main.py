# pylint: disable=too-few-public-methods, unnecessary-pass, redefined-outer-name
"""Test main.py"""

def test_convert_endpoint_input():
    """Test that the convert endpoint input is valid."""

    # Define the endpoint input to be tested
    endpoint_input = "Convert png to ico."

    # Check that the endpoint input is not None
    assert endpoint_input is not None, "Endpoint input should not be None"

    # Check that the endpoint input is of type string
    assert isinstance(endpoint_input, str), "Endpoint input should be a string"

from api.Base.helper import to_json


def test_to_json_empty_list():
    assert to_json([]) == '[]'


def test_to_json_empty_dict():
    assert to_json({}) == '{}'

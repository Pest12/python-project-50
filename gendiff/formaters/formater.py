from gendiff.formaters.stylish import make_stylish
from gendiff.formaters.plain import make_plain
from gendiff.formaters.json import make_json


def get_formater(diff, formater):
    if formater == 'stylish' or formater is None:
        return make_stylish(diff)
    if formater == 'plain':
        return make_plain(diff)
    if formater == 'json':
        return make_json(diff)
    raise ValueError(f"Unrecognized formater: {formater}")

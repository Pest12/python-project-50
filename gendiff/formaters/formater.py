from gendiff.formaters.stylish import to_stylish
from gendiff.formaters.plain import to_plain
from gendiff.formaters.json import to_json


def get_formater(diff, formater):
    if formater == 'stylish' or formater is None:
        return to_stylish(diff)
    if formater == 'plain':
        return to_plain(diff)
    if formater == 'json':
        return to_json(diff)
    raise ValueError('Unrecognized formater: ' + formater)

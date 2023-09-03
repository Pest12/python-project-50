from gendiff.formaters.stylish import make_stylish
from gendiff.formaters.plain import make_plain


def get_formater(diff, formater):
    if formater == 'stylish':
        return make_stylish(diff)
    if formater == 'plain':
        return make_plain(diff)

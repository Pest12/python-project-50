from gendiff.stylish import make_stylish


def get_formater(diff, formater):
    if formater == 'stylish':
        return make_stylish(diff)

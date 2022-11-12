from .models import Tag


def get_father(tag):
    fathers = tag.fathers.all()
    ret = fathers.all()
    for t in fathers:
        ret = ret | get_father(t)
    return ret

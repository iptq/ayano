import shlex


def parse_args(message):
    return shlex.split(message)

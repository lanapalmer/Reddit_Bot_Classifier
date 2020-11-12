import emoji

def split_count(info):
    return len([c for c in info if c in emoji.UNICODE_EMOJI])
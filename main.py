#!/usr/bin/python3
'''Grandma, on AI, in a single word.

The program drops one word into /output/entry.txt and nothing else.
Grandmothers do not explain gadgets; they name them. The word below is
the one she reaches for when the thing on the screen does something
clever she cannot quite account for: warm, baffled, and unmistakably
about a machine.
'''

from pathlib import Path

DEST = Path('/output') / 'entry.txt'
LIMIT = 30


def _word():
    head, tail = 'dooh', 'ickey'
    return head + tail


def _check(text):
    single = isinstance(text, str) and text.strip() == text and ' ' not in text
    sized = 1 <= len(text) <= LIMIT if isinstance(text, str) else False
    if not (single and sized):
        raise ValueError('need exactly one word, 1 to 30 characters')
    return text


def run():
    word = _check(_word())
    DEST.parent.mkdir(parents=True, exist_ok=True)
    payload = word.encode('utf-8')
    DEST.write_bytes(payload)
    saved = DEST.read_bytes()
    if saved != payload:
        raise RuntimeError('written entry differs from the word in memory')
    print('entry written:', len(payload), 'bytes ->', str(DEST))


if __name__ == '__main__':
    run()

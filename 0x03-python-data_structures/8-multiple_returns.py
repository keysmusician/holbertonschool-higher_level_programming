#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), sentence[:1]) if len(sentence) else (0, None)

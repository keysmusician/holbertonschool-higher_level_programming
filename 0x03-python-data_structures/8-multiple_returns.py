#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence):
        return (len(sentence), sentence[:1])
    else:
        return (0, None)

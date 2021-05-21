#!/usr/bin/python3
"""
A function that formats text.

"""


def text_indentation(text):
    """Prints text with 2 new lines after any '.', ':' or '?'."""
    if type(text) is not str:
        raise TypeError("text must be a string")

    # chars = []
    # for c in text:
    #     chars.append(c + ("\n\n" if c in ".?:" else ""))
    # chars = "".join(chars).split("\n\n")
    # for i, line in enumerate(chars):
    #     chars[i] = line.lstrip(" ")
    # formatted_str = "\n\n".join(chars)
    # print(formatted_str)


text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

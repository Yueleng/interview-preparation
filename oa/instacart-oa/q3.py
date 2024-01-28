def solution(paragraphs, aligns, width):
    res = []
    res.append("*" * (width + 2))
    for i in range(len(paragraphs)):
        paragraph = paragraphs[i]
        line = ""
        for word in paragraph:
            if not line:
                line = word
                continue
            # if the word is too long
            if len(line) + len(word) + 1 > width:
                res.append(process(aligns[i], line, width))
                line = word
            elif len(line) + len(word) + 1 == width:
                res.append(process(aligns[i], line + " " + word, width))
                line = ""
            else:
                line += " " + word

        if line:
            res.append(process(aligns[i], line, width))

    res.append("*" * (width + 2))
    return res


def process(align, cur_res, width):
    # print("current res: ", cur_res)
    # print("align: ", align)
    if align == "LEFT":
        return "*" + cur_res + " " * (width - len(cur_res)) + "*"
    else:
        return "*" + " " * (width - len(cur_res)) + cur_res + "*"


print(
    solution(
        [
            ["there are"],
            ["four seasons", "in a year"],
            ["summer", "autumn", "winter", "spring"],
        ],
        aligns=["RIGHT", "LEFT", "RIGHT"],
        width=12,
    )
)


print(
    solution(
        [
            ["hello", "world"],
            ["How", "areYou", "doing"],
            ["Please look", "and align", "to right"],
        ],
        aligns=["LEFT", "RIGHT", "RIGHT"],
        width=16,
    )
)

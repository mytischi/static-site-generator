def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for i in blocks:
        i = i.strip()
        new_blocks.append(i)
    new_blocks = [x for x in new_blocks if x != ""]
    return new_blocks
def search_max_item(li: list) -> int:
    index: int = 0
    max_item: int = li[index]
    size: int = len(li)

    while index < size:
        if li[index] > max_item:
            max_item = li[index]
        index += 1

    return max_item
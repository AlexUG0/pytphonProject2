def fit_in_boxes(content, slot=2):
    sorted_into_boxes = [content[i:i + slot] for i in range(0, len(content), slot)]
    # sorted_into_boxes = [box for box in sorted_into_boxes if box]

    # if slot <= 0:
    # raise ValueError('Размер подсписка должен быть положительным целым числом')
    return sorted_into_boxes


print(fit_in_boxes([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
print(fit_in_boxes([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

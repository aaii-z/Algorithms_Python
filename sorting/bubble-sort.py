def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(i, len(unsorted_list)):
            if unsorted_list[i] >= unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    print(unsorted_list)


bubble_sort([1, 0, 3, 5, 10])
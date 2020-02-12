def merge(list1, list2):
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            list3.append(list2[j])
            j += 1
        else:
            list3.append(list1[i])
            list3.append(list2[j])
            i += 1
            j += 1
    return list3 + list1[i:] + list2[j:]


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))

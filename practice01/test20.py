def pick_peaks(arr):
    pos, peak = [], []
    dic = {"pos": [], "peaks": []}
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            peak, pos = [arr[i]], [i]
        elif arr[i] < arr[i - 1]:
            dic["peaks"] += peak
            dic["pos"] += pos
            peak, pos = [], []
    return dic


print(pick_peaks([1, 11, 11, 16, 3, 6, 4, 1]))

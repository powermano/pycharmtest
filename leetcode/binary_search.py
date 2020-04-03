def search(nums, left, right, target):
    while left < right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def search_left(nums, left, right, target):
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

def search_right(nums, left, right, target):
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return left if nums[left] == target else left + 1

if __name__ == "__main__":
    nums = [1, 2, 3, 7, 7, 7, 7, 7, 7, 7, 9]
    target = 8
    print(search(nums, 0, len(nums), target))
    print(search_left(nums, 0, len(nums), target))
    print(search_right(nums, 0, len(nums), target))

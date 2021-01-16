import unittest


def bubble_sort(arr):
    for i in range(len(arr)):
      # After the first iteration of the outer loop, we know that the last value of the list is where it should be,
      # so we don't need to look at it again in the next loops
      # Same thing for the second iteration, we know that the last 2 values are in their correct position.
      # So we can reduce the size of the inner loop at each outer iteration
        for index in range(len(arr) - i - 1):
            if arr[index] > arr[index + 1]:
                # Avoid a swap in 3 step with an additional temp variable
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    return arr


class TestBubbleSort(unittest.TestCase):
    def test1(self):
        self.assertEqual(bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test2(self):
        self.assertEqual(bubble_sort([4, 1, 3, 9, 7]), [1, 3, 4, 7, 9])

    def test3(self):
        self.assertEqual(
            bubble_sort(
                [46, 1, 14, 28, 27, 47, 2, 24, 38, 11, 9, 0, 35, 36, 34, 5, 15, 44, 4, 17, 41, 42, 20, 18, 40, 48,
                    7, 10, 6, 3, 8, 23, 29, 26, 33, 12, 39, 30, 45, 43, 37, 49, 25, 32, 19, 21, 22, 16, 31, 13]
            ),
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
             28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
        )


if __name__ == "__main__":
    unittest.main()

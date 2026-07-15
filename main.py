from constants import print_linked_lists, list_to_linked_list
from problem_24_swap_nodes_in_pairs import Solution

if __name__ == "__main__":
    solution = Solution()
    case = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.swapPairs(case)

    print_linked_lists(result)

    # print(result)

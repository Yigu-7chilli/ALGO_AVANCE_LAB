from itertools import combinations


def is_valid_coverage(selected_users, graph):
    covered_users = set()

    for user in selected_users:
        covered_users.add(user)

        for friend in graph[user]:
            covered_users.add(friend)

    for user in graph:
        if user not in covered_users:
            return False

    return True


def find_minimum_coverage(graph):
 

    users = list(graph.keys())
    n = len(users)

    for size in range(0, n + 1):
        for subset in combinations(users, size):
            if is_valid_coverage(subset, graph):
                return size, list(subset)

    return n, users


def find_fast_coverage(graph):


    all_users = set(graph.keys())
    covered_users = set()
    selected_users = []

    while covered_users != all_users:
      
        best_user = None
        best_new_coverage = set()

        for user in all_users:
          
            current_coverage = set()
            current_coverage.add(user)

            for friend in graph[user]:
                current_coverage.add(friend)

            new_coverage = current_coverage - covered_users

            if len(new_coverage) > len(best_new_coverage):
                best_user = user
                best_new_coverage = new_coverage

        selected_users.append(best_user)
        covered_users.update(best_new_coverage)

    return len(selected_users), selected_users


if __name__ == "__main__":

    print("\n##################################### test 0: normal test #########################################################")

    graph = {
        0: [1],
        1: [0, 2, 3],
        2: [1],
        3: [1]
    }

    print("test is_valid_coverage([1], graph):")
    print(str(is_valid_coverage([1], graph)).lower())

    print("\ntest is_valid_coverage([0], graph):")
    print(str(is_valid_coverage([0], graph)).lower())

    print("\nexact minimum coverage:")
    size, selected_users = find_minimum_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)

    print("\ngreedy fast coverage:")
    size, selected_users = find_fast_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)



  
    print("\n###################### test 1: empty graph #######################")

    graph = {}

    print("test is_valid_coverage([], graph):")
    print(str(is_valid_coverage([], graph)).lower())

    print("\nexact minimum coverage:")
    size, selected_users = find_minimum_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)

    print("\ngreedy fast coverage:")
    size, selected_users = find_fast_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)




  
    print("\n####################### test 2: single node graph ########################")

    graph = {
        0: []
    }

    print("test is_valid_coverage([], graph):")
    print(str(is_valid_coverage([], graph)).lower())

    print("\ntest is_valid_coverage([0], graph):")
    print(str(is_valid_coverage([0], graph)).lower())

    print("\nexact minimum coverage:")
    size, selected_users = find_minimum_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)

    print("\ngreedy fast coverage:")
    size, selected_users = find_fast_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)








  
    print("\n############################# test 3: disconnected graph #######################")

    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }

    print("test is_valid_coverage([0], graph):")
    print(str(is_valid_coverage([0], graph)).lower())

    print("\ntest is_valid_coverage([0, 2], graph):")
    print(str(is_valid_coverage([0, 2], graph)).lower())

    print("\nexact minimum coverage:")
    size, selected_users = find_minimum_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)

    print("\ngreedy fast coverage:")
    size, selected_users = find_fast_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)


    print("\n####################### test 4: complete graph #########################")

    graph = {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }

    print("test is_valid_coverage([0], graph):")
    print(str(is_valid_coverage([0], graph)).lower())

    print("\nexact minimum coverage:")
    size, selected_users = find_minimum_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)

    print("\ngreedy fast coverage:")
    size, selected_users = find_fast_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)




  
    print("\n###################### test 5: isolated nodes ################")

    graph = {
        0: [],
        1: [],
        2: []
    }

    print("test is_valid_coverage([0], graph):")
    print(str(is_valid_coverage([0], graph)).lower())

    print("\ntest is_valid_coverage([0, 1, 2], graph):")
    print(str(is_valid_coverage([0, 1, 2], graph)).lower())

    print("\nexact minimum coverage:")
    size, selected_users = find_minimum_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)

    print("\ngreedy fast coverage:")
    size, selected_users = find_fast_coverage(graph)
    print("size:", size)
    print("selected users:", selected_users)





















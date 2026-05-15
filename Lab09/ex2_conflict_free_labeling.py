def is_valid_labeling(labeling, graph):
    """
    check if a given labeling is valid.

    a labeling is valid if every connected pair of users
    has different labels.
    """

    for user in graph:
        for friend in graph[user]:
            if labeling[user] == labeling[friend]:
                return False

    return True


def can_use_label(user, label, labeling, graph):
    """
    check if one label can be assigned to one user.

    the label is valid only if none of the already labeled friends
    has the same label.
    """

    for friend in graph[user]:
        if labeling[friend] == label:
            return False

    return True


def backtrack_label(index, users, labeling, graph, k):
    """
    try to assign labels to users one by one using backtracking.
    """

    if index == len(users):
        return True

    user = users[index]

    for label in range(k):
        if can_use_label(user, label, labeling, graph):
            labeling[user] = label

            if backtrack_label(index + 1, users, labeling, graph, k):
                return True

            labeling[user] = -1

    return False


def assign_labels(k, graph):
    """
    try to label the graph using at most k labels.

    return:
        success, labeling
    """

    users = list(graph.keys())

    if len(users) == 0:
        return True, []

    n = max(users) + 1
    labeling = [-1] * n

    success = backtrack_label(0, users, labeling, graph, k)

    if success:
        return True, labeling

    return False, []


def find_min_labels(graph):
    """
    find the minimum number of labels needed to color the graph.
    """

    users = list(graph.keys())
    n = len(users)

    if n == 0:
        return 0, []

    for k in range(1, n + 1):
        success, labeling = assign_labels(k, graph)

        if success:
            return k, labeling

    return n, []



if __name__ == "__main__":

    print("\n############## test 0: normal test ################")

    graph = {
        0: [1],
        1: [0, 2],
        2: [1]
    }

    labeling = [0, 1, 0]

    print("test is_valid_labeling([0, 1, 0], graph):")
    print(str(is_valid_labeling(labeling, graph)).lower())

    print("\ntest assign_labels(2, graph):")
    success, labeling = assign_labels(2, graph)
    print("success:", str(success).lower())
    print("labeling:", labeling)

    print("\nfind minimum labels:")
    minimum_k, labeling = find_min_labels(graph)
    print("minimum k:", minimum_k)
    print("labeling:", labeling)


    print("\n############## test 1: empty graph ################")

    graph = {}

    print("test find_min_labels(graph):")
    minimum_k, labeling = find_min_labels(graph)
    print("minimum k:", minimum_k)
    print("labeling:", labeling)


    print("\n############## test 2: single node graph ################")

    graph = {
        0: []
    }

    labeling = [0]

    print("test is_valid_labeling([0], graph):")
    print(str(is_valid_labeling(labeling, graph)).lower())

    print("\ntest assign_labels(1, graph):")
    success, labeling = assign_labels(1, graph)
    print("success:", str(success).lower())
    print("labeling:", labeling)

    print("\nfind minimum labels:")
    minimum_k, labeling = find_min_labels(graph)
    print("minimum k:", minimum_k)
    print("labeling:", labeling)


    print("\n############## test 3: one edge graph ################")

    graph = {
        0: [1],
        1: [0]
    }

    print("test assign_labels(1, graph):")
    success, labeling = assign_labels(1, graph)
    print("success:", str(success).lower())
    print("labeling:", labeling)

    print("\ntest assign_labels(2, graph):")
    success, labeling = assign_labels(2, graph)
    print("success:", str(success).lower())
    print("labeling:", labeling)

    print("\nfind minimum labels:")
    minimum_k, labeling = find_min_labels(graph)
    print("minimum k:", minimum_k)
    print("labeling:", labeling)


    print("\n############## test 4: complete graph ################")

    graph = {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }

    print("test assign_labels(3, graph):")
    success, labeling = assign_labels(3, graph)
    print("success:", str(success).lower())
    print("labeling:", labeling)

    print("\ntest assign_labels(4, graph):")
    success, labeling = assign_labels(4, graph)
    print("success:", str(success).lower())
    print("labeling:", labeling)

    print("\nfind minimum labels:")
    minimum_k, labeling = find_min_labels(graph)
    print("minimum k:", minimum_k)
    print("labeling:", labeling)


    print("\n############## test 5: isolated nodes ################")

    graph = {
        0: [],
        1: [],
        2: []
    }

    labeling = [0, 0, 0]

    print("test is_valid_labeling([0, 0, 0], graph):")
    print(str(is_valid_labeling(labeling, graph)).lower())

    print("\ntest assign_labels(1, graph):")
    success, labeling = assign_labels(1, graph)
    print("success:", str(success).lower())
    print("labeling:", labeling)

    print("\nfind minimum labels:")
    minimum_k, labeling = find_min_labels(graph)
    print("minimum k:", minimum_k)
    print("labeling:", labeling)


    print("\n############## test 6: triangle graph ################")

    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }

    print("test assign_labels(2, graph):")
    success, labeling = assign_labels(2, graph)
    print("success:", str(success).lower())
    print("labeling:", labeling)

    print("\ntest assign_labels(3, graph):")
    success, labeling = assign_labels(3, graph)
    print("success:", str(success).lower())
    print("labeling:", labeling)

    print("\nfind minimum labels:")
    minimum_k, labeling = find_min_labels(graph)
    print("minimum k:", minimum_k)
    print("labeling:", labeling)

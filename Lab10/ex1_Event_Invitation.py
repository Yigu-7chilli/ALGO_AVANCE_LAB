def is_valid_invitation(invited, graph):
  
    for i in range(len(invited)):
        for j in range(i + 1, len(invited)):
            user1 = invited[i]
            user2 = invited[j]

            if user2 in graph[user1]:
                return False

    return True


def find_max_invitations_exact(graph):
    nodes = []

    for i in range(len(graph)):
        nodes.append(i)

    best_set = []

    def backtrack(position, current_set):
        nonlocal best_set

        if position == len(nodes):
            if len(current_set) > len(best_set):
                best_set = current_set.copy()
            return

        remaining_nodes = len(nodes) - position

        if len(current_set) + remaining_nodes <= len(best_set):
            return

        user = nodes[position]

        valid = True

        for selected_user in current_set:
            if selected_user in graph[user]:
                valid = False

        if valid == True:
            current_set.append(user)
            backtrack(position + 1, current_set)
            current_set.pop()

        backtrack(position + 1, current_set)

    backtrack(0, [])

    return len(best_set), best_set




def find_max_invitations_greedy(graph):
    remaining_nodes = set()

    for i in range(len(graph)):
        remaining_nodes.add(i)

    invited = []

    while len(remaining_nodes) > 0:
        best_node = None
        smallest_degree = 999999

        for node in remaining_nodes:
            degree = 0

            for neighbor in graph[node]:
                if neighbor in remaining_nodes:
                    degree = degree + 1

            if degree < smallest_degree:
                smallest_degree = degree
                best_node = node

        invited.append(best_node)

        nodes_to_remove = set()
        nodes_to_remove.add(best_node)

        for neighbor in graph[best_node]:
            if neighbor in remaining_nodes:
                nodes_to_remove.add(neighbor)

        for node in nodes_to_remove:
            if node in remaining_nodes:
                remaining_nodes.remove(node)

    return len(invited), invited







def run_test(case_name, graph):
    print("=====================================================================")
    print(case_name)
    print("input:")
    print("graph =", graph)
    print()

    exact_size, exact_users = find_max_invitations_exact(graph)
    greedy_size, greedy_users = find_max_invitations_greedy(graph)

    print("output:")

    print("Exact solution:")
    print("Size:", exact_size)
    print("Invited users:", exact_users)
    print("Valid:", is_valid_invitation(exact_users, graph))

    print()

    print("Greedy solution:")
    print("Size:", greedy_size)
    print("Invited users:", greedy_users)
    print("Valid:", is_valid_invitation(greedy_users, graph))

    print()

    if exact_size == greedy_size:
        print("Greedy found the optimal solution.")
    else:
        print("Greedy did not find the optimal solution.")

    print()





def run_test(case_name, graph):
    print("=============================== TEST ====================================")
    print(case_name)
    print()

    exact_size, exact_users = find_max_invitations_exact(graph)
    greedy_size, greedy_users = find_max_invitations_greedy(graph)

    print("output:")

    print("Exact solution:")
    print("Size:", exact_size)
    print("Invited users:", exact_users)
    print("Valid:", is_valid_invitation(exact_users, graph))

    print()

    print("Greedy solution:")
    print("Size:", greedy_size)
    print("Invited users:", greedy_users)
    print("Valid:", is_valid_invitation(greedy_users, graph))

    print()

    if exact_size == greedy_size:
        print("Greedy found the optimal solution.")
    else:
        print("Greedy did not find the optimal solution.")

    print()



def run_valid_test(case_name, graph, invited):

    print(case_name)
    print()

    print("output:")
    print("Valid:", is_valid_invitation(invited, graph))
    print()


################################### case0 ######################################
graph0 = [
    [1, 2],
    [0, 2],
    [0, 1, 3],
    [2, 4],
    [3]
]

run_test("case0: normal test", graph0)




#################################### case1 ##############################
graph1 = []

run_test("case1: empty graph", graph1)




########################### case2 ##############################
graph2 = [
    []
]

run_test("case2: only one user", graph2)





########################### case3 ##############################
graph3 = [
    [],
    [],
    [],
    []
]

run_test("case3: no conflicts", graph3)









########################### case4 ##############################
graph4 = [
    [1, 2, 3],
    [0, 2, 3],
    [0, 1, 3],
    [0, 1, 2]
]

run_test("case4: all users conflict with each other", graph4)










########################### case5 ##############################
graph5 = [
    [1],
    [0, 2],
    [1]
]
invited5 = [0, 1]

run_valid_test("case5: check invalid invitation list", graph5, invited5)





########################### case6 ##############################
graph6 = [
    [1],
    [0, 2],
    [1]
]
invited6 = [0, 2]

run_valid_test("case6: check valid invitation list", graph6, invited6)













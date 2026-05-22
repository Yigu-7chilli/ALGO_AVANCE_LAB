def is_within_budget(selection, costs, budget):
    total = 0

    for user in selection:
        total = total + costs[user]

    if total <= budget:
        return True
    else:
        return False


def maximize_reach_exact(budget, costs, reaches):
    n = len(costs)

    dp = []

    for i in range(n + 1):
        row = []
        for b in range(budget + 1):
            row.append(0)
        dp.append(row)

    for i in range(1, n + 1):
        user = i - 1

        for b in range(budget + 1):

            if costs[user] <= b:
                choose = dp[i - 1][b - costs[user]] + reaches[user]
                not_choose = dp[i - 1][b]

                if choose > not_choose:
                    dp[i][b] = choose
                else:
                    dp[i][b] = not_choose

            else:
                dp[i][b] = dp[i - 1][b]

    max_reach = dp[n][budget]

    selected_users = []
    b = budget

    for i in range(n, 0, -1):
        user = i - 1

        if dp[i][b] != dp[i - 1][b]:
            selected_users.append(user)
            b = b - costs[user]

    selected_users.reverse()

    return max_reach, selected_users


def maximize_reach_greedy(budget, costs, reaches):
    n = len(costs)

    users = []

    for i in range(n):
        ratio = reaches[i] / costs[i]
        users.append([i, ratio])

    for i in range(n):
        for j in range(i + 1, n):
            if users[j][1] > users[i][1]:
                temp = users[i]
                users[i] = users[j]
                users[j] = temp

    selected_users = []
    total_cost = 0
    total_reach = 0

    for item in users:
        user = item[0]

        if total_cost + costs[user] <= budget:
            selected_users.append(user)
            total_cost = total_cost + costs[user]
            total_reach = total_reach + reaches[user]

    return total_reach, selected_users






# ---------------------------------------------------------------------------
#                               Test 
# ---------------------------------------------------------------------------

def run_test(case_name, budget, costs, reaches):
    print("================== TEST ==============")
    print(case_name)
    print("input:")
    print("budget =", budget)
    print("costs =", costs)
    print("reaches =", reaches)
    print()

    exact_reach, exact_users = maximize_reach_exact(budget, costs, reaches)
    greedy_reach, greedy_users = maximize_reach_greedy(budget, costs, reaches)

    print("output:")

    print("Exact solution:")
    print("Reach:", exact_reach)
    print("Selected users:", exact_users)
    print("Within budget:", is_within_budget(exact_users, costs, budget))

    print()

    print("Greedy solution:")
    print("Reach:", greedy_reach)
    print("Selected users:", greedy_users)
    print("Within budget:", is_within_budget(greedy_users, costs, budget))

    print()

    if exact_reach == greedy_reach:
        print("Greedy found the optimal solution.")
    else:
        print("Greedy did not find the optimal solution.")

    print()



########################## case0 ######################################
run_test(
    "case0: normal case",
    50,
    [10, 20, 30],
    [60, 100, 120]
)



########################## case1 ######################################
run_test(
    "case1: budget is zero",
    0,
    [10, 20, 30],
    [60, 100, 120]
)




########################## case2 ######################################
run_test(
    "case2: empty users",
    50,
    [],
    []
)



########################## case3 ######################################
run_test(
    "case3: all users are too expensive",
    5,
    [10, 20, 30],
    [60, 100, 120]
)



########################## case4 ######################################
run_test(
    "case4: one user exactly fits the budget",
    10,
    [10, 20, 30],
    [60, 100, 120]
)





########################## case5 ######################################
run_test(
    "case5: all users can be selected",
    100,
    [10, 20, 30],
    [60, 100, 120]
)




########################## case6 ######################################
run_test(
    "case6: same ratio",
    10,
    [5, 5, 10],
    [10, 10, 20]
)
















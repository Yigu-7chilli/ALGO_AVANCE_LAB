class UserNode:
    def __init__(self, user_id, name, friends):
        self.user_id = user_id
        self.name = name
        self.friends = friends
        self.left = None
        self.right = None


class UserBST:
    def __init__(self):
        self.root = None

    def insert(self, root, user_id, name, friends):
        if root is None:
            return UserNode(user_id, name, friends)

        if user_id < root.user_id:
            root.left = self.insert(root.left, user_id, name, friends)
          
        elif user_id > root.user_id:
            root.right = self.insert(root.right, user_id, name, friends)

        return root

  
    def add_user(self, user_id, name, friends):
        self.root = self.insert(self.root, user_id, name, friends)

  
    def find(self, node, user_id):
        if node is None or node.user_id == user_id:
            return node

        if user_id < node.user_id:
            return self.find(node.left, user_id)
        else:
            return self.find(node.right, user_id)

  
    def inorder_traversal(self, node, result):
        if node is None:
            return

        self.inorder_traversal(node.left, result)
        result.append(node.user_id)
        self.inorder_traversal(node.right, result)

  
    def get_sorted_user_ids(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result

  
    def min_node(self, node):
        while node.left is not None:
            node = node.left
        return node


  
    def delete(self, node, user_id):
        if node is None:
            return None

        if user_id < node.user_id:
            node.left = self.delete(node.left, user_id)

        elif user_id > node.user_id:
            node.right = self.delete(node.right, user_id)

        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            else:
                temp = self.min_node(node.right)
                node.user_id = temp.user_id
                node.name = temp.name
                node.friends = temp.friends
                node.right = self.delete(node.right, temp.user_id)

        return node


  
    def delete_user(self, user_id):
        self.root = self.delete(self.root, user_id)

  
    def suggest_friends(self, user_id, max_suggestions=5):
        user = self.find(self.root, user_id)

        if user is None:
            return []

        count = {}

        for f in user.friends:
            friend_node = self.find(self.root, f)

            if friend_node is not None:
                for x in friend_node.friends:
                    if x != user_id and x not in user.friends:
                        if x not in count:
                            count[x] = 1
                        else:
                            count[x] += 1

        sorted_candidates = sorted(count.items(), key=lambda item: item[1], reverse=True)
        return sorted_candidates[:max_suggestions]

  
    def get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

  
    def is_balanced(self, node):
        if node is None:
            return True

        left_h = self.get_height(node.left)
        right_h = self.get_height(node.right)

        if abs(left_h - right_h) > 1:
            return False

        return self.is_balanced(node.left) and self.is_balanced(node.right)

  
    def get_leaf_count(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return self.get_leaf_count(node.left) + self.get_leaf_count(node.right)



if __name__ == "__main__":


    print("####################### test 1 #########################")
    bst = UserBST()

    print("Find in empty tree:", bst.find(bst.root, 10))
    print("Sorted user IDs in empty tree:", bst.get_sorted_user_ids())
    print("Suggestions in empty tree:", bst.suggest_friends(1))
    print("Height of empty tree:", bst.get_height(bst.root))
    print("Is balanced (empty tree):", bst.is_balanced(bst.root))
    print("Leaf count (empty tree):", bst.get_leaf_count(bst.root))



    print("\n##################### test 2 ###########################")
    bst = UserBST()
    bst.add_user(10, "Alice", [5, 15])
    bst.add_user(5, "Bob", [10, 20])
    bst.add_user(15, "Charlie", [10, 20, 25])
    bst.add_user(3, "David", [5])
    bst.add_user(7, "Emma", [5])
    bst.add_user(20, "Frank", [5, 15])
    bst.add_user(25, "Grace", [15])

    print("Sorted user IDs:", bst.get_sorted_user_ids())
    print("Expected: [3, 5, 7, 10, 15, 20, 25]")



    print("\n###################### test 3 ##########################")
    user = bst.find(bst.root, 10)
    if user is not None:
        print("Find 10:", user.user_id, user.name, user.friends)
    else:
        print("Find 10: None")

    user = bst.find(bst.root, 99)
  
    if user is not None:
        print("Find 99:", user.user_id, user.name, user.friends)
    else:
        print("Find 99: None")



    print("\n##################### test 4 ###########################")
    print("Before deleting leaf 3:", bst.get_sorted_user_ids())
    bst.delete_user(3)
    print("After deleting leaf 3:", bst.get_sorted_user_ids())
    print("Expected: [5, 7, 10, 15, 20, 25]")



    print("\n######################## test 5 ########################")
    bst2 = UserBST()
    bst2.add_user(10, "A", [])
    bst2.add_user(5, "B", [])
    bst2.add_user(15, "C", [])
    bst2.add_user(12, "D", [])


    print("Before deleting 15:", bst2.get_sorted_user_ids())
    bst2.delete_user(15)
    print("After deleting 15:", bst2.get_sorted_user_ids())
    print("Expected: [5, 10, 12]")



    print("\n##################### test 6 ###########################")
    bst3 = UserBST()
    bst3.add_user(10, "A", [])
    bst3.add_user(5, "B", [])
    bst3.add_user(15, "C", [])
    bst3.add_user(12, "D", [])
    bst3.add_user(20, "E", [])

    print("Before deleting 10:", bst3.get_sorted_user_ids())
    bst3.delete_user(10)
    print("After deleting 10:", bst3.get_sorted_user_ids())
    print("Expected: [5, 12, 15, 20]")


    print("\n#################### test 7 ############################")
    print("Before deleting 99:", bst3.get_sorted_user_ids())
    bst3.delete_user(99)
    print("After deleting 99:", bst3.get_sorted_user_ids())
    print("Expected: no change")



    print("\n#################### test 8 ############################")
    print("Suggestions for user 99:", social.suggest_friends(99, 5))
    print("Expected: []")


    print("\n####################### test 9 #########################")
    self_case = UserBST()
    self_case.add_user(1, "User1", [2])
    self_case.add_user(2, "User2", [1, 3])
    self_case.add_user(3, "User3", [2])

    print("Suggestions for user 1:", self_case.suggest_friends(1, 5))
    print("Expected: [(3, 1)]")





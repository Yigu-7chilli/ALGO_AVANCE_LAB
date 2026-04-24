import random
import time


class TrendingHeap:
  
    def __init__(self):
        self.heap = []         
        self.position = {}     

  
    def push(self, post_id, likes, timestamp):
        entry = [likes, post_id, timestamp]
        self.heap.append(entry)
        i = len(self.heap) - 1
        self.position[post_id] = i

        while i > 0 and self.heap[i][0] > self.heap[(i - 1) // 2][0]:
            parent = (i - 1) // 2
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

            self.position[self.heap[i][1]] = i
            self.position[self.heap[parent][1]] = parent

            i = parent

  
    def pop_max(self):
        if len(self.heap) == 0:
            return None

        max_post = self.heap[0]

        if len(self.heap) == 1:
            self.heap.pop()
            del self.position[max_post[1]]
            return tuple(max_post)

        self.heap[0] = self.heap[-1]
        self.position[self.heap[0][1]] = 0
        self.heap.pop()
      
        del self.position[max_post[1]]

        i = 0
      
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.position[self.heap[i][1]] = i
            self.position[self.heap[largest][1]] = largest

            i = largest

        return tuple(max_post)


  
    def peek_max(self):
        if len(self.heap) == 0:
            return None
        return tuple(self.heap[0])


  
    def get_top_k(self, k):
        temp = TrendingHeap()

        for entry in self.heap:
            temp.heap.append(entry.copy())
        temp.position = self.position.copy()

        result = []
        for _ in range(k):
            post = temp.pop_max()
            if post is None:
                break
            result.append(post)

        return result


  
    def update_likes(self, post_id, new_likes, timestamp):
        if post_id not in self.position:
            return

        i = self.position[post_id]
        old_likes = self.heap[i][0]

        self.heap[i][0] = new_likes
        self.heap[i][2] = timestamp

        if new_likes > old_likes:
            while i > 0 and self.heap[i][0] > self.heap[(i - 1) // 2][0]:
                parent = (i - 1) // 2
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

                self.position[self.heap[i][1]] = i
                self.position[self.heap[parent][1]] = parent

                i = parent
        else:
            while True:
                largest = i
                left = 2 * i + 1
                right = 2 * i + 2

                if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
                    largest = left

                if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
                    largest = right

                if largest == i:
                    break

                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]

                self.position[self.heap[i][1]] = i
                self.position[self.heap[largest][1]] = largest

                i = largest


  
    def size(self):
        return len(self.heap)


  
    def is_valid_heap(self):
        for i in range(len(self.heap)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(self.heap) and self.heap[left][0] > self.heap[i][0]:
                return False

            if right < len(self.heap) and self.heap[right][0] > self.heap[i][0]:
                return False

        return True


  
    def get_height(self):
        n = len(self.heap)

        if n == 0:
            return 0

        h = 0
        while n > 0:
            n = n // 2
            h += 1

        return h


  
    def get_level_order(self):
        result = []
        for post in self.heap:
            result.append(tuple(post))
        return result


  
    def simulate_trending_feed(self):
      
        total_time = 0.0

        for post_id in range(1, 101):
            likes = random.randint(0, 1000)
            timestamp = time.time()
            self.push(post_id, likes, timestamp)

        for step in range(1, 10001):
            post_id = random.randint(1, 100)
            new_likes = random.randint(0, 1000)
            timestamp = time.time()

            start = time.perf_counter()
            self.update_likes(post_id, new_likes, timestamp)
            end_time = time.perf_counter()

            total_time += (end_time - start)

            if step % 1000 == 0:
                top5 = self.get_top_k(5)
                print(f"after {step} updates, top 5 posts: {top5}")

        average_time = total_time / 10000
      
        print("average time per operation:", average_time)


  
if __name__ == "__main__":
    h = TrendingHeap()
    
    print("\n############## test1 ###########################")
    e1 = TrendingHeap()
    print("peek max:", e1.peek_max())
    print("pop max:", e1.pop_max())
    print("top 3:", e1.get_top_k(3))
    print("size:", e1.size())
    print("height:", e1.get_height())
    print("level order:", e1.get_level_order())
    print("is valid heap:", e1.is_valid_heap())

    print("\n############## test2 ###########################")
    e2 = TrendingHeap()
    e2.push(201, 99, 5000)
    print("peek max:", e2.peek_max())
    print("size before pop:", e2.size())
    print("pop max:", e2.pop_max())
    print("size after pop:", e2.size())

    print("\n############## test3 ###########################")
    e3 = TrendingHeap()
    e3.push(101, 50, 1000)
    e3.push(102, 80, 1001)
    e3.update_likes(999, 200, 9999)
    print("level order after invalid update:", e3.get_level_order())
    print("size after invalid update:", e3.size())

    print("\n############## test4 ###########################")
    e4 = TrendingHeap()
    e4.push(101, 50, 1000)
    e4.push(102, 80, 1001)
    print("top 5 posts:", e4.get_top_k(5))
    print("heap after get_top_k:", e4.get_level_order())
    print("size after get_top_k:", e4.size())

    print("\n ############## test5 ###########################")
    e5 = TrendingHeap()
    e5.push(301, 100, 1)
    e5.push(302, 100, 2)
    e5.push(303, 100, 3)
    print("peek max:", e5.peek_max())
    print("level order:", e5.get_level_order())
    print("is valid heap:", e5.is_valid_heap())



    

import queue


class MovingAvg():
    def __init__(self, size):
        self.size = size
        self.que = queue.Queue()
        self.sum = 0

    def nextVal(self, num):
        if self.que.qsize() < self.size:
            self.que.put(num)
            self.sum += num
            return self.sum / self.que.qsize()
        else:
            self.que.put(num)
            self.sum += num
            self.sum -= self.que.get()
            return self.sum / self.size



def queueExample():
    q = queue.Queue()
    q.put(1)
    q.put(2)
    print(q.qsize())
    print(q.get())
    print(q.qsize())
    print(q.get())


def main():
    queueExample()

    nums = [2, 8, 19, 37, 4, 5]
    ma = MovingAvg(3)
    results = []
    for num in nums:
        avg = ma.nextVal(num)
        results.append(avg)
    print(results)  # [2.0, 5.0, 9.666666666666666, 21.333333333333332, 20.0, 15.333333333333334]


if __name__ == "__main__":
    main()
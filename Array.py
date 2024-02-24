class Array(object):

    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems
    
    def get(self, n):
        if 0 <= n and n < self.__nItems:
            return self.__a[n]

    def set(self, n, value):
        if 0 <= n and n < self.__nItems:
            self.__a[n] = value

    def swap(self, i, k):
        if (0 <= i and i < self.__nItems and 0 <=k and k, self.__nItems):
            self.__a[i], self.__a[k] = self.__a[k], self.__a[i]

    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def find(self, item):
        for i in range(self.__nItems):
            if self.__a[i] == item:
                return i
            return -1

    def search(self, item):
        return self.get(self.find(item))

    def delete(self, item):
        for i in range(self.nItems):
            if self.__a[i] == item:
                self.__nItems -= 1
                for k in range(i, self.__nItems):
                    self.__a[k] = self.__a[k+1]
                return True
        
        return False

    def traverse(self, function = print):
        for i in range(self.__nItems):
            function(self.__a[i])

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[i])
        ans += "]"
        return ans

    def bubbleSort(self):
        for last in range(self.__nItems-1, 0, -1):
            for inner in range(last):
                if self.__a[inner] > self.__a[inner+1]:
                    self.swap(inner, inner+1)

    def selectionSort(self):
        for outer in range(self.__nItems-1):
            min = outer
            for inner in range(outer+1, self.__nItems):
                if self.__a[inner] < self.__a[min]:
                    min = inner
            self.swap(outer, min)

    def insertionSort(self):
            for outer in range(1, self.__nItems):
                temp = self.__a[outer]
                inner = outer
                while inner > 0 and temp < self.__a[inner-1]:
                    self.__a[inner] = self.__a[inner-1]
                    inner -= 1
                self.__a[inner] = temp

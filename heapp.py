class Heap:

    def __init__(self):
        self.HeapArray = [] # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        self.HeapArray = [None] * ( 2**(depth+1)-1)
        if len(a) == 0:
            return self.HeapArray
        self.HeapArray[0] = a[0]
        for i in range(1, len(a)):  # пробегаем  по данным исходного массива начиная со второго тк первый уже вставили
            self.HeapArray[i] = a[i]
            idx = int((i - 1) // 2)
            for j  in range(len(self.HeapArray)): # не правильно работает!!!!!!!!!!!!
                if self.HeapArray[j] is None:
                    break
                if self.HeapArray[j] > self.HeapArray[int((j - 1) / 2)]:
                    self.HeapArray[j],self.HeapArray[int((j - 1) / 2)] = self.HeapArray[int((j - 1) / 2)],self.HeapArray[j]
        return self.HeapArray


    def GetMax(self):
        count_element = 0
        # вернуть значение корня и перестроить кучу
        for i in range(len(self.HeapArray)):
            if self.HeapArray[i] is not None:
                count_element += 1
        if count_element == 0:# если куча пуста
            return -1
        if count_element == 1:  # если куча  состоит из одного элемента
            return -1
        result = self.HeapArray[0]
        for i in range(len(self.HeapArray)-1,0,-1):
            if self.HeapArray[i] is not None:
                self.HeapArray[0] = self.HeapArray[i]
                self.HeapArray[i] = None
                break
        for i in range(len(self.HeapArray)):
            if 2 * i + 1 > i - 2 or 2 * i + 2 > i - 2:
                return result
            if self.HeapArray[2 * i + 2] >= self.HeapArray[2 * i + 1] and self.HeapArray[2 * i + 2] > self.HeapArray[i]:
                self.HeapArray[i],self.HeapArray[2 * i + 2] = self.HeapArray[2 * i + 2],self.HeapArray[i]
                i = 2 * i + 2
            if self.HeapArray[2 * i + 2] <= self.HeapArray[2 * i + 1] and self.HeapArray[2 * i + 1] > self.HeapArray[i]:
                self.HeapArray[i],self.HeapArray[2 * i + 1] = self.HeapArray[2 * i + 1],self.HeapArray[i]
                i = 2 * i + 1
            if self.HeapArray[i] > self.HeapArray[2 * i + 2] and self.HeapArray[i] > self.HeapArray[2 * i + 1]:
                break
        
        return result

    def Add(self, key):# добавляем новый элемент key в кучу и перестраиваем её
        if None  not in self.HeapArray:
            return False
        id_last_elem = 0
        for i in self.HeapArray:
            if i != None:
                id_last_elem += 1
        self.HeapArray[id_last_elem] = key
        for i in range(id_last_elem,-1,-1):
            if self.HeapArray[i] > self.HeapArray[int((i - 1) / 2)]:
                self.HeapArray[i],self.HeapArray[int((i - 1) / 2)] = self.HeapArray[int((i - 1) / 2)],self.HeapArray[i]
                i = int((i - 1) / 2)
a = [4, 10, 3, 5, 1]
# a = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
heap = Heap()
print(heap.MakeHeap(a, 3))
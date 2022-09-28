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
        count_element  = len(a)
        for i in range(1, len(a)):  # пробегаем  по данным исходного массива начиная со второго тк первый уже вставили
            self.HeapArray[i] = a[i]

            idx = int((i - 1) / 2)
            append_id = i

            while idx >=0 and append_id > 0:
                if self.HeapArray[append_id] > self.HeapArray[idx]:
                    self.HeapArray[append_id],self.HeapArray[idx] = self.HeapArray[idx],self.HeapArray[append_id]
                else:
                    if 2 * append_id + 2 >= len(self.HeapArray) or 2 * append_id + 1 >= len(self.HeapArray):
                        break
                    if self.HeapArray[2 * append_id + 2] is  None and self.HeapArray[2 * append_id + 1] is  None:
                        break
                    if self.HeapArray[2 * append_id + 2] is  None and self.HeapArray[2 * append_id + 1] <= self.HeapArray[append_id]:
                        break
                    if self.HeapArray[2 * append_id + 1] is  None and self.HeapArray[2 * append_id+ 2] <= self.HeapArray[append_id]:
                        break
                    if (self.HeapArray[2 * append_id + 2] is  None or self.HeapArray[2 * append_id + 2] <= self.HeapArray[2 * append_id + 1]) and self.HeapArray[2 * append_id + 1] > self.HeapArray[append_id]:
                        self.HeapArray[append_id],self.HeapArray[2 * append_id + 1] = self.HeapArray[2 * append_id + 1],self.HeapArray[append_id]
                        append_id = 2 * i + 1
                        idx = int((append_id - 1) / 2)
                        break
                    if ((2 * append_id + 2) <= (count_element - 2)) and (self.HeapArray[2 * append_id+ 1] is  None or (self.HeapArray[2 * append_id + 2] >= self.HeapArray[2 * append_id+ 1])) and (self.HeapArray[2 * append_id + 2] > self.HeapArray[append_id]):
                        self.HeapArray[append_id],self.HeapArray[2 * append_id + 2] = self.HeapArray[2 * append_id + 2],self.HeapArray[append_id]
                        append_id = 2 * i + 2
                        idx = int((append_id - 1) / 2)
                        break
                append_id = idx
                idx = int((append_id - 1) / 2)
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
        idx = 0
        for i in range(len(self.HeapArray)):

            if 2 * idx + 2 >= len(self.HeapArray) or 2 * idx + 1 >= len(self.HeapArray):
                return result 
            if self.HeapArray[2 * idx + 2] is  None and self.HeapArray[2 * idx + 1] is  None:
                return result
            if 2 * idx + 1 <= count_element - 2 and self.HeapArray[2 * idx + 2] is  None or self.HeapArray[2 * idx + 2] <= self.HeapArray[2 * idx + 1] and self.HeapArray[2 * idx + 1] > self.HeapArray[idx]:
                self.HeapArray[idx],self.HeapArray[2 * idx + 1] = self.HeapArray[2 * idx + 1],self.HeapArray[idx]
                idx = 2 * i + 1
                continue
            if 2 * idx + 2 <= count_element - 2 and self.HeapArray[2 * idx + 1] is  None or self.HeapArray[2 * idx + 2] >= self.HeapArray[2 * idx + 1] and self.HeapArray[2 * idx + 2] > self.HeapArray[idx]:
                self.HeapArray[idx],self.HeapArray[2 * idx + 2] = self.HeapArray[2 * idx + 2],self.HeapArray[idx]
                idx = 2 * i + 2
                continue

        return result

    def Add(self, key):# добавляем новый элемент key в кучу и перестраиваем её
        if None  not in self.HeapArray:
            return False
        id_last_elem = 0
        for i in self.HeapArray:
            if i != None:
                id_last_elem += 1
        self.HeapArray[id_last_elem] = key
        id_add_elem = id_last_elem# индекс элемента который мы вставляем
        parent_idx = int((id_add_elem - 1) / 2) # индекс его родителя
        for i in range(id_last_elem,-1,-1):
            if self.HeapArray[id_add_elem] > self.HeapArray[parent_idx]:
                self.HeapArray[id_add_elem],self.HeapArray[parent_idx] = self.HeapArray[parent_idx],self.HeapArray[id_add_elem]
                id_add_elem = parent_idx
                parent_idx = int((id_add_elem - 1) / 2)
            else:
                break
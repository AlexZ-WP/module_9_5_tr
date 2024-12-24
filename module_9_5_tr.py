
class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if self.step == 0:# только проверяет ничего не возвращает, но так же восполняет пробел при обращении
            # к классу, добавляя незаданный атрибут (в частности шаг). В чём прикол???? Почему нельзя всё сделать в
            # первом __init__, работает так же???
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self 
    def __next__(self):

        self.pointer += self.step # если в этой позиции, то отображает правильно, но без первого числа
        #sign = lambda x: -1 if x < 0 else 1 if x > 0 else 0

        if self.pointer > self.stop:
            while self.step > 0:
                raise StopIteration()
        if self.pointer < self.stop:
            while self.step < 0:
                raise StopIteration()

        #if self.pointer > self.stop:
            #for self.step > 0: # выдаёт ошибку invalid syntax ???
            #     if self.pointer < self.stop:
            #         for self.step < 0: # выдаёт ошибку invalid syntax ???
            #             raise StopIteration()
        #self.pointer += self.step #если в этой позиции, то так же без первого числа,
        # но даёт на одно число больше???

        return self.pointer
try:
    iter1 = Iterator(100, 200, 0) # почему для данного объекта отдельный цикл, можно ли
    # сделать один с таким исключением для всех ???
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()









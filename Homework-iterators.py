import types
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.list_length = len(list_of_list)
        self.counter = -1

    def __iter__(self):
        self.counter += 1
        self.list_elements_counter = 0
        return self

    def __next__(self):
        if self.list_elements_counter == len(self.list_of_list[self.counter]):
            iter(self)
        if self.counter == self.list_length:
            raise StopIteration
        self.list_elements_counter += 1
        return self.list_of_list[self.counter][self.list_elements_counter-1]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    
    for i in FlatIterator(list_of_lists_1): 
        print (i)
    

#2
def flat_generator(list_of_lists):
    for sub_list in list_of_lists:
        for item in sub_list:
            yield item

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    
    for i in flat_generator(list_of_lists_1):
        print(i)



if __name__ == '__main__':
    # test_1()
    test_2()
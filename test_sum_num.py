from unittest import TestCase
# path ='/home/yogendra/Desktop/unittest'
path ='/mnt/shared_from_host'

class TestSum(TestCase):
    
    def test_sum(self):
        from sum_num import sum

        # first store the expected result in a variable
        result = sum(3, 4)

        # check if the result is equal to expected result
        # here the result should be equal to 7.
        self.assertEquals(7, result)
from unittest import TestCase
from task.answer_01 import check_is_prime

class TestCheckIsPrime(TestCase):
    """== Class test for function check_is_prime == \n
        Scenario Test
        - [-] fail for list of not prime number for input (list of even number)
        - [+] success for list of prime number for input

        -----
        Note:
        1. [+] for positive test || [-] for negative test || [...]P for common test function and written in parent
        2. bl -> business logic
    """

    @classmethod
    def setUpClass(cls):
        """ call once a time, before setUp and test_* """
        super(TestCheckIsPrime, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        """ call once a time, after setUp and test_*  """
        super(TestCheckIsPrime, cls).tearDownClass()

    def setUp(self):
        ''' auto called before current test_* is calling '''

    def tearDown(self):
        ''' auto called after current test_* is calling '''
        pass

    # -------------------------------------------------------------FUNCTION HELPER
    # -------------------------------------------------------------FUNCTION CONSUME
    def test_fail_for_list_of_not_prime_number(self):
        list_prime = [4, 6, 8, 10, 12]          # list of even number
        for val in list_prime:
            self.assertEqual(check_is_prime(val), False)

    def test_success_for_list_of_prime_number(self):
        list_prime = [2, 3, 5, 7, 11, 13, 17]
        for val in list_prime:
            self.assertTrue(check_is_prime(val))

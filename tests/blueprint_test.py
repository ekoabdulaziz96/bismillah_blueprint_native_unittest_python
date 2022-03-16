from unittest import TestCase

class TestCheckIsPrime(TestCase):
    """== Class .... == \n
        Scenario Test
        - [+] success for transfer xfers

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

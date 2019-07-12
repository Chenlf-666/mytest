# coding=utf-8

import sys,unittest,traceback
from common import CommonConf


class Hello(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('setUpClass of class is ## {} ##'.format(self.__name__))


    def setUp(self) -> None:
        print('setUp of class is ## {} ##'.format(self.__class__.__name__))

    def test_hello(self):
        print('the name of method is ## {} ##'.format(sys._getframe().f_code.co_name))
        print('the name of class is ## {} ##'.format(self.__class__.__name__))

    @classmethod
    def tearDownClass(self) -> None:
        print('tearDownClass of class is ## {} ##'.format(self.__name__))

def haha():
    try:
        1/0
        print(111111111111111)
    except:
        logger.error(traceback.format_exc())
        print(222222222222222)
if __name__ == "__main__":
    logger = CommonConf.get_logger()
    haha()
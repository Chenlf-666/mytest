# -*- coding: utf-8 -*-

import time
import unittest
from packages.HTMLTestRunner import HTMLTestRunner
from common import CommonConf
import logging


if __name__ == "__main__":
    start = time.time()

    logconf = CommonConf.ParseConfig()
    logger = logconf.get_logger()
    logger.info("======================Test Start=====================")
    suite = unittest.TestSuite()

    # test_case_list = [ i for i in os.listdir("./test_case") if i.startswith("test") ]
    # for case in test_case_list:
    #     suite.addTest()
    # runner = unittest.TestLoader().discover('test_case')
    # suite.addTest(runner)
    # with open('./report/HTMLReport.html', 'wb') as f:
    #     runner = HTMLTestRunner(stream=f,
    #                             title='My Test Report',
    #                             description='generated by HTMLTestRunner.',
    #                             verbosity=2)
    #     runner.run(suite)
    # f.close()

    runner = unittest.TestLoader().discover('test_case')
    unittest.TextTestRunner(verbosity=2).run(runner)
    end = time.time()
    runtime = str(int(end - start)) + "s"
    logger.info("======================Test End=====================")
    logger.info("===RunTime: " + runtime)

"""
@Project: BeautifulReport
@Author: Mocobk
@Data: 2019/03/18
@File: test_demo_report.py
@License: MIT
"""
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('./tests', pattern='test_demo*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告_demo', description='测试deafult报告', report_dir='report', theme='theme_default')

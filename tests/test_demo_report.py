"""
@Project: BeautyReport
@Author: Mocobk
@Data: 2019/03/18
@File: test_demo_report.py
@License: MIT
"""
import unittest


class UiAutoTestCase(unittest.TestCase):
    """ 测试报告的基础用例Sample """
    # @classmethod
    # def setUpClass(cls):
    #     print(1/0)

    def test_home_page_is_ok(self):
        """测试访问首页正常, 并使用title进行断言"""
        print(1/0)
        self.assertEqual("Raymond's Blog", "Raymond's Blog")

    def test_save_img_and_view(self):
        """打开首页, 截图, 在截图后点击第一篇文章连接, 跳转页面完成后再次截图"""
        self.assertEqual("Raymond's Blog", "Raymond's Blog")

    @unittest.skip('tiaoguo')
    def test_sip_case_img(self):
        """如果case没有出现错误, 即使使用了错误截\n图装饰器, 也不会影响case的使用"""
        self.assertEqual("Raymond's Blog", "Raymond's Blog")

    def test_success_case_img(self):
        """如果case没有出现错误, 即使使用了错误截\n图装饰器, 也不会影响case的使用"""
        self.assertEqual("Raymond's Blog", "Raymond's Blog")

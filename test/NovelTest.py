# coding=utf-8
import unittest
import os
import sys

sys.path.append("../")
from sender.util import Kmail


@unittest.skipIf(True, "only test when email cant run")
class MailTest(unittest.TestCase):
    def testSend(self):
        return

        newf = "奇怪.txt"
        newfc = "你真！！！"

        f = open(newf, "w")
        f.write(newfc)
        f.close()
        mail = Kmail.Mail()
        mail.set_receiver("122694501@qq.com")
        mail.send2kindle([newf, ])

        os.remove(newf)


if __name__ == '__main__':
    unittest.main(warnings='ignore')

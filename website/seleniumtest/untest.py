from testcase import seltest
import unittest
import subprocess

class TestPhpWebsite(unittest.TestCase):
    def test_php(self):
        dockerstop = "docker stop phpcontainer"
        actual_text = seltest()
        readFile = open("phpapp.txt", 'r')
        expected_text = readFile.read()
        readFile.close()
        if (expected_text != actual_text):
            subprocess.call(dockerstop, shell=True)
        self.assertEqual(actual_text,expected_text,msg="Actual and expected does not match")
        print("Matching")

if __name__ == '__main__':
    unittest.main()

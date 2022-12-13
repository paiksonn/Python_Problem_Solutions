import unittest
import main as md


class Test_md_conv(unittest.TestCase):
    
    prog_data = "# title BIGTITLE\n# author memyselfandi\n# description some code description"
    title ='Test test test'
    description = 'some code description'
    source_code = "print('hello')"

    def test_prepare_md_titles(self):
        expected = ('BIGTITLE', 'some code description')
        self.assertEqual(md.prepare_md_titles(self.prog_data), expected)

    def test_prepare_md_format(self):
        test = md.prepare_md_format(self.title, self.description, self.source_code)
        expected = ('+ [Test test test](#test-prog)\n', "## Test test test\nsome code description\n    \n```python\nprint('hello')\n```")
        self.assertEquals(test, expected)


if __name__ == "__main__":
    unittest.main()

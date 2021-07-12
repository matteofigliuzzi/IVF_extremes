import os
import unittest
import IVF_extremes

out_test_folder = 'out_test'
data_path = '../data/Sample_IVF_data.csv'

class TestIVF(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        for f in os.listdir(out_test_folder):
            os.remove(os.path.join(out_test_folder,f))
        os.rmdir(out_test_folder)

    def test_IVF_nobaseline(self):
        df_outliers = IVF_extremes.batch_check(data_path,out_path=out_test_folder)
        outliers = list(df_outliers.Patient_ID.unique())
        expected_outlier = [9,15,16,29,40,44,47,52,55,67,76,79,86]
        self.assertEqual(outliers,  expected_outlier)

    def test_IVF_baseline(self):
        df_outliers = IVF_extremes.batch_check(data_path,out_path=out_test_folder,estimate_baseline=True)
        outliers = list(df_outliers.Patient_ID.unique())
        expected_outlier = [9, 13, 15, 51, 53, 55, 67, 76, 79, 86]
        self.assertEqual(outliers,  expected_outlier)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestIVF('test_IVF_baseline'))
    suite.addTest(TestIVF('test_IVF_nobaseline'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

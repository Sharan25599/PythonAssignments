from src.FindingPercentage.util import findingpercentage

class MyTestCase(unittest.TestCase):
    def test_findingpercentage(self):
        # finding Percentage assignment
        n = 3
        students = ["Krishna 67 68 69", "Arjun 70 98 63", "Malika 52 56 60"]
        query_name = "Arjun"
        res = findingpercentage(n,students,query_name)
        print(res)
        actual = f"{77.00:.2f}"
        self.assertEqual(res, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()

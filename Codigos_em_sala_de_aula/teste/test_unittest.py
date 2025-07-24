import unittest
import funcao_unittes

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(funcao_unittes.soma(2,3),5)
        self.assertEqual(funcao_unittes.soma(5,8),3)

if __name__ == "__main__":
    unittest.main()
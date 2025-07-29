import unittest
import divisao_funcao
import tkinter
class Teste_divisao_funcao(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(divisao_funcao.divisao(4,2),2)
        self.assertEqual(divisao_funcao.divisao(5,0),"Dividendo não pode ser igual a zero")
        self.assertEqual(divisao_funcao.divisao(7.5,3),2.5)
        
if __name__ == "__main__":
    unittest.main()
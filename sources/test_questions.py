import random
import sys
import types
import unittest
from unittest.mock import MagicMock, patch

from questions import QuestionarioGUI
from reports import POSSIBLE_ANSWERS, QUESTIONS, REPORT_PARAGRAPHS


class TestQuestionarioGUI(unittest.TestCase):
    def setUp(self):
        # Use a minimal set for testing
        self.questions = {
            0: 'Nome:',
            1: 'Como foi a adaptação?',
            2: 'Aspecto emocional?',
        }
        self.possible_answers = {
            0: [],
            1: ['Boa', 'Ruim'],
            2: ['Tranquilo', 'Ansioso'],
        }
        self.report_paragraphs = {
            1: {
                'Boa': ['Adaptação excelente.'],
                'Ruim': ['Adaptação difícil.'],
            },
            2: {
                'Tranquilo': ['Emocional estável.'],
                'Ansioso': ['Emocional instável.'],
            },
        }
        # Patch REPORT_PARAGRAPHS in the class
        patcher = patch('questions.REPORT_PARAGRAPHS', self.report_paragraphs)
        self.addCleanup(patcher.stop)
        patcher.start()
        # Patch tkinter root
        self.root = MagicMock()
        self.gui = QuestionarioGUI(
            self.root, self.questions, self.possible_answers
        )

    def test_identificar_resposta_por_codigo(self):
        codigo = '01'  # Nome: (ignored), 1: 'Ruim', 2: 'Tranquilo'
        respostas = self.gui.identificar_resposta_por_codigo(
            self.questions, self.possible_answers, '01'
        )
        self.assertEqual(
            respostas['Nome:'],
            self.possible_answers[0][0]
            if self.possible_answers[0]
            else 'Sem resposta',
        )
        self.assertEqual(respostas['Como foi a adaptação?'], 'Ruim')
        self.assertEqual(respostas['Aspecto emocional?'], 'Tranquilo')

    def test_gerar_relatorio_paragrafos(self):
        respostas = {
            'Nome:': 'João',
            'Como foi a adaptação?': 'Boa',
            'Aspecto emocional?': 'Ansioso',
        }
        # Patch random.choice to always pick the first
        with patch('random.choice', side_effect=lambda x: x[0]):
            relatorio = self.gui.gerar_relatorio_paragrafos(
                self.questions, self.possible_answers, respostas
            )
        self.assertIn('João', relatorio)
        self.assertIn('Adaptação excelente.', relatorio)
        self.assertIn('Emocional instável.', relatorio)

    def test_gerar_relatorio_paragrafos_missing_answer(self):
        respostas = {
            'Nome:': 'Maria',
            'Como foi a adaptação?': 'Boa',
            # 'Aspecto emocional?' missing
        }
        with patch('random.choice', side_effect=lambda x: x[0]):
            relatorio = self.gui.gerar_relatorio_paragrafos(
                self.questions, self.possible_answers, respostas
            )
        self.assertIn('Maria', relatorio)
        self.assertIn('Adaptação excelente.', relatorio)
        # Should not raise error if answer is missing

    def test_identificar_resposta_por_codigo_invalid(self):
        with self.assertRaises(ValueError):
            self.gui.identificar_resposta_por_codigo(
                self.questions, self.possible_answers, 'ZZ'
            )


if __name__ == '__main__':
    unittest.main()


import pytest
from unittest.mock import patch
import tkinter as tk
import zlib
from pathlib import Path

from reports import QUESTIONS, POSSIBLE_ANSWERS, REPORT_PARAGRAPHS
from questions import QuestionarioGUI

@pytest.fixture(scope="module")
def tk_root():
    root = tk.Tk()
    root.withdraw()
    yield root
    root.destroy()


@pytest.fixture
def gui(tk_root):
    return QuestionarioGUI(tk_root, QUESTIONS, POSSIBLE_ANSWERS)

def test_identificar_resposta_por_codigo_valid(gui):
    code = '0' * len(QUESTIONS)
    respostas = gui.identificar_resposta_por_codigo(QUESTIONS, POSSIBLE_ANSWERS, code)
    assert len(respostas) == len(QUESTIONS)
    for idx, pergunta in QUESTIONS.items():
        assert respostas[pergunta] == POSSIBLE_ANSWERS.get(idx, ['Sem resposta'])[0]

def test_identificar_resposta_por_codigo_invalid_length(gui):
    code = '0' * (len(QUESTIONS) - 1)
    with pytest.raises(ValueError):
        gui.identificar_resposta_por_codigo(QUESTIONS, POSSIBLE_ANSWERS, code)

def test_identificar_resposta_por_codigo_invalid_index(gui):
    code = 'F' + '0' * (len(QUESTIONS) - 1)
    with pytest.raises(ValueError):
        gui.identificar_resposta_por_codigo(QUESTIONS, POSSIBLE_ANSWERS, code)

def test_gerar_relatorio_paragrafos(gui):
    respostas = {QUESTIONS[idx]: POSSIBLE_ANSWERS.get(idx, ['Sem resposta'])[0] for idx in QUESTIONS}
    relatorio = gui.gerar_relatorio_paragrafos(QUESTIONS, POSSIBLE_ANSWERS, respostas)
    assert 'Relatório Pedagógico' in relatorio
    assert 'Nome da criança' in relatorio
    assert any(topico.strip() in relatorio for topico in [
        'Sobre à adaptação e rotina escolar,',
        'Ao observar aspectos emocionais e comportamentais,',
        'Nas atividades diárias,',
        'A respeito do desenvolvimento motor e social,',
        'Sobre o desenvolvimento cognitivo e acadêmico,'
    ])

def test_gerar_todas_combinacoes_creates_files(tk_root):
    with patch('sys.stdin.read', return_value='Texto exemplo.'), \
         patch('builtins.input', return_value=''), \
         patch('zlib.compress', side_effect=zlib.compress):
        questions = {0: 'Nome:', 1: 'Pergunta 1'}
        possible_answers = {0: ['Nome Teste'], 1: ['A', 'B']}
        gui = QuestionarioGUI(tk_root, questions, possible_answers)
        pasta_saida = Path('formularios_compactados')
        for f in pasta_saida.glob('*.bin'):
            f.unlink()
        gui.gerar_todas_combinacoes(questions, possible_answers)
        arquivos = list(pasta_saida.glob('*.bin'))
        assert len(arquivos) == 2
        for f in arquivos:
            f.unlink()

def test_mostrar_formulario_compactado_file_not_found(gui):
    with patch('builtins.print') as mock_print:
        gui.mostrar_formulario_compactado('ZZZZ')
        mock_print.assert_called_with('Arquivo não encontrado.')

def test_mostrar_formulario_compactado_success(gui):
    pasta_saida = Path('formularios_compactados')
    pasta_saida.mkdir(exist_ok=True)
    code = 'A' * len(QUESTIONS)
    texto = 'Conteúdo de teste.'
    file_path = pasta_saida / f'{code}.bin'
    with open(file_path, 'wb') as f:
        f.write(zlib.compress(texto.encode('utf-8')))
    with patch('builtins.print') as mock_print:
        gui.mostrar_formulario_compactado(code)
        mock_print.assert_any_call(texto)
    file_path.unlink()

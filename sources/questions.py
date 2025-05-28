QUESTIONS = {
    0: 'Nome:',
    1: 'Como foi a adaptação ?',
    2: 'Característica da criança:',
    3: 'Como ela vivencia a roda rítmica?',
    4: 'Como se alimenta na escola?',
    5: 'Como brinca nos parques? (motricidade, se envolve em conflitos? tem preferências de brincadeiras?)',
    6: 'Como realiza as atividades? (Se recusa, faz sem resistência, tem preferência por algum tipo?)',
    7: 'Qual fase do Grafismo se encontra?',
    8: 'Sabe escrever seu nome?',
    9: 'Identifica alguma letra?',
    10: 'Conta e identifica número?',
    11: 'Participa das aulas de capoeira?',
    12: 'Participa do momento de Euritimia?',
    13: 'Como participa do momento da sala de Leitura?',
    14: 'Participou do projeto Histórias Viajantes?',
    15: 'Como vivencia o momento do faz de conta na sala de aula? (brinca com os brinquedos, é capaz de dividir?)',
    16: 'Após a brincadeira, ajuda a organizar os brinquedos?',
    17: 'Como se comporta nos momentos da Roda de história?',
}

POSSIBLE_ANSWERS = {
    0: ['Nome da criança'],
    1: ['Muito bem', 'Bem', 'Regular', 'Mal', 'Muito mal'],
    2: ['Extrovertida', 'Introvertida', 'Sociável', 'Tímida', 'Outros'],
    3: ['Gosta muito', 'Gosta', 'Regular', 'Não gosta', 'Não participa'],
    4: ['Come bem', 'Come razoavelmente', 'Come pouco', 'Não come'],
    5: ['Muito bem', 'Bem', 'Regular', 'Mal', 'Muito mal'],
    6: [
        'Com facilidade',
        'Com alguma dificuldade',
        'Com muita dificuldade',
        'Não participa',
    ],
    7: [
        'Rabisco desordenado',
        'Rabisco ordenado',
        'Rabisco nomeado',
        'Pré-esquemático',
        'Esquemático',
    ],
    8: ['Sim', 'Não'],
    9: ['Sim', 'Não'],
    10: ['Sim', 'Não'],
    11: ['Sim', 'Não'],
    12: ['Sim', 'Não'],
    13: [
        'Participa com interesse dos momentos de leitura, ouvindo com atenção as histórias contadas.',
        'Demonstra curiosidade pelos livros e gosta de observar as ilustrações.',
        'Interage com os colegas comentando sobre os personagens e enredos.',
        'Reconta as histórias com suas próprias palavras, demonstrando compreensão.',
        'Participa das rodas de conversa após a leitura, expressando suas preferências.',
        'Escolhe livros de forma autônoma e manuseia com cuidado.',
        'Representa as histórias por meio de desenhos e dramatizações.',
        'Demonstra alegria e envolvimento durante os momentos na sala de leitura.',
    ],
    14: [
        'Participou ativamente do projeto, mostrando interesse pelas histórias.',
        'Participou de forma passiva, ouvindo as histórias contadas.',
        'Não participou do projeto.',
    ],
    15: [
        'Brinca com os brinquedos',
        'É capaz de dividir',
        'Brinca sozinho',
        'Não participa',
    ],
    16: ['Ajuda sempre', 'Ajuda às vezes', 'Raramente ajuda', 'Nunca ajuda'],
    17: ['Muito bem', 'Bem', 'Regular', 'Mal', 'Muito mal'],
}

import itertools
import zlib
import os
import sys
from pathlib import Path

def gerar_todas_combinacoes(questions, possible_answers):
    """
    Gera todas as combinações possíveis de respostas para o questionário de forma ordenada.
    Após cada formulário, aguarda o pressionamento da tecla Enter para continuar.
    Salva uma versão comprimida da saída textual em um arquivo.
    Retoma do último formulário salvo, se houver.

    :param questions: Dicionário com perguntas (índice: texto da pergunta)
    :param possible_answers: Dicionário com respostas possíveis (índice: lista de respostas)
    """
    chaves_ordenadas = sorted(questions.keys())
    lista_de_respostas = [possible_answers.get(chave, ['Sem resposta']) for chave in chaves_ordenadas]

    todas_combinacoes = itertools.product(*lista_de_respostas)
    total_perguntas = len(chaves_ordenadas)

    pasta_saida = Path("formularios_compactados")
    pasta_saida.mkdir(exist_ok=True)

    # Determinar último formulário salvo
    arquivos_existentes = list(pasta_saida.glob("*.bin"))
    ultimos_ids = sorted([f.stem for f in arquivos_existentes])
    ultimo_id = ultimos_ids[-1] if ultimos_ids else None

    ignorar = True if ultimo_id else False

    for combinacao in todas_combinacoes:
        identificador = ''.join(f"{lista_de_respostas[i].index(resposta):X}" for i, resposta in enumerate(combinacao))

        if ignorar:
            if identificador == ultimo_id:
                ignorar = False
            continue

        texto_formulario = f"\n=== Formulário preenchido ===\n"
        texto_formulario += f"ID da combinação (hex): {identificador:0>{total_perguntas}}\n\n"
        for chave, resposta in zip(chaves_ordenadas, combinacao):
            print(f"{questions[chave]}\n  -> {resposta}\n")
            texto_formulario += f"{questions[chave]}\n  -> {resposta}\n\n"

        texto_formulario += "\nCole o texto (finalize com Ctrl+D ou Ctrl+Z):"
        print(texto_formulario)

        data = sys.stdin.read()

        # Compactar e salvar
        dados_compactados = zlib.compress(data.encode('utf-8'))
        with open(pasta_saida / f"{identificador}.bin", "wb") as f:
            f.write(dados_compactados)

        input("Pressione Enter para continuar para o próximo formulário...")

def identificar_resposta_por_codigo(questions, possible_answers, codigo_hex):
    """
    Dado um código hexadecimal, identifica como o questionário foi respondido.
    Cada caractere representa o índice hexadecimal da resposta escolhida para cada pergunta.

    :param questions: Dicionário com perguntas (índice: texto da pergunta)
    :param possible_answers: Dicionário com respostas possíveis (índice: lista de respostas)
    :param codigo_hex: String com código hexadecimal de identificação
    :return: Dicionário com perguntas e respostas referentes ao código
    """
    chaves_ordenadas = sorted(questions.keys())
    lista_de_respostas = [possible_answers.get(chave, ['Sem resposta']) for chave in chaves_ordenadas]

    if len(codigo_hex) != len(lista_de_respostas):
        raise ValueError("Código hexadecimal inválido: tamanho incorreto.")

    respostas = {}
    for i, caractere in enumerate(codigo_hex):
        indice = int(caractere, 16)
        opcoes = lista_de_respostas[i]
        if indice >= len(opcoes):
            raise ValueError(f"Índice inválido no código para a pergunta {i}.")
        respostas[questions[chaves_ordenadas[i]]] = opcoes[indice]

    return respostas

def mostrar_formulario_compactado(codigo_hex):
    """
    Lê o arquivo compactado correspondente ao código hexadecimal e exibe o conteúdo descompactado.

    :param codigo_hex: Código hexadecimal do formulário salvo
    """
    caminho = Path("formularios_compactados") / f"{codigo_hex}.bin"
    if not caminho.exists():
        print("Arquivo não encontrado.")
        return

    with open(caminho, "rb") as f:
        dados = f.read()
        texto = zlib.decompress(dados).decode('utf-8')
        print(texto)
mostrar_formulario_compactado('000000000000000000')
#gerar_todas_combinacoes(QUESTIONS,POSSIBLE_ANSWERS)
# Exemplo de uso (descomente para testar):
# respostas = identificar_resposta_por_codigo(QUESTIONS, POSSIBLE_ANSWERS, "000000000000000000")
# for pergunta, resposta in respostas.items():
#     print(f"{pergunta}\n  -> {resposta}\n")


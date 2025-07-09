# Interface gráfica com Tkinter para responder o questionário e exibir o relatório
import itertools
import sys
import tkinter as tk
import zlib
from pathlib import Path
from tkinter import messagebox, scrolledtext, ttk

from reports import QUESTIONS, REPORT_PARAGRAPHS
from possible_answers import POSSIBLE_ANSWERS


class QuestionarioGUI:
    def __init__(self, root, questions, possible_answers):
        self.root = root
        self.questions = questions
        self.possible_answers = possible_answers
        self.respostas_vars = {}
        self.root.title('Questionário Pedagógico')
        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(fill='both', expand=True)
        canvas = tk.Canvas(self.frame)
        scrollbar = ttk.Scrollbar(
            self.frame, orient='vertical', command=canvas.yview
        )
        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind(
            '<Configure>',
            lambda e: canvas.configure(scrollregion=canvas.bbox('all')),
        )
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set, height=600)
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

        # Adiciona todas as perguntas e campos/opções
        for idx in sorted(self.questions.keys()):
            pergunta = self.questions[idx]
            label = ttk.Label(
                self.scrollable_frame,
                text=pergunta,
                wraplength=900,
                font=('Arial', 12, 'bold'),
            )
            label.pack(anchor='w', pady=(10, 0))
            opcoes = self.possible_answers.get(idx, ['Sem resposta'])
            if idx == 0:
                var = tk.StringVar()
                entry = ttk.Entry(
                    self.scrollable_frame, textvariable=var, width=80
                )
                entry.pack(anchor='w', pady=(0, 5))
                self.respostas_vars[pergunta] = var
            else:
                var = tk.StringVar()
                for opcao in opcoes:
                    rb = ttk.Radiobutton(
                        self.scrollable_frame,
                        text=opcao,
                        variable=var,
                        value=opcao,
                    )
                    rb.pack(anchor='w')
                self.respostas_vars[pergunta] = var

        self.botao_gerar = ttk.Button(
            self.scrollable_frame,
            text='Gerar Relatório',
            command=self.mostrar_relatorio,
        )
        self.botao_gerar.pack(pady=20)

    def mostrar_relatorio(self):
        respostas = {}
        for idx in sorted(self.questions.keys()):
            pergunta = self.questions[idx]
            var = self.respostas_vars[pergunta]
            valor = var.get().strip() if var.get() else ''
            if idx == 0:
                respostas[pergunta] = valor if valor else '[Nome da criança]'
            else:
                if not valor:
                    messagebox.showwarning(
                        'Atenção', f'Responda a pergunta: {pergunta}'
                    )
                    return
                respostas[pergunta] = valor
        # Limpa frame e mostra relatório
        for widget in self.frame.winfo_children():
            widget.destroy()
        relatorio = self.gerar_relatorio_paragrafos(
            self.questions, self.possible_answers, respostas
        )
        label = ttk.Label(
            self.frame, text='Relatório Gerado:', font=('Arial', 12, 'bold')
        )
        label.pack(pady=(0, 10))
        txt = scrolledtext.ScrolledText(
            self.frame, width=180, height=80, font=('Arial', 11)
        )
        txt.pack()
        txt.insert('1.0', relatorio)
        txt.config(state='disabled')
        btn = ttk.Button(self.frame, text='Fechar', command=self.root.destroy)
        btn.pack(pady=10)

    def preencher_e_gerar_relatorio(self,questions, possible_answers):
        """
        Realiza as perguntas ao usuário, mostra as opções de resposta e, ao final, gera o relatório pedagógico.
        """
        respostas = {}
        for idx in sorted(questions.keys()):
            pergunta = questions[idx]
            opcoes = possible_answers.get(idx, ['Sem resposta'])
            print(f'\n{pergunta}')
            for i, opcao in enumerate(opcoes):
                print(f'  [{i+1}] {opcao}')
            while True:
                try:
                    escolha = input(
                        f'Escolha uma opção (1-{len(opcoes)}): '
                    ).strip()
                    if idx == 0:
                        # Nome é campo livre
                        respostas[pergunta] = (
                            escolha if escolha else '[Nome da criança]'
                        )
                        break
                    escolha_int = int(escolha)
                    if 1 <= escolha_int <= len(opcoes):
                        respostas[pergunta] = opcoes[escolha_int - 1]
                        break
                    else:
                        print('Opção inválida. Tente novamente.')
                except Exception:
                    print('Entrada inválida. Tente novamente.')
        print('\n--- RELATÓRIO GERADO ---\n')
        print(
            self.gerar_relatorio_paragrafos(questions, possible_answers, respostas)
        )

    def gerar_todas_combinacoes(self,questions, possible_answers):
        """
        Gera todas as combinações possíveis de respostas para o questionário de forma ordenada.
        Após cada formulário, aguarda o pressionamento da tecla Enter para continuar.
        Salva uma versão comprimida da saída textual em um arquivo.
        Retoma do último formulário salvo, se houver.

        :param questions: Dicionário com perguntas (índice: texto da pergunta)
        :param possible_answers: Dicionário com respostas possíveis (índice: lista de respostas)
        """
        chaves_ordenadas = sorted(questions.keys())
        lista_de_respostas = [
            possible_answers.get(chave, ['Sem resposta'])
            for chave in chaves_ordenadas
        ]

        todas_combinacoes = itertools.product(*lista_de_respostas)
        total_perguntas = len(chaves_ordenadas)

        pasta_saida = Path('formularios_compactados')
        pasta_saida.mkdir(exist_ok=True)

        # Determinar último formulário salvo
        arquivos_existentes = list(pasta_saida.glob('*.bin'))
        ultimos_ids = sorted([f.stem for f in arquivos_existentes])
        ultimo_id = ultimos_ids[-1] if ultimos_ids else None

        ignorar = True if ultimo_id else False

        for combinacao in todas_combinacoes:
            identificador = ''.join(
                f'{lista_de_respostas[i].index(resposta):X}'
                for i, resposta in enumerate(combinacao)
            )

            if ignorar:
                if identificador == ultimo_id:
                    ignorar = False
                continue

            texto_formulario = '\n=== Formulário preenchido ===\n'
            texto_formulario += f'ID da combinação (hex): {identificador:0>{total_perguntas}}\n\n'
            for chave, resposta in zip(chaves_ordenadas, combinacao):
                print(f'{questions[chave]}\n  -> {resposta}\n')
                texto_formulario += f'{questions[chave]}\n  -> {resposta}\n\n'

            texto_formulario += (
                '\nCole o texto (finalize com Ctrl+D ou Ctrl+Z):'
            )
            print(texto_formulario)

            data = sys.stdin.read()

            # Compactar e salvar
            dados_compactados = zlib.compress(data.encode('utf-8'))
            with open(pasta_saida / f'{identificador}.bin', 'wb') as f:
                f.write(dados_compactados)

            input(
                'Pressione Enter para continuar para o próximo formulário...'
            )

    def identificar_resposta_por_codigo(self,
        questions, possible_answers, codigo_hex
    ):
        """
        Dado um código hexadecimal, identifica como o questionário foi respondido.
        Cada caractere representa o índice hexadecimal da resposta escolhida para cada pergunta.

        :param questions: Dicionário com perguntas (índice: texto da pergunta)
        :param possible_answers: Dicionário com respostas possíveis (índice: lista de respostas)
        :param codigo_hex: String com código hexadecimal de identificação
        :return: Dicionário com perguntas e respostas referentes ao código
        """
        chaves_ordenadas = sorted(questions.keys())
        lista_de_respostas = [
            possible_answers.get(chave, ['Sem resposta'])
            for chave in chaves_ordenadas
        ]

        if len(codigo_hex) != len(lista_de_respostas):
            raise ValueError('Código hexadecimal inválido: tamanho incorreto.')

        respostas = {}
        for i, caractere in enumerate(codigo_hex):
            indice = int(caractere, 16)
            opcoes = lista_de_respostas[i]
            if indice >= len(opcoes):
                raise ValueError(
                    f'Índice inválido no código para a pergunta {i}.'
                )
            respostas[questions[chaves_ordenadas[i]]] = opcoes[indice]

        return respostas

    def mostrar_formulario_compactado(self,codigo_hex):
        """
        Lê o arquivo compactado correspondente ao código hexadecimal e exibe o conteúdo descompactado.

        :param codigo_hex: Código hexadecimal do formulário salvo
        """
        caminho = Path('formularios_compactados') / f'{codigo_hex}.bin'
        if not caminho.exists():
            print('Arquivo não encontrado.')
            return

        with open(caminho, 'rb') as f:
            dados = f.read()
            texto = zlib.decompress(dados).decode('utf-8')
            print(texto)

    def gerar_relatorio_paragrafos(self,questions, possible_answers, respostas):
        """
        Gera um relatório concatenando parágrafos conforme as respostas do questionário.
        :param questions: Dicionário de perguntas
        :param possible_answers: Dicionário de respostas possíveis
        :param respostas: Dicionário {pergunta: resposta}
        :return: String com o relatório completo
        """
        import random

        # Estrutura de tópicos atualizada conforme as perguntas do formulário
        TOPICOS = {
            '\nSobre à adaptação e rotina escolar,': [1, 4],
            '\nAo observar aspectos emocionais e comportamentais,': [2, 17, 18, 19, 22],
            '\nNas atividades diárias,': [3, 6, 14, 15, 16],
            '\nA respeito do desenvolvimento motor e social,': [5, 12, 13, 20, 21],
            '\nSobre o desenvolvimento cognitivo e acadêmico,': [7, 8, 9, 10, 11, 23],
        }

        paragrafos = []
        nome = respostas.get('Nome:', '[Nome da criança]')
        paragrafos.append(f'Relatório Pedagógico\nNome da criança: {nome}\n')

        for topico, ids in TOPICOS.items():
            paragrafos.append(f'\t{topico}')
            flag = True
            for idx in ids:
                if idx in REPORT_PARAGRAPHS:
                    resposta = respostas.get(questions[idx])
                    paragrafo = REPORT_PARAGRAPHS[idx].get(resposta)
                    if isinstance(paragrafo, list):
                        rand = random.choice(paragrafo)
                        if flag:
                            paragrafos.append(rand[0].lower() + rand[1:])
                            flag = False
                        else:
                            paragrafos.append(rand)
                    elif paragrafo:
                        paragrafos.append(paragrafo)
            paragrafos.append('\n')  # Separador entre tópicos

        return ''.join(paragrafos)


if __name__ == '__main__':
    root = tk.Tk()
    app = QuestionarioGUI(root, QUESTIONS, POSSIBLE_ANSWERS)
    root.mainloop()

# reports.py
# Dicionário que associa cada resposta possível a um parágrafo de relatório pedagógico

REPORT_PARAGRAPHS = {
    1: {
        'Muito bem': [
            'A adaptação da criança ao ambiente escolar foi excelente. Desde o início do período letivo, demonstrou grande entusiasmo e facilidade para se integrar ao novo ambiente, participando ativamente das atividades propostas e estabelecendo vínculos positivos com colegas e educadores. Sua postura colaborativa e aberta contribuiu para um clima harmonioso na sala de aula, favorecendo o desenvolvimento de suas habilidades sociais e emocionais.',
            'A criança se adaptou de forma exemplar ao ambiente escolar, mostrando alegria e disposição em todas as atividades, além de criar laços afetivos rapidamente com colegas e professores.',
            'Desde o início, a criança demonstrou uma integração notável, participando com entusiasmo das rotinas escolares e estabelecendo relações saudáveis com todos ao redor.',
            'A adaptação foi extremamente positiva, com a criança mostrando-se aberta a novas experiências e interagindo de maneira harmoniosa com o grupo.',
            'A criança apresentou uma adaptação admirável, envolvendo-se com facilidade nas propostas pedagógicas e contribuindo para o bom clima da turma.',
            'O processo de adaptação foi tranquilo e produtivo, com a criança demonstrando segurança e interesse em aprender e conviver.',
            'A criança rapidamente se sentiu à vontade no ambiente escolar, participando de todas as atividades e demonstrando satisfação em estar na escola.',
            'A integração da criança ao novo contexto escolar foi muito natural, evidenciando maturidade e sociabilidade.',
            'A criança se destacou pela facilidade com que se adaptou, mostrando-se receptiva e colaborativa em todas as situações.',
            'A adaptação foi marcada por entusiasmo e envolvimento, com a criança aproveitando ao máximo as oportunidades de interação e aprendizado.'
        ],
        'Bem': [
            'A adaptação da criança ao ambiente escolar foi boa. Mostrou-se receptiva às novidades e, com o passar dos dias, foi se envolvendo cada vez mais nas atividades e interagindo de forma positiva com os colegas. Eventuais momentos de insegurança foram superados com o apoio da equipe escolar, permitindo que a criança se sentisse acolhida e motivada a participar.',
            'A criança apresentou uma adaptação satisfatória, participando das atividades e interagindo bem com o grupo, mesmo que de forma gradual.',
            'O processo de adaptação foi positivo, com a criança demonstrando interesse e aceitação pelas rotinas escolares.',
            'A criança se mostrou aberta ao novo ambiente, integrando-se progressivamente às dinâmicas da turma.',
            'A adaptação ocorreu de maneira tranquila, com a criança participando das atividades e estabelecendo vínculos com colegas e professores.',
            'A criança se adaptou bem, mostrando-se confortável e participativa na maioria das situações escolares.',
            'A integração ao ambiente escolar foi boa, com a criança demonstrando disposição para aprender e conviver.',
            'A criança aceitou bem as mudanças, participando das propostas pedagógicas e interagindo de forma respeitosa.',
            'A adaptação foi positiva, com a criança se mostrando cada vez mais à vontade na escola.',
            'A criança apresentou uma boa adaptação, superando eventuais desafios iniciais com o apoio da equipe.'
        ],
        'Regular': [
            'A adaptação da criança foi regular, alternando momentos de participação ativa com outros de maior reserva. Em algumas situações, demonstrou certa hesitação diante de novas experiências, mas, gradualmente, foi se ajustando à rotina escolar. O acompanhamento próximo dos educadores tem sido fundamental para promover avanços nesse processo.',
            'A criança apresentou uma adaptação intermediária, participando de algumas atividades, mas ainda demonstrando certa timidez em outras.',
            'O processo de adaptação foi oscilante, com a criança alternando entre envolvimento e momentos de retraimento.',
            'A adaptação ocorreu de forma moderada, sendo necessário incentivo extra para que a criança se sentisse mais segura.',
            'A criança mostrou-se um pouco reservada no início, mas vem progredindo gradualmente na integração com o grupo.',
            'A adaptação foi razoável, com a criança participando das atividades, porém ainda buscando mais confiança.',
            'A criança está em processo de adaptação, apresentando avanços, mas ainda necessitando de apoio em algumas situações.',
            'A integração ao ambiente escolar foi regular, com a criança demonstrando interesse, mas também certa insegurança.',
            'A criança alterna entre momentos de participação ativa e outros de observação, indicando uma adaptação em andamento.',
            'A adaptação está ocorrendo de forma gradual, com a criança se mostrando cada vez mais aberta às experiências escolares.'
        ],
        'Mal': [
            'A adaptação da criança apresentou dificuldades. Mostrou resistência a algumas atividades e certa dificuldade para se integrar ao grupo, necessitando de apoio constante dos educadores. Recomenda-se a continuidade do acompanhamento individualizado para favorecer sua inclusão e bem-estar.',
            'A criança encontrou obstáculos no processo de adaptação, demonstrando resistência e pouca participação nas atividades.',
            'A adaptação foi difícil, com a criança apresentando dificuldades para se enturmar e aceitar as rotinas escolares.',
            'A criança mostrou-se pouco receptiva ao novo ambiente, necessitando de acompanhamento próximo para superar os desafios.',
            'O processo de adaptação foi marcado por insegurança e pouca interação com o grupo.',
            'A criança apresentou resistência às mudanças, participando pouco das propostas pedagógicas.',
            'A adaptação foi complicada, exigindo estratégias diferenciadas para promover o bem-estar da criança.',
            'A criança demonstrou dificuldades em se adaptar, sendo importante o apoio da equipe escolar e da família.',
            'A integração ao ambiente escolar foi limitada, com a criança preferindo manter-se isolada em diversas situações.',
            'A criança apresentou uma adaptação difícil, necessitando de acompanhamento individualizado e constante.'
        ],
        'Muito mal': [
            'A adaptação da criança foi bastante difícil, exigindo atenção especial da equipe escolar. Demonstrou grande resistência às mudanças e pouca disposição para participar das atividades, sendo fundamental o envolvimento da família e da equipe pedagógica para promover avanços nesse processo.',
            'A criança enfrentou sérias dificuldades de adaptação, recusando-se a participar das atividades e interagir com o grupo.',
            'O processo de adaptação foi extremamente desafiador, com a criança apresentando grande resistência ao novo ambiente.',
            'A criança mostrou-se totalmente avessa às rotinas escolares, necessitando de acompanhamento intensivo.',
            'A adaptação foi marcada por isolamento e recusa em participar das propostas pedagógicas.',
            'A criança não conseguiu se integrar ao grupo, demonstrando desconforto e insegurança constantes.',
            'A adaptação foi muito difícil, exigindo intervenções frequentes da equipe escolar.',
            'A criança apresentou grande resistência ao ambiente escolar, sendo fundamental o apoio da família.',
            'O processo de adaptação foi marcado por desafios significativos, com a criança evitando o contato com colegas e professores.',
            'A criança não se adaptou ao ambiente escolar, necessitando de estratégias específicas para promover sua inclusão.'
        ]
    },
    2: {
        'Extrovertida': [
            'A criança é extrovertida, interagindo facilmente com todos e participando ativamente das atividades coletivas.',
            'Demonstra espontaneidade e alegria ao se comunicar, buscando sempre o contato com colegas e adultos.',
            'Sua personalidade extrovertida contribui para um ambiente animado e acolhedor na sala de aula.',
            'Mostra-se aberta a novas amizades, envolvendo-se com entusiasmo nas dinâmicas do grupo.',
            'A criança se destaca pela facilidade em se expressar e pela disposição em colaborar com os demais.',
            'Participa de todas as atividades com energia, incentivando os colegas a se envolverem também.',
            'Sua extroversão favorece a construção de vínculos positivos e o clima de integração na turma.',
            'Demonstra iniciativa para propor brincadeiras e interagir em diferentes contextos.',
            'A criança é comunicativa, expressando suas ideias e sentimentos com clareza.',
            'Sua postura extrovertida inspira confiança e aproximação dos colegas.'
        ],
        'Introvertida': [
            'A criança apresenta uma personalidade introvertida, preferindo atividades mais reservadas e interações em pequenos grupos.',
            'Observa atentamente o ambiente antes de se envolver, participando de forma significativa quando se sente segura.',
            'Prefere momentos de introspecção, demonstrando sensibilidade e atenção aos detalhes.',
            'Sua introversão é respeitada, permitindo que se expresse no seu próprio tempo.',
            'A criança se sente mais confortável em ambientes tranquilos e com poucos colegas.',
            'Participa das atividades de forma discreta, mas com qualidade e dedicação.',
            'Demonstra preferência por brincadeiras individuais ou em duplas.',
            'Sua postura reservada contribui para um ambiente de respeito e escuta.',
            'A criança valoriza o silêncio e a observação, enriquecendo o grupo com sua percepção.',
            'Com apoio, vai se integrando gradualmente às dinâmicas coletivas.'
        ],
        'Sociável': [
            'A criança é sociável, interagindo bem com colegas e adultos em diferentes situações.',
            'Demonstra facilidade para fazer amizades e se adaptar a novos grupos.',
            'Participa de brincadeiras em grupo, compartilhando materiais e ideias.',
            'Sua sociabilidade contribui para um ambiente harmonioso e colaborativo.',
            'Mostra-se disponível para ajudar os outros e acolher novos colegas.',
            'A criança gosta de conversar e trocar experiências com todos ao redor.',
            'Sua postura amigável favorece a integração e o respeito mútuo.',
            'Demonstra empatia e interesse pelo bem-estar dos colegas.',
            'Participa ativamente das rodas de conversa e atividades coletivas.',
            'Sua sociabilidade é um exemplo positivo para o grupo.'
        ],
        'Tímida': [
            'A criança demonstra certa timidez, necessitando de estímulos para se integrar aos grupos.',
            'Em situações novas, tende a se mostrar reservada, mas, com apoio, vai se soltando gradualmente.',
            'Prefere observar antes de participar, buscando segurança no ambiente.',
            'Sua timidez é respeitada, permitindo que se expresse no seu ritmo.',
            'A criança precisa de incentivo para interagir, mas responde bem ao acolhimento dos colegas.',
            'Demonstra sensibilidade e cuidado nas relações interpessoais.',
            'Com o tempo, vai ganhando confiança e ampliando sua participação.',
            'A timidez não impede que contribua de forma significativa para o grupo.',
            'Prefere atividades em pequenos grupos ou em dupla.',
            'Sua postura reservada é valorizada e respeitada por todos.'
        ],
        'Outros': [
            'A criança possui características singulares que enriquecem o convívio escolar.',
            'Sua individualidade traz novas perspectivas e experiências para o grupo.',
            'Demonstra traços únicos de personalidade, contribuindo para a diversidade da turma.',
            'A criança se destaca por suas particularidades, que são respeitadas e valorizadas.',
            'Sua presença agrega valor ao ambiente escolar, promovendo respeito às diferenças.',
            'Apresenta comportamentos e interesses próprios, enriquecendo as interações.',
            'A individualidade da criança é reconhecida e celebrada pela equipe escolar.',
            'Contribui com ideias e pontos de vista originais nas atividades.',
            'Sua forma de ser inspira acolhimento e empatia entre os colegas.',
            'A criança é incentivada a expressar sua autenticidade em todas as situações.'
        ]
    },
    3: {
        'Gosta muito': [
            'Durante a roda rítmica, mostra entusiasmo e envolvimento, participando com alegria das músicas, movimentos e dinâmicas propostas.',
            'Demonstra grande interesse pela roda rítmica, engajando-se com energia nas atividades.',
            'A criança se destaca pelo entusiasmo nas rodas rítmicas, aproveitando cada momento.',
            'Participa com alegria e disposição das dinâmicas musicais e corporais.',
            'Mostra prazer em compartilhar os momentos de roda rítmica com o grupo.',
            'A criança se envolve profundamente nas atividades rítmicas, contribuindo para o clima positivo.',
            'Demonstra coordenação motora e ritmo durante as rodas rítmicas.',
            'Participa ativamente das músicas e movimentos, incentivando os colegas.',
            'A roda rítmica é um dos momentos preferidos da criança, que se entrega de corpo e alma.',
            'Sua participação nas rodas rítmicas é marcada por entusiasmo e alegria.'
        ],
        'Gosta': [
            'Participa da roda rítmica com interesse, acompanhando as atividades propostas e demonstrando boa disposição.',
            'A criança mostra-se receptiva às dinâmicas rítmicas, participando com satisfação.',
            'Demonstra envolvimento nas rodas rítmicas, aproveitando as músicas e movimentos.',
            'Participa das atividades rítmicas com boa vontade e atenção.',
            'A criança se integra bem às rodas rítmicas, acompanhando o grupo.',
            'Mostra-se motivada a participar das dinâmicas musicais e corporais.',
            'Acompanha as rodas rítmicas com interesse e respeito.',
            'Demonstra prazer em participar das atividades rítmicas da turma.',
            'A criança se envolve nas rodas rítmicas, contribuindo para o sucesso das atividades.',
            'Sua participação nas rodas rítmicas é positiva e constante.'
        ],
        'Regular': [
            'Participa da roda rítmica de forma regular, alternando momentos de envolvimento e distração.',
            'A criança apresenta participação oscilante nas rodas rítmicas.',
            'Em algumas ocasiões, precisa de incentivo para se engajar plenamente.',
            'Mostra interesse moderado pelas atividades rítmicas.',
            'Participa das rodas rítmicas, mas às vezes se dispersa.',
            'A criança alterna entre envolvimento e distração nas dinâmicas rítmicas.',
            'Sua participação nas rodas rítmicas é razoável, com momentos de maior e menor atenção.',
            'Demonstra interesse variável pelas atividades musicais e corporais.',
            'A criança participa das rodas rítmicas, mas nem sempre com o mesmo entusiasmo.',
            'Sua presença nas rodas rítmicas é constante, mas o envolvimento pode variar.'
        ],
        'Não gosta': [
            'Demonstra pouco interesse pela roda rítmica, participando apenas quando incentivada pelos educadores.',
            'A criança prefere outras atividades, mostrando desinteresse pelas rodas rítmicas.',
            'Participa das rodas rítmicas apenas quando estimulada.',
            'Mostra-se pouco motivada para as dinâmicas rítmicas.',
            'A criança raramente se envolve nas rodas rítmicas.',
            'Demonstra resistência às atividades musicais e corporais.',
            'Participa das rodas rítmicas de forma passiva.',
            'A criança precisa de incentivo extra para participar das rodas rítmicas.',
            'Mostra-se desinteressada pelas dinâmicas rítmicas da turma.',
            'Sua participação nas rodas rítmicas é limitada e pouco entusiasmada.'
        ],
        'Não participa': [
            'Não participa das atividades da roda rítmica, preferindo se dedicar a outras propostas ou observar os colegas.',
            'A criança opta por não participar das rodas rítmicas.',
            'Prefere observar as atividades rítmicas sem se envolver diretamente.',
            'A criança não demonstra interesse pelas rodas rítmicas.',
            'Evita participar das dinâmicas musicais e corporais.',
            'A criança se mantém afastada das rodas rítmicas.',
            'Não se envolve nas atividades rítmicas propostas.',
            'A criança prefere outras atividades em vez das rodas rítmicas.',
            'Sua ausência nas rodas rítmicas é frequente.',
            'A criança não participa das rodas rítmicas, mesmo quando incentivada.'
        ]
    },
    4: {
        'Come bem': [
            'A criança se alimenta bem na escola, demonstrando autonomia e interesse pelas refeições oferecidas.',
            'Mostra boa aceitação dos alimentos, servindo-se sozinha e respeitando os horários das refeições.',
            'Demonstra satisfação ao experimentar diferentes pratos e sabores.',
            'Participa das refeições com entusiasmo, contribuindo para um ambiente agradável.',
            'A alimentação é realizada de forma tranquila, com a criança mostrando-se independente.',
            'Aceita bem a variedade alimentar proposta pela escola.',
            'A criança aprecia as refeições, demonstrando hábitos saudáveis.',
            'Mostra-se aberta a novos alimentos, ampliando seu repertório alimentar.',
            'A criança se destaca pela autonomia e interesse durante as refeições.',
            'Sua alimentação na escola é equilibrada e satisfatória.'
        ],
        'Come razoavelmente': [
            'A alimentação na escola é razoável, com momentos de boa aceitação e outros de menor interesse.',
            'Em geral, aceita bem os alimentos, mas pode apresentar seletividade em algumas situações.',
            'A criança participa das refeições, mas nem sempre demonstra entusiasmo.',
            'Mostra aceitação variável dos alimentos oferecidos.',
            'A alimentação é realizada de forma adequada, com eventuais recusas.',
            'A criança aceita parte dos alimentos, recusando outros.',
            'Sua alimentação é satisfatória, mas pode melhorar em variedade.',
            'Demonstra interesse moderado pelas refeições escolares.',
            'A aceitação dos alimentos depende do cardápio do dia.',
            'A criança se alimenta de forma razoável, com momentos de maior e menor interesse.'
        ],
        'Come pouco': [
            'A criança se alimenta pouco na escola, sendo importante acompanhamento para garantir que suas necessidades nutricionais sejam atendidas.',
            'Apresenta seletividade e, por vezes, recusa parte das refeições.',
            'Mostra pouco interesse pelos alimentos oferecidos.',
            'A alimentação é realizada em pequenas quantidades.',
            'A criança precisa de incentivo para experimentar novos alimentos.',
            'Recusa parte das refeições, preferindo alimentos específicos.',
            'A alimentação é limitada, exigindo atenção da equipe escolar.',
            'Demonstra apetite reduzido durante as refeições.',
            'A criança come pouco, sendo importante o acompanhamento nutricional.',
            'Sua alimentação na escola é restrita, com baixa aceitação dos alimentos.'
        ],
        'Não come': [
            'A criança não se alimenta na escola, exigindo atenção especial da equipe.',
            'Recusa todas as refeições oferecidas, preferindo não comer durante o período escolar.',
            'Não demonstra interesse pelos alimentos servidos na escola.',
            'A alimentação não é realizada, sendo necessário diálogo com a família.',
            'A criança não aceita nenhum alimento durante as refeições.',
            'Apresenta recusa total dos alimentos escolares.',
            'A alimentação não ocorre na escola, exigindo estratégias diferenciadas.',
            'A criança não participa das refeições, mantendo-se afastada do refeitório.',
            'Não se alimenta no ambiente escolar, sendo importante investigar as causas.',
            'A recusa alimentar é constante, necessitando acompanhamento especializado.'
        ]
    },
    5: {
        'Muito bem': [
            'Nas brincadeiras nos parques, a criança interage muito bem, apresentando boa motricidade.',
            'Demonstra estar à vontade nos espaços externos, envolvendo-se nas atividades de forma positiva.',
            'Mostra iniciativa para propor brincadeiras e respeita as regras estabelecidas.',
            'A criança se destaca pela participação ativa nas brincadeiras ao ar livre.',
            'Interage com todos os colegas, promovendo um ambiente de cooperação.',
            'Demonstra habilidades motoras e sociais durante as atividades no parque.',
            'A criança aproveita ao máximo as oportunidades de brincar nos espaços externos.',
            'Participa das brincadeiras com entusiasmo e alegria.',
            'Mostra-se confiante e segura durante as atividades no parque.',
            'Sua participação nas brincadeiras externas é exemplar e positiva.'
        ],
        'Bem': [
            'Brinca nos parques com desenvoltura, participando das atividades propostas.',
            'Interage de forma harmoniosa com os colegas durante as brincadeiras.',
            'Demonstra boa coordenação motora e disposição para explorar diferentes brinquedos.',
            'A criança participa das atividades externas com interesse.',
            'Mostra-se motivada a brincar nos espaços ao ar livre.',
            'A integração nas brincadeiras do parque é boa, com envolvimento constante.',
            'Demonstra satisfação ao participar das atividades externas.',
            'A criança se envolve nas brincadeiras, respeitando os colegas.',
            'Participa das atividades no parque com alegria e respeito.',
            'Sua participação nas brincadeiras ao ar livre é positiva e frequente.'
        ],
        'Regular': [
            'Participa das brincadeiras nos parques de forma regular, alternando momentos de maior e menor envolvimento.',
            'Em algumas situações, prefere observar ou brincar sozinha.',
            'Quando estimulada, integra-se ao grupo nas atividades externas.',
            'A criança apresenta participação oscilante nas brincadeiras ao ar livre.',
            'Mostra interesse moderado pelas atividades no parque.',
            'A participação nas brincadeiras externas é razoável, com momentos de maior e menor envolvimento.',
            'Demonstra preferência por algumas brincadeiras específicas.',
            'A criança alterna entre brincar com o grupo e momentos de introspecção.',
            'Sua participação nas atividades externas é variável.',
            'A integração nas brincadeiras do parque ocorre de forma gradual.'
        ],
        'Mal': [
            'Apresenta dificuldades nas brincadeiras nos parques, seja por questões de motricidade ou interação social.',
            'Prefere atividades mais tranquilas, evitando brincadeiras em grupo.',
            'A criança demonstra resistência às atividades externas.',
            'Participa pouco das brincadeiras ao ar livre, necessitando incentivo.',
            'Mostra-se insegura durante as atividades no parque.',
            'A participação nas brincadeiras externas é limitada.',
            'Demonstra pouca disposição para interagir com os colegas no parque.',
            'A criança evita as atividades mais movimentadas.',
            'Sua participação nas brincadeiras ao ar livre é restrita.',
            'A integração nas atividades externas é dificultada por questões motoras ou sociais.'
        ],
        'Muito mal': [
            'Demonstra grande resistência ou desinteresse pelas brincadeiras nos parques.',
            'Evita o contato com os colegas e os brinquedos durante as atividades externas.',
            'A criança não participa das brincadeiras ao ar livre.',
            'Mostra-se isolada durante as atividades no parque.',
            'Recusa-se a brincar nos espaços externos, mesmo quando incentivada.',
            'A participação nas brincadeiras externas é inexistente.',
            'Demonstra desinteresse total pelas atividades ao ar livre.',
            'A criança se mantém afastada das brincadeiras no parque.',
            'Não interage com os colegas durante as atividades externas.',
            'Sua ausência nas brincadeiras ao ar livre é constante.'
        ]
    },
    6: {
        'Com facilidade': [
            'Durante a realização das atividades pedagógicas, demonstra facilidade e boa disposição, realizando as propostas sem resistência.',
            'A criança executa as tarefas com autonomia e interesse, mostrando-se aberta a diferentes estímulos.',
            'Participa das atividades com entusiasmo, sem apresentar dificuldades significativas.',
            'Realiza as propostas pedagógicas de forma eficiente e colaborativa.',
            'Demonstra segurança e desenvoltura ao realizar as atividades escolares.',
            'A criança se destaca pela facilidade em compreender e executar as tarefas.',
            'Mostra-se motivada e engajada durante as atividades pedagógicas.',
            'Cumpre as atividades propostas com dedicação e alegria.',
            'A criança realiza as tarefas com rapidez e qualidade.',
            'Sua participação nas atividades pedagógicas é marcada por facilidade e envolvimento.'
        ],
        'Com alguma dificuldade': [
            'Realiza as atividades com alguma dificuldade, necessitando de apoio dos educadores para compreender as propostas.',
            'A criança apresenta desafios pontuais na execução das tarefas.',
            'Participa das atividades, mas requer incentivo e orientação.',
            'Demonstra interesse, porém encontra obstáculos em algumas propostas.',
            'A criança precisa de acompanhamento para superar certas dificuldades.',
            'Realiza as tarefas com esforço, mas consegue avançar com apoio.',
            'Mostra-se disposta a aprender, mesmo diante das dificuldades.',
            'A criança apresenta progresso gradativo nas atividades pedagógicas.',
            'Necessita de explicações adicionais para compreender algumas tarefas.',
            'Com acompanhamento, apresenta avanços nas atividades escolares.'
        ],
        'Com muita dificuldade': [
            'Enfrenta muitas dificuldades para realizar as atividades, demonstrando resistência ou desinteresse.',
            'A criança apresenta grande desafio na execução das tarefas pedagógicas.',
            'Participa pouco das atividades, necessitando de acompanhamento individualizado.',
            'Demonstra desmotivação e resistência diante das propostas escolares.',
            'A criança encontra obstáculos frequentes para realizar as tarefas.',
            'Mostra-se insegura e pouco confiante durante as atividades.',
            'A participação nas atividades pedagógicas é limitada por dificuldades de compreensão.',
            'Necessita de apoio constante para realizar as tarefas escolares.',
            'A criança apresenta baixo rendimento nas atividades propostas.',
            'O acompanhamento individualizado é fundamental para promover seu desenvolvimento.'
        ],
        'Não participa': [
            'Não participa das atividades pedagógicas, recusando-se a realizar as propostas.',
            'A criança opta por não se envolver nas tarefas escolares.',
            'Recusa-se a participar das atividades, mesmo quando incentivada.',
            'Mostra desinteresse total pelas propostas pedagógicas.',
            'A criança se mantém afastada das atividades escolares.',
            'Não realiza as tarefas propostas, preferindo outras atividades.',
            'A participação nas atividades pedagógicas é inexistente.',
            'A criança não se envolve nas propostas da equipe escolar.',
            'Evita qualquer tipo de atividade pedagógica durante o período escolar.',
            'Sua ausência nas atividades pedagógicas é constante.'
        ]
    },
    7: {
        'Rabisco desordenado': [
            'Quanto ao grafismo, encontra-se na fase de rabisco desordenado, o que é esperado para a sua faixa etária.',
            'A criança realiza rabiscos sem controle definido, explorando o espaço do papel livremente.',
            'Os desenhos apresentam traços soltos e desorganizados, típicos do início do desenvolvimento gráfico.',
            'Demonstra interesse em desenhar, mesmo que de forma desordenada.',
            'O grafismo é marcado por linhas aleatórias e sem intenção clara.',
            'A criança experimenta diferentes movimentos com o lápis, sem preocupação com formas.',
            'Os rabiscos são espontâneos e refletem a fase inicial da expressão gráfica.',
            'A produção gráfica é caracterizada por traços dispersos e sem direção definida.',
            'A criança explora o papel com liberdade, sem buscar representar objetos específicos.',
            'O rabisco desordenado é uma etapa importante para o desenvolvimento da coordenação motora fina.'
        ],
        'Rabisco ordenado': [
            'Apresenta grafismo na fase de rabisco ordenado, demonstrando evolução no controle dos traços.',
            'Os desenhos mostram linhas mais controladas e intencionais.',
            'A criança começa a organizar os traços no espaço do papel.',
            'O grafismo apresenta repetição de movimentos e padrões.',
            'Demonstra maior domínio do lápis ao desenhar.',
            'Os rabiscos são mais regulares e seguem uma direção.',
            'A criança busca preencher o papel de forma mais estruturada.',
            'O rabisco ordenado indica avanço na coordenação motora.',
            'Os desenhos apresentam simetria e repetição de formas.',
            'A criança demonstra intenção ao realizar os traços.'
        ],
        'Rabisco nomeado': [
            'Está na fase de rabisco nomeado, atribuindo significados aos seus desenhos.',
            'A criança começa a dar nomes aos rabiscos, relacionando-os a objetos ou pessoas.',
            'Os desenhos passam a ter sentido para a criança, mesmo que não sejam reconhecíveis.',
            'Demonstra criatividade ao explicar o que representa em seus rabiscos.',
            'O grafismo é acompanhado de narrativas sobre o que foi desenhado.',
            'A criança associa histórias aos seus desenhos, enriquecendo a produção gráfica.',
            'Os rabiscos ganham significado simbólico no universo infantil.',
            'Atribui nomes e funções aos traços realizados no papel.',
            'A criança compartilha com os colegas o que desenhou, estimulando a comunicação.',
            'O rabisco nomeado marca o início da representação simbólica no desenho.'
        ],
        'Pré-esquemático': [
            'Encontra-se na fase pré-esquemática, representando objetos e pessoas de forma mais estruturada.',
            'A criança começa a desenhar formas que lembram figuras conhecidas.',
            'Os desenhos apresentam elementos reconhecíveis, como círculos e linhas para pessoas.',
            'Demonstra intenção de representar o mundo ao seu redor.',
            'O grafismo evolui para formas mais organizadas e com significado.',
            'A criança experimenta diferentes maneiras de desenhar objetos.',
            'Os desenhos mostram tentativas de representar cenas do cotidiano.',
            'A produção gráfica é marcada por avanços na percepção visual.',
            'A criança busca detalhes ao desenhar pessoas e objetos.',
            'O pré-esquemático é uma etapa de transição para o desenho mais elaborado.'
        ],
        'Esquemático': [
            'Apresenta grafismo esquemático, com desenhos bem definidos e riqueza de detalhes.',
            'A criança representa pessoas e objetos com formas claras e proporcionais.',
            'Os desenhos mostram organização espacial e uso de diferentes elementos.',
            'Demonstra domínio da coordenação motora fina ao desenhar.',
            'A produção gráfica é detalhada e estruturada.',
            'A criança utiliza cores e formas para enriquecer os desenhos.',
            'Os esquemas gráficos são repetidos com variações criativas.',
            'O desenho esquemático reflete avanços na percepção e expressão visual.',
            'A criança representa cenas completas, com vários elementos.',
            'O grafismo esquemático indica maturidade no desenvolvimento do desenho.'
        ]
    },
    8: {
        'Sim': [
            'Já demonstra habilidades iniciais de alfabetização, como escrever o próprio nome, evidenciando consciência fonológica e motora.',
            'A criança consegue escrever seu nome, mostrando avanços importantes no processo de alfabetização.',
            'Demonstra capacidade de identificar e escrever o próprio nome, o que indica bom desenvolvimento.',
            'A escrita do nome próprio revela que a criança está desenvolvendo habilidades essenciais para a alfabetização.',
            'Mostra-se apta a escrever o próprio nome, sinalizando progresso na consciência fonológica.',
            'A criança já reconhece e escreve seu nome, o que é um marco importante para a idade.',
            'Demonstra domínio das letras do próprio nome, evidenciando interesse pela escrita.',
            'A escrita do nome próprio ocorre de forma espontânea, indicando maturidade no desenvolvimento.',
            'A criança apresenta boa coordenação motora ao escrever o próprio nome.',
            'Já consegue escrever o nome, mostrando interesse e envolvimento nas atividades de alfabetização.'
        ],
        'Não': [
            'Ainda não escreve o próprio nome, o que é esperado para a faixa etária.',
            'A criança está em processo de reconhecimento das letras do próprio nome.',
            'Não demonstra ainda habilidade para escrever o nome, mas participa das atividades propostas.',
            'O estímulo contínuo e atividades lúdicas contribuirão para o desenvolvimento dessa habilidade.',
            'Ainda não apresenta domínio das letras do nome, sendo importante o acompanhamento.',
            'A criança necessita de mais tempo e incentivo para escrever o próprio nome.',
            'Não escreve o nome, mas demonstra interesse em aprender.',
            'O processo de alfabetização está em andamento, sendo natural não escrever o nome nesta fase.',
            'Ainda não reconhece todas as letras do nome, mas participa das atividades de escrita.',
            'A criança está sendo estimulada a escrever o nome, respeitando seu tempo de aprendizagem.'
        ]
    },
    9: {
        'Sim': [
            'Identifica algumas letras, demonstrando interesse pelo universo da leitura e escrita.',
            'A criança reconhece letras do alfabeto, o que é importante para o processo de alfabetização.',
            'Demonstra curiosidade e capacidade de identificar letras em diferentes contextos.',
            'O reconhecimento de letras indica avanço no desenvolvimento da linguagem escrita.',
            'A criança aponta e nomeia letras, mostrando envolvimento nas atividades de leitura.',
            'Identifica letras em palavras do cotidiano, evidenciando progresso.',
            'Demonstra interesse em aprender novas letras e sons.',
            'A identificação de letras ocorre de forma espontânea em atividades lúdicas.',
            'A criança reconhece letras do próprio nome e de colegas.',
            'Mostra-se motivada a aprender o alfabeto, identificando letras com facilidade.'
        ],
        'Não': [
            'Ainda não identifica letras, o que é natural para a idade.',
            'A criança está em processo de reconhecimento das letras do alfabeto.',
            'Não demonstra ainda habilidade para identificar letras, mas participa das atividades.',
            'O contato frequente com livros e jogos favorecerá o desenvolvimento dessa habilidade.',
            'Ainda não reconhece letras, sendo importante o estímulo contínuo.',
            'A criança necessita de mais tempo para identificar letras.',
            'Não identifica letras, mas demonstra interesse em atividades de leitura.',
            'O processo de reconhecimento de letras está em andamento.',
            'Ainda não aponta ou nomeia letras, mas participa das propostas pedagógicas.',
            'A criança está sendo incentivada a identificar letras, respeitando seu ritmo.'
        ]
    },
    10: {
        'Sim': [
            'Conta e identifica números, demonstrando bom desenvolvimento das noções matemáticas.',
            'A criança reconhece e nomeia números, evidenciando raciocínio lógico.',
            'Demonstra capacidade de contar objetos e identificar numerais.',
            'O reconhecimento de números indica avanço no desenvolvimento cognitivo.',
            'A criança participa de atividades de contagem com interesse.',
            'Identifica números em diferentes contextos, mostrando envolvimento.',
            'Demonstra interesse em aprender novos números e quantidades.',
            'A identificação de números ocorre de forma espontânea em jogos e brincadeiras.',
            'A criança reconhece números do cotidiano, como idade e quantidade de objetos.',
            'Mostra-se motivada a aprender matemática, contando e identificando números.'
        ],
        'Não': [
            'Ainda não conta ou identifica números, o que é esperado para a faixa etária.',
            'A criança está em processo de reconhecimento dos números.',
            'Não demonstra ainda habilidade para contar ou identificar números.',
            'O estímulo por meio de jogos e atividades lúdicas contribuirá para o desenvolvimento dessa habilidade.',
            'Ainda não apresenta domínio dos numerais, sendo importante o acompanhamento.',
            'A criança necessita de mais tempo e incentivo para contar e identificar números.',
            'Não conta ou identifica números, mas demonstra interesse em aprender.',
            'O processo de aprendizagem dos números está em andamento.',
            'Ainda não reconhece números, mas participa das atividades de matemática.',
            'A criança está sendo estimulada a contar e identificar números, respeitando seu tempo.'
        ]
    },
    11: {
        'Sim': [
            'Participa das aulas de capoeira, demonstrando interesse e envolvimento nas atividades corporais e musicais propostas.',
            'A criança se envolve nas aulas de capoeira, participando com entusiasmo das atividades.',
            'Demonstra interesse pelas aulas de capoeira, integrando-se ao grupo com facilidade.',
            'A participação nas aulas de capoeira é marcada por alegria e disposição.',
            'A criança aproveita as oportunidades de aprender novos movimentos na capoeira.',
            'Mostra-se motivada a participar das atividades de capoeira, desenvolvendo habilidades corporais.',
            'A criança interage com os colegas durante as aulas de capoeira, promovendo integração.',
            'Demonstra evolução nas atividades de capoeira, aprendendo novos movimentos.',
            'A participação nas aulas de capoeira contribui para o desenvolvimento motor e musical.',
            'A criança demonstra envolvimento e respeito durante as aulas de capoeira.'
        ],
        'Não': [
            'Não participa das aulas de capoeira, preferindo outras atividades. Recomenda-se buscar estratégias para estimular sua participação.',
            'A criança não se envolve nas aulas de capoeira, mas demonstra interesse por outras atividades.',
            'Não participa das atividades de capoeira, porém observa os colegas com curiosidade.',
            'A participação nas aulas de capoeira ainda não foi consolidada, sendo importante o incentivo contínuo.',
            'A criança está em processo de adaptação às atividades de capoeira.',
            'Ainda não realiza as atividades de capoeira, mas mostra curiosidade pelas músicas e movimentos.',
            'O desenvolvimento da participação nas aulas de capoeira está em andamento, com avanços graduais.',
            'A criança precisa de apoio para participar das aulas de capoeira, o que é natural para a idade.',
            'Não participa das aulas de capoeira, mas participa de outras atividades corporais.',
            'O estímulo à participação nas aulas de capoeira deve ser mantido para favorecer o desenvolvimento.'
        ]
    },
    12: {
        'Sim': [
            'Participa do momento de Euritimia, acompanhando os movimentos e músicas com atenção e interesse.',
            'A criança se envolve nas atividades de Euritimia, participando com entusiasmo.',
            'Demonstra interesse pelo momento de Euritimia, integrando-se ao grupo com facilidade.',
            'A participação nas atividades de Euritimia é marcada por alegria e disposição.',
            'A criança aproveita as oportunidades de aprender novos movimentos na Euritimia.',
            'Mostra-se motivada a participar das atividades de Euritimia, desenvolvendo habilidades corporais.',
            'A criança interage com os colegas durante o momento de Euritimia, promovendo integração.',
            'Demonstra evolução nas atividades de Euritimia, aprendendo novos movimentos.',
            'A participação no momento de Euritimia contribui para o desenvolvimento motor e musical.',
            'A criança demonstra envolvimento e respeito durante o momento de Euritimia.'
        ],
        'Não': [
            'Não participa do momento de Euritimia, preferindo outras atividades. O estímulo contínuo pode favorecer sua integração.',
            'A criança não se envolve nas atividades de Euritimia, mas demonstra interesse por outras atividades.',
            'Não participa do momento de Euritimia, porém observa os colegas com curiosidade.',
            'A participação nas atividades de Euritimia ainda não foi consolidada, sendo importante o incentivo contínuo.',
            'A criança está em processo de adaptação às atividades de Euritimia.',
            'Ainda não realiza as atividades de Euritimia, mas mostra curiosidade pelas músicas e movimentos.',
            'O desenvolvimento da participação no momento de Euritimia está em andamento, com avanços graduais.',
            'A criança precisa de apoio para participar das atividades de Euritimia, o que é natural para a idade.',
            'Não participa do momento de Euritimia, mas participa de outras atividades corporais.',
            'O estímulo à participação nas atividades de Euritimia deve ser mantido para favorecer o desenvolvimento.'
        ]
    },
    13: {
        'Participa com interesse dos momentos de leitura, ouvindo com atenção as histórias contadas.': [
            'Durante os momentos na sala de leitura, mostra-se bastante interessada, ouvindo as histórias com atenção e curiosidade. Demonstra envolvimento e respeito pelo momento de escuta, aproveitando ao máximo as oportunidades de contato com a literatura.',
            'A criança participa com interesse dos momentos de leitura, ouvindo atentamente as histórias.',
            'Demonstra envolvimento durante as atividades de leitura, aproveitando as oportunidades de escuta.',
            'Mostra-se curiosa e atenta durante as histórias contadas na sala de leitura.',
            'A participação nos momentos de leitura é marcada por atenção e respeito.',
            'A criança aproveita ao máximo as oportunidades de contato com a literatura.',
            'Demonstra alegria e envolvimento durante os momentos na sala de leitura.',
            'A criança valoriza o momento de escuta, participando ativamente das atividades de leitura.',
            'Mostra interesse em ouvir novas histórias, ampliando seu repertório literário.',
            'A participação nos momentos de leitura contribui para o desenvolvimento da linguagem.'
        ],
        'Demonstra curiosidade pelos livros e gosta de observar as ilustrações.': [
            'Demonstra curiosidade pelos livros, aprecia observar as ilustrações e explora diferentes títulos de forma autônoma, ampliando seu repertório cultural.',
            'A criança gosta de observar as ilustrações dos livros, mostrando interesse pela leitura.',
            'Demonstra curiosidade ao explorar diferentes títulos e autores.',
            'Aprecia manusear os livros, observando detalhes das imagens.',
            'A criança explora os livros de forma autônoma, ampliando seu repertório cultural.',
            'Mostra interesse em conhecer novas histórias por meio das ilustrações.',
            'Demonstra envolvimento ao observar as imagens dos livros.',
            'A criança valoriza o contato com os livros, apreciando as ilustrações.',
            'Mostra curiosidade em descobrir novos livros e autores.',
            'A apreciação das ilustrações contribui para o desenvolvimento da imaginação.'
        ],
        'Interage com os colegas comentando sobre os personagens e enredos.': [
            'Interage com os colegas durante as rodas de conversa, comentando sobre personagens e enredos, o que contribui para o desenvolvimento da oralidade e do pensamento crítico.',
            'A criança compartilha suas impressões sobre as histórias com os colegas.',
            'Demonstra interesse em conversar sobre personagens e enredos após a leitura.',
            'Participa das rodas de conversa, enriquecendo o debate coletivo.',
            'A interação com os colegas contribui para o desenvolvimento da oralidade.',
            'Mostra-se motivada a discutir as histórias lidas com o grupo.',
            'A criança valoriza o momento de troca de ideias sobre as leituras.',
            'Demonstra envolvimento ao comentar sobre personagens e enredos.',
            'A participação nas rodas de conversa amplia o repertório literário.',
            'A criança contribui para o desenvolvimento do pensamento crítico ao debater as histórias.'
        ],
        'Reconta as histórias com suas próprias palavras, demonstrando compreensão.': [
            'Reconta as histórias com suas próprias palavras, evidenciando compreensão dos textos e criatividade na elaboração de novas narrativas.',
            'A criança demonstra habilidade ao recontar histórias, mostrando compreensão e criatividade.',
            'Reconta as histórias lidas, utilizando sua própria linguagem.',
            'Demonstra compreensão dos textos ao recontar as histórias.',
            'A criança cria novas narrativas a partir das histórias lidas.',
            'Mostra-se motivada a compartilhar suas versões das histórias.',
            'A criatividade é evidenciada ao recontar as histórias com suas próprias palavras.',
            'Demonstra envolvimento ao criar novas narrativas a partir das leituras.',
            'A criança valoriza o momento de recontar histórias, ampliando o repertório literário.',
            'A participação nas atividades de recontar histórias contribui para o desenvolvimento da linguagem.'
        ],
        'Participa das rodas de conversa após a leitura, expressando suas preferências.': [
            'Participa das rodas de conversa após a leitura, expressando suas preferências e opiniões, o que enriquece o debate coletivo.',
            'A criança compartilha suas preferências literárias com o grupo.',
            'Demonstra interesse em expressar opiniões sobre as histórias lidas.',
            'Participa ativamente das rodas de conversa, enriquecendo o debate coletivo.',
            'A expressão de preferências contribui para o desenvolvimento da autonomia.',
            'Mostra-se motivada a debater sobre as leituras realizadas.',
            'A criança valoriza o momento de troca de opiniões sobre as histórias.',
            'Demonstra envolvimento ao expressar suas preferências literárias.',
            'A participação nas rodas de conversa amplia o repertório literário.',
            'A criança contribui para o desenvolvimento do pensamento crítico ao debater as histórias.'
        ],
        'Escolhe livros de forma autônoma e manuseia com cuidado.': [
            'Escolhe livros de forma autônoma, manuseando-os com cuidado e demonstrando responsabilidade pelo material escolar.',
            'A criança seleciona livros de acordo com seus interesses, mostrando autonomia.',
            'Demonstra responsabilidade ao manusear os livros da sala de leitura.',
            'A escolha autônoma de livros contribui para o desenvolvimento da autonomia.',
            'Mostra-se motivada a explorar diferentes títulos de forma independente.',
            'A criança valoriza o contato com os livros, cuidando do material escolar.',
            'Demonstra envolvimento ao escolher livros de forma autônoma.',
            'A seleção de livros é realizada com cuidado e responsabilidade.',
            'A criança amplia seu repertório literário ao escolher livros de forma independente.',
            'A participação nas atividades de escolha de livros contribui para o desenvolvimento da autonomia.'
        ],
        'Representa as histórias por meio de desenhos e dramatizações.': [
            'Representa as histórias lidas por meio de desenhos e dramatizações, integrando diferentes linguagens e ampliando sua expressão artística.',
            'A criança utiliza o desenho para representar as histórias lidas.',
            'Demonstra criatividade ao dramatizar as histórias na sala de leitura.',
            'A representação das histórias por meio de desenhos contribui para o desenvolvimento artístico.',
            'Mostra-se motivada a criar dramatizações a partir das leituras.',
            'A criança valoriza o momento de expressão artística após a leitura.',
            'Demonstra envolvimento ao representar as histórias por meio de diferentes linguagens.',
            'A participação nas atividades de dramatização amplia o repertório literário.',
            'A criança contribui para o desenvolvimento da expressão artística ao representar as histórias.',
            'A criatividade é evidenciada ao criar desenhos e dramatizações a partir das leituras.'
        ],
        'Demonstra alegria e envolvimento durante os momentos na sala de leitura.': [
            'Demonstra alegria e envolvimento durante os momentos na sala de leitura, tornando esse espaço ainda mais significativo para o grupo.',
            'A criança participa com entusiasmo das atividades na sala de leitura.',
            'Demonstra satisfação ao ouvir histórias e participar das atividades literárias.',
            'A alegria é evidenciada durante os momentos de leitura em grupo.',
            'Mostra-se motivada a participar das atividades na sala de leitura.',
            'A criança valoriza o momento de leitura, demonstrando envolvimento.',
            'Demonstra interesse em compartilhar momentos de leitura com os colegas.',
            'A participação nas atividades de leitura contribui para o desenvolvimento da linguagem.',
            'A criança amplia seu repertório literário ao participar das atividades na sala de leitura.',
            'A alegria e o envolvimento são marcas dos momentos na sala de leitura.'
        ]
    },
    14: {
        'Participou ativamente do projeto, mostrando interesse pelas histórias.': [
            'Participou ativamente do projeto Histórias Viajantes, revelando envolvimento, curiosidade e interesse pelo universo literário. Compartilhou suas experiências com os colegas e contribuiu para o sucesso da proposta.',
            'A criança se envolveu com entusiasmo no projeto Histórias Viajantes.',
            'Demonstra interesse pelas histórias do projeto, participando ativamente das atividades.',
            'A participação no projeto Histórias Viajantes é marcada por curiosidade e envolvimento.',
            'A criança compartilha suas experiências literárias com os colegas.',
            'Mostra-se motivada a participar das atividades do projeto.',
            'A criança valoriza o contato com novas histórias por meio do projeto.',
            'Demonstra envolvimento ao ouvir e compartilhar histórias do projeto.',
            'A participação no projeto contribui para o desenvolvimento do gosto pela leitura.',
            'A criança amplia seu repertório literário ao participar do projeto Histórias Viajantes.'
        ],
        'Participou de forma passiva, ouvindo as histórias contadas.': [
            'Participou do projeto Histórias Viajantes de forma passiva, ouvindo as histórias contadas e demonstrando respeito pelo momento de leitura.',
            'A criança acompanhou as atividades do projeto de forma mais reservada.',
            'Demonstra interesse em ouvir as histórias, mesmo que de forma passiva.',
            'A participação no projeto Histórias Viajantes é marcada por escuta atenta.',
            'A criança valoriza o momento de ouvir histórias do projeto.',
            'Mostra-se motivada a participar das atividades de leitura, mesmo que de forma passiva.',
            'A criança amplia seu repertório literário ao ouvir histórias do projeto.',
            'Demonstra envolvimento ao ouvir as histórias contadas no projeto.',
            'A participação no projeto contribui para o desenvolvimento do gosto pela leitura.',
            'A criança valoriza o contato com novas histórias por meio do projeto, mesmo que de forma passiva.'
        ],
        'Não participou do projeto.': [
            'Não participou do projeto Histórias Viajantes, preferindo outras atividades. Recomenda-se buscar estratégias para estimular seu interesse pela leitura.',
            'A criança não se envolveu nas atividades do projeto, mas demonstra interesse por outras propostas.',
            'Não participou das atividades do projeto, porém observa os colegas com curiosidade.',
            'A participação no projeto Histórias Viajantes ainda não foi consolidada, sendo importante o incentivo contínuo.',
            'A criança está em processo de adaptação às atividades do projeto.',
            'Ainda não realiza as atividades do projeto, mas mostra curiosidade pelas histórias.',
            'O desenvolvimento da participação no projeto está em andamento, com avanços graduais.',
            'A criança precisa de apoio para participar das atividades do projeto, o que é natural para a idade.',
            'Não participou do projeto, mas participa de outras atividades literárias.',
            'O estímulo à participação no projeto deve ser mantido para favorecer o desenvolvimento do gosto pela leitura.'
        ]
    },
    15: {
        'Brinca com os brinquedos': [
            'No momento de faz de conta, brinca com os brinquedos disponíveis, demonstrando criatividade e capacidade de se envolver em diferentes papéis e situações imaginárias.',
            'A criança utiliza os brinquedos para criar diferentes cenários durante o faz de conta.',
            'Demonstra criatividade ao brincar com os brinquedos disponíveis.',
            'A participação nas brincadeiras de faz de conta é marcada por envolvimento e imaginação.',
            'A criança valoriza o momento de brincar com os brinquedos, ampliando seu repertório lúdico.',
            'Mostra-se motivada a criar novas histórias durante o faz de conta.',
            'A criança amplia sua criatividade ao brincar com os brinquedos.',
            'Demonstra envolvimento ao criar diferentes papéis nas brincadeiras.',
            'A participação nas atividades de faz de conta contribui para o desenvolvimento da imaginação.',
            'A criança valoriza o momento de brincar com os brinquedos, demonstrando criatividade.'
        ],
        'É capaz de dividir': [
            'É capaz de dividir os brinquedos com os colegas, respeitando o espaço coletivo e promovendo a colaboração durante as brincadeiras.',
            'A criança compartilha os brinquedos com os colegas durante o faz de conta.',
            'Demonstra habilidade em dividir os brinquedos nas brincadeiras.',
            'A participação nas atividades de faz de conta é marcada por colaboração.',
            'A criança valoriza o momento de compartilhar os brinquedos com o grupo.',
            'Mostra-se motivada a dividir os brinquedos durante as brincadeiras.',
            'A criança amplia sua capacidade de colaboração ao dividir os brinquedos.',
            'Demonstra envolvimento ao compartilhar os brinquedos com os colegas.',
            'A participação nas atividades de faz de conta contribui para o desenvolvimento da colaboração.',
            'A criança valoriza o momento de dividir os brinquedos, promovendo a colaboração.'
        ],
        'Brinca sozinho': [
            'Prefere brincar sozinho durante o faz de conta, o que pode indicar necessidade de momentos de introspecção ou preferência por atividades individuais.',
            'A criança opta por brincar sozinha durante as atividades de faz de conta.',
            'Demonstra preferência por atividades individuais nas brincadeiras.',
            'A participação nas atividades de faz de conta é marcada por momentos de introspecção.',
            'A criança valoriza o momento de brincar sozinha, respeitando seu próprio ritmo.',
            'Mostra-se motivada a criar histórias de forma independente.',
            'A criança amplia sua criatividade ao brincar sozinha.',
            'Demonstra envolvimento ao criar diferentes cenários de forma individual.',
            'A participação nas atividades de faz de conta contribui para o desenvolvimento da autonomia.',
            'A criança valoriza o momento de brincar sozinha, demonstrando autonomia.'
        ],
        'Não participa': [
            'Não participa do momento de faz de conta, preferindo outras atividades. O estímulo à imaginação pode favorecer sua integração.',
            'A criança não se envolve nas atividades de faz de conta, mas demonstra interesse por outras propostas.',
            'Não participa das brincadeiras de faz de conta, porém observa os colegas com curiosidade.',
            'A participação nas atividades de faz de conta ainda não foi consolidada, sendo importante o incentivo contínuo.',
            'A criança está em processo de adaptação às atividades de faz de conta.',
            'Ainda não realiza as atividades de faz de conta, mas mostra curiosidade pelas brincadeiras.',
            'O desenvolvimento da participação nas atividades de faz de conta está em andamento, com avanços graduais.',
            'A criança precisa de apoio para participar das atividades de faz de conta, o que é natural para a idade.',
            'Não participa das atividades de faz de conta, mas participa de outras brincadeiras.',
            'O estímulo à participação nas atividades de faz de conta deve ser mantido para favorecer o desenvolvimento da imaginação.'
        ]
    },
    16: {
        'Ajuda sempre': [
            'Ao final das brincadeiras, ajuda sempre na organização dos brinquedos, demonstrando senso de responsabilidade e colaboração.',
            'A criança auxilia na organização dos brinquedos após as brincadeiras.',
            'Demonstra responsabilidade ao ajudar na arrumação dos brinquedos.',
            'A participação na organização dos brinquedos é marcada por colaboração.',
            'A criança valoriza o momento de ajudar na organização dos brinquedos.',
            'Mostra-se motivada a colaborar na arrumação dos brinquedos.',
            'A criança amplia seu senso de responsabilidade ao ajudar na organização.',
            'Demonstra envolvimento ao colaborar na arrumação dos brinquedos.',
            'A participação nas atividades de organização contribui para o desenvolvimento da responsabilidade.',
            'A criança valoriza o momento de ajudar na organização, promovendo a colaboração.'
        ],
        'Ajuda às vezes': [
            'Ajuda às vezes na organização dos brinquedos, principalmente quando incentivada pelos educadores.',
            'A criança auxilia na organização dos brinquedos em algumas ocasiões.',
            'Demonstra responsabilidade ao ajudar na arrumação dos brinquedos quando incentivada.',
            'A participação na organização dos brinquedos é marcada por colaboração ocasional.',
            'A criança valoriza o momento de ajudar na organização dos brinquedos quando estimulada.',
            'Mostra-se motivada a colaborar na arrumação dos brinquedos em algumas situações.',
            'A criança amplia seu senso de responsabilidade ao ajudar na organização quando incentivada.',
            'Demonstra envolvimento ao colaborar na arrumação dos brinquedos em algumas ocasiões.',
            'A participação nas atividades de organização contribui para o desenvolvimento da responsabilidade, mesmo que de forma ocasional.',
            'A criança valoriza o momento de ajudar na organização quando incentivada pelos educadores.'
        ],
        'Raramente ajuda': [
            'Raramente ajuda na organização dos brinquedos, necessitando de estímulos para desenvolver o senso de responsabilidade.',
            'A criança auxilia na organização dos brinquedos em poucas ocasiões.',
            'Demonstra pouca responsabilidade ao ajudar na arrumação dos brinquedos.',
            'A participação na organização dos brinquedos é marcada por colaboração esporádica.',
            'A criança valoriza o momento de ajudar na organização dos brinquedos em raras situações.',
            'Mostra-se pouco motivada a colaborar na arrumação dos brinquedos.',
            'A criança amplia seu senso de responsabilidade ao ajudar na organização em poucas ocasiões.',
            'Demonstra envolvimento ao colaborar na arrumação dos brinquedos em raras situações.',
            'A participação nas atividades de organização contribui para o desenvolvimento da responsabilidade, mesmo que de forma esporádica.',
            'A criança valoriza o momento de ajudar na organização, mesmo que raramente.'
        ],
        'Nunca ajuda': [
            'Não costuma ajudar na organização dos brinquedos, sendo importante trabalhar esse aspecto no cotidiano escolar.',
            'A criança não auxilia na organização dos brinquedos após as brincadeiras.',
            'Demonstra falta de responsabilidade ao não ajudar na arrumação dos brinquedos.',
            'A participação na organização dos brinquedos é inexistente.',
            'A criança não valoriza o momento de ajudar na organização dos brinquedos.',
            'Mostra-se desmotivada a colaborar na arrumação dos brinquedos.',
            'A criança não amplia seu senso de responsabilidade ao não ajudar na organização.',
            'Demonstra falta de envolvimento ao não colaborar na arrumação dos brinquedos.',
            'A participação nas atividades de organização não contribui para o desenvolvimento da responsabilidade.',
            'A criança não valoriza o momento de ajudar na organização, sendo importante trabalhar esse aspecto.'
        ]
    },
    17: {
        'Muito bem': [
            'Nos momentos da roda de história, seu comportamento é muito positivo, participando com atenção e respeito, aproveitando plenamente esse momento de escuta e imaginação.',
            'A criança participa com atenção e respeito durante a roda de história.',
            'Demonstra comportamento exemplar nos momentos de escuta e imaginação.',
            'A participação na roda de história é marcada por envolvimento e respeito.',
            'A criança valoriza o momento de ouvir histórias, aproveitando ao máximo a experiência.',
            'Mostra-se motivada a participar das atividades de roda de história.',
            'A criança amplia seu repertório literário ao participar da roda de história.',
            'Demonstra envolvimento ao ouvir histórias durante a roda.',
            'A participação nas atividades de roda de história contribui para o desenvolvimento da linguagem.',
            'A criança valoriza o momento de escuta e imaginação durante a roda de história.'
        ],
        'Bem': [
            'Durante a roda de história, comporta-se bem, ouvindo as histórias e respeitando os colegas.',
            'A criança participa das atividades de roda de história com respeito.',
            'Demonstra comportamento adequado durante os momentos de escuta.',
            'A participação na roda de história é marcada por respeito e atenção.',
            'A criança valoriza o momento de ouvir histórias, participando ativamente.',
            'Mostra-se motivada a participar das atividades de roda de história.',
            'A criança amplia seu repertório literário ao participar da roda de história.',
            'Demonstra envolvimento ao ouvir histórias durante a roda.',
            'A participação nas atividades de roda de história contribui para o desenvolvimento da linguagem.',
            'A criança valoriza o momento de escuta durante a roda de história.'
        ],
        'Regular': [
            'Apresenta comportamento regular nos momentos da roda de história, alternando atenção e dispersão.',
            'A criança participa das atividades de roda de história de forma oscilante.',
            'Demonstra comportamento variável durante os momentos de escuta.',
            'A participação na roda de história é marcada por momentos de atenção e dispersão.',
            'A criança valoriza o momento de ouvir histórias, mas nem sempre participa ativamente.',
            'Mostra-se motivada a participar das atividades de roda de história em algumas situações.',
            'A criança amplia seu repertório literário ao participar da roda de história de forma variável.',
            'Demonstra envolvimento ao ouvir histórias durante a roda, mas de forma oscilante.',
            'A participação nas atividades de roda de história contribui para o desenvolvimento da linguagem, mesmo que de forma irregular.',
            'A criança valoriza o momento de escuta durante a roda de história, mesmo que de forma variável.'
        ],
        'Mal': [
            'Demonstra dificuldades de comportamento durante a roda de história, necessitando de acompanhamento para melhorar sua participação.',
            'A criança apresenta dificuldades de comportamento nos momentos de roda de história.',
            'Demonstra falta de atenção durante os momentos de escuta.',
            'A participação na roda de história é marcada por dispersão e desatenção.',
            'A criança não valoriza o momento de ouvir histórias, participando pouco.',
            'Mostra-se desmotivada a participar das atividades de roda de história.',
            'A criança não amplia seu repertório literário ao participar da roda de história.',
            'Demonstra falta de envolvimento ao ouvir histórias durante a roda.',
            'A participação nas atividades de roda de história não contribui para o desenvolvimento da linguagem.',
            'A criança não valoriza o momento de escuta durante a roda de história.'
        ],
        'Muito mal': [
            'Apresenta comportamento inadequado durante a roda de história, exigindo intervenções frequentes dos educadores.',
            'A criança apresenta comportamento inadequado nos momentos de roda de história.',
            'Demonstra falta de respeito durante os momentos de escuta.',
            'A participação na roda de história é marcada por desrespeito e desatenção.',
            'A criança não valoriza o momento de ouvir histórias, participando de forma inadequada.',
            'Mostra-se desmotivada a participar das atividades de roda de história, apresentando comportamento inadequado.',
            'A criança não amplia seu repertório literário ao participar da roda de história de forma inadequada.',
            'Demonstra falta de envolvimento ao ouvir histórias durante a roda, apresentando comportamento inadequado.',
            'A participação nas atividades de roda de história não contribui para o desenvolvimento da linguagem devido ao comportamento inadequado.',
            'A criança não valoriza o momento de escuta durante a roda de história, apresentando comportamento inadequado.'
        ]
    },
}

---
id: "42430431244695"
titulo: "Base de Conhecimento - Importação de Fontes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430431244695-Base-de-Conhecimento-Importa%C3%A7%C3%A3o-de-Fontes"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:08:49Z"
rotulos: ["sync_hc", "neppo", "neppo_857999936", "sync_hash_ee4f901778ae"]
---

# Base de Conhecimento - Importação de Fontes

Esta etapa guia o usuário na alimentação de múltiplos dados em uma única base, dividida em três colunas (Painéis).

Índice:

- [1. Painel Esquerdo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430431244695-Base-de-Conhecimento-Importa%C3%A7%C3%A3o-de-Fontes#1-Painel-Esquerdo)
- [2. Painel Central](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430431244695-Base-de-Conhecimento-Importa%C3%A7%C3%A3o-de-Fontes#2-Painel-Central)
- [3. Painel Direito (Status de Processamento)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430431244695-Base-de-Conhecimento-Importa%C3%A7%C3%A3o-de-Fontes#3-Painel-Direito-Status-de-Processamento)
- [4. Processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430431244695-Base-de-Conhecimento-Importa%C3%A7%C3%A3o-de-Fontes#4-Processamento)
- [5. Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430431244695-Base-de-Conhecimento-Importa%C3%A7%C3%A3o-de-Fontes#5-Boas-praticas)

Navegue também:
Introdução a base de conhecimento

![Imagem 1: Navegue também: Introdução a base de conhecimento](https://ajuda.sankhya.com.br/hc/article_attachments/42639881619991)

## 1. Painel Esquerdo

#### Identificação e Fontes

- **Nome**: Campo obrigatório, é o nome da base de conhecimento, só aceita letras minuscúlas, números e caracteres especiais, o nome não pode ter espaço entre as letras.

Ex
ERRADO: Nome: Base de Teste

CORRETO: Nome: base\_de\_teste

- **Descrição:** Campo obrigatório. A base de conhecimento é gerada para um assunto específico. Na descrição, deve ser informado em quais situações essa base deve ser utilizada e qual é o seu objetivo.

  **Exemplo:**
  Nome: erros\_criação\_de\_grupos

  Descrição: Esta base deve ser utilizada em situações relacionadas a erros na criação de grupos de atendimento. Ela contém orientações sobre como identificar e resolver problemas, incluindo passo a passo para os erros X e Y, além dos contatos do time de suporte.
- **Importação de Arquivo:** O limite crítico é de **50MB por arquivo**, formatos aceitos: `.pdf`, `.xls`, `.xlsx`, `.docx`, `.txt`, `.xml`, `.tsv`, `.ods`, `.json` e `.csv`.
- **Importação de URL:** Insira o link e clique em "+". As URLs precisam ser públicas, acessíveis pelo sistema e retornar um conteúdo válido. Para Google Docs ou Drive, a URL deve ter permissão pública ("Qualquer pessoa com o link").
- **Lista de Fontes Adicionadas:** Visualize tudo o que já foi submetido. É possível remover um item facilmente clicando no ícone de "x". Ao adicionar novos arquivos a uma base existente, você pode validá-los e reprocessar a base sem precisar recriá-la.

[GIF animado: Imagem 2: Lista de Fontes Adicionadas: Visualize tudo o que já foi submetido. É possível remover um item facilmente clicando no…](https://ajuda.sankhya.com.br/hc/article_attachments/42639883227543)

---

## 2. Painel Central

O painel central tem dois layout, o inicial, onde permite importar arquivos e solicitar a criação da base de conhecimento, e um segundo template onde visualiza e configura os arquivos selecionados na Lista de Fontes na coluna esquerda.

### Layout Importação

A área central possui uma zona de "drag & drop" (arrastar e soltar) e a opção "Clique para pesquisar".

- **Importação de Arquivo:** O limite crítico é de **50MB por arquivo**.

  - Formatos aceitos: `.pdf`, `.xls`, `.xlsx`, `.docx`, `.txt`, `.xml`, `.tsv`, `.ods`, `.json` e `.csv`.
  - Boas Práticas: O conteúdo precisa ser textual. **Evite PDFs com imagens escaneadas sem OCR**, fotos de documentos ou infográficos isolados, pois o sistema não interpreta elementos puramente visuais. Quando o conteúdo visual for importante, converta-o em texto explicativo.
- **Importação de URL:** Insira o link e clique em "+". As URLs precisam ser públicas, acessíveis pelo sistema e retornar um conteúdo válido. Para Google Docs ou Drive, a URL deve ter permissão pública ("Qualquer pessoa com o link").

[GIF animado: Imagem 3: Importação de URL: Insira o link e clique em "+". As URLs precisam ser públicas, acessíveis pelo sistema e retornar um…](https://ajuda.sankhya.com.br/hc/article_attachments/42639915741591)

### Layout de Configuração e Visualização dos Arquivos

Esta tela é fundamental para entender a interpretação da IA e garantir a atualização automática dos dados.

- **Preview do Documento:** Visualize o documento original anexado com opções de zoom (ex: 100%, 200%) e controle de paginação.
- **Textos Processados:** Após o processamento, é exibida a prévia do texto interpretado pela IA, segmentado em blocos (Texto #1, #2...). O sistema agrupa informações e mostra a quantidade de caracteres por bloco.

- O sistema pode gerar até **10.000 blocos por base**, e cada bloco pode ter no **máximo 10.000 caracteres**. Existe um botão "ver mais" para detalhes extensos.

- **Agendamento Automático (CRON)** É possível automatizar a atualização de fontes (como URLs dinâmicas) individualmente, habilitando a opção **"Agendar atualização"**. O card do arquivo receberá um sinalizador de agenda.
- **Frequências disponíveis:**

  - Minutos: Ex: a cada 5 minutos (excelente para dados que mudam em tempo real).
  - Por Hora: Atualizações de hora em hora.
  - Diário: Ex: rotina processada todo dia à meia-noite.
  - Semanal, Mensal ou Anual: Para relatórios ou documentos de longo prazo.

**Nota Técnica:** Se o link original estiver fora do ar no momento do agendamento, o sistema não acessará a fonte e gerará o erro: "Não foi possível acessar a fonte. Verifique se a URL está correta e se a fonte é pública".

[GIF animado: Imagem 4: Nota Técnica: Se o link original estiver fora do ar no momento do agendamento, o sistema não acessará a fonte e gerará…](https://ajuda.sankhya.com.br/hc/article_attachments/42639896730135)

[GIF animado: Imagem 5: GIF animado: Imagem 4: Nota Técnica: Se o link original estiver fora do ar no momento do agendamento, o sistema não…](https://ajuda.sankhya.com.br/hc/article_attachments/42639916394775)

---

## 3. Painel Direito (Status de Processamento)

- Apresenta uma esteira visual em 4 etapas (Preparação > Processamento > Salvando > Finalizado), refletindo o feedback visual da IA para cada item e indicando erros antes da indexação final. mais informações…

[GIF animado: Imagem 6: Apresenta uma esteira visual em 4 etapas (Preparação > Processamento > Salvando > Finalizado), refletindo o feedback…](https://ajuda.sankhya.com.br/hc/article_attachments/42639897287191)

---

## 4. Processamento

### Como o conteúdo é processado

O sistema transforma o conteúdo importado em blocos menores para permitir a geração de embeddings e a recuperação posterior pelo assistente. O modo como isso acontece varia conforme o tipo de arquivo.

Arquivos textuais

Arquivos textuais merecem atenção especial porque, neles, a qualidade da base depende muito de como o conteúdo foi escrito e organizado.

#### De forma simplificada, o processo ocorre assim:

1. o texto é extraído do arquivo;
2. o sistema tenta identificar divisões naturais e padrões de organização;
3. o conteúdo é agrupado em blocos de texto;
4. esses blocos seguem para geração de embeddings;
5. depois, esses embeddings são usados para recuperar trechos relevantes nas respostas do assistente.

### Como o texto é extraído

O comportamento de extração depende do formato:

- PDF: o texto é extraído, em geral, página por página;
- DOCX: o conteúdo costuma ser lido a partir da estrutura de parágrafos, títulos e listas;
- TXT: o arquivo é tratado como texto puro;
- CSV, TSV e planilhas: o conteúdo tende a ser lido em estrutura tabular;
- JSON e XML: a estrutura hierárquica é usada para formar unidades de conteúdo.

Quando o arquivo segue um padrão reconhecível, a tendência é o sistema conseguir formar blocos melhores.

#### Exemplos de padrões que costumam ajudar:

- títulos e subtítulos consistentes;
- seções repetidas com a mesma estrutura;
- FAQ com pergunta seguida da resposta;
- procedimentos com objetivo, pré-requisito e passo a passo;
- catálogos em que cada item segue o mesmo modelo;
- registros em que cada bloco representa uma unidade fechada de informação.

**Quando esse padrão existe,** o sistema tende a reconhecer melhor os limites entre assuntos e manter no mesmo bloco aquilo que faz sentido junto, como:

- regra + condição + exceção;
- pergunta + resposta;
- item + descrição + características;
- processo + etapas + observações.

Isso melhora a qualidade porque o contexto fica mais preservado dentro de cada bloco.

Na prática, isso significa que o sistema tende a agrupar partes próximas que parecem tratar do mesmo assunto, considerando, por exemplo:

- sequência de parágrafos;
- continuidade local do texto;
- similaridade semântica entre trechos próximos;
- posição dos conteúdos dentro da página ou do arquivo.

**Quando esse padrão não existe,** e quando o documento:

- mistura vários assuntos no mesmo trecho;
- muda de tema sem sinalização clara;
- usa títulos genéricos demais;
- depende do layout visual para fazer sentido;
- espalha o contexto de um mesmo assunto em pontos distantes;
- possui frases soltas, notas breves ou conteúdo muito fragmentado.

Nesses casos, os blocos podem ficar:

- amplos demais;
- específicos demais, mas sem contexto suficiente;
- misturados com outros temas;
- menos úteis para recuperar respostas exatas.

#### Impacto disso na resposta do assistente

Quando os blocos preservam bem o contexto, o assistente tende a responder de forma mais completa e assertiva.

Quando o conteúdo foi mal segmentado, o assistente pode:

- recuperar um trecho incompleto;
- deixar de trazer uma exceção importante;
- responder de forma genérica;
- combinar informações próximas, mas não ideais;
- encontrar o assunto, mas com menor precisão.

Por isso, em arquivos textuais, a qualidade da redação e da organização é tão importante quanto o formato do arquivo.

### Arquivos tabulares

Em arquivos tabulares, como planilhas, CSV e TSV, cada linha tende a representar um bloco ou uma unidade de informação.

#### A qualidade costuma ser melhor quando:

- cada linha representa um registro completo;
- os cabeçalhos são claros;
- não há células mescladas desnecessariamente;
- a informação não está espalhada em várias linhas para o mesmo item.

### Arquivos estruturados

Em arquivos JSON e XML, a estrutura dos campos, objetos e listas ajuda a formar os blocos.

#### A qualidade tende a ser melhor quando:

- os nomes dos campos são claros;
- cada objeto representa uma unidade lógica completa;
- as listas seguem um padrão consistente;
- a estrutura não é profunda ou confusa em excesso

---

## 5. Boas práticas

### Recomendações gerais

Para aumentar a qualidade da base e a assertividade das respostas:

- organize o conteúdo por assunto;
- use títulos claros e específicos;
- mantenha cada seção autocontida;
- aproxime regra, condição e exceção;
- aproxime pergunta e resposta;
- evite misturar muitos temas no mesmo trecho;
- prefira texto claro, direto e completo;
- evite depender de layout visual para transmitir a informação principal;
- transforme conteúdo visual importante em texto.

### O que tende a melhorar a qualidade dos blocos

A qualidade costuma ser melhor quando o documento:

- separa claramente um assunto por seção;
- usa títulos e subtítulos objetivos;
- mantém contexto suficiente dentro de cada parte;
- segue um padrão ao longo do arquivo;
- apresenta unidades fechadas de informação;
- evita referências soltas como “conforme acima”, “como vimos antes” ou “segue abaixo” sem repetir o contexto.

### O que tende a reduzir a qualidade dos blocos

A qualidade costuma piorar quando o documento:

- mistura vários assuntos no mesmo bloco;
- muda de tema sem marcação clara;
- traz listas muito curtas sem contexto;
- usa títulos vagos;
- repete o mesmo assunto em muitos pontos diferentes;
- depende de imagens, prints ou diagramas não descritos em texto;
- contém texto mal extraído, muito fragmentado ou pouco linear.

### Orientações por tipo de arquivo:

#### PDF

Prefira PDFs com texto selecionável, gerados digitalmente, com leitura linear e com títulos e seções claras.

PDFs com os cenários abaixo tendem a gerar pior resultado:

- múltiplas colunas;
- cabeçalhos e rodapés repetitivos;
- tabelas complexas;
- muito conteúdo escaneado;
- prints incorporados;
- conteúdo que depende mais de layout do que de texto.

#### DOCX

Arquivos DOCX costumam apresentar melhor qualidade quando utilizam estrutura real de edição, com títulos, subtítulos, listas e parágrafos bem separados.

- um tópico por seção;
- um parágrafo por ideia principal;
- títulos descritivos;
- listas quando houver passo a passo;
- contexto suficiente em cada seção.

#### TXT

Arquivos TXT funcionam melhor quando o conteúdo é simples, limpo e organizado por linhas e parágrafos.

- usar títulos claros;
- deixar linhas em branco entre seções;
- manter uma ideia por parágrafo;
- evitar blocos longos e pouco estruturados.

#### CSV, TSV e planilhas

- usar cabeçalhos claros;
- fazer cada linha representar um item completo;
- evitar células mescladas;
- evitar dividir um mesmo registro em várias linhas.

#### JSON e XML

- usar nomes de campos claros;
- manter objetos completos e consistentes;
- usar listas padronizadas;
- evitar estruturas profundas demais;
- evitar mistura de muitos contextos no mesmo nível.

### Exemplos bons e ruins de organização

**Exemplo 1: FAQ**

**Bom exemplo**

Como redefinir a senha? Acesse a tela de login, clique em “Esqueci minha senha”, informe seu e-mail cadastrado e siga o link enviado. O link expira em 30 minutos.

Por que funciona melhor: a pergunta e a resposta estão juntas, completas e autocontidas.

Exemplo ruim

Senha Usuário pode trocar. Tem e-mail. Expira rápido.

Por que funciona pior: o conteúdo está incompleto, vago e sem contexto suficiente.

**Exemplo 2: Procedimento**

**Bom exemplo**

Solicitar segunda via de boleto Pré-requisitos: CPF do cliente e número do contrato. Passo 1: acessar o menu Financeiro. Passo 2: buscar pelo CPF ou contrato. Passo 3: selecionar a parcela em aberto. Passo 4: clicar em “Gerar segunda via”. Exceção: se a parcela estiver vencida há mais de 60 dias, o cliente deve falar com o time financeiro.

Por que funciona melhor: o processo está completo, com contexto, etapas e exceção próximas.

**Exemplo ruim**

Financeiro Aqui é possível consultar boletos, atualizar cadastro, emitir nota, ver atraso, contestar cobrança, alterar e-mail e falar com suporte.

Por que funciona pior: vários assuntos foram misturados no mesmo trecho.

**Exemplo 3: Política ou regra**

**Bom exemplo**

Política de férias Aplica-se a todos os colaboradores em regime CLT. As férias devem ser solicitadas com antecedência mínima de 30 dias. A aprovação depende do gestor imediato. Exceção: em casos urgentes, o RH poderá avaliar pedidos fora do prazo.

Por que funciona melhor: regra, escopo e exceção estão no mesmo contexto.

Exemplo ruim

Um único texto corrido contendo férias, benefícios, ponto, dress code, advertências e desligamento sem divisão clara.

Por que funciona pior: temas diferentes podem acabar agrupados no mesmo bloco.

**Exemplo 4: Catálogo ou lista de itens**

**Bom exemplo**

Plano Básico Indicado para pequenos times. Inclui até 5 usuários. Permite abertura de chamados e consulta de relatórios.

Plano Premium Indicado para operações maiores. Inclui usuários ilimitados. Permite integrações e relatórios avançados.

Por que funciona melhor: cada item faz sentido sozinho e contém as informações principais no mesmo lugar.

**Exemplo ruim**

Nomes dos planos em uma seção, características em outra e regras em uma terceira parte do documento.

Por que funciona pior: o contexto de cada item fica fragmentado.

**Exemplo 5: Conteúdo dependente de imagem**

**Bom exemplo**

Fluxo de aprovação de pedido Etapa 1: o vendedor envia o pedido. Etapa 2: o gestor comercial valida os dados. Etapa 3: o financeiro valida limite e condição de pagamento. Etapa 4: o pedido é liberado para faturamento.

Por que funciona melhor: o fluxo foi descrito em texto, então a informação pode ser processada.

**Exemplo ruim**

Um fluxograma em imagem sem descrição textual.

Por que funciona pior: a informação principal está em mídia não suportada como fonte de conhecimento textual.

---

Índice:

- [1. Painel Esquerdo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430431244695-Base-de-Conhecimento-Importa%C3%A7%C3%A3o-de-Fontes#1-Painel-Esquerdo)
- [2. Painel Central](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430431244695-Base-de-Conhecimento-Importa%C3%A7%C3%A3o-de-Fontes#2-Painel-Central)
- [3. Painel Direito (Status de Processamento)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430431244695-Base-de-Conhecimento-Importa%C3%A7%C3%A3o-de-Fontes#3-Painel-Direito-Status-de-Processamento)
- [4. Processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430431244695-Base-de-Conhecimento-Importa%C3%A7%C3%A3o-de-Fontes#4-Processamento)
- [5. Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430431244695-Base-de-Conhecimento-Importa%C3%A7%C3%A3o-de-Fontes#5-Boas-praticas)

Navegue também:
Introdução a base de conhecimento

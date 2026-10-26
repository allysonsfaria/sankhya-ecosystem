---
id: "37774568270103"
titulo: "Como gerar e enviar os eventos S2500 e S2501"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37774568270103-Como-gerar-e-enviar-os-eventos-S2500-e-S2501"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-22T14:08:30Z"
rotulos: ["Eventos", "XML", "Folha", "eSocial", "Processo Trabalhista", "Central do eSocial"]
---

# Como gerar e enviar os eventos S2500 e S2501

| Categoria |
| --- |
| [O que são os eventos S-2500 e S-2501?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37774568270103-Como-gerar-e-enviar-os-eventos-S2500-e-S2501#h_01KFB5EXX1Z9C1JQ3F7XSGHZRV) |
| [S-2500 – Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/37774568270103-Como-gerar-e-enviar-os-eventos-S2500-e-S2501#h_01KFB5ERPHGW7C0QMHC5A56S5F) |
| [S-2501 – Pagamentos do Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/37774568270103-Como-gerar-e-enviar-os-eventos-S2500-e-S2501#h_01KFB5E84XKSGQV2JKY6TJB9K5) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37774568270103-Como-gerar-e-enviar-os-eventos-S2500-e-S2501#h_01KFB5E1HZH9J2WRYX1VMCDAHQ) |
| [Para cadastrar Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/37774568270103-Como-gerar-e-enviar-os-eventos-S2500-e-S2501#h_01KFB5DQ51H2TNYVN4DZVHPCBN) |
| [Geração e envio do evento S2500](https://ajuda.sankhya.com.br/hc/pt-br/articles/37774568270103-Como-gerar-e-enviar-os-eventos-S2500-e-S2501#h_01KFB5D6BSENR59ZZMS264HC49) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37774568270103-Como-gerar-e-enviar-os-eventos-S2500-e-S2501#h_01KFB5CJYXFYS2N2PASZY5BB9S) |

## Eventos S2500 e S2501 - Processo Trabalhista

#### O que são os eventos S-2500 e S-2501?

Os eventos S-2500 e S-2501 fazem parte do módulo de Processos Trabalhistas do eSocial e são utilizados quando há decisão judicial que reconhece verbas trabalhistas com impacto fiscal ou previdenciário para a empresa.

##### S-2500 – Processo Trabalhista:

É o evento responsável por registrar os dados do processo judicial. Nele são informados o número do processo, as partes envolvidas, as verbas reconhecidas, os períodos e valores apurados, além dos encargos devidos. Ele substitui declarações manuais que antes eram feitas após decisões judiciais, oficializando o resultado da ação junto ao governo.

##### S-2501 – Pagamentos do Processo Trabalhista:

Complementa o S-2500, informando os pagamentos efetivos feitos ao trabalhador ou à Justiça, incluindo valores, datas e tributos recolhidos. Ele registra como as verbas reconhecidas judicialmente foram quitadas.

Ambos os eventos alimentam a DCTFWeb de processos trabalhistas, garantindo que os recolhimentos estejam em conformidade com a decisão judicial e evitando divergências com a Receita Federal.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1106240424)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. ##### Para cadastrar Processo Trabalhista

**Acesse**: Pessoal+ » Rotinas Folha » Processo Trabalhista

- Acione o botão “Adicionar Processo Trabalhista”

**Aba Declarante**

- Informe sua empresa
- Marque a opção ‘Há responsabilidade indireta?’ para habilitar o tipo de inscrição
- Escolha o tipo de inscrição do responsável direto e preencha com o numero correspondente

**Atenção!** **Para incluir no sistema registro realizado pelo Portal do eSocial**

- Marque a opção “Inclusão realizada via Portal do eSocial?”
- Informe o numero do recibo eSocial (S2500)
- Acessar a Central do eSocial e gerar evento S2500

**Aba Informações do Processo**

- Informe a origem do processo e as demais informações solicitadas na tela

**Aba Informações do Trabalhador**

- Se a opção “Trabalhador contratado pelo declarante” estiver desmarcada, preencha manualmente os dados pessoais solicitados
- Ao marcar esta opção, o sistema habilita a busca automática das informações com base no código do colaborador, preenchendo os campos de forma integrada
- Nos casos de responsabilidade indireta, é obrigatório preencher os campos Matrícula e Data de Admissão do trabalhador de origem, na seção “Informações do trabalhador no responsável direto”
- Salve as alterações para habilitar a seção “Informações dos Dependentes do Trabalhador”
- Se o trabalhador for contratado pelo declarante, os dependentes já vinculados a ele poderão ser importados automaticamente ao acionar o botão “Importar novo Dependente”
- Caso o trabalhador não seja contratado pelo declarante, acione o botão “Incluir novo Dependente” e preencha manualmente e salve as informações solicitadas na janela pop-up exibida.

**Aba Informações do Contrato de Trabalho**

- Selecione o tipo de contrato
- Informe atrávez das marcações se houve reconhecimento de categoria do trabalhador e natureza da atividade
- Selecione a natureza da atividade (decisão judicial)
- Salve as alterações realizadas
- Na seção “Inclusão de Nova Categoria e/ou Natureza”, clique no botão “Incluir categoria/natureza”
- Busque a nova categoria, informe a natureza e data de inicio
- Salve as informações solicitadas na janela pop-up
- No menu lateral, clique em “Confirmar cadastro” para concluir o lançamento do processo trabalhista

**Aba Informações de Tributos Decorrentes**

- Se houver valor pertinente a contribuição previdenciária e imposto de renda a recolher acione o botão “Incluir nova informação de tributos”
- Preencha as informações solicitadas e em seguida, salve o registro
- Ative a flag “seleção de Processos Trabalhistas” no canto superior da tela
- Selecione o período desejado e clique no botão “Liberar tributos selecionados”
  Para inclusão de mais de um período repita o processo clicando em ‘Incluir nova informação de tributos”

2. ##### Geração e envio do evento S2500

**Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em '**Carregar**'.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Selecionar Eventos**
- Selecione o evento **S-2500** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado na aba '**Eventos Pendentes**', clique sobre o card e confira as informações
- Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

**Geração e envio do evento S2500**

- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Selecionar Eventos**
- Selecione o evento **S-2501** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado na aba '**Eventos Pendentes**', clique sobre o card e confira as informações
- Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.

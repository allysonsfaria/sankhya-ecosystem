---
id: "37639155179159"
titulo: "Como realizar a importação de XML sem vincular a nota a pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37639155179159-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-sem-vincular-a-nota-a-pedidos"
trilha: "Universidade Sankhya > Jornada de Compras"
atualizado_em: "2026-07-22T14:12:12Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "TOP", "Documentos Eletrônicos"]
---

# Como realizar a importação de XML sem vincular a nota a pedidos

| Categoria |
| --- |
| [O que é o processo de importação de documentos eletrônicos?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37639155179159-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-sem-vincular-a-nota-a-pedidos#h_01KEVSHZHNEV5SZTDDMBS7N669) |
| [Quais os riscos de não utilizar o processo de importação manual de documentos eletrônicos?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37639155179159-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-sem-vincular-a-nota-a-pedidos#h_01KEVSJEHMWRG2H8TYYZQ50B6Z) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37639155179159-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-sem-vincular-a-nota-a-pedidos#h_01KFBKZ630FH964GR8H1VKSYS9) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37639155179159-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-sem-vincular-a-nota-a-pedidos#h_01KEVSKG4N1TYV54BH37DGQ2GH) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37639155179159-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-sem-vincular-a-nota-a-pedidos#h_01KEVSNDXXN2NAF9E9NB1Y5F2Z) |

## Importação de documentos eletrônicos

#### O que é o processo de importação de documentos eletrônicos?

O processo de Importação de documentos eletrônicos consiste no registro de notas fiscais de compras e conhecimentos de transporte eletrônicos no sistema ERP Sankhya sem a automatização completa proporcionada pelo XML. Esse método permite que a empresa insira manualmente os dados fiscais e operacionais, garantindo que informações como produtos, valores, tributos e condições comerciais sejam registradas mesmo na ausência do arquivo XML ou em casos de inconsistências. Embora mais demorado, esse processo assegura a conformidade fiscal e a continuidade das operações, integrando informações essenciais ao sistema. Além disso, quando o XML é importado, ele é armazenado no sistema, permitindo consultas futuras e agregando maior segurança operacional e gestão de dados, eliminando a necessidade de digitação completa dos documentos e promovendo eficiência e agilidade em cenários críticos.

#### Quais os riscos de não utilizar o processo de importação manual de documentos eletrônicos?

A ausência do processo de importação manual de documentos eletrônicos coloca a empresa em uma posição altamente vulnerável, com riscos críticos que podem comprometer sua sustentabilidade financeira e competitividade no mercado. Sem esse recurso, aumenta-se a probabilidade de erros manuais no registro de dados fiscais, resultando em inconsistências que prejudicam a conformidade tributária. Além disso, a ineficiência no controle de notas fiscais e conhecimentos de transporte pode levar a descontrole nos estoques, rupturas no abastecimento, e gargalos logísticos, impactando diretamente as operações e o atendimento ao cliente.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052446008)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A compradora da **Axis** recebeu uma nota fiscal eletrônica enviada pela empresa **Real Alimentos.**

**Tarefa:** Baixe o arquivo  XML - NF-e e realize a importação em seu ERP Sankhya.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Tipos de Operação - TOP**
   Menu: Comercial  »  Arquivo » Tipos de Operações (TOP)

- Selecione a **TOP Compra-Revenda**.

  - Na aba **Geral**, preencha o campo **Exigir Pedido** com: Não Exigir

2. **Baixe o arquivo XML:** [**XML - NF-e - sem pedido**](https://drive.google.com/file/d/1XhKnvCmG4KJnChjh6IeSVJHLoBpWVbP0/view?usp=drive_link)
3. **Inclusão do Arquivo XML no Portal de Importação**

- Acesse a tela **Portal de Importação de XML**
  Menu: Comercial »  Rotinas »  Portal de Importação de XML
- Clique no botão **"+"** (**Cadastrar Importação de XML de Notas**) para carregar o arquivo XML.
- Selecione o arquivo no botão “**Escolher arquivo**”
- Clique no botão "**Enviar**”.
- Clique em **Processar** para que o sistema valide o XML.

- O sistema exibirá a mensagem **"Importado com sucesso"**.
- Clique em **Ok**.

4. **Confirmação na Central de Compras**

- Clique no botão **Abrir Documento**,

Será direcionado para a **Central de Compras**.

Revise os dados:

**Cabeçalho:** Empresa, Parceiro, Tipo de Operação, Tipo de Negociação, Nro. Nota, Série,  Nro. único, Natureza, Centro de Resultado e Chave NF-e.

**Itens:** Verifique produtos e quantidades. 

**Rodapé:** Verifique os dados das abas **Totais**, **Impostos** e **Financeiro**.

- Clique em **Confirmar.**

#### Correção e Repetição

- Valide as informações de todas as abas dentro do Portal de Importação XML.
- Caso não tenha sido concluído conforme esperado, refaça o processo corrigindo as informações necessárias.
- Certifique-se de que configurou o Modelo de importação de XML.
- Para praticar, experimente criar novamente um novo orçamento de compra, com outros produtos e fornecedores.

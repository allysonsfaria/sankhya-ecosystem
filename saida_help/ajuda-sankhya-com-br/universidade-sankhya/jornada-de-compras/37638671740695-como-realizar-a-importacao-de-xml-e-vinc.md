---
id: "37638671740695"
titulo: "Como realizar a importação de XML e vincular aos pedidos registrados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37638671740695-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-e-vincular-aos-pedidos-registrados"
trilha: "Universidade Sankhya > Jornada de Compras"
atualizado_em: "2026-08-11T19:42:07Z"
rotulos: ["Produtos", "Parceiro", "NF-e", "XML", "Importação", "Financeiro"]
---

# Como realizar a importação de XML e vincular aos pedidos registrados

| Categoria |
| --- |
| [O que é uma Importação de XML com vinculação do Pedido/Nota e quais seus benefícios?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638671740695-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-e-vincular-aos-pedidos-registrados#h_01KEVR599Y49GA24VCHKNFPS0Q) |
| [Quais os riscos de não utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638671740695-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-e-vincular-aos-pedidos-registrados#h_01KEVR5PFQWP3681D01KYJN8V0) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638671740695-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-e-vincular-aos-pedidos-registrados#h_01KFBH4518QVTRWT8QNH9H4HPR) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638671740695-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-e-vincular-aos-pedidos-registrados#h_01KEVR65AAMRES5RK08MZ2EG2E) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638671740695-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-e-vincular-aos-pedidos-registrados#h_01KEVR6HYQPF17QNHPVRX526FT) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638671740695-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-e-vincular-aos-pedidos-registrados#h_01KEVR9SJ5HKVDE0A3T5PQCG9S) |

## Importação de XML com vinculação do pedido/nota

#### O que é uma Importação de XML com vinculação do Pedido/Nota e quais seus benefícios?

A importação de XML com vinculação do Pedido/Nota é um processo automatizado que permite registrar notas fiscais de compras e conhecimentos de transporte eletrônico no sistema sem a necessidade de digitação manual. Ao importar o XML, a nota fiscal é automaticamente vinculada ao pedido de compra previamente cadastrado, assegurando que os dados de produtos, quantidades, valores e tributos estejam em conformidade com o que foi negociado. Essa prática aumenta a eficiência operacional, reduz erros e garante maior controle e integridade das informações registradas.

#### Quais os riscos de não utilizar?

A ausência desse recurso aumenta a probabilidade de erros manuais no registro de notas fiscais e conhecimentos de transporte, resultando em inconsistências nos dados e falhas no cumprimento de obrigações fiscais. O descontrole nos registros fiscais também compromete a governança corporativa, dificultando auditorias e reduzindo a confiança de investidores.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052445629)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A **Axis** enfrenta dois desafios distintos no processo de importação de XML:

- **Atividade:** A **Real Alimentos e Distribuição** LTDA enviou um XML referente a **720 unidades** do **Feijão Carioca - 1 Kg**, com todas as informações consistentes, incluindo o número do pedido previamente registrado no sistema. O setor de compras precisa confirmar se o sistema, configurado para validação automática, fará o vínculo corretamente, garantindo a eficiência do processo sem intervenção manual.
- **Importante:** Para a execução desta atividade, é necessário criar um pedido de compra: um o fornecedor **Real Alimentos e Distribuição**, com **720 unidades** do produto **Feijão Carioca - 1 Kg** ao custo unitário de **R$ 4,22.**

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Baixe o arquivo XML:** [**NF-e XML**](https://drive.google.com/file/d/14hlarTCpZl6nNNx0MLUQYyXQPXaKrELl/view?usp=sharing)
2. Acesse a tela **Produtos**
   Menu: Comercial  »  Cadastros »  Produtos

- Localize o **Feijão Carioca - 1 Kg**.

  - Na aba **Produtos Equivalentes**, clique em **"+"** e preencha:

    - **Cód. Parceiro:** Escolha o fornecedor. **Real Alimentos e Distribuição LTDA**
    - **Sequência:** 1
    - **Unidade do Parceiro:** UN
    - **Cód. Produto Equivalente:** Informe o código do produto no fornecedor. Informe o código: **X**
    - **Descrição do Produto Equivalente:** Insira o nome do produto utilizado pelo fornecedor. **Feijão Carioca - 1 Kg**

3. **Processamento do Arquivo XML no Portal de Importação**

- Acesse a tela **Portal de Importação de XML**
  Menu: Comercial »  Rotinas »  Portal de Importação de XML
- Clique em **"+"** para carregar o arquivo XML enviado pelo fornecedor, selecione o arquivo e clique em **Enviar**.
- Em seguida, clique no botão **Processar**.

4. **Importação do XML com Divergência**

**Divergência Lotes de Produtos não informados**

- Acesse a aba **Produtos por Parceiro**, insira o código do produto e clique em **Validar Importação**.

**Divergência de pedidos ligados**

- Acesse a aba **Pedidos** e localize o pedido na parte inferior da tela.
- No campo **Vinculado**, insira manualmente a quantidade de produtos.
- Verifique se o sistema atualizou as informações no campo correspondente na grade superior e clique novamente em **Validar Importação**.

**Divergência de financeiro**

- Acesse a aba "**Financeiro**", selecione a opção "**Usar Financeiro do Arquivo**" no campo correspondente e clique no botão "**Validar Importação**".

5. **Aviso:** **"Importado com sucesso!**

- Se não houver divergências durante a importação, o sistema exibirá o aviso: **"Importado com sucesso!"**
  Nesse caso:
- Verifique as informações nas abas **Cabeçalho**, **Parceiro**, **Empresa** e **Transportadora**.
- Clique em **Abrir Documento** para ser direcionado à **Central de Compras**.
- Na Central, revise os dados e clique em **Confirmar Nota de Compra** para concluir o processo.

6. **Aviso:** **“Aguardando liberação para variação do vlr. unitário acima do permitido.-Divergência de valor unitário entre pedido e nota”**

- Esse aviso indica uma divergência no valor unitário entre o pedido e a nota fiscal.
- Trata-se de uma **liberação por valor divergente (evento 68)**, que será explicada na próxima aula, incluindo como realizar a liberação corretamente.

#### Correção e Repetição

- Verifique se inseriu todas as informações do XML e do Pedido de Compra.
- Valide as informações de todas as abas dentro do Portal de Importação XML.
- Não esqueça de sempre corrigir uma divergência clicar em Validar Importação.
- Caso não tenha sido concluído conforme esperado, refaça o processo corrigindo as informações necessárias.
- Certifique-se de que configurou o Modelo de importação de XML.
- Para praticar, experimente criar novamente um novo XML, com outros produtos e fornecedores.

---
id: "37722204003223"
titulo: "Como realizar a formação de duplicatas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37722204003223-Como-realizar-a-forma%C3%A7%C3%A3o-de-duplicatas"
trilha: "Universidade Sankhya > Jornada de Pagamentos"
atualizado_em: "2026-07-22T14:09:12Z"
rotulos: ["Configuração", "Contas", "Parceiro", "Movimentação Financeira", "Financeiro"]
---

# Como realizar a formação de duplicatas

| Categoria |
| --- |
| [Para que serve a formação de duplicatas?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37722204003223-Como-realizar-a-forma%C3%A7%C3%A3o-de-duplicatas#h_01KF3CD3XHDM6VS84SNWDMK8DH) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37722204003223-Como-realizar-a-forma%C3%A7%C3%A3o-de-duplicatas#h_01KF3CCS0DG37Y6GGNG7CH4XX7) |
| [Quais os riscos de não utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37722204003223-Como-realizar-a-forma%C3%A7%C3%A3o-de-duplicatas#h_01KF3CCJEVM9MZ39J848WV01PE) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37722204003223-Como-realizar-a-forma%C3%A7%C3%A3o-de-duplicatas#h_01KF3CC8EQD6BQWQJDQVAYCQRY) |
| [Cenário Prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37722204003223-Como-realizar-a-forma%C3%A7%C3%A3o-de-duplicatas#h_01KF3CBQDDAA4STN0636QH7GYA) |
| [Vamos lá! Transforme a maneira como você gerencia seguindo o passo a passo do Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37722204003223-Como-realizar-a-forma%C3%A7%C3%A3o-de-duplicatas#h_01KF3C7NMR5KFFHEMAYMRATJE7) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37722204003223-Como-realizar-a-forma%C3%A7%C3%A3o-de-duplicatas#h_01KF3C70NJVV93MXSA57SA5FDX) |

## Formação de Duplicatas

#### Para que serve a formação de duplicatas?

A formação de duplicatas serve para agrupar vários títulos que a empresa deve pagar a um mesmo fornecedor em uma única duplicata. Esse processo facilita a gestão dos compromissos financeiros, reduz a quantidade de lançamentos e permite um controle mais organizado dos pagamentos, especialmente em compras a prazo.

#### Quais problemas este recurso resolve?

- **Muitos títulos separados para o mesmo fornecedor:** Permite consolidar pagamentos em uma única duplicata.
- **Dificuldade de organizar compromissos por fornecedor:** Facilita a visualização do total a pagar por parceiro.
- **Lançamentos financeiros inconsistentes:** Padroniza a estrutura dos registros e melhora a qualidade dos dados.

#### Quais os riscos de não utilizar?

Em empresas com muitas compras de um mesmo fornecedor, não formar duplicatas pode gerar dispersão dos títulos, dificultando o controle e a conciliação dos pagamentos. Quando o fornecedor faz um único pagamento para vários lançamentos, a falta de agrupamento pode causar erros de baixa, atrasos, retrabalho e comprometer a rastreabilidade das informações.

##### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1068117944)

#### Cenário Prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A **Axis** costuma realizar diversas compras com um mesmo fornecedor ao longo do mês. Cada pedido gera uma nota fiscal com prazo e valor diferentes, o que resulta em vários boletos a serem pagos separadamente, dificultando o controle e aumentando o custo com tarifas bancárias.
Para organizar melhor os pagamentos e simplificar o processo financeiro, a empresa opta por agrupar essas notas em uma única duplicata, centralizando os débitos em um só título. Dessa forma, é possível gerar apenas um boleto para o fornecedor, mantendo o controle financeiro mais eficiente e reduzindo o número de lançamentos a acompanhar.

**Tarefa:** Localize no sistema as notas fiscais de um mesmo fornecedor que ainda não foram agrupadas. Em seguida, realize a formação de uma duplicata, reunindo essas notas em um único título de despesa. Ao final, verifique se o novo título foi gerado corretamente e está disponível para pagamento.

#### Vamos lá! Transforme a maneira como você gerencia seguindo o passo a passo do Sankhya

1. **Localizar os títulos para a formação de duplicata**

- Acesse a tela **Formação de Duplicatas**
  Menu: Financeiro » Rotinas » Formação de Duplicatas
- No campo **“Filtrar por”**, selecione o tipo de data para consulta (negociação, movimento ou vencimento).
- No campo **“Período”**, informar a data inicial e final.
- No campo **”Tipo”** selecionar a opção **Despesa**.
- Marcar as opções **“Agrupar títulos”**, **“Parceiro Matriz”** e **“Agrupar apenas se houver mais de um título”**.
- No campo **“Ajuste do vencimento”** marcar como **“Primeiro”.**
- Após definir os filtros, clique no botão **"Aplicar"** para carregar as informações no painel à direita da tela.

2. **Formar duplicatas**

- Selecione os títulos que serão utilizados para a formação da duplicata.
- Clique na opção **"Remover os não selecionados"** para manter apenas os títulos desejados.
- Em seguida, clique no botão **"Formar Duplicatas"**.
- Um pop-up será exibido, onde você deverá preencher as seguintes informações:
  **Banco**
  **Conta bancária**
  **Tipo de título**
- Após preencher os dados, clique no botão **OK** para concluir a formação da duplicata.
- O sistema apresentará um pop-up com as informações das duplicatas que foram formadas.

3. **Validação final**

- Filtre a duplicata gerada por meio da movimentação financeira.
- Acesse a tela **Movimentação Financeira**
  Menu: Financeiro » Rotinas » Movimentação Financeira
- Clique em **+ Filtros** para criação de um filtro personalizado para a busca da duplicata.
- Selecione **Filtros personalizados** e **Criar filtro.**
- Informe o **Nome do filtro.**
- Busque o campo **"Nro Duplicata",** essa informação será utilizada para busca dos títulos, preencha o operador com **“Igual (=)”** e marque a flag **“Valor variável”** clique em **Salvar.**
- Informe o número da duplicata criada anteriormente e clique em **"Aplicar"** para carregar os títulos vinculados à duplicata gerada.

#### Correção e Repetição

- Certifique-se de que todos os filtros aplicados na tela Formação de Duplicatas foram configurados corretamente, garantindo que o tipo de data, período e categoria de despesa estejam alinhados com os critérios desejados as informações de agrupamento são muito importantes pois é a partir delas que ocorre a formação da duplicata.
- Para reforçar o aprendizado, realize uma nova formação de duplicata utilizando um cenário diferente, como outro período de vencimento, títulos de fornecedores distintos ou valores variados, assegurando total domínio da operação no sistema.

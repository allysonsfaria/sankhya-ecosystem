---
id: "360044593534"
titulo: "Editor de Variáveis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593534-Editor-de-Vari%C3%A1veis"
trilha: "Manual do Produto > Inteligência e Análise > BI Móvel"
atualizado_em: "2026-07-29T13:39:58Z"
rotulos: ["AJUDA DO SKW", "manual", "Editor de Variáveis", "BI Móvel", "Aba Propriedades", "Aba Campos Associados", "Aba Expressão", "Aba Referência", "BI Móvel->Variáveis->Campos", "br.com.sankhya.bim.edtvariaveis", "Editor de Variáveis manual", "Configuração", "Relatórios", "Variáveis", "Fórmulas", "MSDFORCUNDIA", "Configuração Avançada de Variáveis no BI Móvel", "variáveis propriedades expressões"]
---

# Editor de Variáveis

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42310447482135) Módulo: BI Móvel > Variáveis
```

---

No BI Móvel, todas as informações necessárias para a criação de fórmulas e mensagens são geradas a partir de variáveis. A definição dessas variáveis é realizada através dessa tela.

Nela são inseridos, inicialmente, o **"Código"** e o **"Nome de Exibição"** da variável que está sendo cadastrada.

A marcação **"A variável permite valor** **padrão"**, quando realizada, fará com que a variável assuma um valor padrão, caso não seja possível o cálculo de seu valor.

Para facilitar sua navegação nas funcionalidades dessa tela, acesse os links abaixo:

| Funcionalidades da tela Editor de Variáveis |
| --- |
| [Aba Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593534-Editor-de-Vari%C3%A1veis#abapropriedades) |
| [Aba Referência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593534-Editor-de-Vari%C3%A1veis#abareferncia) |
| [Aba Expressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593534-Editor-de-Vari%C3%A1veis#abaexpresso) |
| [Aba Campos Associados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593534-Editor-de-Vari%C3%A1veis#abacamposassociados) |

Na tabela abaixo é possível visualizar o valor padrão para cada tipo de saída, bem como uma correspondência entre os tipos de definição e os tipos de saída das variáveis:

![Imagem 2: Na tabela abaixo é possível visualizar o valor padrão para cada tipo de saída, bem como uma correspondência entre os…](https://ajuda.sankhya.com.br/hc/article_attachments/20352256011159)

### Aba Propriedades

![Imagem 3: Aba Propriedades](https://ajuda.sankhya.com.br/hc/article_attachments/4404089973271)

Ao criar uma variável, defina as seguintes Propriedades:

1. **Código:** Código único da variável. É atribuído automaticamente.
2. **Descrição:** Breve descrição sobre o que a variável representa.
3. **Nome de Exibição:** Nome que será exibido nas mensagens ao fazerem referência à variável.
4. **Nome da Variável:** Nome que será utilizado ao fazer referência à uma variável em uma condição ou mensagem. O nome da variável, obrigatoriamente, deve ser iniciado pelo caractere $.
5. **Autor:** Pessoa que criou a variável. É preenchido automaticamente.
6. **Grupo:** Grupo ou categoria à qual a variável pertence. Os grupos devem ser previamente cadastrados e possuem a função de organização somente.
7. **Período:** Define os momentos em que o valor da variável será atualizado. Ao clicar em **"Configurar"**, será aberto um pop-up.
8. **Ordem:** Define a prioridade de resolução das variáveis. As variáveis de maior prioridade possuem Ordem = 1. Quando uma variável utiliza em sua fórmula outras variáveis, sua ordem deve ser maior que a maior ordem encontrada nas varáveis de que depende.
9. **Tipo:** Tipo de construção da variável. Ele pode ser:

- Valor: Valor constante. Ex.: 10, 1000, 125.69, textos.
- Calculado: Valor calculado através de uma expressão matemática ou trecho de código de programação. Uma variável pode ser composta de operações com outras variáveis previamente definidas. Ex.: 2\*10, $x + $y onde $x e $y possuem o tipo "Valor". Para exemplos de utilização do tipo Calculado para tratar informações que não são constantes, verificar as demonstrações da linguagem de script do BI Móvel.
- SQL: Valor calculado via consulta no banco de dados utilizando-se a linguagem SQL. Esse tipo de variável admite saídas multidimensionais. Exemplo: SELECT CAMPO1, CAMPO2 FROM TABELA.

**Tipo de Saída:** Refere-se ao tipo de retorno da variável. Deve estar de acordo com o tipo da variável. Eles podem ser:

- **Inteiro:** Valores inteiros. Ex.: -25, 0, 25, 593.
- **Decimal:** Valores contendo casas decimais. Ex.: -5.89, 89.0, 1478, 236.
- **Texto:** Cadeia de caracteres. Ex.: ativo, saldo, compras.
- **Data-Hora:** Expressão contendo um valor de data e hora. Ex.: 04/05/2017 08:52:05
- **Data:** Expressão contendo somente um valor de data. Ex.: 04/05/2017
- **Hora:** Expressão contendo um valor de hora. Ex.: 08:52:05
- **Tabela:** Conjunto de valores bidimensionais arranjados em linhas e colunas.

Exemplo: A imagem abaixo apresenta uma tabela contendo uma lista de e-mails:

![Imagem 4: Exemplo: A imagem abaixo apresenta uma tabela contendo uma lista de e-mails:](https://ajuda.sankhya.com.br/hc/article_attachments/20531962456087)

**Observação:** área reservada para alguma observação opcional sobre a variável.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593534-Editor-de-Vari%C3%A1veis#top)

### Aba Expressão

![Imagem 5: Aba Expressão](https://ajuda.sankhya.com.br/hc/article_attachments/4404089991831)

Valor constante, expressão matemática, trecho de código Java, ou consulta SQL que retorna o valor que será assumido pela variável.

Como exemplo, tem-se a fórmula para a variável $vendmes (Vendas Mensais) do tipo SQL ilustrada na figura do cadastro de variáveis:

SELECT VEN.APELIDO AS VENDEDOR,                                                                

 SUM (CAB.VLRNOTA \* CASE WHEN CAB.TIPMOV = 'D' THEN -1                        

         ELSE 1 END) AS TOTAL\_VENDA,                                

 COUNT (DISTINCT CAB.CODPARC) AS QTD\_PARC,                                        

         TO\_CHAR(SYSDATE,'MONTH') AS MES                                                

 FROM TGFCAB CAB, TGFVEN VEN                                                                

         WHERE VEN.CODVEND = CAB.CODVEND                                                          

                 AND CAB.DTNEG >= TRUNC (SYSDATE, 'month')                                        

                 AND STATUSNOTA = 'L'                                                                        

                 AND CAB.TIPMOV IN ('V', 'D')                                                                

         GROUP BY VEN.APELIDO                                                                                

A variável resultante possui saída do tipo tabela, com os campos:

**CODVEND:** Informa o código do vendedor;

**TOTAL\_VENDA:** Contém o total de vendas do vendedor para o mês corrente;

**QTD\_PARC:** O número parceiros envolvidos nas negociações do vendedor;

**MES:** O mês das negociações;

**Árvore de variáveis:** Exibe todas as variáveis cadastradas através de sua descrição separadas por seu grupo. Pode-se também clicar com o botão esquerdo do mouse sobre as variáveis e arrastá-las, soltando o botão do mouse na área de edição. Fazendo isso, o nome da variável é escrito no editor;

**Visualizador de propriedades:** Exibe as principais propriedades da variável selecionada na árvore de variáveis;

**Execução de variável/mensagem para testes:** Execute as variáveis através do botão indicado na figura abaixo e ver o resultado em uma tabela que é aberta na parte inferior do editor. Para fechar a tabela, basta clicar novamente no botão de **"Executar"**.

**Observação:** para que as mensagens sejam enviadas apenas uma vez por dia, deve-se ligar o parâmetro **"Forçar envio único de Mens. diária BI Móvel? - MSDFORCUNDIA"**, porém, a mensagem deve possuir apenas um agendamento diário. Desse modo, caso haja um envio programado para depois da hora do processamento atual, este não será enviado.

#### Editor Avançado

Clicando no botão Assistente de Query, existe alguns recursos que visam facilitar a edição do código, tais como:

**Colorização da sintaxe:** As variáveis e as palavras reservadas das linguagens de script, SQL e Java ficam destacadas por cores de acordo com sua categoria, facilitando a visualização do código-fonte.

**Execução de SQL sem parâmetros:** O ícone **"Executar"** faz a query em SQL selecionada no editor, exibindo o resultado na aba **"Resultado"**.

![Imagem 6: Execução de SQL sem parâmetros: O ícone "Executar" faz a query em SQL selecionada no editor, exibindo o resultado na…](https://ajuda.sankhya.com.br/hc/article_attachments/4404090019991)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593534-Editor-de-Vari%C3%A1veis#top)

### Aba Referência

![Imagem 7: Aba Referência](https://ajuda.sankhya.com.br/hc/article_attachments/4404090027031)

Nessa aba, tem-se a expressão que define a data de referência para a composição do histórico de valores da variável.

Por exemplo, se uma variável tem a data de referência com variação mensal e o período de atualização é diário, a cada atualização que ocorre durante o mês o valor da variável sofrerá uma modificação. Quando o mês muda, uma nova entrada na tabela de variáveis resolvidas é criada no banco e o último valor do mês anterior, é mantido para fins de histórico, como data de referência para aquele mês.

Esse campo deve ser preenchido com uma das funções de data e tempo abaixo, finalizando com ponto e vírgula:

1. anual();
2. mensal();
3. quinzenal();
4. semanal();
5. diaria();
6. porHora();
7. porMinuto();
8. todoMes(mês);                            Exemplo: todoMes(5);
9. todoDia(dia);                                Exemplo: todoDia(20);
10. todoDiaSemana(diaSemana)                Exemplo: todoDiaSemana("SEG"); os dias da semana devem ser informados da seguinte maneira: "DOM", "SEG", "TER", "QUA", "QUI", "SEX" e "SAB".

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593534-Editor-de-Vari%C3%A1veis#top)

### Aba Campos Associados

![Imagem 8: Aba Campos Associados](https://ajuda.sankhya.com.br/hc/article_attachments/4404090035607)

Trabalhando com uma variável que possua saída do tipo tabela, informe os campos para cada coluna que será gerada. O cadastro de campos é feito previamente através da tela [Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106293).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593534-Editor-de-Vari%C3%A1veis#top)

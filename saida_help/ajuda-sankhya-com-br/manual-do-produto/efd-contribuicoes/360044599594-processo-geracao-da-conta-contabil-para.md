---
id: "360044599594"
titulo: "Processo Geração da Conta Contábil para EFD - Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > EFD Contribuições"
atualizado_em: "2026-09-30T11:14:49Z"
rotulos: ["Configuração", "Impostos", "Contabilização", "Geração da Conta Contábil para EFD - Contribuições manual", "Estoque", "Financeiro", "Geração de Conta Contábil para EFD-Contribuições", "EFD Contribuições"]
---

# Processo Geração da Conta Contábil para EFD - Contribuições

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#oque) [Formas de Buscar a Conta Contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#formas)    ↳ [Opção Cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#cadastros)    ↳ [Opção Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#contabilizacao) [Geração do Registro 0500](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#reg0500) | [Geração do Registro 0600](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#reg0600) [Registros Obrigatórios na Geração da Conta Contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#obrigatorios) [Observações Importantes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#observacoes) |
| --- | --- |

## O que é e para que serve

O **Processo Geração da Conta Contábil para EFD - Contribuições** gera a conta contábil utilizada nos registros da **Escrituração Fiscal Digital (EFD) - Contribuições**.

A conta contábil é buscada em outras telas do sistema — **Empresa**, **Cadastro de Produtos**, **Cadastro de Serviços**, **Tipo de Operação (TOP)** e **Plano de Contas** — e não na tela onde o arquivo é gerado. Ela é pré-requisito para a geração de determinados registros do arquivo (veja a lista completa em [Registros Obrigatórios na Geração da Conta Contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#obrigatorios)); esses registros são gerados na tela **EFD - Contribuições PIS/COFINS**.

## Formas de Buscar a Conta Contábil

Existem duas formas de pesquisar a conta contábil, e cada empresa só pode ter uma definição de busca configurada. Na rotina **Empresa**, aba **EFD - Escrituração Fiscal Digital**, o campo **Tipo da Conta Contábil para EFD** disponibiliza as opções:

- **Cadastros**
- **Contabilização**

### Opção Cadastros

Ao selecionar **Cadastros**, configure a **Conta Contábil para EFD**. Na geração do arquivo da EFD Contribuições, o sistema segue uma ordem de análise para buscar o código vinculado ao campo **Conta Contábil para EFD**.

Para produtos e serviços, a sequência de análise é:

1. Produto › **Cadastro de Produtos**, aba **Impostos / Informações por empresa**; Serviço › **Cadastro de Serviços**, aba **Configurações por Empresa**
2. Produto › **Cadastro de Produtos**, aba **Impostos**; Serviço › **Cadastro de Serviços**, aba **Impostos**
3. **Cadastro de Grupos de Produtos/Serviços**, aba **Impostos por Empresa**
4. **Cadastro de Grupos de Produtos/Serviços**, aba **Geral**
5. **Tipo de Operação - TOP**, aba **Impostos**

Para os registros referentes aos financeiros — como F100, F500 e F525 — a hierarquia segue esta ordem:

1. **Cadastro de Natureza de Receitas e Despesas**, aba **PIS/COFINS**
2. **Tipo de Operação - TOP**, aba **Impostos**

Para os registros referentes ao imobilizado — como F120 e F130 — a ordem de hierarquia é:

1. **Cadastro de Produtos**, aba **Impostos**
2. **Tipo de Operação - TOP**, aba **Impostos**

### Opção Contabilização

Ao adotar **Contabilização**, na geração do registro o sistema verifica a contabilização do documento em questão, ordenando primeiro pelo lançamento na contabilidade de maior valor para a conta configurada no grupo de natureza para EFD definido.

A determinação da conta a ser gerada no arquivo segue a movimentação do registro em foco — o sistema localiza, na contabilização dos registros, as contas contábeis configuradas com a natureza para EFD:

- Para os registros referentes aos movimentos de Estoque contabilizados pela contabilização do Estoque ou do Livro (`TCBINT.ORIGEM = 'E' ou 'L'`)
- Para os registros referentes aos movimentos do Financeiro contabilizados pela contabilização do Financeiro, Baixa, Movimentação Bancária, Renegociação e Juros (`TCBINT.ORIGEM = 'F', 'B', 'M', 'R', 'J'`)
- Para os registros referentes às movimentações do Imobilizado, a busca da conta segue a contabilização que ocorreu no Produto ou no Bem em questão

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#sumario)

## Geração do Registro 0500

O registro 0500 é gerado conforme a configuração do **Cadastro de Plano de Contas** da empresa que estiver gerando a EFD - Contribuições. Caso sejam gerados os registros das filiais no arquivo, também é gerado o plano de contas das filiais. Só são geradas as contas contábeis que já foram geradas nos registros do arquivo.

A tabela a seguir detalha a composição de cada campo do registro 0500:

| **Campo** | **Descrição** | **Fixo** | **Origem (TCBPLA)** |
| --- | --- | --- | --- |
| 1 | Texto fixo contendo `0500`. | `0500` |  |
| 2 | Data da inclusão/alteração. |  | Conforme gravado no banco de dados, campo **Referência de ativação** (`DTINCLUSAO`). |
| 3 | Código da natureza da conta/grupo de contas: 01 - Contas de ativo; 02 - Contas de passivo; 03 - Patrimônio líquido; 04 - Contas de resultado; 05 - Contas de compensação; 09 - Outras. |  | Busca do campo **Grupo de Conta** conforme cadastro. |
| 4 | Indicador do tipo de conta: S - Sintética (grupo de contas); A - Analítica (conta). |  | Busca do campo **Analítica**. |
|  | S - Sintética (grupo de contas); |  |  |
|  | A - Analítica (conta). |  |  |
| 5 | Nível da conta analítica/grupo de contas. |  | Conforme o nível em que a conta contábil foi cadastrada. |
| 6 | Código da conta analítica/grupo de contas. |  | Busca do campo **Conta contábil**. |
| 7 | Nome da conta analítica/grupo de contas. |  | Busca do campo **Descrição**. |
| 8 | Código da conta correlacionada no Plano de Contas Referenciado, publicado pela Receita Federal do Brasil (RFB). |  | Busca do campo **Cód. Conta Ref.**. |
| 9 | CNPJ do estabelecimento, no caso de a conta informada no campo `COD_CTA` ser específica de um estabelecimento. |  | É gerado o código do CNPJ da empresa dona do plano de contas, somente nos casos em que o arquivo está sendo gerado para diversas filiais com planos de contas diferentes. |

Exemplo do registro 0500 gerado no arquivo:

![Imagem 1: Exemplo do registro 0500 gerado no arquivo:](https://ajuda.sankhya.com.br/hc/article_attachments/42432043355287)

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#sumario)

## Geração do Registro 0600

O registro 0600 só é gerado para as empresas que buscam a conta contábil pela opção **Contabilização**, sendo que a contabilização dos movimentos deve ser por Centro de Resultado. Para as empresas que geram a conta contábil de forma fixa (opção **Cadastros**), este registro não é gerado.

Exemplo do registro 0600 gerado no arquivo:

![Imagem 2: Exemplo do registro 0600 gerado no arquivo:](https://ajuda.sankhya.com.br/hc/article_attachments/42432056797847)

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#sumario)

## Registros Obrigatórios na Geração da Conta Contábil

Abaixo estão os blocos e seus respectivos registros nos quais a geração da conta contábil é obrigatória. Cada registro utiliza uma listagem de naturezas das contas contábeis para buscar a conta contábil — essas naturezas são indicadas na rotina **Cadastro de Plano de Contas**, aba **Geral**, campo **Natureza para EFD**.

| **Bloco A** | **Bloco C** | **Bloco C** | **Bloco D** | **Bloco F** | **Bloco P** | **Bloco 1** |
| --- | --- | --- | --- | --- | --- | --- |
| A170 | C170 | C481 | D100 | F100-Orig. Financ. | P100 | 1900 |
|  | C175 | C485 | D101 | F100-Orig.Jur./Mult. |  |  |
|  | C181 | C491 | D105 | F120 |  |  |
|  | C185 | C495 | D201 | F130 |  |  |
|  | C191 | C501 | D205 | F500 |  |  |
|  | C195 | C505 | D501 | F525 |  |  |
|  | C381 | C810 | D505 | F550 |  |  |
|  | C385 | C870 | D601 | F650 |  |  |
|  | C396 | C880 | D605 |  |  |  |

**ℹ️ Nota**

As contas contábeis do Bloco M não são geradas, pois não há apuração do registro no sistema. Informe as contas diretamente no validador.

Cada lista de naturezas utilizada na busca da conta contábil é:

| **Lista** | **Naturezas** |
| --- | --- |
| Lista 01 | 01 - Receita de Vendas, Receitas prestação serviços, Receitas financeiras, Receitas não operacionais 02 - Receitas de vendas não tributadas 04 - Custo de Produtos/Serviços prestados por pessoa jurídica 06 - Despesas Diversas 08 - Estoques, Matéria prima e material de embalagem 09 - Aquisições de bens para revenda, aquisições de insumos para industrialização |
| Lista 02 | 01 - Receita de Vendas, Receitas prestação serviços, Receitas financeiras, Receitas não operacionais 02 - Receitas de vendas não tributadas |
| Lista 03 | 03 - Receita de Fretes, Receita de transportes rodoviário de cargas 05 - Custos com transportes 06 - Despesas Diversas 07 - Despesas de fretes contratados e despesas de comercialização 08 - Estoques, Matéria prima e material de embalagem 09 - Aquisições de bens para revenda, aquisições de insumos para industrialização 11 - Máquinas e Equipamentos do Ativo Imobilizado, ativo fixo, etc. |
| Lista 04 | 03 - Receita de Fretes, Receita de transportes rodoviário de cargas |
| Lista 05 | 06 - Despesas Diversas 07 - Despesas de fretes contratados e despesas de comercialização |
| Lista 06 | 12 - Despesas de Aplicações Financeiras, Despesas Financeiras (juros/Multas) 13 - Receitas de Aplicações Financeiras, Receitas Financeiras (juros/Multas) |
| Lista 07 | 10 - Encargos de depreciação do período, encargos de amortização do período, etc. |
| Lista 08 | 11 - Máquinas e Equipamentos do Ativo Imobilizado, ativo fixo, etc. |
| Lista 09 | 01 - Receita de Vendas, Receitas prestação serviços, Receitas financeiras, Receitas não operacionais 02 - Receitas de vendas não tributadas 03 - Receita de Fretes e Receita de transportes rodoviários de cargas |
| Lista 10 | Não é possível mapear este registro pela Contabilização. O sistema sempre busca a conta contábil configurada nas **Preferências da Empresa**, aba **Reintegra Previdência**, campo **Código Conta Contábil**. |

Para a **Lista 08**, informe a conta contábil que será gerada no registro F130 no campo **Conta Contábil para EFD** (tela **Cadastro de Produtos**, aba **Impostos**).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599594-Processo-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-Contribui%C3%A7%C3%B5es#sumario)

## Observações Importantes

- Os registros que apresentarem a conta contábil sem configuração são gravados no log de erro. O arquivo de log tem o mesmo nome do arquivo gerado, mas com a extensão `.erro` — por exemplo: "REGISTRO: A170. NUNOTA: 475701. SEQUENCIA: 1. ORIGEM: E. Conta Contábil está vazia." Nesse caso, acesse o registro em questão, verifique a contabilização do documento de origem e analise as configurações definidas na busca da conta contábil.
- Na geração da conta contábil nos registros EFD - Contribuições, informe o código da conta contábil credora ou devedora principal — a conta principal é aquela que recebeu o maior valor na contabilização da operação.
- É enviado no arquivo EFD - Contribuições o plano de contas da empresa, somente das contas que obtiveram registros no arquivo. Empresas que também entregam a **Escrituração Contábil Digital (ECD)** devem informar as mesmas contas contábeis, de forma que seja enviado o mesmo plano de contas.
- Na geração da EFD Contribuições, quando se trata de uma empresa com várias filiais, o sistema verifica se cada filial está configurada com o mesmo **Tipo de Conta Contábil para EFD** da matriz.

**⚠️ Atenção**

Caso as filiais não estejam configuradas com o mesmo **Tipo de Conta Contábil para EFD** da matriz, o sistema exibe a mensagem "As empresas filiais da matriz X não possuem a mesma configuração para o campo Tipo da Conta Contábil para EFD e isso poderá impedir que o sistema busque corretamente as contas do arquivo. Deseja continuar?". Ao optar por **Sim**, a geração continua, mantendo o risco de busca incorreta das contas. Ao optar por **Não**, padronize o campo **Tipo de Conta Contábil para EFD** para todas as filiais nas **Preferências da Empresa**, aba **EFD - Escrituração Fiscal Digital**.

A relação entre o Plano de Contas e os registros EFD esperados pelo sistema para a geração das contas contábeis é:

| **Registros** | **Naturezas (lista)** |
| --- | --- |
| A170, C170, C191, C195, C396, C481, C485, C501, C505, F100\_NOTA, F100\_FINANCEIRO | 1, 2, 3, 4, 6, 7, 8, 9 |
| C175, C181, C185, C381, C385, C491, C495, C810, C870 | 1, 2 |
| D100, D101, D105 | 3, 5, 6, 7, 8, 9, 11 |
| D201, D205, D601, D605 | 3 |
| D501, D505 | 6, 7 |
| F500, F510, F525, F550, F560, 1900 | 1, 2, 3 |
| F100\_MULTA, F100\_JURO, F100\_DESCONTO | 1, 2, 6, 7, 12, 13 |

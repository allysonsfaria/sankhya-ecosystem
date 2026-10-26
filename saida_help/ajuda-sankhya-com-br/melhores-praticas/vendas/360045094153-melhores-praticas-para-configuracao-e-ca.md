---
id: "360045094153"
titulo: "Melhores Práticas para Configuração e Cálculo do ICMS-ST Extra Nota (GNRE - Venda)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094153-Melhores-Pr%C3%A1ticas-para-Configura%C3%A7%C3%A3o-e-C%C3%A1lculo-do-ICMS-ST-Extra-Nota-GNRE-Venda"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T15:51:31Z"
rotulos: ["#validadoElisangela", "Configuração", "Impostos", "Vendas", "GNRE", "Financeiro", "Configurar Tipo de Título e GNRE para ST Extra Nota", "Marcar configurações nos tipos de operação e negociação", "Criar e aplicar fórmulas para cálculo e lançamento de ST Extra Nota", "ICMS-ST"]
---

# Melhores Práticas para Configuração e Cálculo do ICMS-ST Extra Nota (GNRE - Venda)

O cálculo de 'ST Extra Nota' é feito em estados, que comercializam seus produtos para fora de seu território, sendo a Nota Fiscal emitida com tributação normal dos produtos, porém a ST é recolhida extra nota. Este recolhimento deverá ser feito pela empresa vendedora e comprovado na barreira estadual, sendo este valor restituído pelo comprador.

Veja Como configurar o Calculo de ICMS-ST Extra Nota- Processo válido para Movimentação de **VENDA.**

![Imagem 1: Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título:](https://ajuda.sankhya.com.br/hc/article_attachments/19196609263255) Financeiro » Arquivos » Cadastros » Tipos de Título » **Tipos de Título:**

- Crie um Tipo de Titulo, que indique a GNRE.

![Imagem 2: Configurações » Avançado » Preferências:](https://ajuda.sankhya.com.br/hc/article_attachments/19196594283159) Configurações » Avançado » Preferências:

- **Tipo de Título p/indicar GNRE p/S.T. - TIPTITGNREST':** Configure esse parâmetro com o tipo de título que será usado para gerar a GNRE.  Se nesse parâmetro houver o tipo de título informado, cuja o mesmo possua cadastro e fórmula na tela Fórmula p/ Parcela Independente ou Tipo de Negociação, o sistema irá ignorar a fórmula contida.

![Imagem 3: Tipo de Título p/indicar GNRE p/S.T. - TIPTITGNREST': Configure esse parâmetro com o tipo de título que será usado para…](https://ajuda.sankhya.com.br/hc/article_attachments/19196609279767)

![Imagem 4: Comercial » Preferências » Empresa:](https://ajuda.sankhya.com.br/hc/article_attachments/19196594293271) Comercial » Preferências » **Empresa:**

- Aba: Livros Fiscais.
- Campo: Gerar GNRE p/ ST?:[Marcado]

Comercial » Preferências » Empresa » Aba Propriedade

![Imagem 5: Comercial » Preferências » Empresa » Aba Propriedade](https://ajuda.sankhya.com.br/hc/article_attachments/20582551956375)

Após o lançamento e a aprovação da nota que resulte no cálculo do DIFAL, é necessário gerar o lote na tela a seguir. É importante observar que, caso alguma das configurações mencionadas acima esteja ausente, as informações financeiras relacionadas a essa nota não serão exibidas na tela para a geração do lote.

![Imagem 6: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP : 'No cadastro da ''TOP'' utilizada na operação, na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/19196594294167) Comercial » Arquivo » Cadastros » **Tipos de Operação - TOP**: 'No cadastro da ''TOP'' utilizada na operação, na aba ''Livros Fiscais'' marque a opção **''Gerar GNRE p/ ST'**

- Aba: Validações
- Campo: Gerar GNRE p/ ST:[Marcado]

![Imagem 7: Comercial » Arquivo » Cadastros » Tipos de Negociação](https://ajuda.sankhya.com.br/hc/article_attachments/19196609295255) Comercial » Arquivo » Cadastros » Tipos de Negociação

Se o campo Fórmula do Tipo de Negociação estiver em branco, automaticamente o sistema passa a olhar para a tela Fórmula p/Parcela Independente. Se estiver utilizando a tela Fórmulas p/ Parcela Independente, a opção "Financeiro para GNRE" deve estar MARCADA.

- Crie um Tipo de Negociação, na aba Parcelas, faça a seguinte configuração:

2(Duas) Parcelas ou mais, sendo: 1ª Parcela, informar Prazo, Banco, Percentual 100%.

No campo: Tipo de Titulo = [Preencher com o código do Tipo de Titulo, do 1º item]

No campo Tipo de Negociação = o campo "Tipo de Financeiro (REC/DESP) deve estar selecionado com a opção "N-Usar da Natureza Padrão."

No campo: 'Formula', use a seguinte expressão: **VLRSTEXTRANOTATOT**

- As demais parcelas, podem ser criados sem fórmula e rateado o percentual de acordo com a quantidade de parcelas, que será considerado para formar o Valor total da Nota.

![Imagem 8: Comercial » Arquivo » Cadastros » Observações para Notas ( Opcional )](https://ajuda.sankhya.com.br/hc/article_attachments/19196609296023) Comercial » Arquivo » Cadastros » Observações para Notas (Opcional)

- Crie uma observação.'Vincular DAE/GNRE' -devera estar marcado.

![Imagem 9: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS:](https://ajuda.sankhya.com.br/hc/article_attachments/19196609300503) Comercial » Arquivo » Cadastros » Alíquotas » **Alíquotas de ICMS:**

Aba: **Geral**

- Tributação: 00-Tributada Integralmente
  Alíquota= [Informe o Percentual]
  Modalidade BC ICMS = [Valor da Operação]
  Observação= [**Preencher com o código da Observação, do 6º item**]

Aba: **Substituição Tributaria**

- Calcula ST extra nota com base em MVA na VENDA(Não utilizar em Compras) = [**Marcado**]
- Informar a ''Margem Lucro(MVA)''
- Informar a ''Aliq.Subst. Tributária'''

Os demais campos não são obrigatórios e não interferem no processo;

![Imagem 10: No cadastro do ''Estado'' do ''Parceiro'' preencher o campo ''Cód. Parceiro Secretaria da Receita Estadual'':](https://ajuda.sankhya.com.br/hc/article_attachments/19196609304855)No cadastro do ''Estado'' do ''Parceiro'' preencher o campo ''Cód. Parceiro Secretaria da Receita Estadual'':

![Imagem 11: No cadastro do ''Estado'' do ''Parceiro'' preencher o campo ''Cód. Parceiro Secretaria da Receita Estadual'':](https://ajuda.sankhya.com.br/hc/article_attachments/19196594313367)

**Vejamos o Lançamento de uma Nota de VENDA:**

![Imagem 12: Os valores de ST Extra Nota, serão apresentados em campos próprios, nos itens e no Rodapé.](https://ajuda.sankhya.com.br/hc/article_attachments/19196609263255) Os valores de ST Extra Nota, serão apresentados em campos próprios, nos itens e no Rodapé.

![Imagem 13: Serão geradas 2 linhas, sendo uma considerando a GNRE do tipo 'Despesa' no Financeiro e a outra, considerando Receita…](https://ajuda.sankhya.com.br/hc/article_attachments/19196594283159)Serão geradas 2 linhas, sendo uma considerando a GNRE do tipo 'Despesa' no Financeiro e a outra, considerando Receita no Financeiro do Total da Nota.

**Parâmetros:**

1. CODOBSGARANTIDO = [Preencher com o código da Observação, do 1º item]
2. CODIMPGARANTIDO = [Preencher com o código do Imposto, do 2º item]
3. TIPTITGNREST = [Não poderá conter o mesmo título do 'Garantido Integral'] - No caso da compra o parâmetro TIPTITGNREST não pode ser igual ao tipo de titulo informando na aba parcelas do Tipo de Negociação criado para parcela que contenha a fórmula; Se nesse parâmetro houver o tipo de título informado, cuja o mesmo possua cadastro e fórmula na tela Fórmula p/ Parcela Independente ou Tipo de Negociação, o sistema irá ignorar a fórmula contida.

**-Veja também:**

[Melhores Práticas para Configuração e Cálculo do Garantido Integral (GNRE - Compra).](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580314)

---
id: "44455691767191"
titulo: "Análise de Rentabilidade: o que compõe o Gasto Variável"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44455691767191-An%C3%A1lise-de-Rentabilidade-o-que-comp%C3%B5e-o-Gasto-Vari%C3%A1vel"
trilha: "Service Desk | área do colaborador  > Melhores práticas"
atualizado_em: "2026-10-22T21:07:31Z"
---

# Análise de Rentabilidade: o que compõe o Gasto Variável

**Mensagem**

Na Análise de Rentabilidade de um pedido ou nota, o **Gasto Variável** aparece com valor, mesmo com o **% C. Variável** zerado nas Preferências do Gerente On-Line (GOL).

**Situação**

Ao abrir a Análise de Rentabilidade (por exemplo, no Portal de Vendas), o Gasto Variável mostra valor e percentual diferentes de zero, e o percentual muda de um documento para outro. Isso acontece mesmo com o % C. Variável configurado como 0,00 no GOL.

**Solução**

O Gasto Variável não é só o % C. Variável. Ele soma os gastos que acompanham a venda, conforme as configurações abaixo. Para identificar o que está compondo o valor e, se quiser, ajustar:

Acesse a tela  **Gerente On-Line - GOL**, abra as **Preferências** e selecione a aba **Margem de Contribuição**.
 Na seção  **Comissão**, verifique se a opção está ligada. Se estiver, a comissão entra no Gasto Variável, conforme o modo escolhido.

**Fixa**: usa o percentual informado ao lado da opção. 
**Nota**: usa a comissão gravada no pedido (campos Comissão e Comissão Gerente do cabeçalho); o percentual informado ao lado é ignorado. 
**Vendedor**,  **Produto** ou **Tipo de Negociação**: usa o percentual desses cadastros. Para não considerar a comissão, desligue a opção.
 Em  **Configurações por Empresa**, confira os percentuais da empresa no período: % C. Variável, % C. Variável sem ST, % Outros, % PIS, % COFINS, % CSLL, % IRPJ e % CPP.
 No cadastro do  **Produto**, aba **Impostos**, verifique o campo  **Considerar débito ICMS nas consultas gerenciais?**. **Sim** ou em branco: o ICMS do documento entra no Gasto Variável. **Não**: o ICMS não entra.
 Na tela  **Preferências**, verifique o parâmetro  **Considerar débito de PIS/COFINS/CSSL na M.C.?** (GOL-PISCOFINS).  **Ligado**: são usados o PIS, a COFINS e os demais impostos calculados no próprio documento. **Desligado**: são usados os percentuais da empresa (passo 3). Eles só entram se a TOP estiver marcada com **Tem PIS**, **Tem COFINS** e  **Tem CSLL** (aba Impostos). O IRPJ e a CPP seguem a marcação  **Tem PIS**.
 Salve as alterações.

**(7)** Reabra a Análise de Rentabilidade e confira o novo valor do Gasto Variável.

**Importante:** essas configurações valem para todos os usuários. Elas alteram ao mesmo tempo a Análise de Rentabilidade e as análises do GOL, inclusive de períodos anteriores. ICMS, PIS e COFINS são impostos sobre a venda: retirá-los do cálculo faz a margem parecer maior do que realmente é.

**Causa**

O Gasto Variável da Análise de Rentabilidade é a soma de:

- comissão, quando ligada no GOL;
- ICMS, quando o produto está configurado para considerá-lo;
- PIS, COFINS, CSLL, IRPJ e CPP, vindos do documento ou dos percentuais da empresa, conforme o parâmetro do passo 5;
- partilha do Simples Nacional, quando a empresa usa essa opção;
- ST e IPI dos itens, quando o Faturamento Personalizado é **Faturamento Bruto**;
- frete por conta do emitente (CIF), embalagem e despesas destacadas na nota;
- percentuais da empresa (% C. Variável, % C. Variável sem ST e % Outros) e, se os parâmetros estiverem ligados, os percentuais de custo variável do vendedor, do parceiro, da região ou do título.

Como a comissão e os impostos são próprios de cada documento, o percentual muda de um pedido para outro. Por exemplo, um pedido de R$ 1.000,00 com 2% de comissão e R$ 120,00 de ICMS tem Gasto Variável de R$ 140,00 (14%).

**Observação:** se o parâmetro  **Função p/ Cálculo Gasto Variável Central/Portal** (CALGAVARCENPORT) tiver uma função personalizada informada, o Gasto Variável de pedidos e vendas é calculado por essa função. A opção **Gasto variável personalizado** das Preferências do GOL define onde a função vale.

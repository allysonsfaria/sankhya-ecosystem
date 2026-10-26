---
id: "360042639634"
titulo: "600 Rejeição: CSOSN incompatível na operação com Não Contribuinte. (NT2015/003)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042639634-600-Rejei%C3%A7%C3%A3o-CSOSN-incompat%C3%ADvel-na-opera%C3%A7%C3%A3o-com-N%C3%A3o-Contribuinte-NT2015-003"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:46Z"
rotulos: ["ERRONF", "#RevisadoBraga", "Configuração", "Parceiro", "NF-e", "Simples Nacional", "SEFAZ", "Impostos", "CFOP", "600", "Corrigir CSOSN no cadastro", "Inutilizar e refazer nota", "CSOSN inválido para não contribuinte", "600 - Rejeição", "NT 2024.003 v 1.03", "[600 - Rejeição]: CSOSN incompatível na operação com Não Contribuinte. (NT2015/003)", "NT 2024.003 v 1.03 - 01/10/2025 - NFe", "NT 2024.003 v 1.03 - NF-e"]
---

# 600 Rejeição: CSOSN incompatível na operação com Não Contribuinte. (NT2015/003)

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16504236007191) **MENSAGEM:**

600 Rejeição: CSOSN incompatível na operação com Não Contribuinte.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16504223745687) SOLUÇÃO:**

Sempre que o emissor da NF-e estiver sobre o Regime de Tributação Simples Nacional, com Destinatário Não Contribuinte do ICMS (indIEDest = 9), utilize os CSOSN de ICMS previstos na regra de validação da Sefaz, que são 102, 103, 300, 400 e 500.

![Imagem 3: Confirme se o parceiro possui a classificação fiscal " Consumidor Final não contribuinte". Para isso, acesse:](https://ajuda.sankhya.com.br/hc/article_attachments/16504223747607) Confirme se o parceiro possui a classificação fiscal "**Consumidor Final não contribuinte".** Para isso, acesse:

- **"[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Caminho de acesso: Configurações » Cadastros) » Aba **"Fiscal" »** Campo "**Classificação ICMS"**.

Caso essa classificação esteja incorreta, realize o ajuste desse cadastro, inutilize a NF-e e refaça o faturamento.

![Imagem 4: Caso a classificação seja consumidor final não contribuinte , verifique/corrija a informação CSOSN para um código…](https://ajuda.sankhya.com.br/hc/article_attachments/16504223751319) Caso a classificação seja consumidor final não contribuinte**,** verifique/corrija a informação CSOSN para um código válido nessa operação (**102, 103, 300, 400 ou 500** - informação a ser validada junto ao Contador)**:**

- Abra a nota através da Central de Vendas/Compras, selecione na grade Itens o primeiro produto.
- No botão **"Outras Opções"** [...] >> **"Consultar/alterar dados dos impostos do Item"** verifique se foi gerada uma linha para o Imposto ICMS.
- Verifique se existe informação no campo "**CST/CSOSN"** (Siga com o passo a passo para todos os demais itens da nota, até que seja localizado o item em que essa informação esteja incorreta).

![Imagem 5: Verifique se existe informação no campo " CST/CSOSN" (Siga com o passo a passo para todos os demais itens da nota, até…](https://ajuda.sankhya.com.br/hc/article_attachments/14598712114071)

- Identificado os itens onde a informação de CST/CSOSN encontra-se incorreta, busque na linha desse item pela informação "**Cód.Alíq.ICMS"** (Caso essa informação não exista no seu layout, necessário adicioná-la pelo Configurador de Layout da Nota).
- Acesse a tela "**[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas) e digite o ID localizado no item 4 ao lado esquerdo da tela ("Localizar"), pressione ENTER: será apresentado na tela a alíquota responsável pela tributação do item analisado.
- Nessa alíquota acesse a aba SIMPLES NACIONAL e ajuste o campo "**Código de Situação da Operação no Simples Nacional - CSOSN**".

![Imagem 6: Inutilize a nota rejeitada, refaça o lançamento, refaça a conferência da informação CST/CSOSN conforme Item 2 e…](https://ajuda.sankhya.com.br/hc/article_attachments/16504236017431) Inutilize a nota rejeitada, refaça o lançamento, refaça a conferência da informação CST/CSOSN conforme Item 2 e confirme a nova nota lançada.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16504223758231) CAUSA:**

Quando for emitida uma NF-e para Destinatário Não Contribuinte do ICMS (indIEDest = 9) e com o Código de Situação da Operação - Simples Nacional (CSOSN) diferente da relação abaixo, será retornado a rejeição "600 - CSOSN incompatível na operação com Não Contribuinte":

**102** - Tributação SN sem permissão de crédito;
**103** - Tributação SN, com isenção para faixa de receita bruta;
**300** - Imune;
**400** - Não tributada pelo Simples Nacional;
**500** - ICMS cobrado anteriormente por substituição tributária ou por antecipação.

Exceções a regas:

- A regra de validação 600 não se aplica para NF-e de entrada (tpNF = 0);
- A regra de validação 600 não se aplica nas operações com CFOP de conserto ou reparo (CFOP 5915, 5916, 6915 e 6916) ou de remessa para demonstração dentro do Estado (CFOP 5912 e 5913);
- A regra de validação 600 não se aplica, em produção, para NF-e com data de emissão anterior a 01/07/2016.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16504223760791) OBSERVAÇÃO:**

([NT2015/003](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=zJGzcwysHPo=)) - Nota Técnica:

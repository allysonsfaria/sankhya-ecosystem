---
id: "31754457773463"
titulo: "Divergência no preenchimento da tag <pMVAST> no XML em relação à regra de alíquota de ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31754457773463-Diverg%C3%AAncia-no-preenchimento-da-tag-pMVAST-no-XML-em-rela%C3%A7%C3%A3o-%C3%A0-regra-de-al%C3%ADquota-de-ICMS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:32:25Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "ICMS", "Impostos", "<pMVAST> no XML", "\"Tipo de Cálculo de ST Específico\"", "valor diferente do tipo \"(0)", "Divergência no preenchimento da tag"]
---

# Divergência no preenchimento da tag <pMVAST> no XML em relação à regra de alíquota de ICMS

**SITUAÇÃO:**

Ao analisar o XML das notas fiscais, é possível identificar divergências no valor apresentado na tag **"pMVAST"** em relação ao valor previsto/cadastrado na regra de alíquota de ICMS, especificamente na aba **"Substituição Tributária"**.

A situação ocorre quando o campo **"Tipo de Cálculo de ST Específico",** na aba **"Substituição Tributária",** da tela **"Alíquota de ICMS** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS) está com valor diferente do tipo **"(0) - Não específico (regra geral)"**. Nesses casos, o sistema não valida o campo **"Margem Lucro (MVA)"**, resultando em diferença entre o valor cadastrado e o valor apresentado na tag **"pMVAST"** do XML.

**SOLUÇÃO**

Atualmente, se o campo Tipo de Cálculo de ST Específico estiver configurado com uma opção **diferente do tipo** (0) - Não específico (regra geral)**, o sistema não faz a validação do campo: Margem Lucro (MVA).** Nesse caso, é utilizado o valor do campo **"IVA" para a construção da tag.** Importante destacar que o campo IVA preenche a tabela TGFDIN.

**Observação:** para encontrar o campo IVA, acesse as centrais e, dentro da grade de itens, clique no botão **"Outras Opções".** Em seguida, selecione a opção **"Consultar/Alterar dados do imposto do item"**.

#### **(1)** Caso de uso Base de cálculo de ICMS: 826,58   Calculo do IVA = 7,32 / 100 = 0,0732 + 1 = 1,0732 >> este valor é o apresentado na TGFDIN (1,07).   Base de cálculo do ST: 826,58 \* 1,0732 = 887,0556

![Imagem 1: (1) Caso de uso Base de cálculo de ICMS: 826,58 Calculo do IVA = 7,32 / 100 = 0,0732 + 1 = 1,0732 >> este valor é o…](https://ajuda.sankhya.com.br/hc/article_attachments/38632351293719)

Por outro lado, se no campo Tipo de Cálculo de ST Específico for usado o tipo (0) - Não específico (regra geral), o valor da tag, a ser levado no XML, será o mesmo que estiver cadastrado no campo Margem Lucro (MVA). 

![Imagem 2: Por outro lado, se no campo Tipo de Cálculo de ST Específico for usado o tipo (0) - Não específico (regra geral) , o…](https://ajuda.sankhya.com.br/hc/article_attachments/38632307232407)

Assim, deve ser validado internamente a necessidade de uso do campo Tipo de Cálculo de ST Específico com um valor diferente do tipo (0).

Pois, caso seja diferente de zero e o cenário de cálculo acima não atenda ao esperado pela empresa, deverá ser verificado se existe algum embasamento legal que justifique essa configuração do campo. Ou, caso haja interesse, avaliar juntamente com o time de Unidade a possibilidade alguma personalização do processo.

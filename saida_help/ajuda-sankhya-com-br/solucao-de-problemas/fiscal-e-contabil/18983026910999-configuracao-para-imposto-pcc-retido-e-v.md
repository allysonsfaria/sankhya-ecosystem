---
id: "18983026910999"
titulo: "Configuração para Imposto PCC retido, e valor ir para o campo Valor Agregado no REINF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18983026910999-Configura%C3%A7%C3%A3o-para-Imposto-PCC-retido-e-valor-ir-para-o-campo-Valor-Agregado-no-REINF"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:51:55Z"
rotulos: ["Configuração", "Movimentação Financeira", "Impostos", "Financeiro", "Configuração na tela Impostos", "Imposto PCC no REINF", "Código de Receita essencial", "Reinf"]
---

# Configuração para Imposto PCC retido, e valor ir para o campo Valor Agregado no REINF

#### Configuração para o Imposto PCC retido, ir para o campo Valor Agregado no REINF.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18982982316567)SOLUÇÃO:**

Para que ao gerar o REINF o imposto do PCC vá de maneira agrupada para o campo Agregados, precisa ser feita uma configuração na tela Impostos, que o no caso é o preenchimento do campo "código da receita" e o Tipo de Imposto precisa ser OUTROS ou PIS/COFINS/CSLL separadamente. 

Preencha as outras informações normalmente com base na rotina da Empresa, determinar a retenção se na Central ou direto na Movimentação Financeira.
 
**Observações:**

É obrigatório para que os valores do PCC retido vá para o campo Valor Agregado o código da Natureza de rendimento e também o Código Receita estar preenchido de acordo com o mesmo no cadastro das preferências da Empresa, aba EFD-REINF, campo Código de Receita para atribuir Agregado/CSRF/PCC.
 
O código que vamos preencher no campo "Código de Receita para atribuir Agregado/CSRF/PCC" nas preferências da empresa, deve ser previamente cadastrado na tela "Códigos de Receita - DARF".

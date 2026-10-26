---
id: "37230519827223"
titulo: "E0708 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37230519827223-E0708-Rejei%C3%A7%C3%A3o-Se-a-al%C3%ADquota-for-informada-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:45Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Alíquotas de ICMS", "Erro", "Lançamento da nota", "alíquotas com intervalo de 0% a 100%", "rejeitada pela SEFAZ", "Emissão de NF-e ou NFC-e", "Alíquota tributária com valor divergente", "documento fiscal com alíquota tributária inválida"]
---

# E0708 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%

**MENSAGEM:**

E0708 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%

**SITUAÇÃO:**

Ao emitir um documento fiscal eletrônico (**NF-e** ou **NFC-e**), a nota foi **rejeitada pela SEFAZ** devido a uma inconsistência relacionada à **alíquota tributária informada**. A rejeição ocorre no momento do envio ou da autorização do documento fiscal.

**SOLUÇÃO:**

Para corrigir esta rejeição, siga o passo a passo abaixo:

**(1)** Verifique no documento fiscal qual alíquota tributária está com valor divergente. O erro pode estar relacionado a:

- Alíquota de **ICMS**
- Alíquota de **IBS (Imposto sobre Bens e Serviços)**
- Alíquota de **CBS (Contribuição sobre Bens e Serviços)**
- Alíquota de **Imposto Seletivo (IS)**
- Outras alíquotas tributárias aplicáveis à operação

**(2)** Acesse a tela correspondente ao tributo identificado:

- **''Alíquotas de ICMS''** (Comercial » Relatórios » Cadastros » Alíquotas de ICMS).
- **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS).
- **''Aliquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(3)** Identifique qual regra de tributação foi utilizada no item do documento fiscal que foi rejeitado.

**(4)** Verifique o campo **“Alíquota”** ou **“Percentual (%)”** e confirme se o valor informado está dentro do intervalo permitido (entre **0 e 100**).

- Caso esteja incorreto, ajuste o percentual.

**(5)** Após realizar os ajustes, salve as alterações no cadastro de alíquotas.

**(6)** Retorne ao documento fiscal e **redigite os itens** ou **refaça o lançamento da nota**, para que o sistema recalcule os tributos com as alíquotas atualizadas.

**(7)** Gere novamente o lote e solicite a **autorização da SEFAZ**.

**CAUSA**

A rejeição ocorreu porque o sistema enviou para a Sefaz um **documento fiscal com alíquota tributária inválida**. A legislação fiscal estabelece que **todas as alíquotas devem estar no intervalo de 0% a 100%**, e qualquer valor fora desse limite é considerado inconsistente e resulta na rejeição do documento.

As causas mais comuns incluem:

- **Erro de digitação** no cadastro de alíquotas, informando valores negativos ou superiores a 100%
- **Configuração incorreta** das regras tributárias no sistema
- **Importação de dados** com valores inconsistentes
- **Atualização incorreta** de cadastros tributários

---
id: "37228221073303"
titulo: "E0706 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228221073303-E0706-Rejei%C3%A7%C3%A3o-Se-a-al%C3%ADquota-for-informada-ent%C3%A3o-deve-ser-igual-ou-maior-que-0-e-menor-ou-igual-a-100"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:13Z"
rotulos: ["Alíquotas", "Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Erro", "Aalíquota tributária", "Alíquota tributária fora do intervalo permitido", "Alíquota deve ser igual ou maior que 0 ou menor ou igual a 100%", "Percentuais de alíquotas tributárias"]
---

# E0706 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%.

##### MENSAGEM

E0706 Rejeição: Se a alíquota for informada, então deve ser igual ou maior que 0 e menor ou igual a 100%.

##### SITUAÇÃO

Esta rejeição ocorre quando o usuário tenta emitir uma **NF-e ou NFC-e** e alguma **alíquota tributária** informada no documento fiscal está **fora do intervalo permitido**. O sistema da Sefaz valida se os percentuais de alíquotas (ICMS, IBS, CBS, PIS, COFINS, entre outros) estão dentro do **limite de 0% a 100%**, e ao identificar um valor inválido, rejeita o documento.

##### SOLUÇÃO

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Identifique o imposto com alíquota incorreta

- Verifique no XML de retorno da rejeição ou na mensagem de erro qual tributo apresentou o problema: **ICMS, IBS, CBS, PIS, COFINS, etc.**

**(2)** Acesse o cadastro de alíquotas correspondente ao imposto rejeitado:

- Para **ICMS,** acesse a tela **"Alíquotas de ICMS"** (Comercial » Relatórios » Cadastros » Alíquotas de ICMS).
- Para **IBS**, acesse a tela **''Aliquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS).
- Para **CBS**, acesse a tela **"Alíquotas CBS"** (Livros Fiscais » Cadastros » Aliquotas de CBS).
- Para **PIS**, acesse a tela **''Alíquotas de PIS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS).
- Para **COFINS**, acesse a tela **"Alíquotas de COFINS''** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS).

**(3)** Localize a regra de alíquota aplicada

- Identifique a configuração específica que incidiu sobre o produto ou operação da nota fiscal rejeitada, utilizando os filtros de pesquisa disponíveis.

**(4)** No campo **“Alíquota”** ou **“Percentual (%)”**, certifique-se de que o valor esteja entre **0 e 100**. Corrija qualquer valor que esteja:

- Negativo (menor que 0)
- Superior a 100
- Com formatação incorreta (ex.: 1000 ao invés de 10,00)

**(5)** Se necessário, verifique também os campos de ''**Redução de Base''**, ''**Alíquota para Crédito''** e outros percentuais relacionados, garantindo que todos estejam dentro do intervalo válido.

**(6)** Salve as alterações realizadas no cadastro de alíquotas.

**(7)** **Inutilize a numeração** da NF-e ou NFC-e rejeitada, caso necessário.

**(8)** Realize um **novo faturamento** do documento fiscal, garantindo que as **alíquotas corretas** sejam aplicadas automaticamente pelo sistema.

**(9)** Confira os valores das alíquotas no documento antes de transmitir.

**(10)** Proceda com a **autorização da nota** junto à Sefaz.

**OBSERVAÇÃO:** Este ajuste é de natureza **fiscal e tributária**, devendo ser realizado por um **usuário com conhecimento** sobre a rotina e, preferencialmente, com **orientação do contador**, para evitar impactos indevidos nas demais operações.

**CAUSA**

A rejeição **E0706** é gerada pela **validação da Sefaz** que verifica se todos os **percentuais de alíquotas tributárias** informados no XML do documento fiscal estão dentro do **intervalo permitido de 0% a 100%**.

As causas mais comuns para esta rejeição são:

- **Cadastro incorreto** de alíquotas no sistema, com valores negativos ou superiores a 100%
- **Erro de digitação** ao configurar percentuais (exemplo: digitar 1000 ao invés de 10,00)
- **Importação de dados** com formatação inadequada
- **Configurações tributárias desatualizadas** ou inconsistentes
- **Parametrizações manuais** realizadas sem validação prévia dos valores

A Sefaz não aceita valores de alíquotas fora do padrão estabelecido, pois isso **comprometeria a integridade** dos cálculos tributários e da **escrituração fiscal**.

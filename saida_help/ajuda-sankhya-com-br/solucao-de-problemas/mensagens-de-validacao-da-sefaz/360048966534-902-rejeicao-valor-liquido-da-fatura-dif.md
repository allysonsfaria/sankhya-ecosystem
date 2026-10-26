---
id: "360048966534"
titulo: "902 - Rejeição: Valor Liquido da Fatura difere do Valor Original menos o Valor do Desconto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360048966534-902-Rejei%C3%A7%C3%A3o-Valor-Liquido-da-Fatura-difere-do-Valor-Original-menos-o-Valor-do-Desconto"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-10-22T17:08:44Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "O.S1433261", "O.S1273730", "Rejeição", "Rejeição 902", "Valor Líquido da Fatura"]
---

# 902 - Rejeição: Valor Liquido da Fatura difere do Valor Original menos o Valor do Desconto

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18604738065687) MENSAGEM**:

902 - Rejeição: Valor Liquido da Fatura difere do Valor Original menos o Valor do Desconto.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18604738067351) CAUSA:**

Rejeição acontecerá quando o Valor Líquido da Fatura [<vLiq>] for diferente do Valor Original da Fatura [<vOrig>] - Valor do Desconto [<vDesc>].

**SOLUÇÃO:**

![Imagem 3: Rejeição acontecerá quando o Valor Líquido da Fatura (<vLiq>) for diferente do Valor Original da Fatura (<vOrig>) -…](https://ajuda.sankhya.com.br/hc/article_attachments/18604726772247) Rejeição acontecerá quando o Valor Líquido da Fatura [<vLiq>] for diferente do Valor Original da Fatura [<vOrig>] - Valor do Desconto [<vDesc>].

![Imagem 4: Considere o exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/18604726773655) Considere o exemplo abaixo:

<fat>
**<vOrig>55.90</vOrig>**
**<vDesc>0.00</vDesc>**
**<vLiq>58.90</vLiq>**
</fat>

Note que o Valor Líquido da Fatura [58,90] difere do Valor Original - Valor do Desconto : 55,90 - 0,00

Uma das causas dessa rejeição no sistema é a configuração do parâmetro abaixo:

- **Destaca imp.federais na NF-e mista qdo.não retido?  - DESTIMPNRETNFEM**

Caso alguma UF precise trabalhar com esse parâmetro **Destaca imp.federais na NF-e mista qdo.não retido?  - DESTIMPNRETNFEM** ligado, recomendamos que essa UF seja listada no parâmetro abaixo:

- Chave: **UFs que somam os impostos retidos na NFe - UFSSOMAIMPRET**
  Descrição: UFs que somam os impostos retidos na NFe
- Este parâmetro poderá conter as UFs que precisam dos parâmetros **Somar valor de imposto retido no valor total da no - SOMIMPRETVLRNOT** e **Destaca imp.federais na NF-e mista qdo.não retido?  - DESTIMPNRETNFEM** ligados, necessários normalmente somente para estados que emitem notas mistas.
- Caso se preencha no parâmetro uma ou mais UFs, os parâmetros
- **Somar valor de imposto retido no valor total da no - SOMIMPRETVLRNOT** e **Destaca imp.federais na NF-e mista qdo.não retido?  - DESTIMPNRETNFEM**
- serão considerados apenas para os estados emitentes informados no parâmetro (separados por vírgula). Para os demais estados, os parâmetros serão considerados desligados.

------------------------------------------------------------------------------------------

Outra causa identificada para essa rejeição:

Quando temos o parâmetro **Destaca imp.federais na NF-e mista qdo.no retido? - DESTIMPNRETNFEM** habilitado, o sistema está deduzindo o valor do frete da tag <vOrig>, gerando rejeição.

[-] SOLUÇÃO: Foi ajustado o sistema para somar na tag vOrig o valor do frete e de outros impostos (tag vOutro) caso exista na nota.

- Para esse caso, atualize a base de teste com a versão mais atual, validar as operações e rotinas da empresa e só depois atualizar a base de produção com segurança: Correção disponível na versão 4.0b127 ou versões superiores.

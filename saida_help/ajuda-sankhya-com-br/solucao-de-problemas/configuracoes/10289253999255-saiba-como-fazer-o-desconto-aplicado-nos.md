---
id: "10289253999255"
titulo: "Saiba como fazer o desconto aplicado nos itens incidir na base de cálculo do ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10289253999255-Saiba-como-fazer-o-desconto-aplicado-nos-itens-incidir-na-base-de-c%C3%A1lculo-do-ICMS"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:04:01Z"
rotulos: ["Configuração", "Fiscal", "ICMS", "Impostos", "Preferências", "não apagar", "Desconto na Base de Cálculo do ICMS"]
---

# Saiba como fazer o desconto aplicado nos itens incidir na base de cálculo do ICMS

**Situação**:

Base de cálculo do ICMS não sai com o desconto informado nos itens.

**Solução:**

Para que o desconto informado nos itens seja levado em consideração na base de cálculo do ICMS, siga o passo abaixo:

![Imagem 1: Acesse a tela "Preferências" (Acesse: Configurações » Avançado » Preferências) e busque pelo parâmetro CALCPRECICMS…](https://ajuda.sankhya.com.br/hc/article_attachments/33700450073879) Acesse a tela **"Preferências"** (Acesse: Configurações » Avançado » Preferências) e busque pelo parâmetro **CALCPRECICMS** (Calc.Preço embutindo índice do Grupo ICMS por Emp.)

![Imagem 2: Caso esteja ligado, desligue o parâmetro CALCPRECICMS.](https://ajuda.sankhya.com.br/hc/article_attachments/33700450077591) Caso esteja ligado, **desligue o parâmetro CALCPRECICMS.**

**Observação:**

Em casos onde haja a necessidade de que o **desconto** informado nos itens **seja levado em consideração somente na base de cálculo do ICMS normal** e não tenha a redução do ICMS ST, se faz necessário verificar a opção **"Considera desconto no cálculo de ST por IVA"** dentro da aba **"Fiscal"** do cadastro de parceiros, e **desmarcar a mesma**.

![Imagem 3: Em casos onde haja a necessidade de que o desconto informado nos itens seja levado em consideração somente na base de…](https://ajuda.sankhya.com.br/hc/article_attachments/14653759271319)

Dessa forma, com o parâmetro CALCPRECICMS desligado e a marcação Considera desconto no cálculo de ST por IVA desmarcada também, o sistema vai considerar o desconto apenas para base do ICMS normal, os que tiverem substituição será considerado o valor bruto para compor a base do tributo.

Quando habilitado o parâmetro CALCPRECICMS, será apresentado um campo: **"Percentual"** no cadastro de parceiros, aba Fiscal, na grade Grupo de ICMS por Empresa, ele terá influência no cálculo do desconto baseado no percentual informado no cadastro do parceiro.

**Causa:**

O sistema não considera o desconto na base de ICMS caso o parâmetro **CALCPRECICMS** esteja ligado.

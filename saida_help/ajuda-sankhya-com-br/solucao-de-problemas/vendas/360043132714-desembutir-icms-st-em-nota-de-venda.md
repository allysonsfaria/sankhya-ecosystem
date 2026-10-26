---
id: "360043132714"
titulo: "Desembutir ICMS-ST em Nota de Venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043132714-Desembutir-ICMS-ST-em-Nota-de-Venda"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:49Z"
rotulos: ["#PUBLIFER", "Configuração", "Fiscal", "Parceiro", "ICMS", "Impostos", "TOP", "Ajustes de Configuração: Preferências e TOP", "Processo de Faturamento: ICMS-ST desembutido", "Desembutir ICMS-ST: Configurações necessárias"]
---

# Desembutir ICMS-ST em Nota de Venda

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16145211287703) SITUAÇÃO:**

Desembutir ICMS-ST em Nota de Venda.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16145235888535) SOLUÇÃO:**

Considere o comportamento da aplicação, conforme abaixo:

![Imagem 3: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16145211291927) Acesse: Configurações » Avançado » Preferências

- **"STEMBUT-Substituição tributária embutida no preço":** desligado
- **"STIPIEMBDESC-ST e IPI embutido como desconto no item da nota":** desligado
- **"PERCSEMIMP-Calcular % desconto sem impostos?":** ligado

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16145211295639) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Tipo de movimento= 'P'- Pedido de Venda
                                     'V' - Venda
                                     'D' - Devolução

**(2)** Aba: **"Impostos"**

- A TOP de Pedido (Tipo de Movimento - Pedido de Venda), **"TEM ICMS"**: desmarcado
- A TOP de Venda (Tipo de Movimento - Venda), **"TEM ICMS"**: marcado
- Cálculo de ICMS, IPI e ISS: calcula e Não digita

![Imagem 5: Acesse: Comercial » Preferências » Empresa Aba: "Propriedades"](https://ajuda.sankhya.com.br/hc/article_attachments/16145235898391) Acesse: Comercial » Preferências » Empresa
**(2)** Aba: **"Propriedades"**

- Campo: **"Calcula ICMS?":** Marcado

![Imagem 6: Acesse: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16145235900439) Acesse: Configurações » Cadastros » Parceiros

**(2)** Aba: **"Fiscal"**

- Campo **"Retirar ST do preço de venda do item":** 'Sim' ou 'Sim e considerar despesas assessorias.'

Após os ajustes, efetue o faturamento entre pedido e nota, o sistema irá desembutir o ICMS-ST, do preço de venda do(s) Produto(s).

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16145235903639) OBSERVAÇÃO:**

Para desembutir o ST é necessário considerar uma tolerância de R$ 0,01 para mais ou para menos na validação.

Nesse contexto, fique atento ao parâmetro: **"REMOVSTEMBDESC - Remove ST embutido em** **desconto?"**, ele é responsável  por controlar a exibição do pop-up de liberação de limites em casos de ST desembutido. Por padrão esse parâmetro fica ligado e o pop-up de liberação não é apresentado. Caso deseje que haja a liberação de um supervisor, desligue o parâmetro e o pop-up será exibido.

A funcionalidade para desembutir o ICMS-ST com diferença está disponível a partir das versões **4.35b713** e **4.36 - ERP Core 5.6.5**. Caso o processo não ocorra conforme esperado, valide a versão do ambiente.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16145211303703) CAUSA:**

Ocorre quando alguns dos principais pontos de configuração não estão corretos, para que no processo de faturamento de venda o sistema possa desembutir o ICMS-ST do preço de venda do produto já considerado no valor unitário do pedido de venda.

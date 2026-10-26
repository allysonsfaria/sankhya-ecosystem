---
id: "360044580394"
titulo: "Melhores práticas de como efetuar uma movimentação de mercadoria de um local controlado por WMS para local não controlado por WMS e vice-e-versa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580394-Melhores-pr%C3%A1ticas-de-como-efetuar-uma-movimenta%C3%A7%C3%A3o-de-mercadoria-de-um-local-controlado-por-WMS-para-local-n%C3%A3o-controlado-por-WMS-e-vice-e-versa"
trilha: "Melhores Práticas > WMS"
atualizado_em: "2026-07-22T15:51:05Z"
rotulos: ["#criadoRoger", "Configuração", "WMS", "Atualização", "TOP", "Estoque", "Preferências", "Desmarque WMS para entrada e atualização de estoque", "Ajuste WMS e atualização de estoque conforme origem e destino", "Configure WMS para baixar e atualizar estoque"]
---

# Melhores práticas de como efetuar uma movimentação de mercadoria de um local controlado por WMS para local não controlado por WMS e vice-e-versa

#### Processo de Transferência entre LOCAIS para SAIR com a Mercadoria do LOCAL CD(Centro de Distribuição) e ENTRAR no LOCAL Estoque Normal/Loja

![Imagem 1: Acesse Comercial » Preferências » Empresa Empresa da NOTA, deve ter o controle pelo WMS. Aba: WMS - devidamente…](https://ajuda.sankhya.com.br/hc/article_attachments/19195950855959) Acesse Comercial » Preferências » Empresa
Empresa da NOTA, deve ter o controle pelo WMS.
Aba:  WMS - devidamente configurado, principalmente o campo: Controlado pelo WMS e Empresa para Estoque no WMS.

![Imagem 2: Acesse Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/19195950864791) Acesse Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Tipo de Movimento [**T-Transferência**]
Aba: WMS

Campos:
Transferência no WMS = [**Considerar ORIGEM**]
Separação Balcão =[**marcado**]
Endereçamento no WMS = [**Automática**]
Atualização no WMS = [**Baixar**]

Aba: Geral
Campo:
Atualização do Estoque = [**Baixar**]

![Imagem 3: Acesse Comercial » Arquivo » Cadastros » Locais](https://ajuda.sankhya.com.br/hc/article_attachments/19195950874263) Acesse Comercial » Arquivo » Cadastros » Locais

Local de Origem Controla WMS = opção '**Controlado pelo WMS** = [marcado]

Local de Destino não Controla WMS = opção '**Controlado pelo WMS** = [desmarcado]

#### Processo de Transferência entre LOCAIS para ENTRAR com a Mercadoria no LOCAL CD(Centro de Distribuição) e SAIR do LOCAL Estoque Normal/Loja

![Imagem 4: Acesse Comercial » Preferências » Empresa Empresa da NOTA, não deve ter o controle pelo WMS. Aba: WMS sem configuração.](https://ajuda.sankhya.com.br/hc/article_attachments/19195950855959) Acesse Comercial » Preferências » Empresa
Empresa da NOTA, não deve ter o controle pelo WMS.
Aba:  WMS sem configuração.

![Imagem 5: Acesse Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/19195950864791) Acesse Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Tipo de Movimento **[T-Transferência]**
Aba: WMS

Campos:
Transferência no WMS = **[Considerar DESTINO]**
Separação Balcão = **[desmarcado]**
Endereçamento no WMS = **[Automática]**
Atualização no WMS = **[Entrar]**

Aba: Geral
Campo:
Atualização do Estoque = **[Entrar]**

![Imagem 6: Acesse Comercial » Arquivo » Cadastros » Locais](https://ajuda.sankhya.com.br/hc/article_attachments/19195950874263) Acesse Comercial » Arquivo » Cadastros » Locais

Local de Origem não Controla WMS:  opção 'Controlado pelo WMS = **[desmarcado]**

Local de Destino Controla WMS: opção 'Controlado pelo WMS = **[marcado]**

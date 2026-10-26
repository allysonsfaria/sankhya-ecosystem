---
id: "43549102448919"
titulo: "Confirmação automática do documento após liberação de evento."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43549102448919-Confirma%C3%A7%C3%A3o-autom%C3%A1tica-do-documento-ap%C3%B3s-libera%C3%A7%C3%A3o-de-evento"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-10-01T18:26:23Z"
rotulos: ["Artigo criado KCS", "Varejo - KCS"]
---

# Confirmação automática do documento após liberação de evento.

Como configurar a liberação de evento para confirmar documentos automaticamente no Sankhya?

A liberação de eventos no Sankhya pode ser configurada para que, ao liberar um evento relacionado a um documento (como pedidos ou notas fiscais), o sistema realize automaticamente a confirmação desse documento, sem a necessidade de intervenção manual após a aprovação. Essa funcionalidade otimiza o fluxo operacional, reduz o tempo de processamento e evita esquecimentos ou retrabalho, especialmente em ambientes com grande volume de liberações.

Para garantir que a confirmação automática ocorra após a liberação, é necessário ajustar algumas configurações específicas na tela de **"Liberação de Limites"** (Comercial Processos Liberação de Limites). O sistema permite que, ao liberar um evento, caso não existam mais solicitações pendentes para aquele documento, a confirmação seja realizada automaticamente, agilizando o processo de faturamento ou movimentação.

#### **(1)** Configuração da confirmação automática

Como habilitar a confirmação automática após a liberação do evento:

**(1)** Acesse a tela **"Liberação de Limites"** (Configurações » Avançado » Liberação de Limites).

**(2)** Clique no botão **"Outras Opções"** »  **Configurações.**

**(3)** Será aberto um poup up Marque a opção **"Tentar confirmar a nota automaticamente"**.

**(4)** Salve as configurações e prossiga com o processo de liberação normalmente.

![Imagem 1: (1) Acesse a tela "Liberação de Limites" (Configurações » Avançado » Liberação de Limites). (2) Clique no botão "Outras…](https://ajuda.sankhya.com.br/hc/article_attachments/43916474312343)

Com essa configuração ativa, ao liberar um evento relacionado ao cabeçalho ou itens da nota, o sistema tentará confirmar automaticamente o documento, desde que não existam outras liberações pendentes para o mesmo.

**Observação:** Essa funcionalidade não se aplica a eventos cuja origem seja o financeiro (NUFIN), pois nesses casos a chave de liberação não é o número único da nota, mas sim do financeiro.

Ao habilitar **"Tentar confirmar a nota automaticamente"**, após a liberação de um evento, o sistema confirmará automaticamente a nota caso não existam outras liberações pendentes.

**Observação:** a funcionalidade aplica-se somente à tela **Liberação de Limites** e não é acionada para eventos de origem financeira, nem pela Central de Vendas ou liberação por e-mail.

####

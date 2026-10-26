---
id: "42951429187735"
titulo: "Configurações - Webhooks"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951429187735-Configura%C3%A7%C3%B5es-Webhooks"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T14:03:05Z"
rotulos: ["zydon", "sync_hc", "zydon_219372460805", "sync_hash_6727b470430b"]
---

# Configurações - Webhooks

Os Webhooks permitem automatizar a comunicação entre o Zydon e seus outros sistemas: sempre que um evento acontece na plataforma (um pedido e criado, um cliente se cadastra, etc.), o Zydon envia uma notificação HTTP para a URL que você configurar.

## Pré-requisitos

Acesso ao Zydon Admin com permissão de administrador.

Ter um endpoint (URL) no seu sistema externo pronto para receber as requisições.

## Onde encontrar

No menu lateral do Zydon Admin, clique em Configurações e depois em Webhooks.

![Imagem 1: No menu lateral do Zydon Admin, clique em Configurações e depois em Webhooks .](https://ajuda.sankhya.com.br/hc/article_attachments/42951443812375)

## Categorias de eventos

No menu lateral da tela de Webhooks, os eventos disponíveis estão organizados em 5 categorias:

- **Pedidos**: Pedido Criado (dispara quando um novo pedido e criado), Pedido Atualizado (quando o pedido e editado - status, itens, entrega, pagamento), Pedido Calculado (quando o total do pedido e recalculado - frete, descontos, tributos, promoções) e Calculo de Preço de Produto (solicita ao seu sistema os valores de venda do item - preço base, descontos comerciais, politicas e tabelas).

![Imagem 2: Pedidos : Pedido Criado (dispara quando um novo pedido e criado), Pedido Atualizado (quando o pedido e editado -…](https://ajuda.sankhya.com.br/hc/article_attachments/42951444013719)

- **Novo cliente**: Novo Registro, disparado sempre que um novo cliente e cadastrado na plataforma. Útil para sincronizar dados com seu CRM, iniciar fluxos de aprovação ou enviar e-mails de boas-vindas.

![Imagem 3: Novo cliente : Novo Registro, disparado sempre que um novo cliente e cadastrado na plataforma. Útil para sincronizar…](https://ajuda.sankhya.com.br/hc/article_attachments/42951444120215)

- **Formas de entrega**: Calcular Forma de Entrega (solicita ao sistema externo as opções de envio disponíveis para o pedido) e Enviar Formas de Entrega (envia as formas de entrega calculadas e selecionadas).

![Imagem 4: Formas de entrega : Calcular Forma de Entrega (solicita ao sistema externo as opções de envio disponíveis para o…](https://ajuda.sankhya.com.br/hc/article_attachments/42951414653591)

- **Agente IA**: Enviar Mensagem, disparado sempre que uma mensagem e enviada pelo agente de IA.

![Imagem 5: Agente IA : Enviar Mensagem, disparado sempre que uma mensagem e enviada pelo agente de IA.](https://ajuda.sankhya.com.br/hc/article_attachments/42951400709271)

- **Webhooks criados**: lista consolidada de todos os webhooks personalizados que você já configurou, independente da categoria de evento.

![Imagem 6: Webhooks criados : lista consolidada de todos os webhooks personalizados que você já configurou, independente da…](https://ajuda.sankhya.com.br/hc/article_attachments/42951425345815)

## Como configurar um webhook

Dentro de qualquer categoria, cada evento exibe um card com sua descrição. Clique em Clique aqui para adicionar (ou em Editar, se já houver um webhook configurado) para abrir a janela Editar webhook e preencher:

- URL de endpoint: endereço do seu sistema externo que vai receber a requisição.
- Máximo de retentativas: quantas vezes o Zydon deve tentar reenviar a requisição em caso de falha.
- Timeout em segundos: tempo máximo de espera pela resposta do seu sistema antes de considerar a chamada como falha.
- Método HTTP: GET, POST ou outro método aceito pelo seu endpoint.
- Cabeçalho: pares de Chave e Valor enviados junto da requisição (ex.: chaves de autenticação). Clique em + Adicionar para incluir quantos precisar.

Depois de preencher, clique em Salvar.

## Últimas requisições

Clique em Últimas requisições, no card de qualquer evento configurado, para abrir o histórico de chamadas daquele webhook. Você verá, para cada requisição, o status (Enviado ou Falhou), o tempo de resposta em milissegundos e a data/hora do disparo.

Clique em qualquer requisição da lista para ver o detalhe completo, dividido em duas abas: Requisição (Headers enviados e Payload em formato JSON navegável, com busca) e Resposta (o que o seu sistema externo respondeu).

Use essa tela para diagnosticar rapidamente por que uma integração esta falhando, sem precisar recorrer aos logs do seu próprio sistema.

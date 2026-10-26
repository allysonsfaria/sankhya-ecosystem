---
id: "44012373240983"
titulo: "[Routing] - Release Notes 2.64"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012373240983--Routing-Release-Notes-2-64"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T19:26:46Z"
rotulos: ["sync_hc", "lincros", "lincros_13433673", "sync_hash_1052b28d96f7"]
---

# [Routing] - Release Notes 2.64

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44012359912215)

## Melhorias:

## Integração com SemParar para Vale-Pedágio

Agora o Routing conta com novas funcionalidades para gestão de pedágios via integração com a SemParar, trazendo mais agilidade e controle para sua operação:

- Compra de Vale-Pedágio: possibilidade de consultar valores e realizar a compra automaticamente pelo sistema.
- Recibos em PDF: geração de recibos de pedágios diretamente na tela de pedágios da sessão ou no relatório de pedágios.
- Cancelamento de Compras: cancelamento de pedágios adquiridos via SemParar diretamente na tela de sessões.
- Envio Automático de Comprovante: novo parâmetro no cadastro de transportadora para envio do comprovante de pedágio por e-mail após a exportação da sessão.
- Configuração de Eixos no Retorno: campo “Quantidade de Eixos no Retorno” no cadastro de Tipo de Veículo, garantindo que apenas os eixos necessários sejam considerados na volta da rota.
- Configuração de Depósito: nova opção “Usar pedágio” nas configurações de Depósito, permitindo selecionar entre Repom e SemParar.

Essas melhorias foram pensadas para tornar o processo de gestão de pedágios mais rápido, flexível e automatizado.

## Edição do campo Pallets na rota

Agora é possível editar a quantidade de pallets diretamente na tela **Informações da Rota** no Routing.

O valor atualizado é refletido na API de consulta de dados da sessão e também na exportação via layout existente.

![Imagem 2: O valor atualizado é refletido na API de consulta de dados da sessão e também na exportação via layout existente.](https://ajuda.sankhya.com.br/hc/article_attachments/44012331450775)

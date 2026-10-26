---
id: "37097479365911"
titulo: "1102 Rejeição: NF-e de devolução de mercadoria com referenciamento a nível de item exige referenciamento do item da NF-e original [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097479365911-1102-Rejei%C3%A7%C3%A3o-NF-e-de-devolu%C3%A7%C3%A3o-de-mercadoria-com-referenciamento-a-n%C3%ADvel-de-item-exige-referenciamento-do-item-da-NF-e-original-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:41Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "Devolução", "Passos para resolver", "Erro", "Como Resolver", "NF-e de devolução", "NF-e de devolução de mercadoria", "NF-e original", "Documentos Eletrônicos"]
---

# 1102 Rejeição: NF-e de devolução de mercadoria com referenciamento a nível de item exige referenciamento do item da NF-e original [nItem: 999]

**MENSAGEM**

1102 Rejeição: NF-e de devolução de mercadoria com referenciamento a nível de item exige referenciamento do item da NF-e original [nItem: 999]

**SITUAÇÃO**

A NF-e de devolução (finalidade 4) foi emitida sem a correta identificação do item da NF-e original que está sendo devolvido, não sendo informado o número do item correspondente no documento referenciado.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione a TOP utilizada para devolução.

**(2)** Na aba **"NF-e/NFC-e"**, verifique se a opção **"Buscar NF de Origem p/ Referenciar na NF-e"** está marcada.

- Caso não esteja, marque-a e salve a alteração.

**(3)** Inutilize a numeração da NF-e de devolução que foi rejeitada.

**(4)** Para realizar corretamente a devolução, acesse a tela **"Central de Vendas"** (Comercial » Rotinas » Central de Vendas).

**(5)** Localize a NF-e original que deseja devolver.

**(6)** Clique no botão **"Devolv./Estor."** e selecione os itens específicos que serão devolvidos.

**(7)** Ao realizar a devolução desta forma, o sistema preencherá automaticamente o grupo de documentos referenciados, incluindo a chave da NF-e original e o número do item que está sendo devolvido.

**(8)** Confirme a operação e emita a nova NF-e de devolução.

**CAUSA**

A rejeição 1102 ocorre devido à implementação da **Nota Técnica 2022.005** que estabeleceu novas regras de validação para NF-e de devolução. Conforme esta norma, quando uma NF-e possui finalidade igual a  **''Devolução"**, é obrigatório não apenas referenciar a NF-e original que está sendo devolvida (através da chave de acesso), mas também informar **qual item específico** da NF-e original está sendo devolvido.

Esta validação faz parte das medidas de controle fiscal implementadas pela SEFAZ para garantir maior rastreabilidade nas operações de devolução, permitindo um controle mais preciso dos itens que estão sendo devolvidos em relação à nota fiscal original.

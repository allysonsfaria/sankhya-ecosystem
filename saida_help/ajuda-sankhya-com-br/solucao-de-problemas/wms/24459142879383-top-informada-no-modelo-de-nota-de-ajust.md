---
id: "24459142879383"
titulo: "Top informada no modelo de nota de ajuste de Saída PRÓPRIO não pode atualizar estoque com/de Terceiros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24459142879383-Top-informada-no-modelo-de-nota-de-ajuste-de-Sa%C3%ADda-PR%C3%93PRIO-n%C3%A3o-pode-atualizar-estoque-com-de-Terceiros"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:46:43Z"
rotulos: ["Configuração", "NF-e", "TOP", "Estoque", "Preferências", "INV_E00008", "TOP não pode atualizar estoque de terceiros", "Ajustar configuração da TOP na tela \"Tipos de Operação\"", "Vinculação incorreta de TOP no modelo de nota", "Erro"]
---

# Top informada no modelo de nota de ajuste de Saída PRÓPRIO não pode atualizar estoque com/de Terceiros

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24459142871447) **MENSAGEM:**

[INV\_E00008] Top informada no modelo de nota de ajuste de Saída PRÓPRIO não pode atualizar estoque com/de Terceiros.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24459114694679)SOLUÇÃO:**

Para solucionar o erro siga os passos abaixo:

![Imagem 3: Acesse a tela "Empresa" (Caminho: Comercial » Preferências » Empresa), vá até a aba "Estoque/preço";](https://ajuda.sankhya.com.br/hc/article_attachments/24511328264343) Acesse a tela **"Empresa"** (Caminho: Comercial » Preferências » Empresa), vá até a aba **"Estoque/preço";**

![Imagem 4: Em seguida, busque pelo campo "Modelo ajuste de Saída de Estoque" e veja a TOP vinculada no modelo de nota/pedido;](https://ajuda.sankhya.com.br/hc/article_attachments/24511328268695) Em seguida, busque pelo campo **"Modelo ajuste de Saída de Estoque"**e veja a TOP vinculada no modelo de nota/pedido;

![Imagem 5: Depois, acesse a tela "Tipos de Operação - TOP" , procure pela TOP identificada no modelo de nota/pedido e veja se ela…](https://ajuda.sankhya.com.br/hc/article_attachments/24511285518615) Depois, acesse a tela **"Tipos de Operação - TOP"**, procure pela TOP identificada no modelo de nota/pedido e veja se ela está configurada movimentar estoque de terceiro, nos campos **"Estoque com/de Terceiros"** e **"Estoque MP de Terceiros"**, da aba "Estoque de terceiros da TOP", com uma configuração diferente de 'Não controla'. Caso tenha, altere a Top e vincule novamente no modelo de nota/pedido.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24459114696087)CAUSA:**

O erro é apresentado ao vincular no campo Modelo ajuste de Saída de Estoque, da aba Estoque/preço, das Preferências da empresa, que não movimenta estoque de terceiros, uma TOP que está configurada para movimentar.

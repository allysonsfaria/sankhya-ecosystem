---
id: "9482869621399"
titulo: "Não é possível efetuar a baixa agrupada pois uma liberação de limites do Evento 24 foi lançada ao tentar baixar os títulos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9482869621399-N%C3%A3o-%C3%A9-poss%C3%ADvel-efetuar-a-baixa-agrupada-pois-uma-libera%C3%A7%C3%A3o-de-limites-do-Evento-24-foi-lan%C3%A7ada-ao-tentar-baixar-os-t%C3%ADtulos"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:07:36Z"
rotulos: ["Configuração", "Movimentação Financeira", "Liberação de Limites", "Financeiro", "CORE_E01706", "Mensagem: Baixa agrupada não permite liberação de limites do Evento 24.", "Causa: Títulos com liberação de limites do Evento 24 não são compatíveis.", "Solução: Baixe títulos separadamente ou ajuste configuração para desabilitar liberação de limites.", "Erro"]
---

# Não é possível efetuar a baixa agrupada pois uma liberação de limites do Evento 24 foi lançada ao tentar baixar os títulos

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19297396403351) MENSAGEM:**

[CORE\_E01706] Não é possível efetuar a baixa agrupada pois uma liberação de limites do Evento 24 foi lançada ao tentar baixar os títulos. O processo de baixa agrupada não é compatível com liberação de limites. Configure o sistema para que os títulos envolvidos na baixa agrupada não necessitem de liberações para serem baixados ou baixe separadamente.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19297368077847) SITUAÇÃO:**

Ao tentar fazer uma baixa agrupada a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19297368080663) CAUSA:**

Tentar realizar uma baixa agrupada de títulos que tenham participado de liberação de limites do evento 24.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19297396423319) SOLUÇÃO:**

Em relação à baixa agrupada de vários títulos, ao inserir valores nos campos **"Desconto"** ou **"Perdão Juros"** e realizar a baixa, não será possível concluí-la, visto que o sistema não encontra-se apto para realizar uma baixa agrupada de vários títulos que solicite uma liberação de limites. Desta forma, caso seja necessário inserir Desconto ou Perdão de Juros, os títulos deverão ser baixados separadamente.

Para solução, efetue a baixa agrupada usando a configuração do evento 24. Será preciso efetuar a baixa separadamente ou não utilizar o evento 24.

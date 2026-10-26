---
id: "9373086370199"
titulo: "O KM de saída 'XXXXX' deve ser maior ou igual ao último KM de chegada registrado para esse veículo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9373086370199-O-KM-de-sa%C3%ADda-XXXXX-deve-ser-maior-ou-igual-ao-%C3%BAltimo-KM-de-chegada-registrado-para-esse-ve%C3%ADculo"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:08:27Z"
rotulos: ["Veículo", "Configuração", "Movimentação Financeira", "Transporte", "CORE_E00818", "Mensagem aparece ao alterar quilometragem retroativa", "Excluir lançamentos posteriores antes de corrigir", "KM de saída deve ser maior ou igual ao último KM registrado", "Erro"]
---

# O KM de saída 'XXXXX' deve ser maior ou igual ao último KM de chegada registrado para esse veículo

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18613796122903) MENSAGEM:**

[CORE\_E00818] O KM de saída 'XXXXX' deve ser maior ou igual ao último KM de chegada registrado para esse veículo.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18613796137239) SITUAÇÃO:**

Alterar o controle de saída/chegada de veículos a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18613796144023) CAUSA:**

Ao tentar inserir uma quilometragem retroativa na tela **Controle de Saída/Chegada de Veículos** (Configurações » Rotinas » Controle de Saída/Chegada de Veículos).

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18613808226455) SOLUÇÃO:**

Na tela **Controle de Saída/Chegada de Veículos**(Configurações » Rotinas » Controle de Saída/Chegada de Veículos) o registro de entrada e saída de veículos realmente não foi construído de forma a aceitar lançamentos retroativos, exceto com a exclusão dos lançamentos posteriores.

[Controle de Saída/Chegada de Veículos – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596414-Controle-de-Sa%C3%ADda-Chegada-de-Ve%C3%ADculos)

**Observação:** Para realizar uma alteração em um registro de saída e chegada de um veículo quando há lançamentos posteriores ao mesmo, deve-se excluir todos os lançamentos de futuros até chegar ao registro que se deseja corrigir.

![Imagem 5: Observação: Para realizar uma alteração em um registro de saída e chegada de um veículo quando há lançamentos…](https://ajuda.sankhya.com.br/hc/article_attachments/9372928723095)

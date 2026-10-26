---
id: "9320246578711"
titulo: "Não é permitido que a ordem de carga geradora da viagem tenha documentos de nota e conhecimento de transporte"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9320246578711-N%C3%A3o-%C3%A9-permitido-que-a-ordem-de-carga-geradora-da-viagem-tenha-documentos-de-nota-e-conhecimento-de-transporte"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:08:45Z"
rotulos: ["ERROMDFE", "MDF-e", "NF-e", "Transporte", "COM_E00044", "Restrição de Documentos em Ordem de Carga para Viagem", "Documentos Eletrônicos"]
---

# Não é permitido que a ordem de carga geradora da viagem tenha documentos de nota e conhecimento de transporte

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18613297515287) MENSAGEM:**

[COM\_E00044] Não é permitido que a ordem de carga geradora da viagem tenha documentos de nota e conhecimento de transporte.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18613342315927) SITUAÇÃO:**

Ao tentar vincular OC em um novo MDF-e ou gerar viagens na tela de Ordens de Carga a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18613342329495) CAUSA:**

Tentar inserir dois tipos de documentos na mesma formação de carga ou tentar lançar MDF-e ligados a notas por outra rotina que não seja a **Viagens de Transporte (MDF-e)** (Comercial » Rotinas » Viagens de Transporte (MDF-e).

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18613297537943) SOLUÇÃO:**

Quando se tratar de MDF-e, havendo documentos ligados as notas, ou mais de um empresa nas notas fiscais a melhor prática é que faça o lançamento do MDF-e direto pela tela de **Viagens de Transporte (MDF-e)** (Comercial » Rotinas » Viagens de Transporte (MDF-e).

![Imagem 5: Quando se tratar de MDF-e, havendo documentos ligados as notas, ou mais de um empresa nas notas fiscais a melhor…](https://ajuda.sankhya.com.br/hc/article_attachments/9320086323095)

Quando se tratar de viagens geradas na tela **Ordens de carga** (Comercial » Rotinas » Ordem de Carga » Ordens de Carga) necessário verificar se todos os documentos da viagem são os mesmos, caso identifique documentos diferentes é necessário realizar os ajustes pois não é permitido dois tipos de documentos na mesma formação de carga.

![Imagem 6: Quando se tratar de viagens geradas na tela Ordens de carga (Comercial » Rotinas » Ordem de Carga » Ordens de Carga)…](https://ajuda.sankhya.com.br/hc/article_attachments/9320252534295)

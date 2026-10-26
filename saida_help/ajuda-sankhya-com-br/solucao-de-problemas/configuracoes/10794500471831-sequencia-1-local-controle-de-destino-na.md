---
id: "10794500471831"
titulo: "Sequência 1: Local/controle de destino não podem ser os mesmos da origem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10794500471831-Sequ%C3%AAncia-1-Local-controle-de-destino-n%C3%A3o-podem-ser-os-mesmos-da-origem"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-29T12:04:31Z"
rotulos: ["Configuração", "TOP", "Estoque", "Transferência", "CORE_E00774", "Sequência 1: Local/controle de destino não podem ser os mesmos da origem", "Configuração de Transferências em Sankhya: Regras e Preferências", "Erro"]
---

# Sequência 1: Local/controle de destino não podem ser os mesmos da origem

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18664544638615) MENSAGEM:**

[CORE\_E00774]  Sequência 1: Local/controle de destino não podem ser os mesmos da origem.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18664512454039) SOLUÇÃO:**

Ao lançar notas de transferência utilizando um Tipo de operação-TOP definido com o tipo de movimento = T-Transferência, será necessário avaliar qual a configuração do local.

![Imagem 3: Ao lançar notas de transferência utilizando um Tipo de operação-TOP definido com o tipo de movimento = T-Transferência,…](https://ajuda.sankhya.com.br/hc/article_attachments/10794293171735)![Imagem 4: Ao lançar notas de transferência utilizando um Tipo de operação-TOP definido com o tipo de movimento = T-Transferência,…](https://ajuda.sankhya.com.br/hc/article_attachments/10794285651863)

O sistema segue uma sequência em cascata de busca lógica pelos cadastros de local de origem e local de baixa respectivamente: 

    **1)** Composição,

      **2)** Operação de estoque;

Para tomada de decisão se houver cadastros em ambos locais a preferência será para o cadastro da composição do produto.

[Configuração de Atividades – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674#sub-abalistademps)

**Sub-aba Material**

![Imagem 5: Sub-aba Material](https://ajuda.sankhya.com.br/hc/article_attachments/10794350385303)

[Composição do Produto – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abamat%C3%A9rias-primas)

![Imagem 6: Composição do Produto – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/article_attachments/10794437920919)

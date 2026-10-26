---
id: "30946315926423"
titulo: "Não é possível iniciar a atividade pois o Centro de Trabalho é exclusivo e está sendo utilizado por outra atividade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30946315926423-N%C3%A3o-%C3%A9-poss%C3%ADvel-iniciar-a-atividade-pois-o-Centro-de-Trabalho-%C3%A9-exclusivo-e-est%C3%A1-sendo-utilizado-por-outra-atividade"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T14:34:11Z"
rotulos: ["Configuração", "Centro de Trabalho", "Ordem de Produção", "Produção", "Passos para resolver", "Razão do erro", "Detalhe do erro", "PROD_E00290", "Não é possível iniciar a atividade", "está sendo utilizado por outra atividade", "o Centro de Trabalho é exclusivo", "Erro"]
---

# Não é possível iniciar a atividade pois o Centro de Trabalho é exclusivo e está sendo utilizado por outra atividade

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30946308200599) **MENSAGEM:**

[PROD\_E00290] Não é possível iniciar a atividade pois o Centro de Trabalho é exclusivo e está sendo utilizado por outra atividade.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30946315917975)SOLUÇÃO:**

![Imagem 3: Acesse a tela "Centros de trabalho" (Produção » Cadastros » Centros de Trabalho) e confirme o tipo de Operação do CT em…](https://ajuda.sankhya.com.br/hc/article_attachments/32581566792215) Acesse a tela **"Centros de trabalho"** (Produção » Cadastros » Centros de Trabalho) e confirme o tipo de Operação do CT em questão.

![Imagem 4: Caso o centro de trabalho seja de operação exclusiva, finalize todas as OPs que fazem uso deste CT, antes de iniciar…](https://ajuda.sankhya.com.br/hc/article_attachments/32581550930839) Caso o centro de trabalho seja de operação exclusiva, **finalize todas as OPs que fazem uso deste CT,** antes de iniciar uma nova OP que irá utilizar este mesmo centro de trabalho. Para facilitar essa ação:

**(2)**Acesse a tela **"Ordens de Produção - Nova"** (Produção > Rotinas > Ordens de Produção - Nova) e use o filtro rápido de Centro de Trabalho para identificar qual OP está utilizando o CT exclusivo.

**Observação:** quando o centro de trabalho definido na OP está configurado como exclusivo, o mesmo irá participar de uma operação por vez, utilizando o controle por fila destas operações.

Caso não tenha a necessidade de acordo com o processo definido de utilizar o centro de trabalho como exclusivo, é possível alterar o tipo de operação do centro de trabalho na tela Centros de trabalho (Produção » Cadastros » Centros de Trabalho).

**Importante: é preciso** avaliar o processo definido para sua empresa antes de alterar essa configuração.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30946308202135)CAUSA:**

Ocorre quando temos um centro de trabalho definido como exclusivo, sendo utilizado em uma Ordem de Produção ou atividade já iniciada e tentamos iniciar uma nova atividade ou OP, que utilizará o mesmo centro de trabalho.

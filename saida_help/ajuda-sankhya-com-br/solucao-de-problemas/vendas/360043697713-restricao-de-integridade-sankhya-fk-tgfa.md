---
id: "360043697713"
titulo: "Restrição de integridade (SANKHYA.FK_TGFACF_NUNOTA_TGFFIN) violada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697713-Restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFACF-NUNOTA-TGFFIN-violada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:47Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "Financeiro", "Solução: emitir NF-e de devolução", "Erro ORA-02292 ao cancelar/excluir", "Documento vinculado à ordem de carga", "Erro", "Documentos Eletrônicos"]
---

# Restrição de integridade (SANKHYA.FK_TGFACF_NUNOTA_TGFFIN) violada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16165294803351) MENSAGEM:**

ORA-02292 Erro ao remover entidade: ORA-02292: restrição de integridade (SANKHYA.FK\_TGFACF\_NUNOTA\_TGFFIN) violada - registro filho localizado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16165317411607) SITUAÇÃO:**

Mensagem apresentada ao tentar cancelar e/ou excluir lançamentos.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16165294810519) SOLUÇÃO:**

![Imagem 4: A mensagem tratada nesse artigo será apresentada quando o documento em questão foi vinculado a uma ordem de carga, que…](https://ajuda.sankhya.com.br/hc/article_attachments/16165317415575) A mensagem tratada nesse artigo será apresentada quando o documento em questão foi vinculado a uma ordem de carga, que teve sua carga formada gerando registros na tela de acerto.

![Imagem 5: O impedimento desse cancelamento deve ser compreendido para evitar inconsistência no processo de 'Distribuição/Formação…](https://ajuda.sankhya.com.br/hc/article_attachments/16165317416727) O impedimento desse cancelamento deve ser compreendido para evitar inconsistência no processo de 'Distribuição/Formação de Cargas' do sistema, incluindo todas as rotinas e relatórios gerenciais ligados ao mesmo.

![Imagem 6: Não existe enquanto aplicação uma prática que consiste em "excluir/desvincular" o documento do acerto de O.C,…](https://ajuda.sankhya.com.br/hc/article_attachments/16165317418263) Não existe enquanto aplicação uma prática que consiste em "excluir/desvincular" o documento do acerto de O.C, recomendando que o processo de cancelar seja substituído pela emissão de uma NF-e de devolução, levando-se em consideração os motivos que geraram essa necessidade.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16165294821911) CAUSA:**

Mensagem será apresentada ao tentar cancelar e/ou excluir lançamentos com registros no 'Acerto de Ordem de Carga'.

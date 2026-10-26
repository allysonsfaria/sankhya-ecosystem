---
id: "360044115953"
titulo: "Financeiro já foi gerado nos Livros Fiscais, não pode ser excluído"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044115953-Financeiro-j%C3%A1-foi-gerado-nos-Livros-Fiscais-n%C3%A3o-pode-ser-exclu%C3%ADdo"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:01:22Z"
rotulos: ["Movimentação Financeira", "Livros Fiscais", "Financeiro", "ICMS/IPI", "ORA-20101", "Financeiro já gerado nos Livros Fiscais", "Tentativa de alterar/excluir lançamentos já gerados", "Excluir registro no \"Cadastro Livro ICMS/IPI\"", "Erro"]
---

# Financeiro já foi gerado nos Livros Fiscais, não pode ser excluído

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16169947000727) MENSAGEM:**

ORA-20101: Financeiro já foi gerado nos Livros Fiscais, não pode ser excluído.

Financeiro de Nro Único: 'X'.

ORA-06512: em "SANKHYA.TRG\_DLT\_TGFFIN", line 297

ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_DLT\_TGFFIN'

**![Imagem 2: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16169947005591) SOLUÇÃO**

![Imagem 3: Anote o número único do lançamento financeiro a ser excluído/alterado.](https://ajuda.sankhya.com.br/hc/article_attachments/16169979184535) Anote o número único do lançamento financeiro a ser excluído/alterado.

![Imagem 4: Acesse a tela "Cadastro Livro ICMS/IPI" (Caminho de acesso: Livros Fiscais » Arquivos » Cadastro Livro ICMS/IPI) e…](https://ajuda.sankhya.com.br/hc/article_attachments/16169979185431) Acesse a tela [**"Cadastro Livro ICMS/IPI"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874) (Caminho de acesso: Livros Fiscais » Arquivos » Cadastro Livro ICMS/IPI) e filtre por esse Número único.

![Imagem 5: Clique em "Aplicar" .](https://ajuda.sankhya.com.br/hc/article_attachments/16169979188119) Clique em **"Aplicar"**.

![Imagem 6: Verifique os dados retornados pelo modo grade.](https://ajuda.sankhya.com.br/hc/article_attachments/16169979189399) Verifique os dados retornados pelo modo grade.

![Imagem 7: Valide se as informações da linha retornada correspondem ao lançamento financeiro que será editado/excluído.](https://ajuda.sankhya.com.br/hc/article_attachments/16169947018647) Valide se as informações da linha retornada correspondem ao lançamento financeiro que será editado/excluído.

![Imagem 8: Através do botão "(-)" exclua tal registro.](https://ajuda.sankhya.com.br/hc/article_attachments/16169979192087) Através do botão **"(-)"** exclua tal registro.

![Imagem 9: Retorne para a tela movimentação financeira e tente realizar a alteração/exclusão novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16169947022615) Retorne para a tela movimentação financeira e tente realizar a alteração/exclusão novamente.

![Imagem 10: Retorne para a tela movimentação financeira e tente realizar a alteração/exclusão novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/14560897205783)

**![Imagem 11: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16169979194135) OBSERVAÇÃO:**

Caso seja apenas uma edição e necessite reenviar esse título aos Livros, acesse a tela [**"Geração ICMS/IPI"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953) e gere o financeiro do período novamente.

Caso deseje gerar apenas esse lançamento, ao clicar em **"Gerar agora"**, informe o número único desse.

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16169947026711) CAUSA:**

Ocorre ao tentar excluir e/ou alterar lançamentos financeiros que já foram gerados nos Livros Fiscais.

---
id: "360044110854"
titulo: "Nota já foi gerada nos Livros Fiscais, não pode ser excluída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110854-Nota-j%C3%A1-foi-gerada-nos-Livros-Fiscais-n%C3%A3o-pode-ser-exclu%C3%ADda"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:59Z"
rotulos: ["Fiscal", "NF-e", "Livros Fiscais", "ICMS", "ORA-20101", "Nota não pode ser excluída após geração nos Livros Fiscais.", "Anote o número único filtre e remova registros em \"Cadastro Livro ICMS/IPI\".", "Gere notas novamente se necessário ou apenas o lançamento específico.", "Erro"]
---

# Nota já foi gerada nos Livros Fiscais, não pode ser excluída

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16590272482199) MENSAGEM:**

[ORA-20101 - Erro ao remover entidade]: Nota já foi gerada nos Livros Fiscais, não pode ser excluída. ORA-06512: em "SANKHYA.TRG\_DLT\_TGFCAB", line 342 ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_DLT\_TGFCAB'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16590287396631)SOLUÇÃO:**

![Imagem 3: Anote o número único do lançamento a ser excluído/alterado;](https://ajuda.sankhya.com.br/hc/article_attachments/16590272488343) Anote o número único do lançamento a ser excluído/alterado;

![Imagem 4: Acesse a tela "Cadastro Livro ICMS/IPI" (Caminho de acesso: Livros Fiscais » Arquivos) e filtre por esse Número único;](https://ajuda.sankhya.com.br/hc/article_attachments/16590272490263) Acesse a tela **"Cadastro Livro ICMS/IPI"** (Caminho de acesso: Livros Fiscais » Arquivos) e filtre por esse Número único;

![Imagem 5: Clique em aplicar;](https://ajuda.sankhya.com.br/hc/article_attachments/16590272492695) Clique em **aplicar;**

![Imagem 6: Verifique os dados retornados pelo Modo Grade;](https://ajuda.sankhya.com.br/hc/article_attachments/16590287410583) Verifique os dados retornados pelo Modo Grade;

**![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16590272495127) IMPORTANTE:**

É retornada 1 linha por item do lançamento.

![Imagem 8: Valide se as linhas retornadas correspondem ao lançamento que será editado/excluído;](https://ajuda.sankhya.com.br/hc/article_attachments/16590272496535) Valide se as linhas retornadas correspondem ao lançamento que será editado/excluído;

![Imagem 9: Através do botão (-) exclua tais registros;](https://ajuda.sankhya.com.br/hc/article_attachments/16590287416215) Através do botão (-) exclua tais registros;

![Imagem 10: Retorne ao lançamento e tente realizar a alteração/exclusão novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16590287418903) Retorne ao lançamento e tente realizar a alteração/exclusão novamente.

**![Imagem 11: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16590287420439)OBSERVAÇÕES:**

**(2)** Caso seja apenas uma edição e necessite enviar essa nota novamente aos Livros, acesse a tela **"Geração ICMS/IPI"** e gere as notas do período novamente;

**(2)** Caso deseje gerar apenas esse lançamento, ao clicar em **"Gerar agora",** informe o número único dessa.

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16590287424279)CAUSA:**

Ocorre quando a nota já está gerada nos Livros Fiscais e precisa ser alterado algum registro na nota.

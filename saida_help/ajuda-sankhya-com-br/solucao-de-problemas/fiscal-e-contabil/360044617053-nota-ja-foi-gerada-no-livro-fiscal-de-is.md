---
id: "360044617053"
titulo: "Nota já foi gerada no Livro Fiscal de ISS, não pode ser alterada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617053-Nota-j%C3%A1-foi-gerada-no-Livro-Fiscal-de-ISS-n%C3%A3o-pode-ser-alterada"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:30Z"
rotulos: ["ISS", "Livro Fiscal", "ORA-20101", "Prefeituras", "NFS-e", "Nota não pode ser alterada após geração no Livro Fiscal de ISS", "Anote número único filtre em \"Cadastro Livro ISS\" e remova registros", "Gere notas novamente se necessário ou apenas o lançamento específico", "Erro"]
---

# Nota já foi gerada no Livro Fiscal de ISS, não pode ser alterada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16814600257303) MENSAGEM:**

[ORA-20101]: Nota já foi gerada no Livro Fiscal de ISS, não pode ser alterada. Nota de Nro Único: 'X'.

[ORA-06512]: em "SANKHYA.TRG\_UPD\_TGFCAB", line 937

[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_UPD\_TGFCAB'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16814623295383) SOLUÇÃO:**

![Imagem 3: Anote o número único do lançamento a ser excluído/alterado;](https://ajuda.sankhya.com.br/hc/article_attachments/16814600268567) Anote o número único do lançamento a ser excluído/alterado;

![Imagem 4: Acesse a tela " Cadastro Livro ISS" (Livros Fiscais » Arquivos) e filtre por esse Número único;](https://ajuda.sankhya.com.br/hc/article_attachments/16814600275351) Acesse a tela "**Cadastro Livro ISS"** (Livros Fiscais » Arquivos) e filtre por esse Número único;

![Imagem 5: Clique em aplicar;](https://ajuda.sankhya.com.br/hc/article_attachments/16814623310103) Clique em **aplicar;**

![Imagem 6: Verifique os dados retornados pelo Modo Grade;](https://ajuda.sankhya.com.br/hc/article_attachments/16814623314711) Verifique os dados retornados pelo Modo Grade;

**![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16814600292631) IMPORTANTE:**

É retornada 1 linha por item do lançamento.

![Imagem 8: Valide se as linhas retornadas correspondem ao lançamento que será editado/excluído;](https://ajuda.sankhya.com.br/hc/article_attachments/16814623323671) Valide se as linhas retornadas correspondem ao lançamento que será editado/excluído;

![Imagem 9: Através do botão "Remover" exclua tais registros;](https://ajuda.sankhya.com.br/hc/article_attachments/16814600303895) Através do botão **"Remover"** exclua tais registros;

![Imagem 10: Retorne ao lançamento e tente realizar a alteração/exclusão novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16814600314391) Retorne ao lançamento e tente realizar a alteração/exclusão novamente.

**![Imagem 11: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16814623345943) OBSERVAÇÕES:**

Caso seja apenas uma edição e necessite enviar essa nota novamente aos Livros, acesse a tela **"Geração ISS"** e gere as notas do período novamente.

Caso deseje gerar apenas esse lançamento, ao clicar em **"Gerar agora"** informe o número único dessa.

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16814600328215) CAUSA:**

Mensagem ocorre quando para o Nro único referente ao lançamento a ser excluído existem registros na tabela de Livros Fiscais (TGFLIV).

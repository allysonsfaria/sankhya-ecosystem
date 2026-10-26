---
id: "360044617073"
titulo: "Nota já foi gerada no Livro Fiscal de ICMS/IPI, não pode ser alterada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617073-Nota-j%C3%A1-foi-gerada-no-Livro-Fiscal-de-ICMS-IPI-n%C3%A3o-pode-ser-alterada"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:29Z"
rotulos: ["NF-e", "SEFAZ", "Livro Fiscal", "ICMS/IPI", "ORA-20101", "Nota não pode ser alterada após geração no Livro Fiscal.", "Anote número único e acesse \"Cadastro Livro ICMS/IPI\" para filtrar.", "Exclua registros e tente alterar o lançamento novamente.", "Erro"]
---

# Nota já foi gerada no Livro Fiscal de ICMS/IPI, não pode ser alterada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16585319936279) MENSAGEM:**

[ORA-20101]: Nota já foi gerada no Livro Fiscal de ICMS/IPI, não pode ser alterada. Nota de Nro Único: 'X'
[ORA-06512]: em "SANKHYA.TRG\_UPD\_TGFCAB", line 960
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_UPD\_TGFCAB'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16585319944471)SOLUÇÃO:**

![Imagem 3: Anote o número único do lançamento a ser alterado;](https://ajuda.sankhya.com.br/hc/article_attachments/16585297962007) Anote o número único do lançamento a ser alterado;

![Imagem 4: Acesse a tela "Cadastro Livro ICMS/IPI" (Caminho de acesso: Livros Fiscais » Arquivos) e filtre por esse número único:](https://ajuda.sankhya.com.br/hc/article_attachments/16585284490519) Acesse a tela **"Cadastro Livro ICMS/IPI"** (Caminho de acesso: Livros Fiscais » Arquivos) e filtre por esse número único:

![Imagem 5: Acesse a tela "Cadastro Livro ICMS/IPI" (Caminho de acesso: Livros Fiscais » Arquivos) e filtre por esse número único:](https://ajuda.sankhya.com.br/hc/article_attachments/15358723169943)

![Imagem 6: Clique em Aplicar;](https://ajuda.sankhya.com.br/hc/article_attachments/16585319962519) Clique em **Aplicar;**

![Imagem 7: Verifique os dados retornados pelo "Modo grade";](https://ajuda.sankhya.com.br/hc/article_attachments/16585305332887) Verifique os dados retornados pelo **"Modo grade";**

**![Imagem 8: IMPORTANTE: É retornada 1 linha por item do lançamento;](https://ajuda.sankhya.com.br/hc/article_attachments/16585319967127) IMPORTANTE:** É retornada 1 linha por item do lançamento;

![Imagem 9: Valide se as linhas retornadas correspondem ao lançamento que será alterado;](https://ajuda.sankhya.com.br/hc/article_attachments/16585298005271) Valide se as linhas retornadas correspondem ao lançamento que será alterado;

![Imagem 10: Através do botão (-) exclua tais registros;](https://ajuda.sankhya.com.br/hc/article_attachments/16585335738775)Através do botão (-) exclua tais registros;

![Imagem 11: Retorne ao lançamento e tente realizar a alteração desejada.](https://ajuda.sankhya.com.br/hc/article_attachments/16585284529815) Retorne ao lançamento e tente realizar a alteração desejada.

**![Imagem 12: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16585305362583) OBSERVAÇÃO:**

Caso seja apenas uma edição e necessite reenviar essa nota aos Livros, acesse a tela **"Geração ICMS/IPI"** e gere as notas do período novamente.

Caso deseje gerar apenas esse lançamento, ao clicar em **"Gerar agora"** informe o número único dessa.

**![Imagem 13: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16585305369367)CAUSA:**

Mensagem ocorre quando para o Nro único referente ao lançamento a ser alterado existem registros na tabela de Livros Fiscais (TGFLIV).

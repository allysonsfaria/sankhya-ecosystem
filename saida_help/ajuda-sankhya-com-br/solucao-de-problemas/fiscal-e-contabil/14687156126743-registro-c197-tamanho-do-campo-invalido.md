---
id: "14687156126743"
titulo: "Registro C197  Tamanho do campo inválido COD_AJ - Registro/Campo não informado ou inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14687156126743-Registro-C197-Tamanho-do-campo-inv%C3%A1lido-COD-AJ-Registro-Campo-n%C3%A3o-informado-ou-inv%C3%A1lido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:58:15Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "SEFAZ", "EFD", "Registro C197", "Verifique código do ajuste na tela \"Configurações de Ajustes de Apuração.\"", "Código ajuste deve ter 08 caracteres incluindo UF da empresa.", "Gere novamente os livros fiscais e arquivo EFD-ICMS/IPI.", "Erro"]
---

# Registro C197  Tamanho do campo inválido COD_AJ - Registro/Campo não informado ou inválido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16806702736791) MENSAGEM:**

Registro C197 Tamanho do campo inválido COD\_AJ - Registro/Campo não informado ou inválido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16806700714775)SOLUÇÃO:**

![Imagem 3: Acesse a tela "Configurações de Ajustes de Apuração" (Caminho de acesso: Livros Fiscais » Arquivos » Configurações de…](https://ajuda.sankhya.com.br/hc/article_attachments/16806700716183) Acesse a  tela **"Configurações de Ajustes de Apuração"** (Caminho de acesso: Livros Fiscais » Arquivos » Configurações de Ajustes de Apuração);

![Imagem 4: No ajuste código: 2 - AJUSTE CREDITO DE ICMS SIMPLES NACIONAL Empresa - X;](https://ajuda.sankhya.com.br/hc/article_attachments/16806702742167) No ajuste código: 2 -  AJUSTE CREDITO DE ICMS SIMPLES NACIONAL Empresa - X;

![Imagem 5: Tipo de Configuração: 1 - Ajustes de Documento, no 2 quadrante "Ajustes de Documentos - EFD Fiscal o campo: Código do…](https://ajuda.sankhya.com.br/hc/article_attachments/16806702743959) Tipo de Configuração: 1 - Ajustes de Documento, no 2 quadrante "Ajustes de Documentos - EFD Fiscal o campo: Código do ajuste: estava com a informação.: 1099050.

![Imagem 6: Tipo de Configuração: 1 - Ajustes de Documento, no 2 quadrante "Ajustes de Documentos - EFD Fiscal o campo: Código do…](https://ajuda.sankhya.com.br/hc/article_attachments/14686882630551)

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16806700722199) OBSERVAÇÃO:**

O código ajuste deve possuir 08 caracteres, os dois primeiros caracteres o sistema utiliza a UF da Empresa.

![Imagem 8: O código ajuste deve possuir 08 caracteres, os dois primeiros caracteres o sistema utiliza a UF da Empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/14686984345495)

![Imagem 9: Após confirmar a alteração, acesse a tela "Geração ICMS/IPI" (Caminho de acesso: Livros Fiscais » Arquivos » Geração…](https://ajuda.sankhya.com.br/hc/article_attachments/16806700723223) Após confirmar a alteração, acesse a tela **"Geração ICMS/IPI"** (Caminho de acesso: Livros Fiscais » Arquivos » Geração ICMS/IPI) e efetue a geração dos livros  fiscais novamente;

![Imagem 10: Na sequência, acesse a tela " EFD - Escrituração Fiscal Digital - ICMS/IPI" (Caminho de acesso: Livros Fiscais »…](https://ajuda.sankhya.com.br/hc/article_attachments/16806702749975) Na sequência, acesse a tela **"EFD - Escrituração Fiscal Digital - ICMS/IPI"** (Caminho de acesso: Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IP) e gere o arquivo EFD-Escrituração Fiscal Digital ICMS/IPI' novamente.

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16806702752279) CAUSA:**

Ocorre por informar o código de Ajuste incorretamente com a quantidade menor que o esperado no PVA no campo 'Código Ajuste'.

**Exemplo:** No PVA o campo espera 10 caracteres, na tela Configurações de Ajustes de Apuração o cadastro deve conter 08, sendo que os dois iniciais o sistema utiliza a UF da Empresa, ficando assim: MG10990505.

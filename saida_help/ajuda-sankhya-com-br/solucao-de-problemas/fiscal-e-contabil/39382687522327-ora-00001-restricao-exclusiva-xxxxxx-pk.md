---
id: "39382687522327"
titulo: "ORA-00001: restrição exclusiva (XXXXXX.PK_TGFEFDFH005) violada na geração do relatório EFD - Bloco H"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39382687522327-ORA-00001-restri%C3%A7%C3%A3o-exclusiva-XXXXXX-PK-TGFEFDFH005-violada-na-gera%C3%A7%C3%A3o-do-relat%C3%B3rio-EFD-Bloco-H"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T13:32:14Z"
rotulos: ["Configuração", "Relatórios", "Fiscal", "EFD", "Estoque", "Erro", "Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# ORA-00001: restrição exclusiva (XXXXXX.PK_TGFEFDFH005) violada na geração do relatório EFD - Bloco H

### MENSAGEM

Ora-00001: restrição exclusiva (xxxxxx.pk\_tgfefdfh005) violada

### SITUAÇÃO

Ao tentar gerar o relatório **"EFD - Fiscal"** (Livros Fiscais Conexão EFD - Fiscal), o sistema apresenta um erro de restrição exclusiva no banco de dados, impedindo a geração do arquivo.

### SOLUÇÃO

Para resolver o erro, verifique o preenchimento do campo **"Data de Inventario em substituição ao Bloco K"** na tela de geração do EFD. Existem duas situações possíveis:

**Situação 1: Quando não é necessário gerar o Bloco K**

**(1)**  Acesse a tela **"**EFD - Fiscal ICMS/IPI**"** (Livros Fiscais » Conexão » EFD - Fiscal ICMS/IPI).

**(2)**  Localize o campo **"Data de Inventario em substituição ao Bloco K"**.

**(3)**  Remova a data preenchida neste campo, deixando-o em branco.

**(4)**  Gere novamente o arquivo EFD. O sistema processará corretamente sem apresentar o erro.

**Situação 2: Quando é necessário gerar o Bloco K**

**(1)**  Acesse a tela **"EFD - Fiscal"** (Livros Fiscais Conexão EFD - Fiscal).

**(2)**  Verifique se o campo **"Data de Inventario em substituição ao Bloco K"** está preenchido.

**(3)**  Certifique-se de que foi realizada a cópia do estoque para a data informada.

**(4)**  Preencha também o campo **"Contagem para o K200"** com a mesma data do inventário de substituição.

**(5)**  Gere novamente o arquivo EFD. O sistema processará corretamente o Bloco H e o Bloco K sem apresentar erros.

### CAUSA

O erro citado, pode ter muitas causas, no caso citado nesse artigo, ocorre devido à duplicidade no insert do registro H005. Quando o campo "Data de Inventario em substituição ao Bloco K" está preenchido, mas a configuração para geração do Bloco K está incompleta ou incorreta, o sistema tenta inserir o mesmo registro duas vezes na tabela TGFEFDFH005, violando a chave primária (PK\_TGFEFDFH005).

Isso acontece porque o sistema identifica a necessidade de gerar informações de inventário, mas encontra inconsistências entre o preenchimento do campo **"Data do inventário de substituição"** e o campo **"Contagem para o K200"**, causando o processamento duplicado do registro.

Obs: O campo "**Data de Inventario em substituição ao Bloco K" só ficará visível caso o parâmetro GERBLHSUBSK estiver ligado.**

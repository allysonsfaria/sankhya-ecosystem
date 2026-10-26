---
id: "39382017523095"
titulo: "ERRO: Atenção, nota cancelada de número único: XXXX. Já existe como não cancelada no número único: XXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39382017523095-ERRO-Aten%C3%A7%C3%A3o-nota-cancelada-de-n%C3%BAmero-%C3%BAnico-XXXX-J%C3%A1-existe-como-n%C3%A3o-cancelada-no-n%C3%BAmero-%C3%BAnico-XXXX"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T13:32:41Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "EFD", "Erro", "Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# ERRO: Atenção, nota cancelada de número único: XXXX. Já existe como não cancelada no número único: XXXX

**MENSAGEM**

Atenção, nota cancelada de número único: XXXX. Já existe como não cancelada no número único: XXXX.

**SITUAÇÃO**

Esta mensagem aparece ao tentar **"Gerar o SPED Fiscal (ICMS/IPI)"** na tela **"Geração ICMS/IPI"** (Livros Fiscais » Conexão » EFD - Fiscal ICMS/IPI). O sistema identifica uma **"inconsistência de status"** para a nota fiscal mencionada, impedindo o prosseguimento da geração do arquivo fiscal.

**SOLUÇÃO**

Para corrigir este erro, configure a nota cancelada para que **"não atualize os livros fiscais"**, seguindo os passos abaixo:

**(1)** Acesse a tela **"Notas Canceladas"** (Comercial » Consulta » Notas Canceladas).
**(2)** Aplique o filtro informando o **"número único da nota"** (no exemplo abaixo) e a **"empresa"** correspondente.
**(3)** Localize e abra a nota cancelada identificada no filtro.
**(4)** Altere o campo **"Atualiza Livros Fiscais"** para a opção **"Não atualiza"**.

![Imagem 1: (1) Acesse a tela "Notas Canceladas" (Comercial » Consulta » Notas Canceladas). (2) Aplique o filtro informando o…](https://ajuda.sankhya.com.br/hc/article_attachments/40634200987031)

**(5)** Salve as alterações realizadas.
**(6)** Retorne à tela **"Geração ICMS/IPI"** e execute novamente a geração do livro fiscal.

Após seguir estes passos, o livro fiscal será gerado sem o erro mencionado.

**CAUSA**

O erro ocorre porque a nota cancelada estava configurada para atualizar os livros fiscais, gerando uma duplicidade de registro com uma nota não cancelada que possui o mesmo número único. Quando o sistema tenta processar ambas as notas durante a geração do **"SPED Fiscal"**, identifica a inconsistência e bloqueia o processo para evitar informações incorretas no arquivo fiscal.

Ao marcar a nota cancelada como **"Não atualiza"** os livros fiscais, o sistema passa a considerar apenas a nota válida, eliminando a duplicidade e permitindo a geração correta do arquivo.

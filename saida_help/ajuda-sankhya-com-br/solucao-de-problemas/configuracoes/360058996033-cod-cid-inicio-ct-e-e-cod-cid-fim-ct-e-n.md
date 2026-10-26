---
id: "360058996033"
titulo: "\"Cód. Cid. Inicio CT-e\" e \"Cód. Cid. Fim CT-e\" não são permitidas para este título.\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360058996033--C%C3%B3d-Cid-Inicio-CT-e-e-C%C3%B3d-Cid-Fim-CT-e-n%C3%A3o-s%C3%A3o-permitidas-para-este-t%C3%ADtulo"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-16T17:55:06Z"
rotulos: ["CT-e", "Configuração", "Importação", "TOP", "CFOP", "não apagar", "#RevisadoFer", "#AguardandoLider", "CORE_E02442", "Cód. Cid. Início CT-e", "Cód. Cid. Fim CT-e", "Importação de CT-e", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# "Cód. Cid. Inicio CT-e" e "Cód. Cid. Fim CT-e" não são permitidas para este título."

[CORE\_E02442] As informações de **"Cód. Cid. Inicio CT-e"** e **"Cód. Cid. Fim CT-e"** não são permitidas para este título.

### SITUAÇÃO

Esta mensagem aparece ao tentar importar um **"CT-e"** (Conhecimento de Transporte Eletrônico) através do **"Portal de Importação de XML"** (Comercial » Rotinas » Portal de Importação de XML). O sistema identifica incompatibilidade entre o tipo de título ou **"TOP"** utilizado e as informações obrigatórias do **"CT-e"**, impedindo a conclusão da importação.

![Imagem 1: Esta mensagem aparece ao tentar importar um "CT-e" (Conhecimento de Transporte Eletrônico) através do "Portal de…](https://ajuda.sankhya.com.br/attachments/token/n2CqOJBVMoITtbk0ULsanbfCB/?name=image.png)

### SOLUÇÃO

Para resolver este erro, execute os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação"** (Comercial » Arquivos » Cadastros » Tipos de Operação) e localize a **"TOP"** utilizada na importação do **"CT-e"**.

**(2)** Na aba **"NF-e / NFC-e"**, configure o campo **"Modelo do Documento"** selecionando o modelo 57 ou 67, conforme o **"XML"** do **"CT-e"** que está sendo importado.

**(3)** Acesse a aba **"Livro Fiscal"** e configure o campo **"Atualização do Livro ICMS"** como **"Livro de Entrada"**, além de informar os **"CFOPs"** corretos para a operação.

**(4)** Verifique se o campo **"Tipo de Movimento"** está configurado como **"Financeiro"**. Se a **"TOP"** estiver com o tipo **"Compras"**, o erro será apresentado. Esta configuração é obrigatória para importação de **"CT-e"**.

**(5)** Salve as alterações realizadas na **"TOP"**.

**(6)** Se já existe um título criado com erro, acesse a tela **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira), localize o título e verifique se o **"Modelo do Documento"** está correto (57 ou 67). Caso esteja incorreto, cancele o título e refaça a importação usando a **"TOP"** ajustada.

**(7)** Retorne ao **"Portal de Importação de XML"** (Comercial » Rotinas » Portal de Importação de XML), selecione o **"XML"** do **"CT-e"** e escolha a **"TOP"** ajustada.

### CAUSA

O erro ocorre quando a **"TOP"** utilizada na importação está configurada com **"Tipo de Movimento"** diferente de **"Financeiro"** (como **"Compras"**), ou quando o **"Modelo do Documento"** não está configurado como 57 ou 67.

Os campos **"Cód. Cid. Início CT-e"** e **"Cód. Cid. Fim CT-e"** são válidos exclusivamente para documentos modelo 57 ou 67 (**"CT-e"**). A **"SEFAZ"** exige obrigatoriamente as informações de cidades de início e fim do transporte para a correta escrituração fiscal e vínculo no **"SPED"**.

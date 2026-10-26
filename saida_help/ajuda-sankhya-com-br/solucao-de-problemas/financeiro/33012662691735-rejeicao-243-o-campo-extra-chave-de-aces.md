---
id: "33012662691735"
titulo: "Rejeição: 243 - O Campo Extra 'Chave de Acesso da NFe ou do CTe/CTE-OS' (Codigo: 'XX') deve ser informado!"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33012662691735-Rejei%C3%A7%C3%A3o-243-O-Campo-Extra-Chave-de-Acesso-da-NFe-ou-do-CTe-CTE-OS-Codigo-XX-deve-ser-informado"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:29:52Z"
rotulos: ["CT-e", "Configuração", "NF-e", "SEFAZ", "GNRE", "Passos para resolver", "Razão do erro", "Detalhe do erro", "O Campo Extra 'Chave de Acesso da NFe ou do CTe/CTE-OS'", "Rejeição: 243", "(Codigo: 'XX') deve ser informado!", "Documentos Eletrônicos"]
---

# Rejeição: 243 - O Campo Extra 'Chave de Acesso da NFe ou do CTe/CTE-OS' (Codigo: 'XX') deve ser informado!

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33012639176855) **MENSAGEM:**

Rejeição: 243 - O Campo Extra 'Chave de Acesso da NFe ou do CTe/CTE-OS' (Codigo: 'XX') deve ser informado!

**SITUAÇÃO:**

Ao tentar enviar um lote **GNRE**, ocorre a rejeição 243 - O Campo Extra 'Chave de Acesso da NFe ou do CTe/CTE-OS' (Codigo: 'XX') deve ser informado!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33012662690455) SOLUÇÃO:**

**(1)** Acesse a tela ''**Estados''** (Configurações» Cadastros» Endereços» Estados);

**(2)** Identifique o estado de destino para o qual a guia GNRE está sendo emitida.

**(3)** No estado identificado no passo anterior, confirme se:

- A opção **"Gera Campos Adicionais na GNRE"** (aba **''Geral''**) está marcada;
- O ''**Código (Campos Extras GNRE)''** (aba Geral) está preenchido com o valor esperado;
- O campo ''**Valor para Campo Extra GNRE''** (aba Geral) está corretamente configurado com a chave de acesso da NFe ou do CTe/CTE-OS, conforme exigência do estado.

![Imagem 3: O campo '' Valor para Campo Extra GNRE'' (aba Geral) está corretamente configurado com a chave de acesso da NFe ou do…](https://ajuda.sankhya.com.br/hc/article_attachments/33214259353623)

**(4)** Após realizar os devidos ajustes, será necessário gerar um novo lote e reenviá-lo ao portal da **GNRE**.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33012639177239)CAUSA:**

A rejeição ocorre ao enviar um lote GNRE quando os campos adicionais obrigatórios não estão corretamente preenchidos para o estado de destino.

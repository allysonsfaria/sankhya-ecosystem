---
id: "9040248704663"
titulo: "Mod.Doc.Fiscal 55 não pode alterar o campo \"Numeração Automática\" e nem o campo \"Último Código\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9040248704663-Mod-Doc-Fiscal-55-n%C3%A3o-pode-alterar-o-campo-Numera%C3%A7%C3%A3o-Autom%C3%A1tica-e-nem-o-campo-%C3%9Altimo-C%C3%B3digo"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:11:13Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "SEFAZ", "CORE_E05137", "Restrições na Alteração de Campos de Numeração Fiscal", "Erro"]
---

# Mod.Doc.Fiscal 55 não pode alterar o campo "Numeração Automática" e nem o campo "Último Código"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16672324470679) MENSAGEM:**

[CORE\_E05137]: Mod.Doc.Fiscal 55 não pode alterar o campo "Numeração Automática" e nem o campo "Último Código".

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16672324475927) SITUAÇÃO:**

Ao tentar alterar os campos **"numeração automática"** e **"ultimo código"** a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16672324483991) CAUSA:**

Ao tentar alterar os campos mencionados acima com usuário que não seja o SUP.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16672324482071) SOLUÇÃO:**

Os campos mencionados acima são de manutenção restrita (alheias ao controle de acesso), devido ao fato de que a numeração enviada para a SEFAZ não pode correr o risco de ficar desordenada, por isso a manutenção é restrita ao usuário SUP.

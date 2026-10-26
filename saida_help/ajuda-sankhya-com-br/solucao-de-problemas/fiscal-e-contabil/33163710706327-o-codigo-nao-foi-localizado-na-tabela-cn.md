---
id: "33163710706327"
titulo: "O Código não foi localizado na 'Tabela CNAE 21' associada a este campo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33163710706327-O-C%C3%B3digo-n%C3%A3o-foi-localizado-na-Tabela-CNAE-21-associada-a-este-campo"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:29:18Z"
rotulos: ["Configuração", "ECD", "ECF", "Fiscal", "Tabela 21 do Spe", "CNAE", "O Código não foi localizado na 'Tabela CNAE 21' associada a este campo", "CNAE Preponderante", "Erro"]
---

# O Código não foi localizado na 'Tabela CNAE 21' associada a este campo

**MENSAGEM**:

O Código não foi localizado na 'Tabela CNAE 21' associada a este campo

**SITUAÇÃO**:

A mensagem de erro geralmente ocorre quando o código **CNAE** (Classificação Nacional de Atividades Econômicas) informado **não consta** na **Tabela 21 do Sped**, utilizada em obrigações acessórias como a **ECD** (Escrituração Contábil Digital) e a **ECF** (Escrituração Contábil Fiscal).

**SOLUÇÃO**:

Acesse a tela **''Empresas''** (Configurações » Cadastros » Empresas) e, na aba **''Naturezas'',** preencha o campo **''CNAE Preponderante''** com o código correspondente.

![Imagem 1: Acesse a tela ''Empresas'' (Configurações » Cadastros » Empresas) e, na aba ''Naturezas'', preencha o campo ''CNAE…](https://ajuda.sankhya.com.br/hc/article_attachments/33163681511703)

**CAUSA**:

Isso indica que o sistema ou o validador tentou verificar a presença do código CNAE, informado na **Tabela 21 – CNAE**, porém **não o encontrou.**

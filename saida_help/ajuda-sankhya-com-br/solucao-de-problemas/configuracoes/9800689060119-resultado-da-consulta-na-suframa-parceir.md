---
id: "9800689060119"
titulo: "Resultado da consulta na SUFRAMA: Parceiro não habilitado na SUFRAMA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9800689060119-Resultado-da-consulta-na-SUFRAMA-Parceiro-n%C3%A3o-habilitado-na-SUFRAMA"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:06:04Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "SUFRAMA", "CORE_E04219", "Resultado da consulta na SUFRAMA: Parceiro não habilitado", "Erro", "Documentos Eletrônicos"]
---

# Resultado da consulta na SUFRAMA: Parceiro não habilitado na SUFRAMA

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19582398421271) MENSAGEM:**

[CORE\_E04219] Resultado da consulta na SUFRAMA: Parceiro não habilitado na SUFRAMA.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19582398430359) CAUSA:**

Quando a configuração do parceiro não foi realizada devidamente na SUFRAMA ou a empresa não foi devidamente informada no parâmetro **"Empresa padrão para utilização do certificado digital - EMPPADCERTDIG"**

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19582405582999) SOLUÇÃO:**

**1º Passo**
Verifique se o **Parceiro** (Caminho de acesso à tela: Configurações » Cadastros » Parceiros) tem cadastro ativo na SUFRAMA:

> Acessando o site:

<https://servicos.suframa.gov.br/cadastroWS/services/CadastroWebService>
> Consulte a Situação Cadastral - Exclusivo Fornecedor [Clique]
> Informe CNPJ
> Verifique inscrição e situação [Habilitada]

**2º Passo**
> Com a inscrição informada no campo 'Código SUFRAMA' clique no botão Outras Opções, em seguida em Atualizar situação cadastral SEFAZ/SUFRAMA.

>> Por fim, verifique se a empresa padrão para utilização de certificado digital foi cadastrada no parâmetro **"Empresa padrão para utilização do certificado digital - EMPPADCERTDIG"**, na tela **Preferências** (Caminho de acesso à tela: Configurações » Avançado » Preferências)

![Imagem 4: https://servicos.suframa.gov.br/cadastroWS/services/CadastroWebService > Consulte a Situação Cadastral - Exclusivo…](https://ajuda.sankhya.com.br/hc/article_attachments/19582398445591)

**Observação:** caso necessite de liberação da nota de forma pontual, para que o bloqueio não ocorra, desmarque no tipo de operação o campo **"Valida situação cadastro na ReceitaWS ?"** e realize um novo lançamento da nota.

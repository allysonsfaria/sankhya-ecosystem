---
id: "360050776454"
titulo: "245 - Rejeição: CNPJ Emitente não cadastrado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360050776454-245-Rejei%C3%A7%C3%A3o-CNPJ-Emitente-n%C3%A3o-cadastrado"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:30:38Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "SEFAZ", "Erro", "Artigo atualizado KCS", "Varejo - KCS", "Documentos Eletrônicos"]
---

# 245 - Rejeição: CNPJ Emitente não cadastrado

**MENSAGEM:**

[245] Rejeição: CNPJ emitente não cadastrado

**SITUAÇÃO**

Esta rejeição ocorre ao tentar emitir uma **"NF-e"** ou **"NFC-e"**, quando o **"CNPJ do emitente"** não está registrado na **"SEFAZ Estadual"** para autorização de documentos fiscais eletrônicos. O problema pode ocorrer por erro de digitação no cadastro da empresa ou pela falta de credenciamento específico no ambiente de testes (Homologação).

**CAUSA**

A rejeição **"245"** ocorre porque a **"SEFAZ"** não reconhece o **"CNPJ"** como autorizado a emitir documentos fiscais naquele ambiente. Isso pode acontecer por dois motivos principais:

1. **Erro no Cadastro:** O **"CNPJ"** informado no sistema está incorreto ou a empresa não está com a situação cadastral ativa ou habilitada junto à **"SEFAZ"**.

2. **Ambiente de Homologação:** Os ambientes de homologação e produção são independentes. Mesmo que o **"CNPJ"** esteja ativo na produção, ele precisa de cadastro específico na homologação para testes.

**SOLUÇÃO**

Siga os passos abaixo para verificar e corrigir a rejeição:

**(1)Verificação de Cadastro Interno:**
Acesse a tela **"Empresas"** (Configurações >> Cadastros >> Empresas), selecione a aba **"Geral"** e revise o campo **"CNPJ/CPF"**. Certifique-se de que os números estão corretos.

**(2)Consulta ao SINTEGRA:**
Consulte o **"CNPJ"** no site do **"SINTEGRA"** para validar os dados. Certifique-se de que a situação cadastral da empresa está **"ATIVA/HABILITADA"**. Caso encontre divergências, ajuste o cadastro no sistema e tente emitir novamente.
![Imagem 1: (1) Verificação de Cadastro Interno: Acesse a tela "Empresas" (Configurações >> Cadastros >> Empresas), selecione a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/18588204289687)

**(3)Verificação na SEFAZ (CCC):**
Se o cadastro no sistema estiver correto, acesse o [Portal de Consulta do Cadastro Centralizado de Contribuinte (CCC)](https://dfe-portal.svrs.rs.gov.br/NFE/CCC) . Selecione o ambiente (Homologação ou Produção) e verifique se o **"CNPJ"** consta como habilitado.

![Imagem 2: Solicitação de Credenciamento: Caso o "CNPJ" não esteja cadastrado (especialmente em homologação), entre em contato com…](https://ajuda.sankhya.com.br/hc/article_attachments/39568474292503)

**(4)Solicitação de Credenciamento:**
Caso o **"CNPJ"** não esteja cadastrado (especialmente em homologação), entre em contato com a **"SEFAZ"** do seu estado solicitando o credenciamento para o ambiente desejado. Informe que o **"CNPJ"** já está habilitado na produção, se for o caso.

**(5)Aguardar e Testar:**
Aguarde o prazo informado pela **"SEFAZ"** para a efetivação. Após o credenciamento, realize um novo teste de emissão no sistema.

**Importante:** Se a situação cadastral ou a permissão para **"NF-e"** não estiver ativa, acione o contador da empresa para regularização junto à **"SEFAZ"**.

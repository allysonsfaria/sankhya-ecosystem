---
id: "32379493025431"
titulo: "Rejeição: 288 - UF favorecida não está com a versão '2.00' do XML de dados habilitada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32379493025431-Rejei%C3%A7%C3%A3o-288-UF-favorecida-n%C3%A3o-est%C3%A1-com-a-vers%C3%A3o-2-00-do-XML-de-dados-habilitada"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:31:35Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "GNRE", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Rejeição: 288", "'2.00' do XML de dados habilitada", "UF favorecida nao esta com a versao", "Erro"]
---

# Rejeição: 288 - UF favorecida não está com a versão '2.00' do XML de dados habilitada

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32379493018391) **MENSAGEM:**

Lote XXX

Campo: ufFavorecida

Rejeição: 288 - UF favorecida nao esta com a versao '2.00' do XML de dados habilitada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32379493019415)SOLUÇÃO:**

Verifique se a versão correta da GNRE está configurada para o estado vinculado ao lote. Para isso, acesse a tela **"Estados"** (Caminho: Configurações » Cadastros » Endereços » Estados), selecione o cadastro da Unidade Federativa (UF) correspondente, vá até as abas **"Geral" e** **"GNRE Unidade Federativa"** e garanta que em ambas os campos **"Versão GNRE"**estejam com opção **2.0 selecionada.**

![Imagem 3: Verifique se a versão correta da GNRE está configurada para o estado vinculado ao lote. Para isso, acesse a tela…](https://ajuda.sankhya.com.br/hc/article_attachments/32379462524695)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32379493020439)CAUSA:**

Esta mensagem é exibida ao tentar consultar o status de um lote GNRE na tela **"Geração de Lote GNRE"**, quando o estado vinculado ao lote não possui a versão 2.0 da GNRE corretamente configurada.

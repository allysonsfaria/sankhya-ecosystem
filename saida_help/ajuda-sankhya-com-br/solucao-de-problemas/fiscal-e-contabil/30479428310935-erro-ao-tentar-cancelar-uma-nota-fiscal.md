---
id: "30479428310935"
titulo: "Erro ao tentar Cancelar uma Nota Fiscal de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30479428310935-Erro-ao-tentar-Cancelar-uma-Nota-Fiscal-de-Servi%C3%A7o"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-09-25T13:52:03Z"
rotulos: ["Configuração", "Cidades", "Portal de Vendas", "Prefeituras", "NFS-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro ao tentar Cancelar uma Nota Fiscal de Serviço", "código do erro: 1304", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Erro ao tentar Cancelar uma Nota Fiscal de Serviço

**MENSAGEM**

Ao tentar cancelar NFS-e, o sistema apresenta a seguinte mensagem de erro:

**"código do erro: 1304 Mensagem: Erro ao cancelar NFS-e: Esta NFS-e não poderá ser cancelada pois já foi emitida a guia de recolhimento de ISS para ela"**

**SITUAÇÃO**

Essa mensagen ocorre quando o usuário tenta cancelar uma nota fiscal através do sistema, mas existem impedimentos relacionados a registros em livros fiscais e fechamento de competência de ISS.

**SOLUÇÃO**

A solução varia conforme o erro apresentado. Siga opasso a passo a seguir:

**Erro 1304 - NFS-e com guia de recolhimento de ISS emitida**

**(1)**Verifique junto ao setor de NFS-e da Prefeitura qual é o período do fechamento da competência para cancelamento ou substituição. Caso o prazo esteja ultrapassado, verifique a possibilidade de processo administrativo para cancelamento.

**(2)**Após autorização da Prefeitura, acesse a tela **"Cidades"** (Configurações >> Cadastros >> Endereços >> Cidades), aba **"NFS-e"**, e altere o campo **"Tipo de Cancelamento para NFS-e"** para a opção de "Cancelamento via Prefeitura sem numero de protocolo". Salve.

![Imagem 1: (1) Verifique junto ao setor de NFS-e da Prefeitura qual é o período do fechamento da competência para cancelamento ou…](https://ajuda.sankhya.com.br/hc/article_attachments/30485179652503)

**(3)**Acesse o **"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas), localize a nota e clique em **"Cancelar"**. Preencha os dados no pop-up e confirme.

![Imagem 2: (1) Verifique junto ao setor de NFS-e da Prefeitura qual é o período do fechamento da competência para cancelamento ou…](https://ajuda.sankhya.com.br/hc/article_attachments/30485179655319)

**(4)Importante:** Após o cancelamento manual, retorne ao **"Cidades"** e volte o campo **"Tipo de Cancelamento para NFS-e"** para **"Via WebService"**.

**CAUSA**

O erro ao cancelar notas fiscais tem a seguinte causa:

• **Registro em livros fiscais:** Nota já escriturada nos livros de ICMS ou ISS.

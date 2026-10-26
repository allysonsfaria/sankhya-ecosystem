---
id: "360043363673"
titulo: "Tipo de serviço deve ser informado no cadastro do serviço ou na alíquota de ISS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043363673-Tipo-de-servi%C3%A7o-deve-ser-informado-no-cadastro-do-servi%C3%A7o-ou-na-al%C3%ADquota-de-ISS"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:19Z"
rotulos: ["#PUBLIFER", "CORE_E03913", "Produtos", "ISS", "Configuração", "Impostos", "NFS-e", "Preencher campo \"Tipo de Serviço\"", "Verificar cadastro de Serviço e Alíquotas de ISS", "Problema ocorre por campo incompleto na NFS-e"]
---

# Tipo de serviço deve ser informado no cadastro do serviço ou na alíquota de ISS

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16108911224215) MENSAGEM:**

[CORE\_E03913] Tipo de serviço deve ser informado no cadastro do serviço ou na alíquota de ISS.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108895301143) SOLUÇÃO:**

![Imagem 3: Acesse a tela "Serviço" ( Caminho de acesso: Configurações » Cadastros » Produtos » Serviço) e verifique os cadastros…](https://ajuda.sankhya.com.br/hc/article_attachments/16108946801047) Acesse a tela **"Serviço"** (Caminho de acesso: Configurações » Cadastros » Produtos » Serviço) e verifique os cadastros abaixo:

- Aba **Impostos** » campo **"Tipo de Serviço"**: preencha

![Imagem 4: Aba Impostos » campo "Tipo de Serviço" : preencha](https://ajuda.sankhya.com.br/hc/article_attachments/14653532476823)

- Aba **Alíquotas de ISS »** campo **"Tipo de Serviço":**  analise se existem configurações para a empresa do lançamento e preencha o campo.

![Imagem 5: Aba Alíquotas de ISS » campo "Tipo de Serviço": analise se existem configurações para a empresa do lançamento e…](https://ajuda.sankhya.com.br/hc/article_attachments/14653566132119)

![Imagem 6: Acesse a tela "Alíquotas de ISS" (Caminho de acesso: Contratos » Arquivos » Cadastros » Alíquotas de ISS): localize a…](https://ajuda.sankhya.com.br/hc/article_attachments/16108895305495) Acesse a tela **"Alíquotas de ISS"** (Caminho de acesso: Contratos » Arquivos » Cadastros » Alíquotas de ISS): localize a cidade, o serviço e a empresa específicos para o lançamento e preencha o campo **"Tipo de Serviço"**.

![Imagem 7: Acesse a tela "Alíquotas de ISS" (Caminho de acesso: Contratos » Arquivos » Cadastros » Alíquotas de ISS): localize a…](https://ajuda.sankhya.com.br/hc/article_attachments/14653815963031)

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16108911228311) CAUSA:**

Ao realizar emissão de NFS-e, e para determinado serviço  o campo Tipo de Serviço não encontrar-se devidamente preenchido ou com informação incorretas, será apresentada a mensagem.

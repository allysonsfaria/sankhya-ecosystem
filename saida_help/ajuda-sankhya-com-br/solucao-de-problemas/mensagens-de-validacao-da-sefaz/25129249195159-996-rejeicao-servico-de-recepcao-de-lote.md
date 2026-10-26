---
id: "25129249195159"
titulo: "996 - Rejeição: Serviço de recepção de lotes desativado (NT2024.001). Migrar para recepção síncrona!"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25129249195159-996-Rejei%C3%A7%C3%A3o-Servi%C3%A7o-de-recep%C3%A7%C3%A3o-de-lotes-desativado-NT2024-001-Migrar-para-recep%C3%A7%C3%A3o-s%C3%ADncrona"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-24T12:42:31Z"
rotulos: ["ERROMDFE", "MDF-e", "Configuração", "Atualização", "SEFAZ", "Transporte", "996 - Rejeição", "Documentos Eletrônicos"]
---

# 996 - Rejeição: Serviço de recepção de lotes desativado (NT2024.001). Migrar para recepção síncrona!

A rejeição acima é apresentada na tentativa de emissão do MDF-e no envio assíncrono. Pois e**m 29/04/2024 a [SEFAZ do RS informou que o serviço assíncrono do MDF-e será desligado em 30/06/2024](https://dfe-portal.svrs.rs.gov.br/Dce/Avisos), conforme previsto no MOC 3.00b e confirmando na NT 2024.001. Porém, com o problema das enchentes no Rio Grande do Sul, o ambiente de testes deles ficou fora do ar por muito tempo, o que retardou o processo de testes e liberação dos ajustes necessários.

Portanto, as empresas que utilizam o MDF-e não poderão mais utilizar o serviço assíncrono. Desta forma, a partir de 01/07/2024, as comunicações com a SEFAZ do MDF-e deverão ser todas síncronas, ou seja, manifesto a manifesto. Vale destacar que, a SEFAZ do Rio Grande do Sul é responsável pelo processamento do MDF-e de todo o país, conforme determinação do CONFAZ.

No serviço síncrono, o Sankhya Om envia um MDF-e e precisa aguardar a SEFAZ receber o documento, processá-lo e devolver o retorno. Como há uma dependência direta da SEFAZ, receber e processar cada documento, o tempo de processamento de cada MDF-e pode ficar um pouco maior. Logo, pode ser necessário ampliar o timeout (tempo limite) de comunicação (Console NF-e » Configurações).**

![Imagem 1: A rejeição acima é apresentada na tentativa de emissão do MDF-e no envio assíncrono. Pois e m 29/04/2024 a SEFAZ do RS…](https://ajuda.sankhya.com.br/hc/article_attachments/25129283616919)

**Para adequação à essas determinações, a Sankhya está liberando os seguintes builds (número após a letra “b”, ex.: 4.2Xb150, o 150 é o build) do Sankhya Om:**

4.28b26, 4.27b85, 4.26b209, 4.25b238, 4.24b234

**Caso utilize o SANNFe externo, também precisará atualizá-lo, conforme builds:**

SanNFe 4.28b1315, SanNFe 4.27b1315, SanNFe 4.26b1315, SanNFe 4.25b1315, SanNFe 4.24b1315

**Além da atualização para os builds recomendados acima, ou superiores, siga os passos abaixo:**

Entre na tela **"Empresa"** (Caminho: Comercial » Preferências » Empresa), acesse a aba **"MDF-e"** e ative o campo **“Usar modo síncrono para envio do XML”**, como mostrado na figura a seguir:

![Imagem 2: Entre na tela "Empresa" (Caminho: Comercial » Preferências » Empresa), acesse a aba "MDF-e" e ative o campo “Usar modo…](https://content.app-us1.com/cdn-cgi/image/width=650,dpr=2,fit=scale-down,format=auto,onerror=redirect/rJdy4/2024/06/28/dce6bb18-971a-43e2-819d-7a3265f1db33.png?r=670884786)

**Dessa forma, as emissões do MDF-e subsequentes serão feitas utilizando o serviço síncrono conforme determinado. Se o serviço assíncrono for utilizado ele gerará a rejeição:
996 - Rejeição: Serviço de recepção de lotes desativado (NT2024.001). Migrar para recepção síncrona!**

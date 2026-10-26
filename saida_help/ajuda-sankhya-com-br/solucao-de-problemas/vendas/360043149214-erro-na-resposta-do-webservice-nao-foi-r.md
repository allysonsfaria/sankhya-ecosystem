---
id: "360043149214"
titulo: "Erro na resposta do Webservice não foi retornado um xml válido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043149214-Erro-na-resposta-do-Webservice-n%C3%A3o-foi-retornado-um-xml-v%C3%A1lido"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:02Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "XML", "SEFAZ", "NFS-e", "Erro no XML do Webservice", "Verificar certificado digital", "Indisponibilidade da SEFAZ", "Erro"]
---

# Erro na resposta do Webservice não foi retornado um xml válido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16144747234199) MENSAGEM:**

Erro na resposta do Webservice não foi retornado um xml válido. Uma das possíveis causas para esse erro é algum erro que ocorreu no servidor SEFAZ e foi redirecionado para uma página HTML

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16144747237527) SOLUÇÃO:**

Abaixo serão descritas possíveis causas para essa mensagem:

**![Imagem 3: Certificado Digital expirado :](https://ajuda.sankhya.com.br/hc/article_attachments/16144747241367) Certificado Digital expirado**:

- Acesse a tela **"[Console NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597734)"** (Caminho de acesso: Comercial > Configuração)
- Verifique se para o CNPJ da empresa emitente o certificado está com data de validação atualizada:

![Imagem 4: Verifique se para o CNPJ da empresa emitente o certificado está com data de validação atualizada:](https://ajuda.sankhya.com.br/hc/article_attachments/14687706022807)

- Caso o certificado encontre-se expirado, providencie o arquivo atualizado no formato A1 junto ao seu contador. Em caso de dúvida no processo de troca, verifique o artigo: [Como realizar troca de certificado digital no Sankhya W?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043023933)

![Imagem 5: Indisponibilidade no serviço, SEFAZ ESTADUAL ou Prefeitura:](https://ajuda.sankhya.com.br/hc/article_attachments/16144747246103) **Indisponibilidade no serviço, SEFAZ ESTADUAL ou Prefeitura:**

- Caso a mensagem ocorra na emissão de NFS-e, certifique-se junto a sua Prefeitura que o serviço de emissão encontra-se em Operação.
- Caso a mensagem ocorra na emissão de NF-e, acesse o link [http://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=Skeuqr8PQBY= ,](http://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=Skeuqr8PQBY=)para verificar disponibilidade do seu Estado.
- Caso a indisponibilidade exista, é necessário aguardar o retorno da operação para retomar suas emissões.
- Acesse a tela Console NF-e, na aba **"Status do Serviço"** selecione o CNPJ da empresa emissora e o Ambiente **"Produção"** e clique em testar.
- Se for retornado algum erro, busque pela solução do mesmo em nossa Central de Ajuda.

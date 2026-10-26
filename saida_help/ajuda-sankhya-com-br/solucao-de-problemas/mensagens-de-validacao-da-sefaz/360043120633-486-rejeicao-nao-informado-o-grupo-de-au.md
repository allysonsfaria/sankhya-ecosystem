---
id: "360043120633"
titulo: "486 Rejeição: Não informado o Grupo de Autorização para UF que exige a identificação do Escritório de Contabilidade na Nota Fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043120633-486-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-o-Grupo-de-Autoriza%C3%A7%C3%A3o-para-UF-que-exige-a-identifica%C3%A7%C3%A3o-do-Escrit%C3%B3rio-de-Contabilidade-na-Nota-Fiscal"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:20Z"
rotulos: ["ERRONF", "#RevisadoGui", "Configuração", "NF-e", "XML", "SEFAZ", "486", "Rejeição por Falta de Identificação do Escritório de Contabilidade", "Erro", "Documentos Eletrônicos"]
---

# 486 Rejeição: Não informado o Grupo de Autorização para UF que exige a identificação do Escritório de Contabilidade na Nota Fiscal

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16486334106519) **MENSAGEM:**

486 Rejeição: Não informado o Grupo de Autorização para UF que exige a identificação do Escritório de Contabilidade na Nota Fiscal

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16486322693911) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16486322700695) Acesse: Comercial » Preferências » Empresa

- Aba: **"Contador"**
- Campo **"Enviar responsável contábil na NFE?":** marque

**Nota:** Esta informação dependerá de cada SEFAZ Estadual exigi-la. Verifique com o contador da Empresa se a Sefaz do seu estado exige esta informação e, caso positivo, marque esta opção e preencha os dados desta aba. Caso negativo, desmarque a opção.

![Imagem 4: Após os ajustes, gere o lote da nota novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16486334114327) Após os ajustes, gere o lote da nota novamente.

![Imagem 5: Configure a aba " Acesso ao XML da NF-e/CTe", na tela " Empresa " (Caminho de acesso: Comercial » Preferências »…](https://ajuda.sankhya.com.br/hc/article_attachments/16486334119959) Configure a aba "**Acesso ao XML da NF-e/CTe",** na tela **"**[**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)**"** (Caminho de acesso: Comercial » Preferências » Empresa)com o nome SEFAZ e o CNPJ informada na mensagem de erro.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16486334126359) CAUSA:**

Quando for emitida uma NF-e e a Sefaz exigir que seja informado no Grupo de Autorização para obter o XML (autXML) a identificação (CNPJ ou CPF) do Escritório de Contabilidade e o grupo em questão não for informado, será retornada a rejeição.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16486334129303) OBSERVAÇÃO:**

([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=v9JbkEY7evI=)) - Nota Técnica.

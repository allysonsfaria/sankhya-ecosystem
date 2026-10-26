---
id: "360043100913"
titulo: "Invalid content was found starting with element 'xNome'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043100913-Invalid-content-was-found-starting-with-element-xNome"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:51Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "NF-e", "XML", "SEFAZ", "CFOP", "Correção do Erro 'xNome' na NF-e", "Erro"]
---

# Invalid content was found starting with element 'xNome'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16504175552535) MENSAGEM:**

cvc-complex-type.2.4.a: Invalid content was found starting with element 'xNome'. One of '{"http://www.portalfiscal.inf.br/nfe":CNPJ, "http://www.portalfiscal.inf.br/nfe":CPF, "http://www.portalfiscal.inf.br/nfe":idEstrangeiro}' is expected.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16504163209623) SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16504175560983) Acesse: Configurações » Cadastros » Parceiros

Aba: **"Identificação"**

- Campo **"Nome"**
- Campo **"CNPJ/CPF"**

Verifique se o valor informado no campo CNPJ/CPF está correto e válido junto a Receita Federal.

![Imagem 4: Caso a nota que esteja emitindo seja uma nota de acompanhamento de cupom fiscal, o sistema vai trazer o parceiro…](https://ajuda.sankhya.com.br/hc/article_attachments/16504175562135) Caso a nota que esteja emitindo seja uma nota de acompanhamento de cupom fiscal, o sistema vai trazer o parceiro "CONSUMIDOR" utilizado no lançamento do cupom fiscal, porém devido a regras de validação da SEFAZ será necessário cadastrar o novo parceiro para o qual está sendo emitido o acompanhamento e alterar o código do parceiro no lançamento da nota de acompanhamento. Feito isso, gere o lote novamente.

![Imagem 5: Em operações de exportações, parceiros destinatário do exterior (CFOP Iniciado em 7), verifique o parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/16504175563927) Em operações de exportações, parceiros destinatário do exterior (CFOP Iniciado em 7), verifique o parâmetro **"CODPAISBRASIL"**, esse deve ser configurado com o valor  "55".
Também informe o campo Identificação de Estrangeiro no cadastro de Parceiro.

**![Imagem 6: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16504175567639) CAUSA**:

Ocorre quando é emitido uma NF-e de acompanhamento e o Parceiro é um cadastro 'curinga' para emissão de Cupom Fiscal e precisa posteriormente emitir uma Nota de Acompanhamento de Cupom Fiscal e não se cadastra definitivamente o Parceiro da Nota.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16504163227927) OBSERVAÇÃO:**

**(1)** Consulta:

**(2)**CPF:

<https://www.receita.fazenda.gov.br/Aplicacoes/SSL/ATCTA/CPF/ConsultaSituacao/ConsultaPublica.asp>

**(2)**CNPJ:

<https://www.receita.fazenda.gov.br/pessoajuridica/cnpj/cnpjreva/cnpjreva_solicitacao2.asp>

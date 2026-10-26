---
id: "360042725654"
titulo: "NF-e com identificação de estrangeiro e inscrição estadual informada para destinatário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042725654-NF-e-com-identifica%C3%A7%C3%A3o-de-estrangeiro-e-inscri%C3%A7%C3%A3o-estadual-informada-para-destinat%C3%A1rio"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:41Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "NF-e", "SEFAZ", "CFOP", "925", "Rejeição 925: Identificação Estrangeiro com Inscrição Estadual", "Identificação de Estrangeiro"]
---

# NF-e com identificação de estrangeiro e inscrição estadual informada para destinatário

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16512065472919) MENSAGEM:**

[925 - Rejeição]: NF-e com identificação de estrangeiro e inscrição estadual informada para destinatário.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16512078254487) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: O erro será retornado quando haver ' Identificação de Estrangeiro' e ' Insc. Estadual / Identidade' e se trabalhar com…](https://ajuda.sankhya.com.br/hc/article_attachments/16512078257559) O erro será retornado quando haver 'Identificação de Estrangeiro' e  'Insc. Estadual / Identidade' e se trabalhar com CFOP's iniciados em 3 ou 7.

Desta forma, informe apenas a 'Identificação de Estrangeiro', **deixando em branco a 'Insc. Estadual / Identidade'.**

![Imagem 4: Acesse a tela " Parceiros" (Caminho de acesso: Configurações » Cadastros )](https://ajuda.sankhya.com.br/hc/article_attachments/16512065483287) Acesse a tela "**[Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)** (Caminho de acesso: Configurações » Cadastros)

- Aba: **"Identificação"**
- Campo **"Identificação de Estrangeiro":** utilize o campo "**Identificação de Estrangeiro**" para Parceiros do exterior, em vendas com geração de NF-e ou NFC-e. Informe aqui o número do passaporte ou outro documento legal para identificar a pessoa estrangeira. A informação deste campo deve ter entre 5 e 20 caracteres/números.

![Imagem 5: Campo "Identificação de Estrangeiro": utilize o campo " Identificação de Estrangeiro " para Parceiros do exterior, em…](https://ajuda.sankhya.com.br/hc/article_attachments/14612294635543)

![Imagem 6: Após os ajustes, gere o lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16512078262167) Após os ajustes, gere o lote novamente.

**![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16512078265367) IMPORTANTE:**

O parâmetro **"ACEITAIEBRANCO - Aceita Insc. Est. de Parceiro em branco?"** deve estar habilitado para que a I.E. fique vazia no cadastro do Parceiro.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16512065493783)CAUSA:**

Quando for realizada uma operação estrangeira, tag <idEstrangeiro>, e CFOP com iniciais 3 ou 7, mas em conjunto está sendo informada 'Inscrição Estadual', tag <IE>, do Parceiro.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16512065495703) OBSERVAÇÃO:**

([NT2019/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=)) - Nota técnica

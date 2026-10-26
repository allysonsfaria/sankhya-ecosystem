---
id: "360042525874"
titulo: "IE do destinatário não informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042525874-IE-do-destinat%C3%A1rio-n%C3%A3o-informada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-21T18:51:00Z"
rotulos: ["ERRONF", "ERROMDFE", "ERROCTE", "#PUBLIFER", "#RevisadoClaudio", "Configuração", "Fiscal", "Parceiro", "NF-e", "SEFAZ", "232", "Verifique Inscrição Estadual no SINTEGRA", "Ajuste IE e Classificação de ICMS", "Gere novo lote após ajustes", "Erro"]
---

# IE do destinatário não informada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16457260373143) MENSAGEM:**

[232 - Rejeição]: IE do destinatário não informada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457260377239) SOLUÇÃO:**

![Imagem 3: Consulte o CNPJ do destinatário no SINTEGRA para verificar qual a Inscrição Estadual está vinculada ao seu CNPJ.](https://ajuda.sankhya.com.br/hc/article_attachments/16457211476119) Consulte o CNPJ do destinatário no SINTEGRA para verificar qual a Inscrição Estadual está vinculada ao seu CNPJ.

<http://www.sintegra.gov.br/>

No site do Sintegra, selecione o Estado do respectivo parceiro destinatário e realize a consulta de seu CNPJ.

É possível também usar o [Portal de Consulta do Cadastro Centralizado de Contribuinte (CCC)](https://dfe-portal.svrs.rs.gov.br/NFE/CCC)

![Imagem 4: Identificado a Inscrição Estadual correta do destinatário, altere essa informação no cadastro do parceiro:](https://ajuda.sankhya.com.br/hc/article_attachments/16457260387735) Identificado a Inscrição Estadual correta do destinatário, altere essa informação no cadastro do parceiro:

- Tela "[**Parceiros"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494) (Caminho de acesso: Configurações » Cadastros)
- Aba: "**Identificação"**

![Imagem 5: Aba: " Identificação"](https://ajuda.sankhya.com.br/hc/article_attachments/14446951831703)

![Imagem 6: Certifique-se de que a 'Classificação de ICMS' vinculada em seu cadastro, encontra-se correta, em caso negativo realize…](https://ajuda.sankhya.com.br/hc/article_attachments/16457260390935) Certifique-se de que a 'Classificação de ICMS' vinculada em seu cadastro, encontra-se correta, em caso negativo realize os devidos ajustes:

- Tela Parceiros : (Caminho de acesso: Configurações » Cadastros)
- Aba:  "**Fiscal"**
- Campo: **"Classificação de ICMS"**

![Imagem 7: Campo: "Classificação de ICMS"](https://ajuda.sankhya.com.br/hc/article_attachments/14446862609687)

![Imagem 8: Realizado os ajustes acima, redigite o cabeçalho da nota e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16457260394007) Realizado os ajustes acima, redigite o cabeçalho da nota e gere um novo lote.

**![Imagem 9: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16457211489431) IMPORTANTE:**

Para destinatários do '**Distrito Federal**', ao realizar a consulta no Sintegra, verifique se existem informações para o campo '**CF/DF' (Cadastro Fiscal do Distrito Federal).** Caso exista, essa informação deverá ser preenchida no campo "**Inscrição Estadual"**.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16457260399639) CAUSA:**

Quando for emitida uma NF-e para destinatário, identificado como Isento (indIEDest = 2) ou Não Contribuinte (indIEDest = 9), que possui Inscrição Estadual (IE) ativa no seu Estado (UF) e essa não for informada em seus dados, será retornado a rejeição.

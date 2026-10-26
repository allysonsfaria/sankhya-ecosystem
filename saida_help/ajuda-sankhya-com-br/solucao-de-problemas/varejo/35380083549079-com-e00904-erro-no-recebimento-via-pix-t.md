---
id: "35380083549079"
titulo: "[COM_E00904] Erro no recebimento via PIX TEF - Não há configuração adequada ao PIX TEF no cadastro da empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35380083549079--COM-E00904-Erro-no-recebimento-via-PIX-TEF-N%C3%A3o-h%C3%A1-configura%C3%A7%C3%A3o-adequada-ao-PIX-TEF-no-cadastro-da-empresa"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T14:25:15Z"
rotulos: ["Configuração", "TEF", "Preferências", "Financeiro", "PIX", "TEFGATEWAY", "Passos para resolver", "Razão do erro", "Detalhe do erro", "SITEF", "PIX TEF", "Erro", "COM_E00904", "Tipo de Pix", "Squad Varejo"]
---

# [COM_E00904] Erro no recebimento via PIX TEF - Não há configuração adequada ao PIX TEF no cadastro da empresa

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/35380051727511) **MENSAGEM:**

[COM\_E00904] Não há configuração adequada ao PIX TEF no cadastro da empresa.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35380083543447)SOLUÇÃO:**

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** No campo **''Chave ou descrição''** pesquise pelo parâmetro **''TEFGATEWAY''** e verifique se ele está configurado como **SiTef**.

![Imagem 3: (2) No campo ''Chave ou descrição'' pesquise pelo parâmetro ''TEFGATEWAY'' e verifique se ele está configurado como…](https://ajuda.sankhya.com.br/hc/article_attachments/36628308847255)

**(3)** Em seguida, acesse a tela [**''Empresa''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa).

**(4)** Na aba [**''Pix''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/4413021641495-Pix) confirme que o campo **''Tipo de Pix''** está definido como **''TEF''.**

![Imagem 4: (4) Na aba ''Pix'' confirme que o campo ''Tipo de Pix'' está definido como ''TEF''.](https://ajuda.sankhya.com.br/hc/article_attachments/36636868046103)

**(5)** Além disso, é indispensável que os campos **''Conta para Recebimento PIX TEF''**, **''TOP Cancelamento Pix - Financeiro''**, **''TOP Cancelamento Pix - Recebimento''**, **''TOP Cancelamento Pix - Pagamento''** e **''Natureza Cancelamento Pix''** deverão estar devidamente preenchidos para que o processo de recebimento ocorra com sucesso.

Saiba mais em: [Saiba como configurar o recebimento via Pix](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35380083545239)CAUSA:**

A mensagem ocorre quando não existe configuração do PIX TEF na base ou quando as configurações relacionadas estão incompletas, impedindo que o sistema valide corretamente o processo de recebimento.

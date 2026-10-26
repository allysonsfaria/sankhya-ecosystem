---
id: "42310016816151"
titulo: "O valor inicial doGrau 1 n\\u00e3o pode conter mais do que 0 d\\u00edgitos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42310016816151-O-valor-inicial-doGrau-1-n-u00e3o-pode-conter-mais-do-que-0-d-u00edgitos"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-09-30T16:48:59Z"
rotulos: ["MASCENDWMS", "WMS - KCS", "Gerar endereços", "Cadastro Massivo de Endereços", "gerar sequências com letras ou alfanuméricas"]
---

# O valor inicial doGrau 1 n\u00e3o pode conter mais do que 0 d\u00edgitos

**MENSAGEM**

O valor inicial doGrau 1 n\u00e3o pode conter mais do que 0 d\u00edgitos

**SITUAÇÃO**

Ao clicar no botão **''Gerar endereços''** na tela **''Cadastro Massivo de Endereços''** (WMS » Cadastros » Cadastro Massivo de Endereços) o sistema apresenta a mensagem acima.

**SOLUÇÃO**

**(1)** Acesse a tela **''Preferências''** (Configurações » Avançado » Preferências).

**(2)** Localize o parâmetro **''MASCENDWMS''**.

**(3)** Altere a configuração de **''aa\.aa\.aa\.aa\.aa;1''**, para **''99\.99\.99\.99\.99;1'**'

**CAUSA**

A tela ''Cadastro Massivo de Endereços'' (WMS » Cadastros » Cadastro Massivo de Endereços) não foi projetado para gerar sequências com letras ou alfanuméricas, apenas numéricas.

---
id: "18708801374103"
titulo: "The value '0.00' of element 'ItemListaServico' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18708801374103-The-value-0-00-of-element-ItemListaServico-is-not-valid"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:52:10Z"
rotulos: ["Configuração", "Cidades", "Impostos", "NFS-e", "Erro de Validação: Valor Inválido para ItemListaServico", "Erro"]
---

# The value '0.00' of element 'ItemListaServico' is not valid

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18708833153431) **MENSAGEM:**

cvc-enumeration-valid: Value '1.05' is not facet-valid with respect to enumeration '[01.01, 01.02, 01.03, 01.04, 01.05, 01.06, 01.07, 01.08, 01.09, 02.01, 03.02, 03.03, 03.04, 03.05, 04.01, 04.02, 04.03, 04.04, 04.05, 04.06, 04.07, 04.08, 04.09, 04.10, 04.11, 04.12, 04.13, 04.14, 04.15, 04.16, 04.17, 04.18, 04.19, 04.20, 04.21, 04.22, 04.23, 05.01, 05.02, 05.03, 05.04, 05.05, 05.06, 05.07, 05.08, 05.09, 06.01, 06.02, 06.03, 06.04, 06.05, 06.06, 07.01, 07.02, 07.03, 07.04, 07.05, 07.06, 07.07, 07.08, 07.09, 07.10, 07.11, 07.12, 07.13, 07.16, 07.17, 07.18, 07.19, 07.20, 07.21, 07.22, 08.01, 08.02, 09.01, 09.02, 09.03, 10.01, 10.02, 10.03, 10.04, 10.05, 10.06, 10.07, 10.08, 10.09, 10.10, 11.01, 11.02, 11.03, 11.04, 11.05, 12.01, 12.02, 12.03, 12.04, 12.05, 12.06, 12.07, 12.08, 12.09, 12.10, 12.11, 12.12, 12.13, 12.14, 12.15, 12.16, 12.17, 13.02, 13.03, 13.04, 13.05, 14.01, 14.02, 14.03, 14.04, 14.05, 14.06, 14.07, 14.08, 14.09, 14.10, 14.11, 14.12, 14.13, 14.14, 15.01, 15.02, 15.03, 15.04, 15.05, 15.06, 15.07, 15.08, 15.09, 15.10, 15.11, 15.12, 15.13, 15.14, 15.15, 15.16, 15.17, 15.18, 16.01, 16.02, 17.01, 17.02, 17.03, 17.04, 17.05, 17.06, 17.08, 17.09, 17.10, 17.11, 17.12, 17.13, 17.14, 17.15, 17.16, 17.17, 17.18, 17.19, 17.20, 17.21, 17.22, 17.23, 17.24, 17.25, 18.01, 19.01, 20.01, 20.02, 20.03, 21.01, 22.01, 23.01, 24.01, 25.01, 25.02, 25.03, 25.04, 25.05, 26.01, 27.01, 28.01, 29.01, 30.01, 31.01, 32.01, 33.01, 34.01, 35.01, 36.01, 37.01, 38.01, 39.01, 40.01, 99.99]'. It must be a value from the enumeration.
cvc-type.3.1.3: The value '1.05' of element 'ItemListaServico' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18708792942231)SOLUÇÃO:**

Ative o parâmetro **"** **Usa formatação LC116 do cadastro da cidade? -  NFSEFORLC116CI"**

![Imagem 3: Ative o parâmetro " Usa formatação LC116 do cadastro da cidade? - NFSEFORLC116CI"](https://ajuda.sankhya.com.br/hc/article_attachments/18708784742679)

Na tela **Cidades** (Configurações » Cadastros » Endereços » Cidades) deixe as opções de "não formatar lC116" e "remover zero a esquerda" desabilitadas.

![Imagem 4: Na tela Cidades ( Configurações » Cadastros » Endereços » Cidades ) deixe as opções de "não formatar lC116" e "remover…](https://ajuda.sankhya.com.br/hc/article_attachments/18729520914839)

Em Brasília as informações devem ser nesse formato:

Para a tag <ItemListaServico>01.05</ItemListaServico>
para a tag <CodigoTributacaoMunicipio>105</CodigoTributacaoMunicipio>

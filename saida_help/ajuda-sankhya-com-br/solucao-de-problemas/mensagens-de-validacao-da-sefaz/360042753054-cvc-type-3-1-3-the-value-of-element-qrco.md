---
id: "360042753054"
titulo: "cvc-type.3.1.3: The value '' of element 'qrCodCTe' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042753054-cvc-type-3-1-3-The-value-of-element-qrCodCTe-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:24Z"
rotulos: ["#criadoRoger", "ERROCTE", "#revisadohugo", "CT-e", "Configuração", "XML", "SEFAZ", "Valor inválido qrCodCTe", "Ajustar parâmetros CT-e", "Atualizar modelo DACTE", "Documentos Eletrônicos"]
---

# cvc-type.3.1.3: The value '' of element 'qrCodCTe' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16088712355607) MENSAGEM:**

cvc-pattern-valid: Value '' is not facet-valid with respect to pattern '((HTTPS?|https?)://.\*\?chCTe=[0-9]{44}&tpAmb=[1,2](&sign=[!-y])?)' for type '#AnonType\_qrCodCTeinfCTeSuplTCTe'.
cvc-type.3.1.3: The value '' of element '**qrCodCTe**' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16088727033495) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Avançado » Preferências Parâmetro "DATINIULTNTCTE" : informe a UF e data da última NT Exemplo:…](https://ajuda.sankhya.com.br/hc/article_attachments/16088712363543) Acesse: Configurações » Avançado » Preferências
Parâmetro **"DATINIULTNTCTE"**: informe a UF e data da última NT
                                                     Exemplo: **MG:31/12/2019**

Parâmetro **"DATINICTEQRCOD":** informe a data início da implementação do QRcode em CT-e
                                                     Exemplo: **AN:07/10/2019**

![Imagem 4: Acesse: Comercial » Preferências » Empresa Aba: CT-e Opção "Versão NT CTE": última (Nota Técnica 3.00a)](https://ajuda.sankhya.com.br/hc/article_attachments/16088712366487) Acesse: Comercial » Preferências » Empresa
Aba: **CT-e**
Opção **"Versão NT CTE":** última (Nota Técnica 3.00a)

![Imagem 5: Acesse: Comercial » Arquivo » Cadastros » Modelo de Impressão (Nota/Pedido) Botão "Baixar Modelos Padrões", baixe o…](https://ajuda.sankhya.com.br/hc/article_attachments/16088712368663) Acesse: Comercial » Arquivo » Cadastros » Modelo de Impressão (Nota/Pedido)
Botão **"Baixar Modelos Padrões",** baixe o modelo DACTE atualizado para impressão do QRCode

![Imagem 6: Após os ajustes, efetue o lançamento do documento novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16088727045143) Após os ajustes, efetue o lançamento do documento novamente.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16088712376215) CAUSA:**

Ocorre quando a versão da NT não esta em conformidade com a data correta da obrigatoriedade da informação no XML da CT-e

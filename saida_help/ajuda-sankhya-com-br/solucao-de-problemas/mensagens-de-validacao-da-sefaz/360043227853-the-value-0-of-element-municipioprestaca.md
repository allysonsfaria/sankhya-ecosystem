---
id: "360043227853"
titulo: "The value '0' of element 'MunicipioPrestacao' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043227853-The-value-0-of-element-MunicipioPrestacao-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:22Z"
rotulos: ["#criadoRoger", "#revisadohugo", "Configuração", "Cidades", "Portal de Vendas", "NFS-e", "Valor '0' no Campo 'MunicipioPrestacao' Inválido", "Erro"]
---

# The value '0' of element 'MunicipioPrestacao' is not valid

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16087027615127) MENSAGEM**:

cvc-minInclusive-valid: Value '0' is not facet-valid with respect to minInclusive '1' for type 'tpCodCidade'.
cvc-type.3.1.3: The value '0' of element 'MunicipioPrestacao' is not valid.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16086998409495) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a NFS-e no Portal de Vendas, verifique se o campo "Cidade de Prestação do Serviço" está disponível para uso.…](https://ajuda.sankhya.com.br/hc/article_attachments/16086998411159) Acesse a NFS-e no Portal de Vendas, verifique se o campo **"Cidade de Prestação do Serviço"** está disponível para uso. Caso não esteja, considere liberar  através do [Configurador de Layout de Nota.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)

Preencha este campo com a informação desejada.

![Imagem 4: Preencha este campo com a informação desejada.](https://ajuda.sankhya.com.br/hc/article_attachments/14659269544343)

![Imagem 5: Salve o registro na nota e gere o Lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16086998416919) Salve o registro na nota e gere o Lote novamente.

**![Imagem 6: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16086998418711) CAUSA**:

Ocorre quando na emissão de uma NFS-e, o campo 'Cidade de Prestação do Serviço' não está devidamente preenchido.

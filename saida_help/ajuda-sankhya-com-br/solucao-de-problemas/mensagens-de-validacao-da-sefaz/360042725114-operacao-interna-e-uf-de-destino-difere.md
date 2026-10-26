---
id: "360042725114"
titulo: "Operação Interna e UF de destino difere da UF de origem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042725114-Opera%C3%A7%C3%A3o-Interna-e-UF-de-destino-difere-da-UF-de-origem"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:43Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "NF-e", "SEFAZ", "CFOP", "773", "Rejeição por UF de Destino Incorreta", "Erro"]
---

# Operação Interna e UF de destino difere da UF de origem

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16334575403543) MENSAGEM:**

[773 - Rejeição]: Operação Interna e UF de destino difere da UF de origem.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16334575404439) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Verifique o CFOP apresentado nos Itens:](https://ajuda.sankhya.com.br/hc/article_attachments/16334575407255) Verifique o CFOP apresentado nos Itens:

**(2)** CFOP'S iniciados com **1** e **5**: Emissões para **DENTRO** do Estado

**(2)** CFOP'S iniciados com **2** e **6**: Emissões para**FORA** do Estado

![Imagem 4: Verifique se o ENDEREÇO do parceiro condiz com a condição de CFOP acima.](https://ajuda.sankhya.com.br/hc/article_attachments/16334540538263) Verifique se o ENDEREÇO do parceiro condiz com a condição de CFOP acima.

(1)** Exemplo:**

**(2)**Se sua empresa está cadastrada com Endereço de MG e a nota está sendo emitida para um parceiro com Endereço/CNPJ de MT, utilize CFOP'S iniciadas com 1 e 5

**(2)** Se sua empresa está cadastrada com Endereço de MG e a nota está sendo emitida para um parceiro com Endereço/CNPJ de MG, utilize CFOP'S iniciadas com 2 e 6.

![Imagem 5: Caso o CFOP esteja correto e o endereço incorreto, realize os devidos ajustes no cadastro do parceiro.](https://ajuda.sankhya.com.br/hc/article_attachments/16334575415191) Caso o CFOP esteja correto e o endereço incorreto, realize os devidos ajustes no cadastro do parceiro.

![Imagem 6: Caso os endereços estejam corretos e o CFOP incorreto, verifique no cadastro do " Tipo de Operação" utilizado, aba "…](https://ajuda.sankhya.com.br/hc/article_attachments/16334575416855) Caso os endereços estejam corretos e o CFOP incorreto, verifique no cadastro do "**Tipo de Operação"** utilizado, aba "**Livros Fiscais",** a configuração atual de CFOP para Dentro/Fora do Estado, realizando os devidos ajustes conforme item 1.

![Imagem 7: Realizados os ajustes aconselha-se a inutilização/exclusão da NF-e rejeitada e um novo faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16334540543895) Realizados os ajustes aconselha-se a inutilização/exclusão da NF-e rejeitada e um novo faturamento.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16334575419799) CAUSA:**

Quando for emitida uma NF-e de Saída ou de Entrada de Operação Estadual, sendo essa Operação com Consumidor Normal  e a UF do Destinatário for diferente da UF do Emitente, será retornado a rejeição.

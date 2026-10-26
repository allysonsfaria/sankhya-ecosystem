---
id: "360042727474"
titulo: "Operação interestadual e UF de destino igual a UF de origem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042727474-Opera%C3%A7%C3%A3o-interestadual-e-UF-de-destino-igual-a-UF-de-origem"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:37Z"
rotulos: ["ERRONF", "#PUBLIFER", "Configuração", "Fiscal", "NF-e", "SEFAZ", "TOP", "CFOP", "772", "Rejeição por UF de Destinatário"]
---

# Operação interestadual e UF de destino igual a UF de origem

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16513139048087) MENSAGEM:**

[772 - Rejeição]: Operação Interestadual e UF de destino igual a UF de origem.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16513139056279) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Verifique qual o CFOP apresentado nos Itens:](https://ajuda.sankhya.com.br/hc/article_attachments/16513180369303) Verifique qual o CFOP apresentado nos Itens:

- CFOP'S iniciados com **1** e **5**: Emissões para **DENTRO** do Estado
- CFOP'S iniciados com **2** e **6**: Emissões para**FORA** do Estado

![Imagem 4: Verifique se o Endereço do parceiro condiz com a condição de CFOP acima.](https://ajuda.sankhya.com.br/hc/article_attachments/16513180371479) Verifique se o Endereço do parceiro condiz com a condição de CFOP acima.

(1)** Exemplo:**

- Se sua empresa está cadastrada com Endereço de MG e a nota está sendo emitida para um parceiro com Endereço/CNPJ de MG, não utilize CFOP'S iniciadas com 2 e 6.
- Se sua empresa está cadastrada com Endereço de MG e a nota está sendo emitida para um parceiro com Endereço/CNPJ de MT, não utilize CFOP'S iniciadas com 1 e 5.

![Imagem 5: Caso o CFOP esteja correto e o endereço incorreto, realize os devidos ajustes no cadastro do parceiro.](https://ajuda.sankhya.com.br/hc/article_attachments/16513180378647)Caso o CFOP esteja correto e o endereço incorreto, realize os devidos ajustes no cadastro do parceiro.

![Imagem 6: Caso os endereços estejam corretos e o CFOP incorreto, verifique no cadastro do " TIPO DE OPERAÇÃO " (Caminho de…](https://ajuda.sankhya.com.br/hc/article_attachments/16513139076247) Caso os endereços estejam corretos e o CFOP incorreto, verifique no cadastro do "**[TIPO DE OPERAÇÃO](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: Comercial » Arquivo » Cadastros/Financeiro » Arquivos » Cadastros) utilizado, aba "**Livros Fiscais"** a configuração atual de CFOP para Dentro/Fora do Estado, realizando os devidos ajustes conforme item 1.

![Imagem 7: Realizados os ajustes aconselha-se a inutilização/exclusão da NF-e rejeitada e um novo faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16513139078423) Realizados os ajustes aconselha-se a inutilização/exclusão da NF-e rejeitada e um novo faturamento.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16513180392599) CAUSA:**

Quando for emitida uma NF-e de Saída (tpNF = 1) ou de Entrada (tpNF = 0) para acobertar uma Operação Interestadual (idDest = 2), com a UF do Destinatário igual a UF do Emitente e o CNPJ do Destinatário diferente do CNPJ do Emitente, será retornado a rejeição.

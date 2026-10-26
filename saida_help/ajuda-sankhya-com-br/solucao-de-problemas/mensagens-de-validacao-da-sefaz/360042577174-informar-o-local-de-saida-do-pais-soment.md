---
id: "360042577174"
titulo: "Informar o local de saída do País somente no caso da exportação (NT2013/005)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042577174-Informar-o-local-de-sa%C3%ADda-do-Pa%C3%ADs-somente-no-caso-da-exporta%C3%A7%C3%A3o-NT2013-005"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:14Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "TOP", "356", "Rejeição [356] - Local de saída do País não informado", "Preencher \"Local do Embarque\" e \"UF Local Embarque\"", "Exportação com dados incorretos", "Exportacao"]
---

# Informar o local de saída do País somente no caso da exportação (NT2013/005)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16473835749783) MENSAGEM:**

[356 - Rejeição]: Informar o local de saída do País somente no caso da exportação(NT2013/005).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16473835751959) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a NF-e, verifique onde estão disponíveis os campos " Local do Embarque" ," UF Local Embarque" , geralmente os…](https://ajuda.sankhya.com.br/hc/article_attachments/16473835752599) Acesse a NF-e, verifique onde estão disponíveis os campos "**Local do Embarque"** ,"**UF Local Embarque"**, geralmente os campos estão dispostos na aba: "**Transporte"** do Rodapé da Nota.

![Imagem 4: Acesse a NF-e, verifique onde estão disponíveis os campos " Local do Embarque" ," UF Local Embarque" , geralmente os…](https://ajuda.sankhya.com.br/hc/article_attachments/14475123720855)

- Caso não esteja disponível para preenchimento, acesse com um usuário que tenha permissão a rotina: 'Comercial » Configuração » Configurador de Layout da Nota, verifique qual é o Layout Utilizado na nota e disponibilize os 2(dois) campos.

![Imagem 5: Após o procedimento, volte a acessar a NF-e novamente e faça o devido preenchimento do Local e UF do Embarque, salve o…](https://ajuda.sankhya.com.br/hc/article_attachments/16473835753367) Após o procedimento, volte a acessar a NF-e novamente e faça o devido preenchimento do Local e UF do Embarque, salve o cabeçalho da NF-e.

![Imagem 6: Gere um novo Lote ou busque autorização, conforme status NF-e atual.](https://ajuda.sankhya.com.br/hc/article_attachments/16473851380503) Gere um novo Lote ou busque autorização, conforme status NF-e atual.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16473835754775) CAUSA:**

Quando for emitida uma NF-e e o Grupo de Exportação for informado, mas o Tipo de Operação da NF-e for "0 - Entrada" e o Identificador de destino da operação for igual a "1 - Operação interna" ou "2 - Operação interestadual", será retornado a rejeição.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16473835756311) OBSERVAÇÃO:**

([NT2013/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=jLEf0c3bSBI=)) - Nota Técnica.

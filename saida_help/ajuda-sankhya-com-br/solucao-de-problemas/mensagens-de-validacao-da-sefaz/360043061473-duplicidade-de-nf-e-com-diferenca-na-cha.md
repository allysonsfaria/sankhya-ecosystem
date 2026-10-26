---
id: "360043061473"
titulo: "Duplicidade de NF-e, com diferença na Chave de Acesso(NT2011/004)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043061473-Duplicidade-de-NF-e-com-diferen%C3%A7a-na-Chave-de-Acesso-NT2011-004"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-25T13:25:23Z"
rotulos: ["ERRONF", "ERROMDFE", "Configuração", "NF-e", "SEFAZ", "TOP", "539", "Verificação e ajuste numeração", "Rejeição duplicidade NF-e", "Consulta chave acesso SEFAZ", "Erro", "Chave de Acesso"]
---

# Duplicidade de NF-e, com diferença na Chave de Acesso(NT2011/004)

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16482037951511) **MENSAGEM:**

[539 - Rejeição]: Duplicidade de NF-e, com diferença na Chave de Acesso(NT2011/004).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16481995207703) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Através da chave NF-e da respectiva nota rejeitada, faça a consulta no Portal Nacional e Estadual da SEFAZ:](https://ajuda.sankhya.com.br/hc/article_attachments/16481995214103) Através da chave NF-e da respectiva nota rejeitada, faça a consulta no Portal Nacional e Estadual da SEFAZ:

<http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=>

(1)** SE AUTORIZADA:**

![Imagem 4: Selecione a NF-e no respectivo Portal » Botão NF-e » " Consulta situação atual da nota". Clique em SIM para atualizar o…](https://ajuda.sankhya.com.br/hc/article_attachments/16481995221783) Selecione a NF-e no respectivo Portal » Botão NF-e » "**Consulta situação atual da nota".** Clique em SIM para atualizar o STATUS no sistema.

(1)** SE INEXISTENTE:**

![Imagem 5: Caso a consulta de chave retorne a informação de Inexistente, a seguinte possibilidade deve ser analisada:](https://ajuda.sankhya.com.br/hc/article_attachments/16482037965079) Caso a consulta de chave retorne a informação de Inexistente, a seguinte possibilidade deve ser analisada:

Quando já existe uma NF-e na SEFAZ com esse mesmo Número Nota, Série , Modelo, CNPJ Emitente:

**3.1** Em alguns casos, a SEFAZ retorna ao final da rejeição um conteúdo [  ] com as informações da chave duplicada.

- Se for o seu caso, consulte essa chave no link mencionado no Item 1, para compreender a duplicidade.

**3.2** Caso a SEFAZ não tenha retornado essa informação, avalie se a numeração gerada estáde acordo com a sua sequência atual com um usuário certificado, com conhecimento no processo, seguindo as orientações abaixo:

- Verifique o controle de Numeração da TOP: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP.
- Acesse: **"Outras Opções**" » "**Controle de Numeração"**.
- Identifique a linha correspondente a Empresa, Série, Modelo de Doc. Fiscal.
- Verifique o campo "**Último Código"**.
- Este campo registra o último número de NF-e gerada.

Caso seja uma TOP nova, que utiliza a base de Numeração = 'Venda', identifique o último número da nota gerada, de acordo com a Empresa e Série, e insira no campo 'Último Código'.

![Imagem 6: Após os ajustes, realize um novo faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16482037967511) Após os ajustes, realize um novo faturamento.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16481995234327) CAUSA:**

Quando for emitida uma NF-e e na Sefaz já existir outra NF-e, já autorizada, com o mesmo CNPJ Emitente, Modelo, Série e Número, mas com Data de Emissão, Tipo de Emissão ou Código Numérico ou outras posições da Chave de Acesso diferentes, será retornada a rejeição "Duplicidade de NF-e, com diferença na Chave de Acesso".

Esta Rejeição ocorre quando uma NF-e emitida, já constar outra NF-e AUTORIZADA, com o mesmo Emitente, CNPJ, Modelo, Número/Série, mas com Data de Emissão, Tipo de Emissão e Código Aleatório diferente da Chave de Acesso.

(1)** SITUAÇÕES DA CAUSA:**

- 1.1- Ao realizar a Transmissão de uma NF-e, no ambiente NORMAL, caso ocorra alguma instabilidade na comunicação do retorno, indicando que a NF-e foi recebida ou processada, essa situação não é retornada.
- 1.2- Quando a NF-e é transmitida para a SEFAZ e antes que a SEFAZ devolva o retorno da transmissão, uma nova transmissão é efetuada, gerando apenas uma diferença entre o Código Numérico.
- 1.3- Quando uma NF-e foi transmitida a tempos atrás com uma Numeração XXXX e Série 1, por exemplo.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16481995236887) OBSERVAÇÃO:**

(**NT2011/004**) Nota Técnica:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ysYXxjwjYyk=>

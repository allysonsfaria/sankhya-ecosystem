---
id: "360043020633"
titulo: "Duplicidade de NF-e [nRec:'XXXXXXXXXXX']"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043020633-Duplicidade-de-NF-e-nRec-XXXXXXXXXXX"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:10:04Z"
rotulos: ["ERRONF", "ERROMDFE", "Configuração", "Fiscal", "NF-e", "SEFAZ", "204", "Duplicidade detectada", "Consulte SEFAZ e atualize status", "Chave de acesso duplicada", "Erro", "Documentos Eletrônicos"]
---

# Duplicidade de NF-e [nRec:'XXXXXXXXXXX']

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16457460845847) MENSAGEM:**

[204 - Rejeição]: Duplicidade de NF-e [nRec:'XXXXXXXXXXX'].

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457411883671) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Através da chave NF-e da respectiva nota rejeitada, faça a consulta no Portal Nacional e Estadual da SEFAZ:](https://ajuda.sankhya.com.br/hc/article_attachments/16457460858519) Através da chave NF-e da respectiva nota rejeitada, faça a consulta no Portal Nacional e Estadual da SEFAZ:

<http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=>

(1)** SE AUTORIZADA:**

![Imagem 4: Selecione a NF-e na tela "Portal de vendas " (Caminho de acesso: Comercial » Consulta » Portal de Vendas)](https://ajuda.sankhya.com.br/hc/article_attachments/16457411892887) Selecione a NF-e na tela [**"Portal de vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)" (Caminho de acesso: Comercial » Consulta » Portal de Vendas)

- Botão "**NF-e"** : "**Consulta situação atual da nota".** Clique em SIM para atualizar o STATUS no sistema.

![Imagem 5: Botão " NF-e" : " Consulta situação atual da nota". Clique em SIM para atualizar o STATUS no sistema.](https://ajuda.sankhya.com.br/hc/article_attachments/14447640283671)

(1)** SE INEXISTENTE:**

![Imagem 6: Caso a consulta de chave retorne a informação de Inexistente, a seguinte possibilidade deve ser analisada:](https://ajuda.sankhya.com.br/hc/article_attachments/16457411896855) Caso a consulta de chave retorne a informação de Inexistente, a seguinte possibilidade deve ser analisada:

Quando já existe uma NF-e na SEFAZ com esse mesmo Número Nota, Série ,Modelo, CNPJ Emitente:

      3.1 Na rejeição retornada pela SEFAZ, constará o número de recebimento do documento que está causando a rejeição. Nesse caso, será necessário que o Contador da empresa contacte a SEFAZ com essa informação, para compreender qual é essa nota e a partir dessa informação seguir com as próximas análises.

      3.2 Necessário avaliar se a numeração gerada está de acordo com a sua sequência atual com um usuário certificado, com conhecimento no processo, seguindo as orientações abaixo:

- Acesse a tela : "[**Tipos de Operação"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) verifique o controle de Numeração da TOP:
- Acesse: "**Outras Opções"**- "**Controle de Numeração**".
- Identifique a linha correspondente à Empresa, Série, Modelo de Doc. Fiscal.
- Verifique o campo "**Último Código"**. Este campo registra o último número de NF-e gerada.
- Caso seja uma TOP nova, que utiliza a base de Numeração = 'Venda', identifique o último número da nota gerada de acordo com a Empresa e Série e insira no campo "**Último Código"**
- Após os ajustes, exclua a NF-e atual e lance/fature uma nova Nota.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16457460874007) CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65), com a mesma Chave de Acesso de uma NF-e já autorizada pela Sefaz, será retornado a rejeição.

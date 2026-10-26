---
id: "360042575834"
titulo: "Unidade Tributável incompatível com o NCM informado na operação com Comércio Exterior [nItem:nnn](NT2016/001)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042575834-Unidade-Tribut%C3%A1vel-incompat%C3%ADvel-com-o-NCM-informado-na-opera%C3%A7%C3%A3o-com-Com%C3%A9rcio-Exterior-nItem-nnn-NT2016-001"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-23T18:02:37Z"
rotulos: ["ERRONF", "Produtos", "Configuração", "NF-e", "XML", "SEFAZ", "CFOP", "817", "Unidade Tributável Incompatível com NCM", "Artigo atualizado KCS", "Docs Eletrônicos - KCS", "Comércio Exterior"]
---

# Unidade Tributável incompatível com o NCM informado na operação com Comércio Exterior [nItem:nnn](NT2016/001)

**MENSAGEM:**

[![Imagem 1: ( ) Rejeição: Unidade Tributável incompatível com o NCM informado na operação com Comércio Exterior (nItem:999)](https://chat.google.com/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=ABLWXTe9aJ4BS2tw%2BzceuvoNC5Wx4nMPNMGDbNlC6otBkkKxpUXyKtgAqLPoWSA%2BO8wk6PW6CPY4MVEwe3xcS5oqXJJutj0AsYNe2mki%2Fa67cYzkI2i%2FKF92hV9jTwqxRaOI5AJtPA3z4UFwEhSTVXRCSiKG1RxJIagkdasNqzWqgwwgj1OOEm8kuUsVI6Iox4iXEkm0WocdLyXgX8H%2Fgzqb%2Fwkmxag%2B3h%2Bg5t7FKcIVMSNIeHLuShIy0glqt408zjYjMhcX6cBc4RQY7AsQEPK2rRv5vwM%2Bgt0qkMQgwPI880cmhD%2FK6XREYFRvAH4UbA5S67dtmXWBcLOHcanJhTObw7d0WRxLYq0uLVUfxwkGi2X9N8KgST5UGf9arZqC20oxvHbxw%2FP06o95kQA2LvrJn2%2BE4BR5nXHbsJPX%2FkdL7usKa8w5ReD4jz4t%2F0N9H1YeZrUvmzLlUPV20ctQtd7Y7UZOerwHwbLA6hDg0zw9Nggb7uZHy2tednU1HO2qQIAzP4nuTRV9YF0Kid2dmIWMBCNHgq58nPEXHywLr75kaBOHfdUER6bzDfuu4vL4qjc1EfoTUDNgLju6DMyeeiVsa8cghhOxDegIkl2pE3Nq%2FLhZGquidlCIv6Cd4MUY3m4a&allow_caching=true)] Rejeição: Unidade Tributável incompatível com o NCM informado na operação com Comércio Exterior [nItem:999]

**SOLUÇÃO:**

Para correção, siga os passos abaixo:

Identifique o item: Caso a NF-e possua múltiplos itens, utilize a tela **"Portal de Vendas"** (Comercial >> Consulta), selecione a nota, clique em **"NF-e"** >> **"Gerar XML da NF-e em arquivo para Conferência"**. Abra o XML em um editor de texto e utilize a busca (Ctrl+F) pelo termo 'nItem' para localizar o item apontado na rejeição.

Considere o comportamento da aplicação conforme abaixo:

**SITUAÇÃO¹:**

Quando trabalhar com a **"Unidade"** apenas com dois caracteres, exemplo: UN, KG, MT.

**Exemplo:** Foi emitida uma NF-e de exportação, com a Unidade Tributável igual a UN e NCM igual a 44170010. De acordo com a **"Tabela NCM e Unidades de Medidas Tributáveis no Comércio Exterior"**, divulgada pela SEFAZ, para o NCM 44170010, a tag <uTrib> deve ser igual a unidade KG.

- Configurações (Configurações >> Cadastros >> Produtos >> Produtos)
- Aba: **"Unidade Alternativa"**

Cadastre uma **"Unidade Alternativa"** em KG. A marcação **"Unidade de Tributação"** deve estar selecionada, marcado a opção Ativo, para que seja gerado dentro do XML <uTrib> e <qTrib>.
![Imagem 2: Cadastre uma "Unidade Alternativa" em KG. A marcação "Unidade de Tributação" deve estar selecionada, marcado a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/43709219530903)

Verifique se o campo **"Descrição Un. Tributação Exportação"** está visível. Caso não esteja, clique no **"ícone de engrenagem"** e configure para que o campo apareça na tela.

Preencha o campo **"Descrição Un. Tributação Exportação"** com a mesma unidade tributável configurada. Observação: Quando o CFOP for algum dos que estão destacados em parênteses (5501, 5502, 5504, 5505, 6501, 6502, 6504, 6505, 7101, 7102, 7127, 7949) considere utilizar este campo, pois ele sobrepõe a configuração anterior.

![Imagem 3: Preencha o campo "Descrição Un. Tributação Exportação" com a mesma unidade tributável configurada. Observação: Quando o…](https://ajuda.sankhya.com.br/hc/article_attachments/35593139604503)

Considere a marcação **"Un. Tributação Exportação em Toneladas"**. Na geração do XML, a marcação do campo fará com que a tag <uTrib> seja enviada com o valor TON, quando o CFOP for algum dos que estão destacados em parênteses (5501, 5502, 5504, 5505, 6501, 6502, 6504, 6505, 7101, 7102, 7127, 7949).

**SITUAÇÃO²:**

Quando trabalhar com a unidade com mais de dois caracteres, exemplo: PARES, TON, DUZIA.

**Exemplo:** Foi emitida uma NF-e de exportação, com a Unidade Tributável igual a UN e NCM igual a 52010010. De acordo com a **"Tabela NCM e Unidades de Medidas Tributáveis no Comércio Exterior"**, divulgada pela SEFAZ, para o NCM 52010010, a tag <uTrib> deve ser igual a unidade TON.

Atualmente, o cadastro de volumes permite apenas dois caracteres para a sigla. Para que seja possível a criação de uma unidade com mais de dois caracteres, realize as alterações:

- Configurações (Configurações >> Avançado >> Preferências) - Parâmetro **"USACODVOLPARC"**: Habilitado.
- Configurações (Configurações >> Cadastros >> Produtos >> Unidades) - Será criada a aba **"Unidade Fiscal por Parceiro"**, desta forma, realize o cadastro.

![Imagem 4: Configurações (Configurações >> Cadastros >> Produtos >> Unidades) - Será criada a aba "Unidade Fiscal por Parceiro" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/14507078545687)

- A unidade criada deve estar vinculada à **"Unidade Alternativa"** do produto. A marcação **"Unidade de Tributação"** deve estar feita. Ao realizar a emissão da nota, quando informado no item a unidade T, dentro do XML será gerado TON.

Após ajustes, salve o cadastro do produto, exclua a NF-e rejeitada e emita novamente. Verifique no XML de conferência se a unidade (uTrib) está correta. Lembre de inutilizar a numeração da NF-e que for ser excluído.

**CAUSA:**

A rejeição ocorre porque o sistema não estava considerando apenas a marcação da **"Unidade Tributação"** no cadastro do produto. Para operações de comércio exterior (especialmente exportações), é obrigatório preencher o campo **"Descrição Un. Tributação Exportação"** com a unidade compatível com o NCM, conforme a tabela oficial da SEFAZ. Quando há divergência entre a unidade informada no XML e a unidade aceita para aquele NCM, ocorre a rejeição 817.

**OBSERVAÇÃO:**

Parâmetros:

**"USARUNIDPADNFE"**: Quando ligado, o sistema sempre imprimirá no DANFE os produtos na **"Unidade Padrão"**, independente da nota estar ou não na **"Unidade Alternativa"**.

Ao habilitar o parâmetro **"USACODVOLPARC"**, o sistema deverá ser reiniciado para a criação da aba **"Unidade Fiscal por Parceiro"** no cadastro de **"Unidades"** (Configurações >> Cadastros >> Produtos >> Unidades).

---
id: "42427465974679"
titulo: "Como conectar uma exportação do Power BI Desktop ao Power BI Online usando a Power BI Key?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427465974679-Como-conectar-uma-exporta%C3%A7%C3%A3o-do-Power-BI-Desktop-ao-Power-BI-Online-usando-a-Power-BI-Key"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-11T16:14:55Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14474117", "sync_hash_8185abff6233"]
---

# Como conectar uma exportação do Power BI Desktop ao Power BI Online usando a Power BI Key?

A integração com o Power BI permite exportar dados do Ploomes por meio de um link que pode ser atualizado automaticamente conforme a configuração realizada na plataforma.

Além de utilizar esse link diretamente no Power BI Desktop, também é possível publicar o dashboard no Power BI Online para manter as atualizações automáticas na nuvem.

Neste artigo, você verá como configurar a exportação utilizando a Power BI Key.

⚠️ **Atenção:** este artigo é destinado apenas para cenários que utilizam a autenticação via Power BI Key.
Caso sua exportação não utilize essa chave de segurança, não é necessário realizar os passos descritos abaixo.

## Pré-requisitos

Antes de iniciar a configuração no Power BI Online, é necessário:

- já ter gerado a exportação no Ploomes;
- ter conectado a exportação no Power BI Desktop.

Siga primeiro o artigo: [Integração com Power BI](https://sankhya.zendesk.com/hc/pt-br/articles/42427413992983).

## Como conectar

## 1. Ajustar o código no Editor Avançado do Power BI

No Power BI Desktop, acesse o **Editor Avançado** e ajuste o código da consulta para utilizar o método `Web.Contents` com `RelativePath`.

Essa configuração é necessária para permitir a atualização automática no Power BI Online.

### Exemplo de link exportado

```
https://pbi.ploomes.com/powerbi/callback/eb63d20fe2a94b2?code=eddTWbLXzRxcfNlhFnE81GNz5Rf2orOz/ZeyXu+uiuP5NSjAQ==
```

### Estrutura do link

| **Parte** | **Exemplo** |
| --- | --- |
| Início do link | [`https://pbi.ploomes.com`](https://pbi.ploomes.com) |
| Código de exportação | `powerbi/callback/eb63d20fe2a94b2` |
| Referência da exportação | `eddTWbLXzRxcfNlhFnE81GNz5Rf2orOz/ZeyXu+uiuP5NSjAQ==` |

## 2. Substituir caracteres codificados da URL

A referência da exportação pode conter caracteres codificados em HTML (URL Encode).
Antes de utilizar no código, substitua os valores decodificados, conforme o exemplo abaixo:

| Codificação | Substituir por |
| --- | --- |
| `%2F` | `/` |
| `%3D` | `=` |
| `%2B` | `+` |

[GIF animado: Imagem 1: +](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2246533289/71240a8bd38e4a496deba5579286/anima%C3%A7%C3%A3o162.gif?expires=1786536000&signature=403eb68d5718323b74599a80de5bb9439b3a6cd6ed539d371fefa2d0d83bc3d7&req=diIjEMx9noNXUPMW3nq%2Bgc6SCqMAO%2BuhZ8WBC75Zmqa%2B2%2B%2FaL90XY%2BC2GG%2BI%0AygpmKJh7TbbHKp2bN5qHkoQh42I%3D%0A)

## 3. Inserir o código da consulta

Após separar as informações do link, utilize uma estrutura semelhante ao exemplo abaixo:

```
let
    Fonte =
        Json.Document(
            Web.Contents(
                "https://pbi.ploomes.com",
                [
                    RelativePath = "Código de exportação",
                    Query = [
                        code = "Referência da exportação"
                    ],
                    Headers = [
                        PowerBiKey = "Chave de segurança da sua exportação"
                    ]
                ]
            )
        )
in
    Fonte
```

⚠️ **Atenção:** o código acima é apenas um exemplo de implementação.
Caso seja necessário alterar colunas, campos ou estruturas da consulta, o código deverá ser adaptado conforme sua necessidade.

## 4. Publicar o dashboard no Power BI Online

Após salvar as alterações no Power BI Desktop:

1. publique o dashboard no Power BI Online;
2. acesse o workspace onde o dashboard foi publicado.

![Imagem 2: acesse o workspace onde o dashboard foi publicado.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2246393769/adf58c497668d0603562fcc6d58a/image.png?expires=1786536000&signature=aeda342429ec83b43d30d96b0c95e091956ff2e5ac8c4322121332dded55bac0&req=diIjEMp3noZZUPMW3nq%2BgQKy5J8DwOOxj6qwVgPImdho9xWe2p7fuaFFBKcB%0AKcUHvqbrOf1YBAORCRiL5nmnRXY%3D%0A)

## 5. Configurar a atualização automática

No Power BI Online:

1. acesse as configurações do dataset;
2. edite as credenciais da fonte de dados;
3. marque a opção **"Ignorar conexão de teste"**;
4. configure a frequência de atualização conforme sua necessidade.

[GIF animado: Imagem 3: configure a frequência de atualização conforme sua necessidade.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2246414389/6ce46755ab78e784d9be9672746c/anima%C3%A7%C3%A3o161.gif?expires=1786536000&signature=cb09a722674e8a72b2e2f2337d1d68a207e40564d3b5e0547cd7397608d3b586&req=diIjEM1%2FmYJXUPMW3nq%2BgR2vMnLVr04j1gY1wGvMxBuKHsw3OrSuXRDBNh5M%0AFWXRo%2BfCXHWejeNnwzCAyyLrANE%3D%0A)

## Pronto!

Após concluir as configurações, o dashboard ficará disponível no Power BI Online e os dados serão atualizados automaticamente conforme as configurações realizadas no Ploomes e no Power BI.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).

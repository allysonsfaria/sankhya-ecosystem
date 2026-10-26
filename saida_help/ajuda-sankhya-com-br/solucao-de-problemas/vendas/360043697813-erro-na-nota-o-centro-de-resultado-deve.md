---
id: "360043697813"
titulo: "Erro na nota. O Centro de Resultado deve ser informado. O parâmetro 'EXIGCRCFR' está ligado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697813-Erro-na-nota-O-Centro-de-Resultado-deve-ser-informado-O-par%C3%A2metro-EXIGCRCFR-est%C3%A1-ligado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:43Z"
rotulos: ["CORE_E00901", "CORE_E02406", "Configuração", "Centro de Resultado", "Nota Fiscal", "Preferências", "Financeiro", "Centro de Resultado obrigatório", "Parâmetro EXIGCRCFR ativado", "Preencher nas telas específicas"]
---

# Erro na nota. O Centro de Resultado deve ser informado. O parâmetro 'EXIGCRCFR' está ligado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16164217168407) MENSAGEM:**

[CORE\_E02406] Erro na nota. O Centro de Resultado deve ser informado. O parâmetro 'EXIGCRCFR' está ligado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16164255425047) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Quando o parâmetro "EXIGCRCFR" estiver ligado, o sistema exigirá que o usuário indique o "Centro de Resultado" nas…](https://ajuda.sankhya.com.br/hc/article_attachments/16164217173015) Quando o parâmetro **"EXIGCRCFR"** estiver ligado, o sistema exigirá que o usuário indique o **"Centro de Resultado"** nas seguintes telas:

**(2)** Movimentos lançados nas Centrais (Compra/Venda/Mov.Interna);

**(2)** Tela Rateio de Receitas e Despesas;

**(2)** Financeiros das centrais;

**(2)** Movimentação financeira;

**(2)** Modelo de Notas e Pedidos;

![Imagem 4: (2) Modelo de Notas e Pedidos;](https://ajuda.sankhya.com.br/hc/article_attachments/14712097445911)

![Imagem 5: Dessa forma, para que a mensagem deixe de ser apresentada, o campo "Centro de Resultado" deve ser devidamente…](https://ajuda.sankhya.com.br/hc/article_attachments/16164255437335) Dessa forma, para que a mensagem deixe de ser apresentada, o campo **"Centro de Resultado"** deve ser devidamente preenchido nas respectivas telas, conforme processo realizado no momento da apresentação da mensagem.

![Imagem 6: Caso seja identificada a necessidade de não mais trabalhar com a exigência dessa informação 'Centro de Resultado', o…](https://ajuda.sankhya.com.br/hc/article_attachments/16164217180695) Caso seja identificada a necessidade de não mais trabalhar com a exigência dessa informação 'Centro de Resultado', o parâmetro deverá ser **desligado** através da tela **"Preferências"** (Configurações » Avançado) - chave **"EXIGCRCFR"**:

**![Imagem 7: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16164217187735) OBSERVAÇÕES:**

**(1)** Se a rejeição ocorre no momento de utilizar a rotina **"[Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)"**, verifique na tela **"Empresa"** (Comercial » Preferências), aba **"Modelo de Importação de XML"**, os modelos vinculados.

Após isso, acesse a tela **"[Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)"** (Caminho de acesso: Comercial » Consulta), localize os respectivos modelos e valide a configuração do campo 'Centro de Resultado', para solução da mensagem apresentada.

**(1)** Se a rejeição ocorre no momento de utilizar a rotina **"[Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117633-Ajuste-de-Estoque-)"**, verifique na tela **"Empresa"** (Caminho de acesso: Comercial » Preferências), aba **"Estoque/Preço"**, os modelos de ajuste de entrada e ajuste de saída vinculados.

Após isso, acesse a tela **"[Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)"** (Caminho de acesso: Comercial » Consulta), localize os respectivos modelos e valide a configuração do campo **"Centro de Resultado"**, para solução da mensagem apresentada.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16164217194903) CAUSA:**

Ao realizar lançamentos financeiros e/ou nas Centrais, caso o campo Centro de Resultado não seja informado e o parâmetro EXIGCRCFR esteja ligado, será apresentada a mensagem.

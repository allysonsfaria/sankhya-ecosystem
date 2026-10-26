---
id: "360043359273"
titulo: "A natureza deve ser informada. O parâmetro 'EXIGNATCFR' está ligado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043359273-A-natureza-deve-ser-informada-O-par%C3%A2metro-EXIGNATCFR-est%C3%A1-ligado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-25T11:58:18Z"
rotulos: ["#criadoRoger", "CORE_E00899", "Configuração", "Movimentação Financeira", "XML", "Preferências", "Natureza", "CORE_E02405", "CORE_E03356", "Natureza obrigatória", "Parâmetro ativado", "Preencher natureza", "Erro"]
---

# A natureza deve ser informada. O parâmetro 'EXIGNATCFR' está ligado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16112893527447) MENSAGEM:**

[CORE\_E00899] A natureza deve ser informada. O parâmetro 'EXIGNATCFR' está ligado.

[CORE\_E02405] A natureza deve ser informada. O parâmetro 'EXIGNATCFR' está ligado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16112893530135) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Quando o parâmetro "EXIGNATCFR" estiver ligado, o sistema exigirá que o usuário indique a natureza nas seguintes telas:](https://ajuda.sankhya.com.br/hc/article_attachments/16112924862615) Quando o parâmetro **"EXIGNATCFR"** estiver ligado, o sistema exigirá que o usuário indique a natureza nas seguintes telas:

**(2)** Movimentos lançados nas Centrais (Compra/Venda/Mov. Interna);

**(2)** Tela **"[Rateio de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas)"**;

**(2)** Financeiros das centrais;

**(2)** Movimentação financeira;

**(2)** Modelo de Notas e Pedidos;

![Imagem 4: (2) Modelo de Notas e Pedidos;](https://ajuda.sankhya.com.br/hc/article_attachments/14549791761815)

![Imagem 5: Dessa forma, para que a mensagem deixe de ser apresentada, preencha devidamente o campo "NATUREZA" na respectiva tela.](https://ajuda.sankhya.com.br/hc/article_attachments/16112893540119) Dessa forma, para que a mensagem deixe de ser apresentada, preencha devidamente o campo **"NATUREZA"** na respectiva tela.

![Imagem 6: Caso seja identificado a necessidade de não mais trabalhar com a exigência dessa informação natureza, o parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/16112886257815) Caso seja identificado a necessidade de não mais trabalhar com a exigência dessa informação natureza, o parâmetro deverá ser desligado através da tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)"** (Configurações » Avançado) - chave EXIGNATCFR:

**![Imagem 7: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16112897221783) OBSERVAÇÕES:**

**(1)** Se a rejeição ocorre no momento de utilizar a rotina **"[Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)"**, verifique na tela **"[Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas)"** (Caminho de acesso: Comercial » Preferências), aba **"Modelo de Importação de XML",** os modelos vinculados.

Após isso, acesse a tela **"[Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos)"** (Comercial » Consulta), localize os respectivos modelos e valide a configuração do campo **"Natureza"**, para solução da mensagem apresentada.

**(1)** Se a rejeição ocorre no momento de utilizar a rotina **"[Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117633-Ajuste-de-Estoque-)"**, verifique na tela Empresa, aba **"Estoque/Preço"**, os modelos de ajuste de entrada e ajuste de saída vinculados.

Após isso, acesse a tela Modelo de Notas e Pedidos, localize os respectivos modelos e valide a configuração do campo Natureza, para solução da mensagem apresentada.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16112909982871) CAUSA:**

Ao realizar lançamentos financeiros e/ou nas Centrais, caso o campo natureza não seja informado e o parâmetro EXIGNATCFR esteja ligado, será apresentada a mensagem.

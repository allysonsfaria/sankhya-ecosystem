---
id: "36404424430103"
titulo: "Variação do tamanho da fonte entre o Sankhya-W e a TV Corporativa. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36404424430103-Varia%C3%A7%C3%A3o-do-tamanho-da-fonte-entre-o-Sankhya-W-e-a-TV-Corporativa-Como-resolver"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:23:03Z"
rotulos: ["Configuração", "Relatórios", "Sankhya-W TV Corporativa", "TV Corporativa Sankhya", "XML", "Sankhya-W", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Componente de BI", "TV Corporativa"]
---

# Variação do tamanho da fonte entre o Sankhya-W e a TV Corporativa. Como resolver?

**SITUAÇÃO:**

Ao acessar o dashboard na **TV Corporativa**, o conteúdo aparece com a **fonte muito grande**, ficando **diferente da visualização quando o dashboard é exibido no Sankhya-W**.

![Imagem 1: Ao acessar o dashboard na TV Corporativa , o conteúdo aparece com a fonte muito grande , ficando diferente da…](https://ajuda.sankhya.com.br/hc/article_attachments/36404629675159)

**SOLUÇÃO:**

**(1)** Acesse o [**''Construtor de Componente de BI''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI) (Configurações **»** Avançado **»** Construtor de Componentes de BI) e edite o componente utilizado no dashboard.

**(2)** Em seguida, **desmarque** a opção **''Utilizar a Nova Versão da Grade''**.

**(3)** No campo **''Tamanho do texto''**, altere para qualquer tamanho, desde que não seja para o **''Normal''**.

**(4)** Salve a configuração e retorne ao componente.

**(5)** Marque novamente a opção **''Utilizar a Nova Versão da Grade''** e ajuste o tamanho do texto para **''Normal''**.

**(6)** Salve a configuração mais uma vez para que o XML seja regravado com os parâmetros corretos:

`useNewGrid="S" tamTexto="12"`

**(7)** Por fim, acesse a TV Corporativa e teste o dashboard para confirmar que o tamanho da fonte foi normalizado.

![Imagem 2: (7) Por fim, acesse a TV Corporativa e teste o dashboard para confirmar que o tamanho da fonte foi normalizado.](https://ajuda.sankhya.com.br/hc/article_attachments/36404613331351)

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/36404410937879)CAUSA:**

A diferença ocorre porque o Sankhya-W e a TV Corporativa utilizam **escalas distintas para exibir os componentes** de BI.

No Sankhya-W, o tamanho de fonte padrão é **12**, enquanto na TV Corporativa é **30**.

Essa diferença de escala faz com que o dashboard seja exibido visualmente maior na TV quando comparado ao Sankhya-W.

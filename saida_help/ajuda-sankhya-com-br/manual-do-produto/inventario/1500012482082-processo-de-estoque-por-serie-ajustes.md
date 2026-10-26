---
id: "1500012482082"
titulo: "Processo de estoque por série - Ajustes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012482082-Processo-de-estoque-por-s%C3%A9rie-Ajustes"
trilha: "Manual do Produto > Suprimentos e Estoque > Inventário"
atualizado_em: "2026-07-29T14:48:35Z"
rotulos: ["Produtos", "Configuração", "br.com.sankhya.mgeinv.ajusteestoqueporserie", "TOP", "Estoque", "NOTAENTAJUSTEST", "NOTASAIAJUSTEST", "Ajuste: Informar dados e gerar notas", "Divergências: Notas faltantes erros e roubo", "Configuração: Modelos e tipos de nota", "ERP"]
---

# Processo de estoque por série - Ajustes

Após a cópia e a contagem do estoque por série, alguns produtos podem apresentar divergências, sendo necessário ajustar o estoque no sistema. Dependendo do volume, tem-se a necessidade de uma sindicância a fim de descobrir as causas das diferenças, que podem ser:

- Notas sem registro no sistema;
- Algum local sem contagem;
- Erro de digitação;
- Erro de anotação;
- Erro na inadimplência de produto;
- Roubo;

Assim, nesse artigo trataremos da última etapa do processo de estoque por série, ou seja, o ajuste de estoque por série.

| ``` Etapas do processo de estoque por série ``` |
| --- |

| [![Imagem 1: Etapas do processo de estoque por série](https://ajuda.sankhya.com.br/hc/article_attachments/42312628073751)](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500011948362-Processo-de-estoque-por-serie-) | ![Imagem 2: Etapas do processo de estoque por série](https://ajuda.sankhya.com.br/hc/article_attachments/42312628076311) | [![Imagem 3: Etapas do processo de estoque por série](https://ajuda.sankhya.com.br/hc/article_attachments/42312628076695)](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500012454222) | ![Imagem 4: Etapas do processo de estoque por série](https://ajuda.sankhya.com.br/hc/article_attachments/42312628076311) | [GIF animado: Imagem 5: Etapas do processo de estoque por série](https://ajuda.sankhya.com.br/hc/article_attachments/42312594766103) |
| --- | --- | --- | --- | --- |

| ``` Dica: Clique sobre as etapas do fluxograma e saiba mais sobre cada uma delas. ``` |
| --- |

Antes de efetuar o Ajuste de Estoque por Série, é necessário que você realize as seguintes configurações:

**1°)** Por meio da tela [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos), configure as Empresas com os modelos das notas, e informe o **"Tipo Operação"**que será utilizado na geração da nota.

**Observação:** Para que o status vá corretamente para o Histórico da Série, o [Tipo de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) informado para o ajuste, deve estar configurado com a opção **"de Ajuste"**, campo **"Tipo de Emissão"**, da aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce).

**2°)** Feito isso, acesse a tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abaestoquepreo) e indique os modelos de nota de entrada e saída através dos campos, **"Modelo Ajuste de Entrada de Estoque"** e **"Modelo Ajuste de Saída de Estoque"**.

**3°)** Você também pode configurar os modelos, por meio dos parâmetros **"Nota Modelo Ajuste Estoque (Entrada) - NOTAENTAJUSTEST"** e **"Nota Modelo Ajuste Estoque (Saída) - NOTASAIAJUSTEST"**.

Com as configurações acima efetuadas, podemos realizar o ajuste de estoque por série. Assim, acesse a tela [Ajuste de Estoque Por Série](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117673-Ajuste-de-Estoque-por-S%C3%A9rie) e informe a **"Empresa"** que será feito o ajuste. Defina também, o **"Preço Unitário"** a ser utilizado nas notas de ajuste, conforme as seguintes opções:

- Usar o preço informado na TOP;
- Preço de Venda;
- Último Custo de Reposição;
- Último Custo Variável;
- Último Custo Gerencial;
- Último Custo de Entrada Com ICMS;
- Último Custo de Entrada Sem ICMS;
- Último Custo Médio Gerencial;
- Último Custo Médio Com ICMS;
- Último Custo Médio Sem ICMS.

Em seguida, na seção **"Datas"** indique no campo **"Cópia"** a data da Cópia do Estoque, e no campo **"Contagem"**, a data da Contagem do Estoque. Você pode visualizar as datas que foram realizadas as cópias/contagens por meio da lupa ![Imagem 6: Em seguida, na seção "Datas" indique no campo "Cópia" a data da Cópia do Estoque , e no campo "Contagem" , a data da…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019728302).

[GIF animado: Imagem 7: Em seguida, na seção "Datas" indique no campo "Cópia" a data da Cópia do Estoque , e no campo "Contagem" , a data da…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019878542)

| ``` ![Imagem 8: Se não houver Cópia ou Contagem nas datas informadas, o sistema exibirá um aviso solicitando que os filtros sejam…](https://ajuda.sankhya.com.br/hc/article_attachments/42312594766743)Se não houver Cópia ou Contagem nas datas informadas, o sistema exibirá um aviso          solicitando que os filtros sejam verificados. ``` |
| --- |

---

**Regras do processo**

Antes de selecionarmos o botão **"Ajustar"**, devemos nos atentar para as regras do processo.

Primeiramente, o tipo de nota que será gerada dependerá se o produto é apresentado na cópia ou na contagem, observe:

![Imagem 9: Primeiramente, o tipo de nota que será gerada dependerá se o produto é apresentado na cópia ou na contagem, observe:](https://ajuda.sankhya.com.br/hc/article_attachments/1500019718302)

Ou seja, se o produto com série estiver na cópia e não apresentar na contagem, será gerada uma nota de Saída. Se o produto com série apresentar na contagem e não estiver na cópia, será gerada uma nota de Entrada.

Assim, ao clicar no botão Ajustar os produtos que precisam ser ajustados serão lançados na Nota de Ajuste e o sistema executará automaticamente a funcionalidade do botão **"Gerar zero para produtos inexistentes na Contagem ou na Cópia"**, sendo que:

1. Para cada Série que existir na Cópia, mas que não foi apresentada na Contagem, será criada uma linha na Contagem com estoque zero para referenciar a linha existente na Cópia.
2. Para Séries que existirem na Contagem, mas que não foram encontradas na Cópia, será criada uma linha na Cópia com estoque zero para referenciar a linha existente na Contagem.

Além disso, as Séries identificadas na Cópia e que não foram apresentadas na Contagem, serão lançadas na Nota de Saída; Séries existentes na Contagem e não apresentadas na Cópia, serão lançadas na Nota de Entrada.

---

Agora que já entendemos as regras do processo, clique no botão **"Ajustar"** para que seja apresentada a tela com os números únicos da nota de saída e entrada que foram geradas. Com um duplo clique na linha desejada, é possível abrir a nota selecionada.

[GIF animado: Imagem 10: Agora que já entendemos as regras do processo, clique no botão "Ajustar" para que seja apresentada a tela com os…](https://ajuda.sankhya.com.br/hc/article_attachments/1500020161441)

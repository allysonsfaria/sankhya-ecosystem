---
id: "360044609614"
titulo: "Contagem de Estoque Por Série"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609614-Contagem-de-Estoque-Por-S%C3%A9rie"
trilha: "Manual do Produto > Suprimentos e Estoque > Inventário"
atualizado_em: "2026-07-29T14:49:04Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Inventário", "estoque", "contagem", "Contagem de Estoque Por Série", "controle adicional", "INITLOCCONTSE", "produto", "série", "VALEMPCONTSERIE", "br.com.sankhya.mgeinvent.cad.contagemestoqueporserie", "Contagem de Estoque Por Série manual", "Parâmetros influenciam rotina", "Contagem estoque série", "Confirmação grava contagem"]
---

# Contagem de Estoque Por Série

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312589746967) Módulo: Inventário > Arquivo
```

---

Opção que realiza a contagem de estoque por série, ou seja, esta tela será utilizada por empresas que controlam seu estoque através do controle adicional de estoque por **"Série"**.

O procedimento para realização da contagem por série é similar ao procedimento da [Contagem de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694-Contagem-de-Estoque), isto significa que, antes de fazer a contagem propriamente dita, será necessário realizar a [Cópia do Estoque por Série](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609674-C%C3%B3pia-de-Estoque-por-S%C3%A9rie).

Nesta tela de Contagem por Série, você passará o código de barras do produto caso este seja exatamente o número de série, ou irá digitar a série e o sistema reconhecerá o produto.

![Imagem 2: Nesta tela de Contagem por Série , você passará o código de barras do produto caso este seja exatamente o número de…](https://ajuda.sankhya.com.br/hc/article_attachments/360083135693)

O campo **"Data da Contagem"** será preenchido automaticamente pelo sistema com a data do dia.

O campo **"Tipo de Contagem"** também será preenchido pelo sistema, com a descrição **"Contagem"** e não poderá ser modificado.

Informe no campo **"Série"** a série para identificação do produto, se não estiver utilizando o código de barras.

O **"Cód. Produto"** que está sendo contado será preenchido automaticamente, assim que a Série for informada.

A **"Descrição (Produto)"** do produto que está sendo contado, assim como campo anterior, será preenchido automaticamente assim que a Série for informada.

O campo **"Cód. Empresa"** refere-se ao código da empresa que está realizando a contagem do estoque.

O campo **"Nome Fantasia"** refere-se ao nome da empresa que está realizando a contagem do estoque.

Informe o **"Cód. Local"** do produto (controle adicional de estoque).

No campo **"Descrição (Local)"** será apresentada a descrição do local do produto, uma vez informado o Cód. Local (controle adicional do estoque).

####

#### Botões da tela

- **Confirmar:** Se acionado, o sistema irá gravar a contagem efetuada, que ainda não tenha sido salva.
- **Rejeitar:** Desfaz as informações inseridas na última contagem efetuada.
- **Filtro:** Possibilita a criação de filtros, que facilite a busca dos registros necessários na grade.

Depois de confirmadas as informações, os campos serão desabilitados para edições, não permitindo **"Alterações"**, apenas a **"Exclusão"** do lançamento. Sendo feita a tentativa de alteração, será apresentada a seguinte mensagem:

**"Não é permitida a alteração de uma linha com Tipo Cópia ou Contagem que tenha sido confirmada".**

Poderá ser feita a exclusão de um lançamento do tipo **"Contagem"**; ao tentar excluir uma **"Cópia"** o sistema emitirá a mensagem:

**"Cópia não pode ser excluída nesta tela".**

**Observação:** de modo a evitar a inserção de produtos e séries repetidas para locais diferentes, que posteriormente geram duplicidade no momento do ajuste de estoque por série, o sistema conta com a trigger **"TRG\_INC\_UPD\_TGFCTS"** que valida se existem contagens no mesmo dia, da mesma série e em locais diferentes; caso exista, será apresentada a mensagem **"Série 000 já contada no local 111"**; não existindo, o processo segue normalmente.

#### Parâmetros que influenciam nesta rotina

O parâmetro **"Inicializa empresa/local na contagem por série - INITLOCCONTSE"**, quando é acionado e o produto tendo estoque, ao ser realizada sua contagem, na digitação da série, além da descrição do produto, serão apresentadas também a empresa e o local deste produto.

**Observação:** caso o parâmetro acima esteja desligado e o produto esteja com a marcação **"Usa local"** desabilitada, não será possível editar o campo **"Local"** da Contagem de Estoque por Série.

O parâmetro **"Valida empresa na contagem por série - VALEMPCONTSERIE"**, assim como o anteriormente informado, por padrão é apresentado desligado. Ao ser acionado, na confirmação da contagem, se a empresa informada não for a empresa do estoque, a confirmação não será efetuada e será apresentada uma mensagem informando este fato.

![Imagem 3: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16252576281879) Acesse também:

[Ajuste de Estoque por Série](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117673)

[Cópia de Estoque por Série](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609674)

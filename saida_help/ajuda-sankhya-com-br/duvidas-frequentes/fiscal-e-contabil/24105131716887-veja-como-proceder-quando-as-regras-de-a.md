---
id: "24105131716887"
titulo: "Veja como proceder quando as regras de alíquota não estão sendo levadas para a Central de Notas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24105131716887-Veja-como-proceder-quando-as-regras-de-al%C3%ADquota-n%C3%A3o-est%C3%A3o-sendo-levadas-para-a-Central-de-Notas"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:47:43Z"
rotulos: ["Alíquotas", "Configuração", "Central de Notas", "NF-e", "ICMS", "Impostos", "Regras de alíquota", "Regras ICMS", "Zeramento ICMS", "regras de alíquota não estão sendo levadas para a Central de Notas"]
---

# Veja como proceder quando as regras de alíquota não estão sendo levadas para a Central de Notas

Diante de um cenário em que **todas configurações para Cálculo de ICMS estão feitas**, porém **nenhuma regra de Alíquota de ICMS** está sendo **levada para a Central de Notas,** zerando o ICMS, **existe a possibilidade de estar acontecendo 3 tipos de situação, são elas:**

![Imagem 1: Marcação de Tem ICMS está desmarcada; Caso não seja uma Nota de Compra, e no cadastro do Produto, o campo "Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/24113661736215) Marcação de Tem ICMS está desmarcada;
 
![Imagem 2: Marcação de Tem ICMS está desmarcada; Caso não seja uma Nota de Compra, e no cadastro do Produto, o campo "Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/24113687422487) Caso não seja uma Nota de Compra, e no cadastro do Produto, o campo **"Tipo Substituição"** estiver igual a **"Revenda com subst. tributária (cálculo de Subst. na Compra)"** e também não ser uma Movimentação do Simples Nacional, o ICMS será Zerado.
 
![Imagem 3: Marcação de Tem ICMS está desmarcada; Caso não seja uma Nota de Compra, e no cadastro do Produto, o campo "Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/24113687434519) Quantidade negociada é menor que **zero.**

Assim, caso as configurações da nota atenda qualquer um desses 3 requisitos, a rotina de Zeramento do ICMS será efetuada. Sendo a segunda opção a maneira mais comum de acontecer. Desse modo, mesmo que todas configurações para o Cálculo de ICMS estejam corretas, se qualquer uma dessas 3 situações acontecer, prevalecerá o zeramento do ICMS, e não será vinculado nenhuma regra de ICMS consequentemente mantendo o ICMS igual a Zero.
 
Vale ressaltar que, para o resolver o problema, é necessário rever as configurações, no exemplo do 2º caso, é necessário que a marcação do Tipo de Substituição seja outro, para que não pare nessa regra de validação e zere o ICMS

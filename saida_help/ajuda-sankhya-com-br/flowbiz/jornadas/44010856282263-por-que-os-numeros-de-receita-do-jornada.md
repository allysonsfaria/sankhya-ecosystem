---
id: "44010856282263"
titulo: "Por que os números de receita do Jornadas e do Google Analytics são diferentes?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010856282263-Por-que-os-n%C3%BAmeros-de-receita-do-Jornadas-e-do-Google-Analytics-s%C3%A3o-diferentes"
trilha: "Flowbiz > Jornadas"
atualizado_em: "2026-10-05T18:49:19Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_146", "sync_hash_a1077fb240fd"]
---

# Por que os números de receita do Jornadas e do Google Analytics são diferentes?

Se você já comparou os dados do **Jornadas** da Flowbiz com os do **Google Analytics** e percebeu uma diferença nos valores de receita, saiba que isso é esperado!

### Entenda a diferença

#### 🟡 Como o Jornadas calcula a receita recuperada:

- A receita só é atribuída ao canal e-mail **se o cliente clicar no link do e-mail da jornada de carrinho abandonado**.
- Depois de clicar, **a compra precisa ser finalizada em até 7 dias**.
- Se o cliente não clicar no e-mail, ou comprar depois dos 7 dias, **a venda não entra na contagem do Jornadas**, mesmo que tenha ocorrido.

#### 🔵 Como o Google Analytics (GA) calcula a receita:

- O GA usa o modelo **last click** (último clique): ele atribui a receita ao último canal de origem da sessão onde a compra foi feita.
- Ele **não considera se o cliente passou por um e-mail de carrinho antes**.
- Então, se o cliente clicou no e-mail, saiu do site e depois voltou pelo Google e comprou, o GA vai atribuir a venda ao Google, não ao e-mail.

### ⚠️ Isso significa que um relatório pode mostrar receita, e o outro não?

Sim, exatamente. É comum o GA mostrar que o e-mail gerou vendas, enquanto o painel do Jornadas mostra R$ 0,00. Isso não é um erro, é só uma **diferença nos critérios de atribuição**.

## 🧭 E como eu sei se o e-mail gerou resultado?

A dica é verificar dois pontos:

1. O cliente **clicou no link do e-mail da jornada**?
2. Ele **concluiu a compra em até 7 dias** depois desse clique?

Se a resposta for sim para os dois, o Jornadas vai considerar essa receita como recuperada por e-mail. Caso contrário, ela pode aparecer apenas no GA, atribuída a outro canal.

## ✅ Resumo rápido

O Jornadas só considera a receita quando o cliente clica no link do e-mail e finaliza a compra em até 7 dias. Já o Google Analytics mostra a receita com base no último canal acessado antes da compra. Por isso, os números podem ser diferentes.

## 🤝 Precisa de ajuda?

Se ainda tiver dúvidas sobre os relatórios ou quiser ajuda para analisar algum caso específico, é só falar com a gente pelo chat da plataforma ou pelo e-mail [suporte@flowbiz.com.br](mailto:suporte@flowbiz.com.br). Estamos por aqui para te ajudar!

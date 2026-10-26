---
id: "360044612634"
titulo: "Recálculo do Preço de Tabela pela Fórmula de Precificação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612634-Rec%C3%A1lculo-do-Pre%C3%A7o-de-Tabela-pela-F%C3%B3rmula-de-Precifica%C3%A7%C3%A3o"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:27:20Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Fórmulas", "Atualização", "ALTTABFORRECPRE", "cálculo", "Família", "fórmula", "precificação", "preço", "Recálculo do Preço de Tabela pela Fórmula de Precificação", "tabela", "br.com.sankhya.com.mov.recalculoprectab", "Recálculo do Preço de Tabela pela Fórmula de Precificação manual", "Fórmula de precificação", "Atualização de Preços", "Tabela Específica", "Comercial"]
---

# Recálculo do Preço de Tabela pela Fórmula de Precificação

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311963410967) Módulo: Comercial > Avançado
```

---

Através desta tela você pode atualizar os preços das tabelas utilizando a Fórmula de Precificação vinculada ao produto, e as notas de entrada do produto considerando o período de movimento informado. Sendo que, a fórmula de precificação utilizada nesta rotina e no [Recálculo de Custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594214) são iguais.

**Observação:** Esta tela foi desenvolvida para atualizar apenas a tabela 'zero', sendo que, quando o parâmetro **"Alt.Tab/Fórmula Recálculo Preço Form.Precificação? - ALTTABFORRECPRE"** estiver habilitado, será permitida a alteração de tabelas que possuem origem diferente de 'zero'.

![Imagem 2: Observação: Esta tela foi desenvolvida para atualizar apenas a tabela 'zero', sendo que, quando o parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/14150208779799)

No campo **"Período de movimento"** informe o intervalo de Notas de Entrada para o sistema utilizar no cálculo do preço de tabela.

**Observação:** o sistema irá buscar os custos dos produtos no período informado para realizar o cálculo, além de buscar as informações das seções **"% de custo variável a ser calculado sobre o faturamento"** e **"% de custo fixo"** da aba [Margem de Contribuição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853#abamargemdecontribuio) localizada nas [Preferências do Gerente On-Line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853). Então, para definição de % de custo fixo e % de custo variável, será considerada a referência do custo mais recente no período de movimento.

Através do campo **"Empresa"**, aponte a instituição para o recálculo do preço de tabela.

O período pelo qual os novos preços entrarão em vigor é discriminado no campo **"Data de Vigor"**.

Por meio do campo **"Data de Alteração"**, indique a data em que tabela de preço foi alterada.

A opção **"Usar custos do produto pai"** terá implicação sobre o cálculo de custo dos produtos configurados na aba [Família](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abafamlia) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113). Se marcada, o sistema calculará os preços dos produtos filhos (informados na aba Família), de acordo com o custo dos produtos pais. Se desmarcada, o sistema calculará os preços utilizando os custos de cada produto, independente de seus vínculos com outros produtos.

O campo **"Tabela"** permite que seja informada uma tabela específica para o recálculo, ou seja, o sistema fará o recálculo para a tabela informada aqui e não para a Tabela 0.

Através do campo **"Fórmula"**, você pode discriminar uma fórmula exclusiva, isto é, neste caso será utilizada a fórmula informada neste campo e não a configurada no Cadastro do Produto.

**Observação:** A visualização dos campos Tabela e Fórmula depende do acionamento do parâmetro **"Alt.Tab/Fórmula Recálculo Preço Form.Precificação? - ALTTABFORRECPRE"**.

Temos ainda a possibilidade de criar filtros personalizados atendendo cada necessidade específica de cada usuário.

Uma vez definido os filtros, basta pressionar o botão **"Recalcular"** para que o sistema faça o ajuste de preço de todos os produtos da Tabela 0, automaticamente.

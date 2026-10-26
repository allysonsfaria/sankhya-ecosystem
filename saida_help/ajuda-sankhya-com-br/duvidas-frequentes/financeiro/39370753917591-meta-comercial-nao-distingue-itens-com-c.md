---
id: "39370753917591"
titulo: "Meta comercial não distingue itens com CFOP de bonificação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39370753917591-Meta-comercial-n%C3%A3o-distingue-itens-com-CFOP-de-bonifica%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-10-22T13:00:48Z"
rotulos: ["Produtos", "Parceiro", "Relatórios Gerenciais", "CFOP", "Planejamento Orçamentário", "Artigo criado KCS", "Financeiro - KCS", "Meta Comercial"]
---

# Meta comercial não distingue itens com CFOP de bonificação

No **Planejamento Orçamentário**, quando a meta comercial tem os campos significativos **Parceiro** e **Produto**, com a opção **Meta por quantidade** ativada, o sistema não distingue itens bonificados de itens vendidos que estejam na mesma nota fiscal, mesmo que tenham CFOPs diferentes.

### Como o sistema trata a meta comercial

A meta é apurada com base no parceiro e no produto. O sistema considera as notas lançadas com as TOPs informadas na aba **TOP** da meta.

Quando uma nota tem itens de venda e itens bonificados ao mesmo tempo, e a TOP dessa nota está informada na meta, todos os itens do produto com valor previsto são considerados na meta, independentemente do CFOP.

### Limitações do sistema

O sistema não separa:

- Produtos bonificados (CFOP 5910/6910) de produtos vendidos (CFOP 5101/5102/6101/6102) dentro da mesma nota.
- Lançamentos por CFOP quando os campos significativos são Parceiro e Produto.
- Valores de bonificação dos valores de venda na apuração da meta.

Esse é o comportamento padrão do sistema. A meta comercial não foi desenvolvida para fazer distinção por CFOP.

### Impacto na gestão comercial

Quando a empresa trabalha com bonificações parciais, ou seja, itens bonificados e vendidos na mesma nota, os itens bonificados também entram no realizado da meta. Isso pode distorcer a análise de desempenho comercial, porque bonificações não geram receita de venda.

### Alternativas de controle

- **Emitir notas separadas com TOP específica para bonificação:** use uma TOP exclusiva para as bonificações e não a informe na aba **TOP** da meta. Assim, só as notas de venda entram no realizado. Atenção: separar as notas sem usar uma TOP diferente não resolve, porque a nota de bonificação continuaria sendo considerada.
- **Relatórios personalizados:** crie relatórios que filtrem os lançamentos por CFOP para acompanhar as vendas sem as bonificações.

**Importante:** Fale com a sua equipe de controladoria para definir a melhor forma de acompanhar as metas comerciais quando houver bonificações no processo de vendas.

---
id: "360044519073"
titulo: "Precisa recompor um título e esqueceu de marcar a opção 'Recompor título original', o que fazer?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044519073-Precisa-recompor-um-t%C3%ADtulo-e-esqueceu-de-marcar-a-op%C3%A7%C3%A3o-Recompor-t%C3%ADtulo-original-o-que-fazer"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T15:55:59Z"
rotulos: ["#criadoRoger", "Configuração", "Estorno", "Movimentação Financeira", "Financeiro", "Parâmetro", "Recompor título original no estorno", "Automatizar com parâmetro ESTRECOMPOPC", "Campos devem estar vazios para recomposição"]
---

# Precisa recompor um título e esqueceu de marcar a opção 'Recompor título original', o que fazer?

Efetuou um estorno de um titulo e esqueceu de marcar a opção 'Recompor título original'?. Não se preocupe, é possível efetuar novamente a baixa do titulo parcialmente e no ato do estorno, marque a opção 'Recompor título original', desta forma o sistema ira agrupar o valor do título baixado ao título original que esta aberto.

Para automatizar a recomposição do título, considere desligar o parâmetro mencionado abaixo.

**Nota**: Parâmetro **ESTRECOMPOPC-Estorno com Recomposição Opcional?**

Este parâmetro quando estiver **habilitado** e o título for correspondente à recomposição, no momento de finalizar o estorno o sistema apresentará um pop-up questionando se o usuário deseja recompor o título original. Por outro lado, quando encontrar-se desabilitado, será apresentada uma mensagem informando que ao concluir, será recomposto o título original, ou seja, o usuário não poderá realizar o estorno.

**Observação**: Os campos de Nosso numero, Linha Digitável e Código de Barras, devem estar vazios(no titulo original), para ocorrer a recomposição de forma completa.

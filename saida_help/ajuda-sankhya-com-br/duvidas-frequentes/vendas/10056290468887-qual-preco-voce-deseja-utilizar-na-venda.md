---
id: "10056290468887"
titulo: "Qual preço você deseja utilizar na venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10056290468887-Qual-pre%C3%A7o-voc%C3%AA-deseja-utilizar-na-venda"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:04:56Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "#PubliFer", "Ticket#228231", "Sistema solicita escolha de tabela de preço ao inserir itens no carrinho", "Preços são definidos pela aba Preços nas configurações do painel de resultados", "Multiplicador ajusta o preço da tabela escolhida; sistema usa data de vigor mais recente", "Venda Mais", "Preços"]
---

# Qual preço você deseja utilizar na venda

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19575326456599) SOLUÇÃO:**

Ao realizar a inserção dos itens através do 'carrinho' nas  Centrais, o sistema poderá solicitar a definição de **"qual preço você deseja utilizar".** Nesse artigo seguem os detalhes das configurações responsáveis por essa solicitação :

![Imagem 2: Ao realizar a inserção dos itens através do 'carrinho' nas Centrais, o sistema poderá solicitar a definição de "qual…](https://ajuda.sankhya.com.br/hc/article_attachments/10065395477271)

### Tela 'Consulta de Produtos' : Configurações do Painel de Resultados - 'Aba Preços'

Na imagem acima, o sitema estava solicitando a seleção da tabela desejada, conforme configuração realizada nas 'Configurações do Painel de Resultados - Aba Preços' :

![Imagem 3: Na imagem acima, o sitema estava solicitando a seleção da tabela desejada, conforme configuração realizada nas…](https://ajuda.sankhya.com.br/attachments/token/3YjtQAhpflnAjiXqRFxugFd3t/?name=image.png)

A consulta irá exibir os preços dos produtos de acordo com as definições efetuadas nessa aba. Os preços poderão ser definidos informando os campos "Descrição", "Tabela específica" e "Multiplicador", sendo que, **se a tabela específica não for informada, será utilizada a tabela padrão (0) do produto.**

Após acionar o botão de pesquisa, a janela de consulta "Pesquisando "Tabela de Preço"" é apresentada; nela, são exibidos em "Código" apenas os códigos das tabelas. Internamente, o sistema verifica o Cód. Único da Tabela (NUTAB) desse cód. da tabela (CODTAB), retornando para você, apenas a que possui data de vigor mais atual.

Nota: Caso você tenha inserido no sistema uma tabela de preço com data de vigor antiga, após a atualização da versão, o sistema automaticamente selecionará a mesma tabela, porém com a data de vigor mais atual.

O campo "Multiplicador" é o valor pelo qual será multiplicado o preço da tabela, seja ela uma tabela específica ou a tabela padrão do produto.

Poderão ser definidos vários preços nessa aba. Clicando sobre um produto no painel de resultados, serão exibidos todos os preços cadastrados no painel de "Detalhes de preço".

**Observação**: A visualização do novo "Preço" cadastrado poderá ser configurada através da aba Layout da célula para ser visualizada em outros locais.

Mais detalhes, [clique aqui !](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353)

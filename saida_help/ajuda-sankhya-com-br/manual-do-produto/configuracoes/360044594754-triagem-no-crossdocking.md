---
id: "360044594754"
titulo: "Triagem no Crossdocking"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594754-Triagem-no-Crossdocking"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-10-19T20:28:23Z"
rotulos: ["Produtos", "Triagem no Crossdocking manual", "Configuração", "WMS", "Estoque", "Preferências", "Situação do Recebimento: \"Aguardando Armazenagem\"", "Utiliza triagem no Crossdocking", "Endereço de Crossdocking", "Crossdocking"]
---

# Triagem no Crossdocking

Esta rotina permite que você realize triagens quando existir um [Empenho do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos) para o Recebimento.

**Observação:** este processo só dará suporte à produtos que utilizarem o código de barras concatenado.

Primeiramente, para utilização correta desta rotina, deve-se atribuir a tarefa de Triagem Crossdocking ao executante, através da tela [Configurações por Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595354).

Após isto, é necessário efetuar a marcação **"Utiliza triagem no Crossdocking"** localizada nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms), conforme demonstrado abaixo:

![Imagem 1: Após isto, é necessário efetuar a marcação "Utiliza triagem no Crossdocking" localizada nas Preferências da Empresa ,…](https://ajuda.sankhya.com.br/hc/article_attachments/9535088359831)

**⚠️ Atenção**

Com a marcação **Utiliza triagem no Crossdocking** ativada, o encaminhamento automático da mercadoria para o endereço de Crossdocking fica desligado. Você precisa executar a triagem no Coletor de Dados. Sem a triagem, a mercadoria não chega ao Crossdocking e a onda do pedido empenhado não é liberada.

Assim, efetuadas as configurações acima, para que a rotina seja executada corretamente, deverá existir algum produto da Nota de Compra que contenha pelo menos um empenho realizado, ou seja, deve-se empenhar os itens de uma Nota de Compra em um Pedido de Venda para o Crossdocking; caso contrário, ao utilizar a função de Triagem Crossdocking no Coletor de Dados e informar a doca de recebimento, será exibida a seguinte mensagem:

**"Nenhuma triagem pendente encontrada para o endereço informado".**

**Observações:**

**(3)**A mensagem acima também será exibida quando o Recebimento estiver com a situação **"Aguardando Conferência"**.

**(3)**Apenas será autorizado o início da triagem quando a situação do Recebimento for **"Aguardando Armazenagem"**.

**(3)**Quando um ou mais produtos forem triados e possuírem produtos não triados na grade, caso seja acionado o botão **"Tudo Crossdocking"** do Coletor de Dados, o sistema encaminhará para o Endereço de Crossdocking todo o estoque referente àquela triagem que existe na Doca de Entrada.

**(3)**A rotina de Triagem de Crossdocking não aceita quantidade de Empenho menor que a quantidade total, apenas maior.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594754-Triagem-no-Crossdocking#top)

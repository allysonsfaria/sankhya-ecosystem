---
id: "360053863493"
titulo: "Itens Conferidos no Coletor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360053863493-Itens-Conferidos-no-Coletor"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:16:32Z"
rotulos: ["Conferência", "Configuração", "WMS", "Coletor", "Estoque", "Itens Conferidos no Coletor", "Mensagens e remoção manual", "Informe executante e remova"]
---

# Itens Conferidos no Coletor

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311592813591) Módulo: WMS > Consultas
```

---

![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/360087828494)

A pessoa responsável por esta tela na empresa deve informar o **"Executante da conferência"** e clicar no botão **"Remover conferências..."**, para que sejam removidas todas as conferências daquele executante e para que ele possa realizar a conferência novamente.

O parâmetro **"Permite remover conferên. não enviadas no coletor? - PERMREMCONFERE"** possui influência nessa rotina da seguinte forma:

- Tendo sido iniciada uma conferência que ainda possua itens conferidos, mas que estes não foram enviados e este parâmetro estiver **desligado**, ao retomar a conferência de saída no coletor, será exibida a mensagem: **"Conferência não enviada! Deseja enviar?"**; caso clique em **"Não"**, é apresentada a seguinte mensagem no coletor:

**"Favor procurar o responsável para remover as conferências não enviadas.".**

**Observação:** este responsável deverá ser a pessoa que possui acesso à tela Itens Conferidos no Coletor.

- Por outro lado, se o parâmetro estiver **ligado** e a última conferência em andamento não tiver sido enviada, ela será excluída automaticamente pelo sistema, sem precisar removê-la manualmente na tela Itens Conferidos no Coletor.

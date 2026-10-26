---
id: "8929102402711"
titulo: "Grupos de Endereços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8929102402711-Grupos-de-Endere%C3%A7os"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:17:13Z"
rotulos: ["Configuração", "WMS", "Usuários", "Estoque", "br.com.sankhya.wms.GruposdeEnderecos", "Cadastro", "Cadastro: Alocar operadores", "Configuração: Faixas endereços tarefas", "Restrições: Tarefas e áreas limitadas", "Logística"]
---

# Grupos de Endereços

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311657526935) Módulo: WMS > Cadastros
```

---

Essa tela serve para que o Gestor do WMS possa alocar os operadores em áreas de trabalho específicas, determinadas por faixas de endereços. Uma vez configurada uma faixa de endereço e alocado um operador, será possível determinar qual(is) atividade(s) esse operador poderá executar dentro daquela faixa configurada, podendo ser uma Separação, Reabastecimento, Armazenamento, Transferência ou Inventário.

Inicialmente, deve ser cadastrado o nome da área que reflete na área de trabalho dentro do armazém.

Em nosso exemplo, teremos uma área de armazenagem de Ferragens:

![Imagem 2: Em nosso exemplo, teremos uma área de armazenagem de Ferragens :](https://ajuda.sankhya.com.br/hc/article_attachments/8929252298647)

O próximo passo é incluir na aba **"Executante"** quais operadores irão realizar as operações nessa área do armazém e quais tarefas ele pode operar dentro da faixa de endereços ou da área de Ferragens:

![Imagem 3: O próximo passo é incluir na aba "Executante" quais operadores irão realizar as operações nessa área do armazém e quais…](https://ajuda.sankhya.com.br/hc/article_attachments/8929396681495)

No nosso caso, o usuário Felipe poderá operar apenas as tarefas de **"Separação"**.

Após cadastrar o nome do Grupo de Endereços, o usuário e as tarefas, agora podemos fazer o cadastro da **"Faixa de Endereços"** que o Felipe irá trabalhar.

![Imagem 4: Após cadastrar o nome do Grupo de Endereços , o usuário e as tarefas, agora podemos fazer o cadastro da "Faixa de…](https://ajuda.sankhya.com.br/hc/article_attachments/8929444150935)

A área de trabalho Ferragens irá iniciar no endereço **"3.001.001.0"** e finalizar no endereço **"3.909.911"**.

Uma vez configurada a faixa de endereços e vinculado o operador a ela, ele ficará restrito às demais áreas do armazém, executando somente a tarefa de separação dentro daquela determinada faixa de endereço.

Mesmo que o usuário tenha acesso à outras tarefas, caso ele tente puxar tarefas que não estão configuradas nessa tela, o coletor retornará a mensagem abaixo, validando a tarefa e faixa de endereço:

[GIF animado: Imagem 5: Mesmo que o usuário tenha acesso à outras tarefas, caso ele tente puxar tarefas que não estão configuradas nessa tela,…](https://ajuda.sankhya.com.br/hc/article_attachments/8929805322647)

**Observações:**

- As configurações realizadas nessa tela sobrepõem a configuração de [Área de Separação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o), ou seja, se um separador está alocado em uma área de separação que a faixa de endereçamento é maior do que a configurada nessa tela, o operador poderá operar somente na faixa definida na tela Grupos de Endereços.
- Para tarefas de Armazenagem e Transferência, devem ser incluídos endereços de docas na faixa de endereços, pois esses endereços estão diretamente envolvidos nessas tarefas.

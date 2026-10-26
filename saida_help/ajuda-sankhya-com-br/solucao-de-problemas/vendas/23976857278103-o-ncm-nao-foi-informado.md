---
id: "23976857278103"
titulo: "O NCM não foi informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/23976857278103-O-NCM-n%C3%A3o-foi-informado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:47:57Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Preferências", "CORE_E06789", "Erro"]
---

# O NCM não foi informado

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/23976834696983) **MENSAGEM:**

[CORE\_E06789] O NCM não foi informado

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/23976834700695) **SOLUÇÃO:**

Para resolver a questão, acesse a tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"**(Caminho: Configurações » Avançado » Preferências), busque pelo parâmetro **"VALUSOPRODNCM"**e verifique se no campo **"Texto"** está descrita a letra 'S'. Caso não esteja, coloque a letra 'S'.

![Imagem 3: Para resolver a questão, acesse a tela " Preferências " (Caminho: Configurações » Avançado » Preferências), busque pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/23976834703639)

**Observação:** a inserção da letra 'S no campo Texto faz com que o sistema não realize a validação do campo NCM e passe a considerar a informação preenchida no campo **"Usado como"** do cadastro de Produtos/Serviços. Neste caso por se tratar de serviço, o campo Usado como é automaticamente preenchido com a letra 'S'. Dessa forma, estando preenchido o campo Texto com a letra 'S', o campo Usado como já estará cadastrado automaticamente com a letra 'S', a mensagem de erro deixará de ser apresentada. 

![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/23976857270039) **CAUSA:**

Ao cadastrar um Serviço, tendo o parâmetro VALUSOPRODNCM  configurado de maneira indevida, a mensagem é apresentada.

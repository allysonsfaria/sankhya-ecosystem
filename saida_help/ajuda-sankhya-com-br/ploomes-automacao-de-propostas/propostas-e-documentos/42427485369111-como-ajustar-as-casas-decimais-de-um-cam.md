---
id: "42427485369111"
titulo: "Como ajustar as casas decimais de um campo de porcentagem?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427485369111-Como-ajustar-as-casas-decimais-de-um-campo-de-porcentagem"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-10T18:03:09Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6027052", "sync_hash_dbc7a2db1766"]
---

# Como ajustar as casas decimais de um campo de porcentagem?

Os campos do tipo **Porcentagem** podem receber até **9 caracteres** e permitem mais de uma casa decimal.

No entanto, por padrão, o sistema exibe apenas **uma casa decimal**. Assim, por exemplo, se um desconto for informado como **11,25%**, após a geração da proposta o valor será **arredondado para 11,3%**.

## Como ajustar?

- Acesse **Administração > Modelos de documento**;
- Selecione o **modelo de documento** desejado;
- Clique em **Código-fonte**, no canto superior direito;
- Utilize **Ctrl + F** para pesquisar pelo nome do **campo de porcentagem** no código.

[GIF animado: Imagem 1: Utilize Ctrl + F para pesquisar pelo nome do campo de porcentagem no código.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2152260773/0def4f27df2c9bb8eeba5abf427b/codigo.gif?expires=1786536000&signature=51f84e93acd2bfe66ae95ed15cdcff136d9cbe458052a5f93ee77ac44c618075&req=diEiFMt4nYZYWvMW3nq%2BgRXgD23EJJgBT5cjRZfkzQd%2FSymmWAB4BbJ6pxUZ%0ATniOPqOhgCPHIHYb9AVe0C7264U%3D%0A)

A **tag** do campo começa em `<field>` e termina em `</field>`. Dentro dessa tag, localize o seguinte código:

```
format="n1"
```

Esse número define a **quantidade de casas decimais** exibidas após a vírgula.

Exemplos:

- **n0** -> 11,25 se torna **11**
- **n1** -> 11,25 se torna **11,3**
- **n2** -> 11,25 se torna **11,25**
- **n3** -> 11,25 se torna **11,250**

Altere o número conforme a **quantidade de casas decimais** que deseja exibir. Em seguida, clique em **Ok** e depois em **Salvar**.

Para aplicar a alteração também em **propostas já criadas**, acesse a proposta e clique em **Editar > Atualizar dados e modelo**.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).

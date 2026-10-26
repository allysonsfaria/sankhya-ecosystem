---
id: "42427486550807"
titulo: "Exibição condicional de campos no formulário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427486550807-Exibi%C3%A7%C3%A3o-condicional-de-campos-no-formul%C3%A1rio"
trilha: "PLOOMES: Automação de propostas  > Campos e formulários"
atualizado_em: "2026-08-11T16:14:44Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452353", "sync_hash_0809b93f6b1d"]
---

# Exibição condicional de campos no formulário

A exibição condicional permite ocultar ou exibir um campo automaticamente com base em uma fórmula ou restrição de usuários.

A configuração de exibição pode ser feita em qualquer campo, de qualquer entidade. No exemplo a seguir, farei com um campo do formulário de **clientes**.

## Como configurar a condição de exibição

**1. Acesse o formulário**

Em Administração > Campos e Formulários, você pode personalizar os formulários de:

- Cliente (Empresas, Pessoas, Produto de cliente)
- Produto (Produtos, Grupos, Famílias, Vínculos)
- Sua empresa
- Usuário (Usuários, Equipes)
- Registro de Interação

Os formulários de **Negócios** são configurados diretamente no funil correspondente. [Clique aqui](https://sankhya.zendesk.com/hc/pt-br/articles/42427677266455) para saber sobre formulários de negócios.

Já os formulários de **Propostas, Vendas e Documentos** são configurados diretamente em seus respectivos modelos. [Clique aqui](https://sankhya.zendesk.com/hc/pt-br/articles/42427464523031) para saber sobre formulários de propostas.

**2. Localize o campo e clique no ícone de edição**

![Imagem 1: 2. Localize o campo e clique no ícone de edição](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329431/017b529832795ad9b5cc97ae/mceclip4.png?expires=1786536000&signature=2c27a8a135d043717efe48b8f964ff8cbd95d450ab1463daf3a421b47d85bd39&req=dyYuFct3mYJeFb4V1XW4ga73zXqaCXWPPsS97uPUD65ciG7WxJyavFy93Zch%0ASsEzXKdOuuITN8cLPQTN2laEzg%3D%3D%0A)

**3. Localize e expanda a seção de "Configurações de visualização do campo"**

Clique em "Configurar" para definir a fórmula de regra da exibição.

![Imagem 2: Clique em "Configurar" para definir a fórmula de regra da exibição.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329434/d5cdede8825a39c25469a8ff/mceclip3.png?expires=1786536000&signature=0e072a2dcc62742093a9e92c5dfb0aedd8045d3e721475c15762b0f9dfc92f79&req=dyYuFct3mYJbFb4V1XW4gUI4n10bjyMahWx3JHLgbLDDtYnGlf37PcfJAVo8%0Agnpb%2BClr0UTKdTp8g9MxYez20g%3D%3D%0A)

**4. Configure a fórmula**

Agora vamos criar uma fórmula em Javascript**.** Se nossa fórmula retornar verdadeiro (true), o campo será ocultado. Se retornar falso (false), será exibido.

Caso tenha dificuldade com essa etapa do processo, não hesite em pedir ajuda a nosso time de suporte.

Vou criar um exemplo onde meu campo (Porte da empresa) será exibido se o segmento for igual a "Distribuidora".

[GIF animado: Imagem 3: Vou criar um exemplo onde meu campo (Porte da empresa) será exibido se o segmento for igual a "Distribuidora".](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329438/33522bc2addc02073e3de8a7/formula_artigo.gif?expires=1786536000&signature=a7a2f11dcecff62fcd4282deecae455c0e8034760d5939fecb61126c8e2266b8&req=dyYuFct3mYJXFb4V1XW4gZ%2F2y6oAlNN39EpdnLv97nsPLI8uTJ6%2FgDHYjLD%2B%0Aqaj7nZKve%2FPciNDJ%2BPtBTsXW0w%3D%3D%0A)

```
if("[Cliente.Segmento]"==="Distribuidora"){false}else{true}
```

Em português:

Se o segmento for igual a "Distribuidora", falso (exibe); caso contrário, true (oculta)

Podemos mudar a lógica da fórmula para dizer o contrário:

Se o segmento for Diferente de "Distribuidora", falso (exibe); caso contrário, true (oculta)

O operador !== indica diferença:

```
if("[Cliente.Segmento]"!=="Distribuidora"){false}else{true}
```

Fórmulas mais avançadas ("Contém", com a função .includes, por exemplo) podem ser aplicadas da mesma maneira.

**5. Configure para ocultar por padrão**

Se deseja que a fórmula apenas exiba o campo em certas situações (como no exemplo supracitado), preciso bloquear a exibição por padrão. Assim, quando abro o formulário, o campo já vem oculto.

Para isso, basta ativar a chave:

![Imagem 4: Para isso, basta ativar a chave:](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329442/a11819c278310ba84f879190/mceclip5.png?expires=1786536000&signature=1235d95a82987e7e887a6483c9a6dd9145fe75ce5b897dc2627199301b11b596&req=dyYuFct3mYVdFb4V1XW4gWpowhq1YVa%2FvYIedRMBExdFw5E0EeLgue7Kv0oS%0ABCWY27KGYv%2BRLJwbwqR9aTI9sw%3D%3D%0A)

**6. Salve as alterações**

Clique em "Salvar formulário" para confirmar os ajustes.

![Imagem 5: Clique em "Salvar formulário" para confirmar os ajustes.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329446/68feb4a447819f3ce257c5bc/mceclip7.png?expires=1786536000&signature=24022f273c73f7a3740a82b3f0c15855f92dabef9515d5ea8a93991b6c712142&req=dyYuFct3mYVZFb4V1XW4gYE6BfQNmG6gD1WYaVDTaNFzeNphKU67mJzkwesK%0Ar%2BYZdmMkn0qBuDwvaQYZeEtSYA%3D%3D%0A)

Abaixo, um exemplo do funcionamento da fórmula ao cadastrar um novo cliente:

[GIF animado: Imagem 6: Abaixo, um exemplo do funcionamento da fórmula ao cadastrar um novo cliente:](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329448/b23e379a81e0e1f11b8debf2/campo_oculto.gif?expires=1786536000&signature=a0a053a86083b7bed8f15f522ef363ef4aa43ed339ef60f2dc4ca769aa2a4aa6&req=dyYuFct3mYVXFb4V1XW4gUxdoH7un1joQJZjKeMlRRdUtrqEo%2BFN8OGZ5gUk%0Anqrk1GAZT7wN4wt%2FG9NNtUB6mQ%3D%3D%0A)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).

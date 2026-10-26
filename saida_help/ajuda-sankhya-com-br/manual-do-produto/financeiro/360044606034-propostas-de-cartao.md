---
id: "360044606034"
titulo: "Propostas de Cartão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606034-Propostas-de-Cart%C3%A3o"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:38:17Z"
rotulos: ["AJUDA DO SKW", "manual", "Parceiro", "Crédito", "Financeiro", "br.com.sankhya.opcredito.propostacartao", "Propostas de Cartão manual", "Rotina Exclusiva de Parceiro", "Financeiro > Operações de Crédito", "Não avaliada Deferida Inconsistente Indeferida", "B2B não pode alterar status; conversão só por não B2B", "Proposta", "Operações de Crédito"]
---

# Propostas de Cartão

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312278884503) Módulo: Financeiro> Rotinas> Operações de Crédito
```

---

![Imagem 2: Esta rotina é exclusiva de um parceiro e habilitada por um parâmetro específico.](https://ajuda.sankhya.com.br/hc/article_attachments/16541919553303) Esta rotina é exclusiva de um parceiro e habilitada por um parâmetro específico.

Nesta tela serão lançadas, por parceiros B2B**\*** ou não, propostas de cartões de créditos, que poderão, posteriormente, passar por uma análise extra sistema, onde será definido se o Prospect deverá ou não ser cliente.

**B2B\*** é o nome dado às relações (comércio\negociação) entre empresas ("de empresa para empresa").

![Imagem 3: B2B * é o nome dado às relações (comércio\negociação) entre empresas ("de empresa para empresa").](https://ajuda.sankhya.com.br/hc/article_attachments/4416150304023)

**Funcionalidades da tela**

Você pode definir o **"Status da Proposta"**, de acordo com as seguintes alternativas:

- **Não avaliada:** Proposta ainda em aberto.
- **Deferida:** Proposta Aprovada.
- **Inconsistente:** Proposta incompleta, faltando informações.
- **Indeferida:** Proposta negada.

Ao modificar o Status da proposta para Deferido após a confirmação de update ou insert será validada e exibida a tela de conversão de Prospect para Parceiro e caso não exista nenhum campo pendente de preenchimento será exibida a seguinte tela:

![Imagem 4: Ao modificar o Status da proposta para Deferido após a confirmação de update ou insert será validada e exibida a tela…](https://ajuda.sankhya.com.br/hc/article_attachments/4416165904407)

```
![Imagem 5: Ao modificar o Status da proposta para Deferido após a confirmação de update ou insert será validada e exibida a tela…](https://ajuda.sankhya.com.br/hc/article_attachments/42312278885143) Após a conversão os campos do formulário não poderão ser editados.
```

Caso a proposta esteja Deferida e o usuário logado não seja B2B, o mesmo poderá converter este Prospect para um Parceiro, por meio do botão **"Outras opções"**, opção **"Converter prospect em parceiro"**.

No campo **"Nome do Cartão"**, informe qual é o cartão de crédito do Prospects, por exemplo, Visa, Mastercard, entre outras.

**Observação:** este campo se tornará obrigatório sempre que o campo **"Possui cartão de Crédito"** estiver marcado.

Se o campo **"Observações"** for preenchido na conversão de Prospect para Parceiro, as informações deste campo serão levadas para o campo Observações, no [Cadastro de Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494).

Caso você tente excluir um Prospect já convertido, será exibida a seguinte mensagem:

**"Não é permitida a exclusão de Prospects convertidos para Parceiros."**

Ao tentar editar um Prospect já convertido, será apresentado o seguinte aviso:

**"Não é permitida a edição de Prospects convertidos para Parceiros."**

Uma vez logado com um usuário B2B, somente serão apresentadas propostas lançadas pelo mesmo. Caso contrário, quando o usuário logado não for B2B, serão exibidos todos os registros (de todos os usuários).

Com relação à identificação no banco de dados, existe na tabela TCSPAP o campo ISPROPOSTACARTAO que estará assinalado com **"S"** quando os lançamentos forem realizados pela tela de Proposta de Cartão e como **"N"** quando os registros forem inseridos pela tela [Prospects](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612814-Prospects).

**Nota:** os demais campos desta tela são campos básicos.

---

![Imagem 6: Informações adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/16541919556759) **Informações adicionais**

- Propostas podem ser lançadas por usuários que sejam ou não B2B;
- Usuários B2B não conseguem excluir propostas e o status de propostas lançadas pelos mesmos não poderá ser alterado, sendo somente leitura. Neste caso, ao salvar a proposta o status ficará como **"Não avaliada"**.
- Se você não for um usuário B2B poderá **"deferir"** ou **"indeferir"** uma proposta. Para este o status não ficará somente no modo leitura, permitindo ao mesmo alterá-lo conforme desejar.
- Apenas usuários que não sejam B2B poderão converter o Prospect em Parceiros, e é por este motivo que somente para estes usuários o botão **"Outras opções"** será liberado na tela com a opção **"Converter prospect em parceiro"** (A conversão funciona da mesma forma que na tela de [Prospect](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612814) da Venda Consultiva).
- Apenas propostas que estejam com o status Deferida poderão ser convertidas de Prospects para Parceiro;
- Para Prospects que já foram convertidos para Parceiros não será permitida a alteração de nenhum campo (exceto pelo usuário SUP).

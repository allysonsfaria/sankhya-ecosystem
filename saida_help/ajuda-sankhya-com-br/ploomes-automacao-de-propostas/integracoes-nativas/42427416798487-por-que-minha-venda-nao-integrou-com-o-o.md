---
id: "42427416798487"
titulo: "Por que minha venda não integrou com o Omie?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427416798487-Por-que-minha-venda-n%C3%A3o-integrou-com-o-Omie"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:23Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5602899", "sync_hash_146a5e4ef370"]
---

# Por que minha venda não integrou com o Omie?

A integração de vendas entre o Ploomes e o Omie funciona de forma bilateral. Isso significa que uma venda criada no Ploomes será enviada para o Omie e que uma venda criada no Omie será criada no Ploomes.

Na maioria dos casos, uma venda não é integrada porque algum dado obrigatório não foi preenchido ou foi preenchido incorretamente. Para que uma venda seja enviada do Ploomes para o Omie, verifique se todos os requisitos abaixo foram atendidos:

- O Cliente existe no Omie, está ativo e integrado com o Ploomes\*.
- O Cliente possui **CPF** (se for pessoa) ou **CNPJ** (se for empresa) preenchido, caso essa obrigatoriedade esteja habilitada no Omie.

  ![Imagem 1: O Cliente possui CPF (se for pessoa) ou CNPJ (se for empresa) preenchido, caso essa obrigatoriedade esteja habilitada…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2470407314/a8bbe073ba4f8de8f7ef85840cf5/image.png?expires=1786536000&signature=b5b2a5506f68513fb1c88f667595050ef7b80324926fa0c7bd98db54f649fe2c&req=diQgFs1%2BmoJeXfMW3nq%2BgUzWDI%2FSSqQuJCGfWUk%2FCM8rXZVqKzluhmxLIMaM%0AwDCO1VQjPlEgrDVQJYF0DHpEh60%3D%0A)
- Os campos **Cidade** e **Estado** do Cliente estão preenchidos.
- O Produto existe no Omie, está ativo e integrado com o Ploomes\*.
- O Produto pertence à família **Produtos** ou **Serviços** no Ploomes.
- Os campos **[Produto da venda.Quantidade]** e **[Produto da venda.Valor unitário]** estão preenchidos.
- O campo **[Produto da venda.Desconto]** e/ou **[Produto.Desconto]** está preenchido e com valor igual ou superior a 0.
- Caso exista um Responsável na venda ou serviço, o Usuário está integrado ao Omie\* e possui o mesmo e-mail cadastrado para o vendedor do Omie.
- A Transportadora selecionada existe no Omie e está ativa.

**💡 Importante**

\* Para identificar se um cliente, produto ou usuário está integrado, verifique o campo **Id Omie**. Esse campo é preenchido automaticamente durante a integração e deve conter um ID válido ou o valor 0, quando aplicável.

O campo não pode conter uma string vazia ("").

Se todos os itens acima estiverem corretos e a venda continuar sem ser enviada para o Omie, entre em contato com o Suporte informando o **link da venda** para que possamos analisar o motivo.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).

---
id: "42427413400855"
titulo: "Checklist para integração de clientes no Omie"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427413400855-Checklist-para-integra%C3%A7%C3%A3o-de-clientes-no-Omie"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:00:53Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7984480", "sync_hash_4266e79079ac"]
---

# Checklist para integração de clientes no Omie

As entidades de Clientes/Fornecedor (Omie) e Contatos (Ploomes) estão sincronizadas simultaneamente com seus campos mais importantes.

## Mapeamento fixo de campos:

- Nome;
- Razão Social;
- Email;
- CNPJ;
- CPF;
- Telefone;
- Telefone 2;
- Fax;
- Website;
- Endereço;
- Complemento;
- Número;
- Bairro;
- CEP;
- Cidade;
- Estado;
- País;
- Tags (Omie) ⇔ Marcadores (Ploomes);
- Código CNAE;
- Vendedor Padrão (Omie) ⇔ Responsável (Ploomes);
- Inativo (Omie) => Status (Ploomes);

## Informações importantes para integração

- É possível colocar mais de um endereço no Omie, mas não no Ploomes (precisa criar novos campos). Então, por enquanto, o Ploomes conseguiria integrar apenas um endereço. O endereço integrado será o primeiro inserido no Omie.
- O Omie possui um limite de três telefones por cadastro, diferente do Ploomes que permite a inclusão de vários números em um só contato. Por isso, os números de telefones cadastrados no Ploomes são enviados para os seguintes campos do Omie: Telefone 1, Telefone 2 e Fax. Para o campo Fax ser preenchido no Omie, o Telefone tem que ser do tipo Fax no Ploomes. Se mais de três números de telefones forem cadastrados, apenas os três primeiros números serão enviados ao Omie.
- O Omie possui uma funcionalidade de ativar/inativar clientes cadastrados. Clientes inativados continuam na base mas não podem ser selecionados para vendas. As informações de ativo/inativo serão enviadas ao Ploomes como opções do campo de Status do cliente. No entanto, a edição do campo no Ploomes não afetará a ativação/inativação no Omie via API. Portanto, ao ativar a integração, é **recomendável bloquear o campo** status **da entidade Cliente no Ploomes** (por segurança, ele já força manter o valor).
- O campo responsável representa um usuário no Ploomes, e para integrar com o Omie, é preciso que haja um vendedor **com o mesmo e-mail** cadastrado no Omie.
- O Omie exige preenchimento dos campos Razão Social e também do Nome Fantasia e no Ploomes só é exigido o campo Nome. Caso a razão social não seja preenchida no Ploomes, é tomado o que foi digitado no campo Nome para maior flexibilidade ao usuário.

- O Ploomes não permite que um contato seja trocado de tipo pessoa física para jurídica (pessoa ou empresa) ou vice e versa, já o Omie sim. Por isso, trocar o tipo de pessoa no Omie não irá refletir no Ploomes.
- A validação de duplicidade é feita por meio do CPF/CNPJ ou pelo ID do Omie, caso o mesmo já esteja preenchido.
- Ao criar um cliente no Ploomes, se o campo "responsável" estiver preenchido e ele estiver inativo no Omie, o cliente não será criado no Omie. No entanto, o inverso ocorre: se o usuário estiver inativo no Ploomes e a criação for realizada no Omie com esse usuário, ele será criado no Ploomes sem erros.
- Ao cadastrar um cliente no Ploomes e atribuir um responsável (vendedor) que não está cadastrado no Omie, é importante destacar que a integração entre os dois sistemas não realiza a criação de usuários no Omie, portanto o campo ficará vazio. Isso ocorre também na criação entre Omie x Ploomes.
- **No Omie é** possível **configurar se o cadastro** exigirá **algum preenchimento, como o de CPF/CNPJ por exemplo**, caso o usuário tente criar sem esse preenchimento no Ploomes, o Omie irá criar um registro de interação informando o erro na inserção do cliente e não ocorrerá a integração até que a informação seja preenchida.

![Imagem 1: No Omie é possível configurar se o cadastro exigirá algum preenchimento, como o de CPF/CNPJ por exemplo , caso o…](https://downloads.intercomcdn.com/i/o/754495146/835854e3c7e328c1a022b5ca/image.png?expires=1786536000&signature=be89f596d811282b8c64747e60b7f70f220d2a180368acd4f751986338a90fa2&req=cyUjEsB7nIVZFb4V1XW4ga%2FrDMGQJH4GzsFDQ5nTNUUhMmLY0sgcNvoMjF%2Fi%0AJkNfRwQ1boQS%2Fie%2BfnD1IgUP3w%3D%3D%0A)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).

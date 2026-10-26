---
id: "44011071744791"
titulo: "Entendendo Campos Personalizados | Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011071744791-Entendendo-Campos-Personalizados-Sankhya"
trilha: "Flowbiz > Listas de Contatos"
atualizado_em: "2026-10-05T18:54:59Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_543", "sync_hash_649b5c722e4a"]
---

# Entendendo Campos Personalizados | Sankhya

Após concluir a integração entre a **Flowbiz** e a **Sankhya**, você poderá importar seus contatos em listas e configurar campos personalizados para iniciar envios de e-mail e WhatsApp.

**Mapeamento de campos**

Por padrão, alguns campos já são automaticamente mapeados. No entanto, a Sankhya possui diversos outros campos disponíveis que também podem ser utilizados conforme sua necessidade.

Você pode consultar todos os campos disponíveis na documentação oficial:
<http://swagger.sankhya.com.br/tabelas/TGFPAR.html>

**![Imagem 1: Como solicitar novos campos](https://ajuda.sankhya.com.br/hc/article_attachments/44011104351255)Como solicitar novos campos**

Caso deseje utilizar campos adicionais, será necessário informar quais devem ser mapeados para uso na Flowbiz. O envio deve seguir o seguinte padrão:

**Campo técnico na Sankhya = Nome do campo na lista da Flowbiz**

## Exemplo:

Se você precisar do código do parceiro:

- Nome técnico na Sankhya: `CODPARC`
- Nome desejado na Flowbiz: `Código do Parceiro` (ou qualquer outro nome que preferir)

**Importante:**

- O mapeamento é sempre feito com base no **nome técnico** do campo na Sankhya.
- Na Flowbiz, você pode nomear o campo da forma que fizer mais sentido para sua operação.

**Campos de tabelas relacionadas**
Além dos campos da **TGFPAR** (Parceiros), também é possível integrar informações armazenadas em outras tabelas do Sankhya.
**O simples fato de existir uma relação com a TGFPAR não garante que a informação possa ser integrada.**
Para que um campo de outra tabela possa ser utilizado, o relacionamento precisa estar **modelado na entidade de forma que seja possível identificar um único registro correspondente a cada parceiro**.
Ou seja, podem existir vários registros relacionados a um mesmo parceiro, desde que a integração tenha uma regra que permita determinar qual registro será utilizado.

**Como solicitar**
A equipe de **Implantação** realiza o levantamento das informações e registra a solicitação para o **Suporte**, que avalia a possibilidade de integração, realiza o mapeamento e cria o campo adicional quando aplicável.

Para a solicitação, informe:

- **Nome técnico do campo**;
- **Tabela de origem**;
- **Como a tabela se relaciona com a TGFPAR**.

A disponibilidade do campo será avaliada pelo Suporte conforme a estrutura do relacionamento e as possibilidades da integração.
Em caso de dúvidas, não hesite em nos acionar pelo chat da ferramenta.

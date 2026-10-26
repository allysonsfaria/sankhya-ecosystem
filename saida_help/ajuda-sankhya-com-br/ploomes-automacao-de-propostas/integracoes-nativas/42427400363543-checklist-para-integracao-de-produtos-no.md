---
id: "42427400363543"
titulo: "Checklist para integração de Produtos no Omie"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427400363543-Checklist-para-integra%C3%A7%C3%A3o-de-Produtos-no-Omie"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-11T16:14:57Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7984505", "sync_hash_3f2796abc870"]
---

# Checklist para integração de Produtos no Omie

Este artigo explica **quais são os requisitos e regras para que produtos e serviços do Omie integrem corretamente com o Ploomes**, incluindo limitações, mapeamento de campos e boas práticas para evitar erros na integração.

Diferente de outras entidades, **produtos e serviços seguem apenas o fluxo Omie → Ploomes**.

- Não é possível criar produtos no Ploomes e enviá-los para o Omie;
- Qualquer criação ou edição estrutural de produtos deve ser feita diretamente no Omie;
- O Ploomes apenas consome as informações enviadas pelo ERP.

## Famílias e grupos de produtos no Ploomes

Ao ativar a integração com o Omie, o Ploomes cria automaticamente duas famílias padrão:

- **Produtos**
- **Serviços**

Essas famílias são utilizadas para diferenciar, no Omie, **pedidos de venda** e **pedidos de serviço** gerados a partir do Ploomes.

Regras de alocação:

1. Produtos do Omie **sem família informada** são alocados no grupo **“Produtos”**, dentro da família **“Produtos”** no Ploomes;
2. Como o Omie não possui campo de família para serviços, todos os serviços são cadastrados no grupo **“Serviços”**, dentro da família **“Serviços”** no Ploomes.

![Imagem 1: Como o Omie não possui campo de família para serviços, todos os serviços são cadastrados no grupo “Serviços” , dentro…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1974852886/fcf3de42a5512146161446a4ab20/image.png?expires=1786536000&signature=d7354d77bf5f28c5256f2162ff9fbf15c2008168ddf5248cb80501942b981d06&req=dSkgEsF7n4lXX%2FMW3nq%2BgaODBRe9OyRsw21MGnuR2I3tKfMdupc7Z5auja4P%0ArfnkRXYDL3vGxvrZ0s%2BCoFl%2FsZs%3D%0A)

⚠️ **Atenção**: os produtos **devem obrigatoriamente pertencer às famílias “Produtos” ou “Serviços”** no Ploomes. A remoção ou alteração dessas famílias pode causar falhas na integração de vendas.

## Campos obrigatórios para criação de produtos no omie

Para um produto ser criado corretamente no Omie (e consequentemente integrado ao Ploomes), é obrigatório preencher:

- **Descrição**;
- **Unidade**;
- **Código NCM**;
- **Código do Produto** (gerado automaticamente pelo Omie).

## Mapeamento fixo de campos na integração

Os campos abaixo possuem **mapeamento fixo** na integração entre Omie e Ploomes.

**Produtos**

| **Omie** | **Ploomes** |
| --- | --- |
| Descrição | Nome |
| Código | Código |
| Unidade de Medida | Unidade de medida |
| Preço unitário | Valor unitário |
| Família | Grupo |
| Inativo | Marcadores |

**Serviços**

| **Omie** | **Ploomes** |
| --- | --- |
| Descrição | Nome |
| Código | Código |
| Preço unitário | Valor unitário |
| Inativo | Marcadores |

O campo **Marcadores** dos produtos no Ploomes segue o mesmo comportamento do campo de **status**, conforme descrito em:

[Checklist para integração de clientes no Omie](https://sankhya.zendesk.com/hc/pt-br/articles/42427413400855)

## Consulta de estoque no Ploomes

O estoque dos produtos integrados é exibido no Ploomes por meio de um **campo dinâmico de texto multilinha**, que armazena uma **tabela em HTML**.

### Regras de exibição

- A tabela respeita as permissões definidas no Omie;
- Apenas locais de estoque **habilitados para venda** são exibidos;
- Essa configuração é controlada no painel de **Locais de Estoque** do Omie.

![Imagem 2: Essa configuração é controlada no painel de Locais de Estoque do Omie.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1974894047/68fa93cd1a24d1b8738e8e415ec6/image.png?expires=1786536000&signature=6f79c1a7a3583397f6c4d2f1352ab5d22339bf7227c9d1aa926a5efb4edcd311&req=dSkgEsF3mYFbXvMW3nq%2BgZwNVqPvN9hRk9tPq5pDweE6XEgT0TpNloa6osf0%0Aqf3jdQ7kK3l07o149sNlp8VHAXI%3D%0A)

### Exemplo da tabela no Ploomes

![Imagem 3: Exemplo da tabela no Ploomes](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1974967705/d3c68f4a1a3aa52386fabea56242/image.png?expires=1786536000&signature=04b2a8ec49c0131bbe998f9929581a09dd116e3cf32724d201bf9d14fdad2dc9&req=dSkgEsB4moZfXPMW3nq%2Bgdf1xtIAwDWQt8Up5IPlIOJ64gS%2F3KZW7cO79MjX%0AE358%2FouD5pCaL78e8Ndm9zbRvpI%3D%0A)

### Informações exibidas na tabela

- Status do Estoque;
- Local de Estoque;
- Estoque Disponível;
- Estoque Mínimo;
- Previsão de Saída;
- Tipo de Local de Estoque;

### Atualização dos dados

A tabela é atualizada quando:

- Ocorre uma movimentação no estoque do produto;
  ou
- Um administrador clica manualmente em **Atualizar**, o que força a atualização de todos os produtos.

Ao final da tabela, é exibida a **data e hora da última atualização**, garantindo mais transparência.

## Limitação relacionada às imagens de produtos

Os links de imagens de produtos gerados pelo sistema Omie possuem um **prazo de validade de 7 dias**. Após esse período, o link expira automaticamente e a imagem deixa de ser exibida, sendo necessário renovar o link no Omie.

Esse comportamento é uma limitação do Omie e, por consequência, impacta a integração com o Ploomes, que apenas consome o link disponibilizado pelo ERP.

**Formas de contorno:**

- **Editar manualmente o produto no Omie**, salvando novamente o cadastro para renovar o link da imagem (solução temporária, válida por mais 7 dias);
- **Criar uma rotina semanal de [edição em lote de produtos no Omie](https://ajuda.omie.com.br/pt-BR/articles/5391514-atualizando-em-lote-as-fotos-do-seus-produtos)**, para renovação periódica dos links;
- **Hospedar as imagens em uma plataforma pública de armazenamento** (como Google Drive, por exemplo) e substituir, no Ploomes, o link da imagem pelo link público dessa plataforma (manualmente ou via importação);
- **Adicionar a imagem diretamente no Ploomes**, fazendo upload do arquivo pelo botão **“Selecionar”** no campo de imagem e, em seguida, **“Adicionar imagem”** (processo manual).

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).

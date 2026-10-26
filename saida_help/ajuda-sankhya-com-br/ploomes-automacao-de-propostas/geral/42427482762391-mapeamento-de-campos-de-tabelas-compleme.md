---
id: "42427482762391"
titulo: "Mapeamento de campos de tabelas complementares na Integração Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427482762391-Mapeamento-de-campos-de-tabelas-complementares-na-Integra%C3%A7%C3%A3o-Sankhya"
trilha: "PLOOMES: Automação de propostas  > Geral"
atualizado_em: "2026-08-10T18:02:34Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14367098", "sync_hash_4290fd5d3c82"]
---

# Mapeamento de campos de tabelas complementares na Integração Sankhya

## 1) Sobre o Mapeamento de campos de Tabelas Complementares na integração Sankhya

O **Mapeamento de campos de Tabelas Complementares** é um recurso da integração Sankhya que permite importar para o Ploomes dados de tabelas relacionadas à uma entidade principal integrada, sem que seja necessário criar campos com fórmulas na tabela principal do Sankhya.

No Sankhya, é comum que informações de um mesmo cadastro estejam distribuídas entre a tabela principal e tabelas auxiliares vinculadas a ela. Por exemplo, os dados de um Parceiro ficam na tabela principal (TGFPAR), mas informações complementares — como o endereço de entrega — ficam em uma tabela separada chamada Complemento de Parceiro (TGFCPL).

Com esse recurso, você pode mapear campos dessas tabelas complementares diretamente na configuração da integração, e esses dados serão importados automaticamente para o Ploomes junto com os dados da entidade principal quando o DTALTER do cadastro na entidade principal integrada for alterado.

Para que esse mapeamento seja possível, a tabela complementar precisa ter uma **ligação 1-1** (um para um) com a entidade principal. Isso significa que cada registro da entidade principal se relaciona com, no máximo, um registro na tabela complementar.

**Importante:** os campos de Tabelas Complementares funcionam exclusivamente na via de **importação** (Sankhya → Ploomes). Esses campos não são exportados do Ploomes para o Sankhya.

---

## 2) Pré-requisitos

- Possuir a **integração Sankhya V3** ativa na conta Ploomes.
- Ter a **via de importação ativa** na regra de negócio que deseja configurar.
- O **usuário da integração no Sankhya** deve possuir acesso às tabelas complementares que serão consultadas.

---

## 3) Configurando o Mapeamento de campos de Tabelas Complementares

## 3.1) Regras de negócio elegíveis

O mapeamento de campos de Tabelas Complementares está disponível para as seguintes regras de negócio da integração:

- **Parceiro Cliente PJ > Empresa**
- **Parceiro Cliente PF > Pessoa**
- **Contato de Cliente > Pessoa**
- **Produto > Produto**
- **Orçamento > Proposta**
- **ItemNota > Produto da Proposta**
- **Pedido de Venda e Nota de Venda > Venda**
- **ItemNota > Produto da Venda**

**Observação:** as regras de Grupo de Produto/Serviço e de Vendedor possuem mapeamento de campos fixo e não suporta o mapeamento de Tabelas Complementares.

## 3.2) Adicionando uma seção de mapeamento complementar

O mapeamento de Tabelas Complementares é configurado dentro da tela de configuração da integração Sankhya, na subseção de cada regra de negócio.

**Passo a passo:**

1. Acesse a tela de configuração da integração Sankhya no Ploomes.
2. Localize a regra de negócio desejada (ex: Parceiro Cliente PJ) e acesse sua configuração.
3. Com a via de importação ativa, localize a opção **Adicionar mapeamento complementar**.

![Imagem 1: Com a via de importação ativa, localize a opção Adicionar mapeamento complementar .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223961019/61e629b07c5e8dcb532df1c3ce69/IntegracaoSankhya-MapeamentoTabelaComplementar-AdcTabela.png?expires=1786536000&signature=2dcb7381aaa4875b7b941f334de8da16f24ee3866bd3736cf7783a97b4319828&req=diIlFcB4nIFeUPMW3nq%2Bgaf1kswNL5aUVHWsvX69x%2B%2BvRz%2B8%2FN7U1wUK4N60%0Al%2BpKKQ3otGqPh9aKFWvA9holAGc%3D%0A)

1. Ao acionar essa opção, a integração consultará o Sankhya e exibirá as tabelas complementares que possuem **ligação 1-1** com a entidade principal da regra.
2. Selecione a tabela complementar desejada.

![Imagem 2: Selecione a tabela complementar desejada.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223961749/e40c4e697689539aade2fb23fb24/IntegracaoSankhya-MapeamentoTabelaComplementar-AdcTabela2.png?expires=1786536000&signature=46a7c313265ae369e7d1235466c614fa03d4bb31f79dfadc77a13f23db402dc8&req=diIlFcB4nIZbUPMW3nq%2BgUESslV3EFsv%2FQiTGODUS2v4WNzIuPZAYgJmOiFY%0AZ5DU8F%2F3Ho3ohb6f48iMVJcCe%2FY%3D%0A)

**Caso a entidade não possua ligação 1-1 com nenhuma tabela complementar:** será exibida a mensagem "Essa entidade não possui ligação 1-1 com tabelas complementares no Sankhya", e nenhuma opção de mapeamento complementar estará disponível.

**Caso exista uma tabela complementar personalizada**, será possível realizar o mapeamento da entidade desde que o tipo de ligação com a entidade principal seja 1-1. Não é possível realizar mapeamento de campos de tabelas complementares que possuam ligação 1-N.

## 3.3) Mapeando campos da Tabela Complementar

Após selecionar a tabela complementar, será exibido o modal de mapeamento de campos para que você configure os pares de campos entre Sankhya e Ploomes.

**Passo a passo:**

1. No modal, selecione o **campo da tabela complementar do Sankhya** que deseja importar.
2. Em seguida, selecione o **campo correspondente no Ploomes** para receber o valor. Você pode utilizar:

   - Campos **nativos** do Ploomes (já existentes na plataforma).
   - Campos **customizados** previamente criados.
   - Campos criados na hora por meio da **criação rápida de campos**, disponível diretamente na interface de mapeamento.
3. Confirme o mapeamento e repita o processo para cada campo que deseja importar.

![Imagem 3: Confirme o mapeamento e repita o processo para cada campo que deseja importar.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2223963744/1d672c4aaa485afa6134b7746e76/IntegracaoSankhya-MapeamentoTabelaComplementar-AdcTabela3.png?expires=1786536000&signature=3401fd7258e30dc2518fc03dd7ba83d0968f934d41d339dba38b3581b2042c69&req=diIlFcB4noZbXfMW3nq%2BgZ0GXIlqZ3LPcEVUHLjKhBJewBic5E3GpS%2BbO%2F9e%0Ax00Ubxj4kSoXNtk69wAPjAy%2F7Dk%3D%0A)

### Tipos de campos suportados:

Os campos de Tabelas Complementares suportam os seguintes tipos: **inteiro**, **float** (decimal) e **string** (texto). Para campos que possuem opções pré-cadastradas no Sankhya, será importado apenas o código da opção em formato de texto.

Os campos de tabelas complementares mapeados como "opções pré-cadastradas" que sejam apenas lista de opções no Sankhya, também passam por recompatibilização de opções durante aplicação de edição da integração. Campos de tabelas complementares mapeados como "opções pré-cadastradas" que sejam entidades no Sankhya não passam por recompatibilização pela integração.

**Exemplo prático:** ao configurar a regra de Parceiro Cliente PJ, você pode adicionar a tabela complementar Complemento de Parceiro (TGFCPL) e mapear campos como endereço de entrega, bairro de entrega e CEP de entrega para campos correspondentes no Ploomes. Assim, sempre que um Parceiro for importado do Sankhya, esses dados complementares serão trazidos automaticamente.

---

## 4) Utilizando o Mapeamento de campos de Tabelas Complementares

## 4.1) Importação com campos de Tabelas Complementares

Com o mapeamento configurado, sempre que a integração importar dados do Sankhya para o Ploomes, os campos da entidade principal e os campos das Tabelas Complementares mapeadas serão trazidos em conjunto.

**Como funciona:**

1. Um cadastro da entidade integrada é criado ou editado no Sankhya.
2. Na próxima consulta periódica (pooling), a integração detecta a alteração na entidade principal.
3. A integração importa os dados da entidade principal para o Ploomes e também consulta as Tabelas Complementares mapeadas para trazer os campos configurados.
4. Os valores dos campos complementares são gravados nos campos correspondentes do Ploomes.

**Atenção:** os dados das Tabelas Complementares **só são atualizados no Ploomes quando a entidade principal sofre uma alteração no Sankhya**. Isso ocorre porque a integração utiliza a data de alteração (DTALTER) da entidade principal como referência para identificar registros modificados. Edições realizadas exclusivamente na tabela complementar, sem alteração na entidade principal, não serão detectadas pelo pooling.

## 4.2) Exportação com campos de Tabelas Complementares mapeados

Ao exportar dados do Ploomes para o Sankhya, apenas os valores dos **campos da entidade principal** são enviados. Os campos mapeados de Tabelas Complementares **não são exportados** e não geram nenhuma ação no Sankhya.

Isso significa que, se você editar no Ploomes o valor de um campo que foi mapeado a partir de uma tabela complementar, essa alteração não será refletida no Sankhya. **O fluxo de dados dos campos complementares é exclusivamente de importação.**

---

## 5) Limitações

- **Apenas ligação 1-1:** somente tabelas complementares que possuem ligação 1-1 (um para um) com a entidade principal podem ter seus campos mapeados. Tabelas com ligação 1-N (um para muitos) não são elegíveis.
- **Apenas importação:** os campos de Tabelas Complementares funcionam exclusivamente na via de importação (Sankhya → Ploomes). Não é possível exportar os dados desses campos do Ploomes para o Sankhya.
- **Tipos de campos limitados:** somente campos dos tipos inteiro, float (decimal) e string (texto) são suportados. Campos de apresentação de entidades relacionadas não estão disponíveis. Para campos de opções pré-cadastradas, apenas o código é importado em formato de texto.
- **Atualização depende da entidade principal:** os dados complementares só são atualizados no Ploomes quando o DTALTER da entidade principal é alterado no Sankhya. Edições feitas exclusivamente na tabela complementar não são detectadas automaticamente.
- **Entidades não suportadas:** a regra de Grupo de Produto/Serviço e de Vendedor mantém seu mapeamento de campos fixo e não permite o mapeamento de Tabelas Complementares.
- **Recomendação de performance:** embora não haja um limite rígido de tabelas complementares por regra, recomenda-se não exceder **3 tabelas complementares** por regra de negócio. Quanto mais tabelas complementares mapeadas, maior o tempo de consulta ao Sankhya durante o pooling, o que pode impactar diretamente a performance da importação.
- **Erros por deleção de campos ou remoção de vínculos:** se um campo mapeado for deletado no Sankhya ou se o vínculo entre as tabelas for removido, a integração será interrompida. O campo ou entidade afetada será destacado com alerta na tela de configuração, e os logs da integração informarão o problema ocorrido.
- **Alteração do tipo de ligação:** caso uma tabela complementar mapeada tenha seu tipo de ligação alterado de 1-1 para 1-N no Sankhya, o mapeamento dessa entidade será interrompido automaticamente.

---

## 6) F.A.Q.

**Posso exportar campos de Tabelas Complementares do Ploomes para o Sankhya?**

Não. Os campos de Tabelas Complementares funcionam exclusivamente na via de importação. Os dados são trazidos do Sankhya para o Ploomes, mas alterações feitas no Ploomes nesses campos não são enviadas de volta ao Sankhya.

**Por que os dados da tabela complementar não atualizaram no Ploomes?**

Os dados complementares só são importados quando a entidade principal sofre uma alteração no Sankhya. Se apenas a tabela complementar foi editada, sem nenhuma modificação na entidade principal, a integração não detectará a mudança. Para que os dados sejam atualizados, é necessário que o registro da entidade principal também seja alterado no Sankhya.

**O que acontece se um campo mapeado for deletado no Sankhya?**

A integração será interrompida. O campo deletado será destacado com um alerta na tela de configuração da integração, e os logs informarão qual regra de negócio foi afetada. Será necessário remover ou atualizar o mapeamento para que a integração volte a funcionar.

**Posso usar campos nativos do Ploomes no mapeamento?**

Sim. No lado do Ploomes, você pode utilizar campos nativos (já existentes na plataforma), campos customizados previamente criados ou criar novos campos diretamente pela interface de mapeamento através da criação rápida de campos.

**Quantas tabelas complementares posso mapear por regra de negócio?**

Não há um limite rígido, mas recomenda-se não exceder 3 tabelas complementares por regra. Cada tabela adicional aumenta o tempo de consulta ao Sankhya durante a importação, podendo impactar a performance.

**Por que não vejo nenhuma tabela complementar disponível para mapeamento?**

Isso pode ocorrer por dois motivos: a entidade principal da regra de negócio não possui ligação 1-1 com nenhuma tabela do Sankhya, ou o usuário da integração não possui permissão de acesso às tabelas complementares no Sankhya. No primeiro caso, será exibida a mensagem informando a ausência de ligação 1-1. No segundo caso, será exibido um alerta de erro de permissão.

**Campos de opções pré-cadastradas são importados corretamente?**

Para campos que possuem opções pré-cadastradas no Sankhya, a integração importa apenas o código da opção selecionada, em formato de texto. A descrição da opção não é importada.

---

## 7) Glossário

- **Tabela Complementar:** tabela do Sankhya que armazena dados adicionais relacionados a uma entidade principal. Exemplo: a tabela Complemento de Parceiro (TGFCPL) é complementar à tabela de Parceiros (TGFPAR).
- **Ligação 1-1 (um para um):** tipo de relação entre tabelas no qual cada registro da tabela principal corresponde a, no máximo, um registro na tabela complementar.
- **Ligação 1-N (um para muitos):** tipo de relação entre tabelas no qual um registro da tabela principal pode se relacionar com vários registros na tabela complementar. Esse tipo de ligação não é suportado pelo mapeamento complementar.
- **Mapeamento:** configuração que associa um campo do Sankhya a um campo do Ploomes, definindo como os dados devem ser sincronizados entre os dois sistemas.
- **DTALTER:** campo de data de alteração presente nas entidades do Sankhya, utilizado pela integração como referência para identificar registros que foram modificados.
- **Pooling:** processo periódico de consulta que a integração realiza no Sankhya para verificar se ocorreram novos eventos ou alterações.
- **Campo nativo:** campo que já existe por padrão no Ploomes, sem necessidade de criação manual.
- **Campo customizado:** campo criado manualmente pelo usuário no Ploomes para atender a necessidades específicas.
- **Campo de apresentação:** campo do Sankhya que exibe uma descrição legível de um valor de referência (ex: nome do parceiro em vez do código). Esse tipo de campo não é suportado pelo mapeamento complementar.
- **Rule (Regra de negócio):** configuração da integração que define o comportamento de sincronização para um tipo específico de entidade (ex: Parceiro Cliente PJ, Produto, Proposta, etc.).

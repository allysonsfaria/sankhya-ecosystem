---
id: "37880817786263"
titulo: "Analise de Impostos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880817786263-Analise-de-Impostos"
trilha: "Universidade Sankhya > Jornada da NFSe"
atualizado_em: "2026-07-22T14:06:25Z"
rotulos: ["Alíquotas", "Configuração", "Fiscal", "Impostos", "Financeiro", "NFS-e"]
---

# Analise de Impostos

## Impostos

O Cadastro de Impostos define como o PIS/COFINS/CSLL  será calculado, destacado e retido na NFS-e, além de onde isso ocorre (na nota ou no financeiro). Para serviços, a hierarquia **Empresa** → **TOP** → **Serviço** assegura base e alíquota corretas no XML/RPS. Uma configuração coerente evita rejeições e mantém a NFS-e aderente às regras municipais.

#### Siga as orientações para realizar a configuração no ERP Sankhya

1. Acesse a tela **Impostos**

**Menu:** Configurações » Cadastros »  Impostos

- Na porção superior da tela, clique em “**+**” (**Cadastrar Imposto**).
- Os campos ”**Nome**” e “**Descrição**” são para identificação do imposto cadastrado.
  Ex.: PIS RETIDO
- Informe o valor mínimo que determina o cálculo do imposto no campo “**Vlr. mínimo do Imposto**” .
  Ex.: 1,40
- Selecione no campo “**Tipo**” a opção **todos, EXCETO os com a coluna "calcular" DESMARCADA**.
- Marque a flag do campo “**Ativo**”.
- Selecione o imposto que está cadastrando no campo “**Tipo** **Imposto**”.
  Ex.: PIS
- Selecione a opção **Preço da Nota** no campo “**Usar para itens da nota**” para definir o valor do item a ser considerado para o cálculo do imposto.
- Selecione no campo “**Destaque** **do Imposto**” a opção **Proporcionaliza o imposto na baixa** para determinar como o sistema deve proceder o cálculo quando de uma baixa parcial de títulos.
- Salve o registro.

**Aba Serviço**
Esta aba ficará disponível quando a opção "**Calcular com base mensal?**" estiver **desmarcada**. Ela é utilizada para relacionar o imposto que está sendo cadastrado com determinados Serviços. Os serviços aqui inseridos terão o imposto nele vinculado, apresentado na tela “**Serviço**”, aba Outros Impostos.

- Nesta aba clique em “**+**” (**Cadastrar** **Outros Impostos**).
- Informe no campo indicado o **serviço** a ser vinculado ao imposto.
- Selecione a opção **Subtrair** no campo “**Na Nota**”.
- Preencha o percentual no campo "**Alíquota**", considerando o que foi definido pela Legislação para o cálculo do imposto.
  Ex.: 0,65
- No campo "**No Financeiro de Origem Estoque**" selecione a opção **Nenhum**.
- Salve o registro.

**Importante**

- As abas Parceiro, TOP e Empresa não precisam ser preenchidas.
- O parâmetro "Permite configuração alíquota por serviço/produto? - CFGALIQSERVPROD" deverá ser ligado, se as abas Parceiro, TOP ou Empresa não possuírem nenhuma informação configurada. Deste modo, o sistema conseguirá fazer o cálculo do imposto apenas para o Produto ou Serviço vinculados nas abas Produto, ou Serviço.

**Atenção**

Crie um cadastro para cada imposto, seguindo os dados da tabela abaixo

| **Nome/Descrição** | **Tipo Imposto** | **Valor mínimo do imposto** | **Alíquota - Aba Serviço** |
| --- | --- | --- | --- |
| PIS RETIDO | PIS | 1,40 | 0,65 |
| COFINS RETIDO | COFINS | 6,45 | 3 |
| CSLL RETIDO | CSLL | 2,15 | 1 |

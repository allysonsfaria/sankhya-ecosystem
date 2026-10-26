---
id: "42950762574359"
titulo: "Como criar um novo campo no Layout de Cabeçalho utilizando o Construtor de Telas do Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950762574359-Como-criar-um-novo-campo-no-Layout-de-Cabe%C3%A7alho-utilizando-o-Construtor-de-Telas-do-Sankhya"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T16:11:23Z"
rotulos: ["sync_hc", "vidya", "vidya_600094", "sync_hash_ef64b4d41f51"]
---

# Como criar um novo campo no Layout de Cabeçalho utilizando o Construtor de Telas do Sankhya

### Objetivo

Este artigo apresenta o procedimento para criação de um novo campo no **Layout de Cabeçalho** do Sankhya, utilizando o **Construtor de Telas**.

O procedimento é indicado para situações em que seja necessário disponibilizar uma nova informação no cabeçalho de uma tela, principalmente quando o campo precisa estar associado à estrutura de dados utilizada pela tela.

Como exemplo, o procedimento demonstrado utiliza a instância:

- **Tabela:** `TGFCAB`
- **Instância:** `CabecalhoNota`
- **Descrição:** `Nota/Pedido`

Durante o processo, é utilizado como exemplo o campo:

- **Nome do campo:** `CODJUSTIFICATIVA`
- **Descrição:** `Justificativa Bonificação`
- **Tipo de dados:** `Número Inteiro`
- **Tipo de apresentação:** `Padrão`

> **Importante:** os nomes apresentados acima são os utilizados no exemplo do vídeo. Para uma nova customização, os nomes, tipos e relacionamentos devem ser definidos de acordo com a regra de negócio.

---

### 1. Acessar o Construtor de Telas

No Sankhya, acesse a rotina:

**Construtor de Telas**

A tela possui, entre outras opções, os seguintes filtros:

- Nome da Tabela
- Nome da Instância
- Descrição da tela
- Categoria

O Construtor de Telas permite localizar uma determinada estrutura e realizar configurações sobre seus:

- Campos
- Ligações
- Ações
- Eventos

---

### 2. Localizar a estrutura do Cabeçalho

Para trabalhar com o cabeçalho de Nota/Pedido, localize a estrutura correspondente à tabela:

```
TGFCAB
```

E a instância:

```
CabecalhoNota
```

A estrutura apresentada no vídeo possui:

| Propriedade | Valor |
| --- | --- |
| Nome da Tabela | `TGFCAB` |
| Nome da Instância | `CabecalhoNota` |
| Descrição da Instância | `Nota/Pedido` |

Após localizar a estrutura, abra a aba **Campos**.

---

## 3. Acessar a aba Campos

Na estrutura do `CabecalhoNota`, selecione a aba:

**Campos**

Essa aba apresenta os campos atualmente disponíveis na estrutura.

Também são disponibilizadas ações para:

- Criar campo
- Editar campo
- Excluir campo
- Importar campo
- Configurar atributos
- Configurar proteção de dados

Para criar um novo campo, utilize o botão **Adicionar (+)**.

---

## 4. Criar o novo campo

Ao selecionar o botão **+**, o Sankhya apresenta a área de configuração do novo campo.

Os principais dados que devem ser informados são:

#### Nome do campo

Informe o nome técnico que será utilizado pelo sistema.

No exemplo apresentado no vídeo:

```
CODJUSTIFICATIVA
```

O nome deve seguir o padrão de nomenclatura adotado para os campos customizados da base.

> Recomenda-se definir previamente o nome do campo, considerando também a estrutura física do banco de dados e os padrões de customização utilizados no ambiente.

---

### 5. Informar a descrição do campo

No campo **Descrição do campo**, informe uma descrição amigável e clara para identificar a finalidade da informação.

No exemplo:

```
Justificativa Bonificação
```

A descrição é importante porque será utilizada para identificar o campo na interface do Sankhya e facilitar sua utilização pelos usuários e pela equipe técnica.

---

## 6. Definir o tipo de dados

O próximo campo obrigatório é:

**Tipo de dados**

No exemplo do vídeo, foi utilizado:

```
Número Inteiro
```

A escolha do tipo de dados deve considerar o conteúdo que será armazenado no campo.

Exemplos:

| Necessidade | Tipo recomendado |
| --- | --- |
| Código/ID numérico | Número Inteiro |
| Quantidade decimal | Número Decimal |
| Texto curto | Texto |
| Data | Data |
| Data e hora | Data/Hora |
| Informação booleana | Sim/Não |
| Código de registro relacionado | Número Inteiro |

> **Atenção:** quando o campo representar o código de um registro de outra tabela, normalmente ele será armazenado como um identificador numérico. Nesse cenário, além da criação do campo, pode ser necessária a configuração de uma **Ligação**.

---

## 7. Definir o tipo de apresentação

Após definir o tipo de dados, configure:

**Apresentação**

No exemplo apresentado:

```
Padrão
```

O Sankhya disponibiliza diferentes formas de apresentação, de acordo com o tipo de informação.

Entre as opções demonstradas no vídeo estão:

- Múltiplos arquivos
- Arquivo
- Checkbox
- Formatação HTML
- Imagem
- Caixa de Texto
- Padrão
- Lista de Opções

A escolha deve considerar como o usuário deverá informar ou visualizar o dado.

Por exemplo:

- Um texto livre pode utilizar **Caixa de Texto**.
- Uma informação com opções predefinidas pode utilizar **Lista de Opções**.
- Uma informação simples pode utilizar **Padrão**.

---

## 8. Configurações adicionais do campo

A tela de configuração também apresenta algumas opções adicionais.

### Permite pesquisa?

Determina se o campo poderá ser utilizado nos mecanismos de pesquisa/filtros relacionados à estrutura.

Deve ser habilitado somente quando fizer sentido disponibilizar esse campo para pesquisa.

---

### Visível no grid de pesquisa?

Define se o campo poderá aparecer no grid apresentado durante pesquisas.

Essa opção é útil quando o usuário precisa visualizar a informação diretamente nos resultados de pesquisa.

---

### Campo calculado

Indica que o valor do campo será obtido por meio de uma expressão, em vez de ser simplesmente armazenado como uma informação convencional.

Quando essa opção é utilizada, deve-se configurar também a **Expressão** correspondente.

> Para campos que armazenarão informações digitadas ou selecionadas pelo usuário, normalmente não se utiliza essa opção.

---

## 9. Configurar uma Ligação quando o campo possuir relacionamento

A criação de um campo e a criação de uma ligação são conceitos diferentes.

A **Ligação** deve ser utilizada quando o campo criado representa uma referência para outra estrutura/tabela e é necessário que o Sankhya consiga identificar o registro relacionado.

Por exemplo:

```
TGFCAB.CODPROD
        ↓
TGFPRO.CODPROD
```

Nesse cenário, o cabeçalho possui um código e esse código identifica um registro na tabela de produtos/serviços.

---

## 10. Acessar a aba Ligações

Na estrutura `CabecalhoNota`, acesse:

**Ligações**

A tela apresenta as ligações existentes na estrutura.

É possível visualizar informações como:

- Origem dos Dados
- Filtro de Ligação
- Adicional
- Nome Interno

Para criar uma nova ligação, utilize o botão **+**.

---

## 11. Selecionar o destino da ligação

Ao iniciar uma nova ligação, o Sankhya apresenta a janela:

**Criar Ligação**

Nessa etapa é necessário:

**Selecionar o destino da ligação.**

O destino corresponde à estrutura/tabela que será relacionada ao campo existente no cabeçalho.

No vídeo, é utilizado como exemplo a pesquisa por:

```
TGFPRO
```

A pesquisa retorna diversas instâncias relacionadas à tabela.

Entre elas aparece:

```
Serviço
```

A instância selecionada no exemplo é:

```
TGFPRO — Serviço
```

> Em uma implementação real, deve ser selecionada a tabela/instância que efetivamente corresponde ao relacionamento desejado.

---

## 12. Adicionar os campos da ligação

Após selecionar a estrutura de destino, o Sankhya apresenta a etapa:

**Adicionar os campos da ligação**

Nessa tela existem dois campos principais:

- **Campo nesta tabela**
- **Campo na tabela estrangeira**

O objetivo é informar qual campo da estrutura atual será relacionado a qual campo da estrutura estrangeira.

#### Exemplo demonstrado no vídeo

A estrutura selecionada possui:

```
Campo nesta tabela: Serviço
```

E o campo correspondente na estrutura estrangeira:

```
Campo na tabela estrangeira: Código
```

A relação fica conceitualmente:

```
Cabeçalho
   |
   | Serviço
   ↓
TGFPRO
   |
   | Código
```

Essa configuração permite que o Sankhya saiba como localizar o registro correspondente.

---

## 13. Validar o relacionamento entre os campos

Antes de concluir a ligação, confira se os dois campos representam realmente a mesma chave de relacionamento.

Por exemplo:

```
Campo local       = CODPROD
Campo estrangeiro = CODPROD
```

ou, dependendo da nomenclatura da instância:

```
Campo local       = Serviço
Campo estrangeiro = Código
```

O importante é que os campos utilizados na ligação possuam correspondência lógica e compatibilidade de dados.

> Não crie uma ligação apenas porque os campos possuem nomes semelhantes. É necessário validar a origem, finalidade e cardinalidade do relacionamento.

---

## 14. Utilizar a opção Importar Campo

O Construtor de Telas também disponibiliza a opção:

**Importar Campo**

Essa funcionalidade permite selecionar um campo proveniente de outra estrutura relacionada.

Ao selecionar **Importar Campo**, o Sankhya apresenta a janela:

**Importar Campo — Selecione a origem do campo**

Nessa etapa é possível pesquisar a origem do campo que será importado.

Essa funcionalidade é especialmente útil quando a informação que precisa ser disponibilizada no layout não pertence diretamente à tabela principal, mas está disponível em uma estrutura relacionada.

---

## 15. Diferença entre criar campo e importar campo

É importante diferenciar as duas operações.

#### Criar campo

Utilizado quando a estrutura precisa possuir um novo campo próprio.

Exemplo:

```
TGFCAB.CODJUSTIFICATIVA
```

#### Importar campo

Utilizado quando se deseja disponibilizar uma informação existente em outra estrutura relacionada.

Exemplo conceitual:

```
TGFCAB
   ↓
CODPROD
   ↓
TGFPRO
   ↓
DESCRPROD
```

Nesse cenário, uma informação da estrutura `TGFPRO` pode ser disponibilizada por meio da ligação, sem necessariamente criar uma nova coluna física para armazenar novamente a descrição do produto.

---

## 16. Exemplo utilizado no vídeo

Durante a demonstração, o campo criado na estrutura `CabecalhoNota` possui as seguintes características:

| Configuração | Valor |
| --- | --- |
| Tabela | `TGFCAB` |
| Instância | `CabecalhoNota` |
| Campo | `CODJUSTIFICATIVA` |
| Descrição | `Justificativa Bonificação` |
| Tipo de dados | `Número Inteiro` |
| Apresentação | `Padrão` |

A demonstração também passa pela configuração de ligações utilizando a estrutura de produtos/serviços.

O vídeo mostra, especificamente, a seleção da instância:

```
TGFPRO — Serviço
```

e o relacionamento com o campo:

```
Código
```

---

## 17. Cuidados antes de salvar

Antes de concluir a configuração, valide os seguintes pontos:

- O nome do campo está correto?
- O campo segue o padrão de nomenclatura adotado?
- O tipo de dados é compatível com a informação?
- A apresentação escolhida atende à necessidade?
- O campo precisa aparecer nas pesquisas?
- O campo precisa aparecer no grid?
- O campo é calculado?
- Existe relacionamento com outra tabela?
- Caso exista relacionamento, os campos utilizados na ligação estão corretos?
- A tabela estrangeira corresponde realmente à informação desejada?
- O usuário possui permissão para visualizar/editar o campo?

---

## 18. Validação após a criação

Depois de concluir a configuração no Construtor de Telas, recomenda-se realizar uma validação funcional.

#### Passo 1 — Acessar a tela relacionada

Abra a tela que utiliza a estrutura configurada.

No exemplo:

**Nota/Pedido**

#### Passo 2 — Abrir o cabeçalho

Acesse o cabeçalho do documento.

#### Passo 3 — Localizar o novo campo

Verifique se o campo configurado está disponível no local esperado.

#### Passo 4 — Testar preenchimento

Caso seja um campo editável, informe um valor válido.

#### Passo 5 — Salvar o documento

Salve o registro e confirme se não ocorreu erro.

#### Passo 6 — Reabrir o registro

Feche e reabra o documento para verificar se o valor foi efetivamente persistido.

#### Passo 7 — Validar o relacionamento

Caso exista uma ligação, confirme se o registro relacionado é apresentado corretamente.

---

## 19. Possíveis problemas

### Campo não aparece na tela

Verifique:

1. Se o campo foi criado na instância correta.
2. Se a tela utilizada realmente corresponde à instância configurada.
3. Se o campo está disponível na estrutura.
4. Se existem configurações de acesso/proteção de dados.
5. Se é necessário atualizar/recarregar a tela.

---

### Campo aparece, mas não permite preenchimento

Verifique:

- Permissões do usuário.
- Proteção de dados.
- Se o campo é calculado.
- Se existe alguma regra de negócio alterando o comportamento.
- Se o campo pertence à estrutura correta.

---

### Ligação não retorna registros

Verifique:

1. O campo local utilizado na ligação.
2. O campo da tabela estrangeira.
3. O tipo de dados dos campos.
4. Se o valor armazenado no campo local realmente existe na tabela estrangeira.
5. Se a instância selecionada é a correta.
6. Se existe algum filtro adicional configurado na ligação.

---

### O campo foi criado, mas não existe fisicamente no banco

A criação/configuração de um campo pelo Construtor de Telas não deve ser confundida com uma alteração SQL feita diretamente no banco.

Antes de realizar qualquer alteração estrutural, confirme o comportamento esperado no ambiente e os padrões adotados para customizações da base.

> Alterações estruturais em banco de dados devem ser realizadas somente por profissionais autorizados e seguindo o procedimento interno de implantação/migração.

---

## 20. Fluxo resumido

O processo pode ser representado da seguinte forma:

```
Construtor de Telas
        ↓
Localizar estrutura
        ↓
TGFCAB / CabeçalhoNota
        ↓
Aba Campos
        ↓
Adicionar (+)
        ↓
Informar nome do campo
        ↓
Informar descrição
        ↓
Definir tipo de dados
        ↓
Definir apresentação
        ↓
Configurar opções adicionais
        ↓
Salvar
        ↓
┌───────────────────────────────┐
│ O campo possui relacionamento?│
└───────────────┬───────────────┘
                │
        ┌───────┴───────┐
       NÃO             SIM
        │                │
        ↓                ↓
    Validar        Aba Ligações
    na tela             ↓
                   Criar Ligação
                        ↓
                 Selecionar destino
                        ↓
                  Mapear campos
                        ↓
                     Salvar
                        ↓
                    Validar
```

---

## 21. Boas práticas

#### Utilize nomes técnicos consistentes

Prefira nomes que identifiquem claramente a finalidade do campo.

Exemplo:

```
CODJUSTIFICATIVA
```

em vez de nomes genéricos como:

```
CAMPO1
TESTE
NOVOCAMPO
```

#### Utilize descrições claras

A descrição deve permitir que outro analista compreenda a finalidade do campo sem precisar consultar o desenvolvedor responsável pela criação.

#### Evite campos duplicados

Antes de criar um novo campo, pesquise se a informação já existe em alguma estrutura do Sankhya.

#### Valide a origem da informação

Se o campo representar um código de outra entidade, identifique primeiro:

- Tabela de origem.
- Campo chave.
- Instância utilizada.
- Descrição apresentada ao usuário.

#### Teste em ambiente adequado

Sempre que possível, realize a configuração inicialmente em ambiente de homologação/testes antes de disponibilizá-la no ambiente produtivo.

---

## 22. Resumo

Para criar um novo campo no cabeçalho utilizando o Construtor de Telas:

1. Acesse o **Construtor de Telas**.
2. Localize a estrutura desejada.
3. Para o exemplo do vídeo, utilize `TGFCAB / CabecalhoNota`.
4. Acesse a aba **Campos**.
5. Clique em **Adicionar (+)**.
6. Informe o **Nome do campo**.
7. Informe a **Descrição do campo**.
8. Defina o **Tipo de dados**.
9. Defina o **Tipo de apresentação**.
10. Configure as opções adicionais quando necessário.
11. Caso exista relacionamento com outra tabela, acesse **Ligações**.
12. Crie a ligação e selecione a estrutura de destino.
13. Faça o mapeamento entre o campo local e o campo da tabela estrangeira.
14. Utilize **Importar Campo** quando a necessidade for disponibilizar uma informação proveniente de uma estrutura relacionada.
15. Salve as alterações.
16. Acesse a tela funcional e valide o comportamento do novo campo.

> **Exemplo do vídeo:** `TGFCAB / CabecalhoNota` → campo `CODJUSTIFICATIVA` → descrição `Justificativa Bonificação` → tipo `Número Inteiro` → apresentação `Padrão`.

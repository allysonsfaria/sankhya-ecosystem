---
id: "4403124794775"
titulo: "Política de Consumo das Licenças [Cliente]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403124794775-Pol%C3%ADtica-de-Consumo-das-Licen%C3%A7as-Cliente"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-10-02T12:35:22Z"
rotulos: ["Configuração", "Grupos", "Licenças", "Módulos", "Financeiro", "Entendendo a Política de Consumo de Licenças [Cliente]", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# Política de Consumo das Licenças [Cliente]

### Consumo da Licença

O sistema de licenças do Sankhya funciona com o conceito de grupos. Em um mesmo contrato podem existir diversos grupos.

Cada grupo possui pelo menos 3 características:

a) Nome do grupo (geralmente A, B, C, …)

b) Qtd. de licenças concomitantes para aquele grupo

c) Tipo do grupo (FIT ou FULL)

d) Lista de módulos participantes daquele grupo. Cada grupo pode possuir 1 ou mais módulos

Isso significa que o controle de licenças não é exatamente por módulo, mas sim por grupos. O mais comum é que cada grupo possua um conjunto distinto de módulos e que esses módulos não participem de outros grupos, assim:

| **Nome** | **Tipo** | **Módulos** | **Qtd. licenças concomitantes** |
| --- | --- | --- | --- |
| A | Full | Comercial, Financeiro | 50 |
| B | Full | Contabilidade, Fiscal | 5 |
| C | Full | Folha | 10 |
| D | Fit | Pedido Web | 100 |

Tabela 1- Grupos de licença

O consumo de licença é sempre por grupo, como nesse exemplo considerando a tabela acima:

Cada linha consome 1 licença do módulo destacado:

| **#** | **Nome** | **Operação** | **Tela/Módulo** | **Grupo** | **Licenças disponíveis** |
| --- | --- | --- | --- | --- | --- |
| 1 | José | Abre | Financeiro | A | 49 |
| 2 | Maria | Abre | Financeiro | A | 48 |
| 3 | João | Abre | Contabilidade | B | 4 |
| 4 | José | Abre | Comercial | A | 48 |
| 5 | Silvia | Abre | Pedido Web | D | 99 |
| 6 | Silvia | Abre | Financeiro | A | 47 |
| 7 | José | Fecha | Comercial | A | 47 |

Tabela 2- Grupos de consumo da licença

**Notas importantes:**

Exemplos baseados nas tabelas 1 e 2.

Na linha #4, o usuário José abre uma tela do módulo Comercial e como o mesmo já possui uma licença do grupo A (por conta da abertura da linha #1) a quantidade de licenças disponíveis desse grupo permanece inalterada.

A usuária Silvia está consumindo 2 licenças, uma do grupo D e uma do grupo A, pois ela abriu telas de módulos desses grupos.

Na linha #7, o usuário José fecha a tela do comercial que estava usando e a qtd. de licenças disponíveis permanece inalterada, pois ele ainda está usando o Financeiro, portanto a licença continua com ele.
Observa-se, portanto, que o sistema obtém a licença quando o usuário abre a primeira tela de qualquer um dos módulos presentes no grupo e devolve quando não existem mais telas em aberto de qualquer um desses módulos.

O mesmo módulo pode estar em mais de um grupo e nesse caso os grupos precisam ser de tipos distintos (um Fit e outro Full).

Esse tipo de configuração atende casos em que existe uma alta concentração de usuários operacionais em um ou mais módulos, mas que o backoffice também precisa abrir telas desses módulos para consultas ou fechamentos sem atrapalhar ou ocupar as licenças operacionais.

Outro exemplo, dessa vez com grupo Fit compartilhando módulo(s) com grupo Full:

| **Nome** | **Tipo** | **Módulos** | **Qtd. licenças concomitantes** |
| --- | --- | --- | --- |
| A | Full | Comercial, Financeiro | 10 |
| B | Fit | Financeiro | 30 |

Tabela 3 - Grupo FULLl e FIT

Cada linha consome 1 licença do módulo destacado:

| **#** | **Usuário** | **Operação** | **Tela/Módulo** | **Grupo** | **Licenças disponíveis** |
| --- | --- | --- | --- | --- | --- |
| 1 | José | Abre | Financeiro | B | 29 |
| 2 | Maria | Abre | Financeiro | B | 28 |
| 3 | João | Abre | Comercial | A | 9 |
| 4 | José | Abre | Comercial | A | 8 |
| 5 | Silvia | Abre | Comercial | A | 7 |
| 6 | José | Fecha | Comercial | A | 8 |
| 7 | João | Abre | Financeiro | A | 8 |

Tabela 4- Consumo da licença grupo FULL e FIT

Exemplos baseados nas tabelas 3 e 4.

Nas linhas #1 e #2, os usuários José e Maria abriram telas do módulo Financeiro. Por padrão, o sistema tenta sempre obter licença Fit para qualquer módulo e nesse caso o módulo Financeiro participa de um grupo Fit, portanto as licenças são obtidas do grupo B.

Caso o sistema não consiga licença em grupo Fit e aquele módulo esteja presente em outro grupo, o sistema vai tentar obter a licença nesse outro grupo.

Na linha #3 o usuário João abre primeiramente uma tela do módulo Comercial, nesse caso, como não há Comercial em grupo Fit, o sistema obtém uma licença do grupo A, que é do tipo Full

Na linha #4, o usuário José abre uma tela do módulo Comercial. Nesse momento o usuário fica com duas licenças em uso, uma do grupo A e outra do grupo B, pois a licença que ele já tinha (grupo B) não possui o módulo Comercial.

Na linha #6 o usuário José fecha a última tela do módulo Comercial e assim o sistema devolve a licença do grupo A, ao qual pertence o módulo, ficando agora com apenas 1 licença do grupo B.

No exemplo acima, considerando a operação da linha #6, caso o usuário José fechasse as telas do módulo Financeiro ao invés do Comercial, o sistema iria devolver a licença do grupo B, que é Fit, e mais tarde, caso o usuário abrisse novamente alguma tela do Financeiro, o sistema não pegaria outra licença, pois José já possui uma licença do grupo A e esse grupo também possui o módulo Financeiro, conforme imagem 1.

![Imagem 1: Exemplos baseados nas tabelas 3 e 4.](https://ajuda.sankhya.com.br/hc/article_attachments/4421252316951)

### Acompanhamento do consumo da licença

Via Sankhya OM na tela Administração do Servidor, aba: **"Licença"**, na guia de **"Grupo"**, é possível identificar como estão dispostas as licenças, quantidade de licenças adquiridas e quantidade de licença em uso, exemplo na imagem 2.

![Política](https://ajuda.sankhya.com.br/hc/article_attachments/15635099106455)

Mas caso o parceiro tenha necessidade de mais detalhes assim como gerir os usos das licenças, será necessário acessar a tela Gestão de Licenças**.**

Para mais detalhes acessar os links abaixo:

- [**Gestão de Licenças**](https://ajuda.sankhya.com.br/hc/pt-br/articles/22864139891223-Gest%C3%A3o-de-Licen%C3%A7as)

[**- Administração do Servidor**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor)
[**- Monitoramento e Gestão da licenças**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615973-Quantidade-de-licen%C3%A7as-esgotado-para-Como-resolver-)

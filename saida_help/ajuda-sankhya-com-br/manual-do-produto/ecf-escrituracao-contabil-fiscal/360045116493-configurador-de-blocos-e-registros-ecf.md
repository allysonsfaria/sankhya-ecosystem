---
id: "360045116493"
titulo: "Configurador de Blocos e Registros - ECF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116493-Configurador-de-Blocos-e-Registros-ECF"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > ECF (Escrituração Contábil Fiscal)"
atualizado_em: "2026-09-15T17:33:12Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Blocos", "ECF", "Registros", "Contabilidade", "Configurador", "br.com.sankhya.contab.configuradorblocosregistros", "Configurador de Blocos e Registros - ECF manual", "Configuração Flexível do ECF"]
---

# Configurador de Blocos e Registros - ECF

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42314992078615) Módulo: Contabilidade > Conexão > ECF > Configuração P/ ECF
```

---

O objetivo desta tela é permitir a configuração dos Blocos e seus respectivos Registros que serão utilizados no ECF.

Ao dar início a um cadastro, defina o "Bloco" que será configurado bem como seu **"Registro"** correspondente. O campo **"Código"** se refere à codificação da Tabela Dinâmica a ser considerada no cadastro. Essas três informações são de preenchimento obrigatório.

Além das configurações acima, a tela possui:

| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116493-Configurador-de-Blocos-e-Registros-ECF#abageral) | [Aba Contas p/ Configurador de Blocos e Registros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116493-Configurador-de-Blocos-e-Registros-ECF#abacontasp/configuradordeblocoseregistros) |
| --- | --- |

![Imagem 2: Aba Contas p/ Configurador de Blocos e Registros](https://ajuda.sankhya.com.br/hc/article_attachments/360102141814)

## Aba Geral

Nessa aba, efetue as configurações globais do cadastro.

O campo **"Tipo de Dados"** é de extrema importância nessa configuração; ele pode ser definido de acordo com as seguintes opções:

- **P - Plano de Contas:** Essa opção faz com que a aba Contas p/ Configurador de Blocos e Registros seja habilitada para preenchimento, onde você informa o Cód. Reduzido da Conta Contábil.
- **V - Valor:** Por esta opção, o campo Valor (também presente na aba Geral), será habilitado para preenchimento.
- **S - Comando sql:** Através dessa opção, o campo SQL será habilitado para você configurar uma instrução SQL que está restrita à algumas condições. Além disso, serão aceitos apenas os parâmetros CODEMP, DTINI e DTFIM. O resultado da consulta deve trazer apenas uma coluna do tipo numérico.
- **A - Arquivo texto:** Essa opção faz com que o campo **"Arquivo"** seja habilitado para escolha de um arquivo.

A marcação **"Ativo"** determinará se a configuração em questão está ou não apta para ser utilizada.

Ao efetuar a marcação **"Permite gerar registro com valor zerado?"**, os registros gerados poderão assumir valores nulos, ou seja, zerados.

**Observação:** Caso o Bloco V esteja selecionado para ser gerado, o sistema realizará a geração dos registros de abertura e fechamento, além de totalizar as linhas no bloco 9900 no arquivo. Abaixo, trouxemos um exemplo de geração do registro:

|V010|INSTITUICAO|DE|EUR|

|9900|V001|1|||

|9900|V159|140|||

Os registros **"N030"**, **"N500"**, **"N620"**, **"N650"** e **"N660"** poderão ser gerados nessa tela, após a configuração na tela [Preferências da Empresa (Contabilidade)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114).

Você também poderá pesquisar as tabelas desses registros por meio do campo Código no painel principal dessa tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116493-Configurador-de-Blocos-e-Registros-ECF#top)

## Aba Contas p/ Configurador de Blocos e Registros

Essa aba é destinada a especificar as Contas Contábeis para configuração dos Blocos e Registros e será habilitada para preenchimento apenas se o campo Tipo de Dados presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116493-Configurador-de-Blocos-e-Registros-ECF#abageral) estiver definido com a opção **"P - Plano de contas"**.

![Imagem 3: Essa aba é destinada a especificar as Contas Contábeis para configuração dos Blocos e Registros e será habilitada para…](https://ajuda.sankhya.com.br/hc/article_attachments/360102141874)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116493-Configurador-de-Blocos-e-Registros-ECF#top)

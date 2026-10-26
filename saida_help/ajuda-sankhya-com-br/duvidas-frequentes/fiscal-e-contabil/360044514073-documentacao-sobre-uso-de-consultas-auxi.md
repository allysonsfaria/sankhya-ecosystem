---
id: "360044514073"
titulo: "Documentação sobre uso de Consultas Auxiliares na Fórmula de Contabilização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044514073-Documenta%C3%A7%C3%A3o-sobre-uso-de-Consultas-Auxiliares-na-F%C3%B3rmula-de-Contabiliza%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:56:06Z"
rotulos: ["#criadoRoger", "#revisadojunior", "Configuração", "Fórmulas", "Impostos", "TOP", "Contabilização", "Financeiro", "Nova Funcionalidade SQL", "Utilização de Consultas", "Configuração de Arquivos"]
---

# Documentação sobre uso de Consultas Auxiliares na Fórmula de Contabilização

**(1)** Foi criada uma forma nova de executar as fórmulas na contabilização. O usuário poderá criar arquivos de querys (.sql) e colocar no **Repositório de arquivos** no seguinte caminho:

```
Sistema/ctbz/consultas.
```

Todos esses arquivos de querys serão carregados no início de execução da contabilização.

**(1)** Para facilitar o entendimento segue os exemplos da utilização de duas formas diferentes:

**Exemplo 1:**

CONSULTA('impostos.sql', 'VLRDESDOB')

Neste primeiro exemplo o usuário passará os seguintes parâmetros:

![Imagem 1: Nome do arquivo (.sql) salvo no repositório de arquivos para o campo "Consultas Auxiliares" ;](https://ajuda.sankhya.com.br/hc/article_attachments/16831223761047)  Nome do arquivo (.sql) salvo no repositório de arquivos para o campo **"Consultas Auxiliares"**;

![Imagem 2: Dentro da aba "Configurações p/ Lançamentos Contábeis" no campo "Fórmula" na tela TOP Contabilização , a consulta ao…](https://ajuda.sankhya.com.br/hc/article_attachments/28929621133719)
![Imagem 3: Dentro da aba "Configurações p/ Lançamentos Contábeis" no campo "Fórmula" na tela TOP Contabilização , a consulta ao…](https://ajuda.sankhya.com.br/hc/article_attachments/16831223761687)  Dentro da aba **"Configurações p/ Lançamentos Contábeis"** no campo **"Fórmula"** na tela [TOP Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o), a consulta ao sql fica no seguinte formato: CONSULTA('impostos.sql', 'VLRDESDOB'), onde impostos.sql é o nome do arquivo .sql e VLRDESDOB é o nome do campo que desejamos buscar para usar na Fórmula.

Dessa forma, o arquivo (.sql) deve possuir o seguinte formato:

```
SELECT SUM(NVL(VLRDESDOB,0)) AS VLRDESDOB
FROM CTBZCARTOES
WHERE NUNOTA= :CHAVE
```

![Imagem 4: Dessa forma, o arquivo (.sql) deve possuir o seguinte formato:](https://ajuda.sankhya.com.br/hc/article_attachments/28929596968855)

**Exemplo 2:** 

CONSULTA('impostos.sql', 'VLRDESDOB', 123456)

No segundo exemplo o usuário passa a usar os seguintes parâmetros:
![Imagem 5: No segundo exemplo o usuário passa a usar os seguintes parâmetros: Nome do arquivo (.sql) salvo no repositório de…](https://ajuda.sankhya.com.br/hc/article_attachments/16831223761047)  Nome do arquivo (.sql) salvo no repositório de arquivos para o parâmetro Consultas Auxiliares;

![Imagem 6: Dentro da aba Configurações p/ Lançamentos Contábeis no campo Fórmula , a consulta ao sql fica no seguinte formato:…](https://ajuda.sankhya.com.br/hc/article_attachments/28929621133719)
![Imagem 7: Dentro da aba Configurações p/ Lançamentos Contábeis no campo Fórmula , a consulta ao sql fica no seguinte formato:…](https://ajuda.sankhya.com.br/hc/article_attachments/16831223761687)  Dentro da aba Configurações p/ Lançamentos Contábeis no campo Fórmula, a consulta ao sql fica no seguinte formato: CONSULTA('impostos.sql', 'VLRDESDOB'', 123456), onde impostos.sql é o nome do arquivo .sql e VLRDESDOB é o nome do campo que desejamos buscar para usar na Fórmula e 123456 é o CODCTACTB;
![Imagem 8: Dentro da aba Configurações p/ Lançamentos Contábeis no campo Fórmula , a consulta ao sql fica no seguinte formato:…](https://ajuda.sankhya.com.br/hc/article_attachments/16831223762583) Nome da chave auxiliar (#CHAVEAUX) dentro do arquivo .sql.

O arquivo (.sql) deve possuir o seguinte formato:

```
/*#CHAVEAUX: CODCTACTB*/
SELECT CODCTACTB
, SUM(NVL(VLRDESDOB,0)) AS VLRDESDOB
FROM CTBZCARTOES
WHERE NUNOTA= :CHAVE
GROUP BY CODCTACTB
```

![Imagem 9: O arquivo (.sql) deve possuir o seguinte formato:](https://ajuda.sankhya.com.br/hc/article_attachments/28929596976919)

**![Imagem 10: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/28928973486103) Informações adicionais:**

CTBZCARTOES é o nome de uma VIEW na base do cliente. No exemplo 1 o usuário deseja buscar apenas o valor do campo **"VLRDESDOB"** para o resultado da query. Já no exemplo 2 o usuário deseja buscar o valor do campo VLRDESDOB para a CODCTACTB igual a 123456

- As querys deverão ter apenas o parâmetro: Chave que será preenchido durante a contabilização.

**Por exemplo:**

- Contabilização de **Nota**: CHAVE = NUNOTA
- Contabilização de **Financeiro**: CHAVE = NUFIN
- Contabilização de **Baixa**: CHAVE = NUFIN, etc.

Essas novas funções serão utilizadas nas seguintes contabilizações: lançamentos de Nota, lançamentos de Financeiro, lançamentos de Baixa e lançamentos de Redução Z.

- Criamos o campo "**Consultas Auxiliares**" no cadastro da TOP. Neste campo o usuário irá informar quais arquivos aquela TOP usará na contabilização. O usuário deverá separar o nome dos arquivos por ','.
  Exemplo: queryImposto.sql, queryImpostoPis.sql, queryImpostoCofins.sql

Este campo estará visível apenas na tela [Top Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174), no caminho: Contabilização » Arquivos » TOP Contabilização.

![Imagem 11: Este campo estará visível apenas na tela Top Contabilização , no caminho: Contabilização » Arquivos » TOP…](https://ajuda.sankhya.com.br/hc/article_attachments/14661795977879)

 'Contabilização » Arquivos » TOP Contabilização'

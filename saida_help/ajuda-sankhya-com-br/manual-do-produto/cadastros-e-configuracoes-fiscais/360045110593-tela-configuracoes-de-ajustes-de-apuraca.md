---
id: "360045110593"
titulo: "Tela Configurações de Ajustes de Apuração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Cadastros e Configurações Fiscais"
atualizado_em: "2026-09-23T16:32:12Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Livros Fiscais", "ICMS", "Impostos", "EFD", "br.com.sankhya.mgeliv.cad.configajustesapuracao", "Configurações de Ajustes de Apuração manual", "ICMS ajustes: Evita erros manuais", "Aba filtros: Configurar documentos", "Apuração automática: FECP Rio", "Ajustes de Apuração"]
---

# Tela Configurações de Ajustes de Apuração

**Módulo:** Livros Fiscais › Arquivos

**Caminho de acesso:** Menu Principal › Livros Fiscais › Arquivos › Configurações de Ajustes de Apuração

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#oque)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#antes)
- [Como usar a tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#comousar)
- [Aba Ajustes de Documentos - EFD Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#docefd)
- [Aba Ajustes de Apuração ICMS/ICMS ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#apuracao)
- [Aba Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#filtros)
- [Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#botoes)
- [Executando a rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#executando)
- [Apuração automática do FECP (Rio de Janeiro)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#fecp)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#atencao)

## O que é e para que serve

A **Tela Configurações de Ajustes de Apuração** melhora a forma de inserção dos ajustes de ICMS vinculados a itens de nota no Livro Fiscal, evitando o retrabalho e reduzindo os erros causados pelo lançamento de ajustes manuais. A partir das configurações definidas aqui, o sistema popula automaticamente os ajustes usados na geração dos registros de documento e de apuração do SPED Fiscal. A tela **não** gera o arquivo da EFD nem o Livro Fiscal — a geração é feita na tela [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953); aqui você apenas configura os ajustes que serão aplicados.

![Imagem 1: A Tela Configurações de Ajustes de Apuração melhora a forma de inserção dos ajustes de ICMS vinculados a itens de nota…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007622082)

---

## Antes de começar

Antes de configurar os ajustes, crie as observações que serão vinculadas aos campos **Observação** e **Observação Padrão** na tela [Observações para Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173). Os códigos de ajuste seguem a lista disponibilizada pela UF (SPED).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#sumario)

---

## Como usar a tela

No Painel Principal, defina o tipo de configuração e a origem dos ajustes antes de preencher as abas:

- **Tipo de Configuração** — define o tipo do ajuste, com as opções **1 - Ajustes de Documento** e **2 - Ajustes de Apuração de ICMS/ICMS ST**.

#### Origem do Ajuste

**O que faz:** determina de onde os documentos que receberão o ajuste serão buscados.

**Como funciona:** na opção **Nota**, o sistema busca primeiro pela data de negociação e, depois, pela data de entrada/saída. Na opção **Financeiro**, busca os financeiros conforme os filtros definidos.

**Configurações relacionadas:** quando a origem é **Financeiro**, as fórmulas devem conter apenas campos das tabelas `TGFFIN` e `TGFTOP` (FIN e TOP).

#### Utiliza doc. relacionado de outra referência

**O que faz:** quando marcada, o sistema busca documentos fora do período de geração que estejam relacionados a documentos dentro do período.

**Quando usar:** a marcação só pode ser habilitada quando o campo **Tipo de Configuração** estiver como **2 - Ajustes de Apuração de ICMS/ICMS ST**.

**ℹ️ Nota**

Se você inserir duas configurações com o campo **Tipo de Configuração** igual a **1 - Ajustes de Documento** e com o mesmo número de nota e sequência, o sistema informa que já foi realizada uma configuração com o Tipo 1.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#sumario)

---

## Aba Ajustes de Documentos - EFD Fiscal

Informe nesta aba os dados que serão empregados na aba **EFD C195/C197/C595/C597 - D195/D197** do Cadastro Livro ICMS/IPI para a geração dos registros de ajuste de documento.

![Imagem 2: Informe nesta aba os dados que serão empregados na aba EFD C195/C197/C595/C597 - D195/D197 do Cadastro Livro ICMS/IPI…](https://ajuda.sankhya.com.br/hc/article_attachments/13642249260823)

### Campos

- **Observação** — vincule a observação previamente criada na tela **Observações para Notas**.
- **Código Ajuste** — o código de ajuste a ser utilizado, localizado na lista de códigos disponibilizados pela UF (SPED).
- **Indicador de Sub-Apuração** — indica se o ajuste pertence ou não a uma sub-apuração e qual o seu tipo.
- **Sub-Apuração** — marcação que complementa o **Indicador de Sub-Apuração**.
- **Compl. Obs. Padrão** — campo para inserir informações além da observação padrão, caso necessário.
- **Agrupar por Documento Fiscal** — quando marcada, os registros são agrupados por documento fiscal na geração do `C197`, desconsiderando o código do produto no agrupamento.
- **Fórmula Base de ICMS** — fórmula cujo resultado preenche o campo **Base do ICMS** no ajuste.
- **Fórmula Alíquota de ICMS** — fórmula cujo resultado preenche o campo **Alíquota do ICMS** no ajuste.
- **Fórmula Valor ICMS** — fórmula cujo resultado preenche o campo **Vlr. do ICMS** no ajuste.
- **Fórmula Valor Outros** — fórmula cujo resultado preenche o campo **Vlr. de outros** no ajuste.

Os campos de fórmula desta aba aceitam as tabelas `TGFITTE`, `TGFPRO`, `TSIEMP`, `TGFTOP`, `TGFDIN` (dados de ICMS, ICMS ST e IPI), `TGFADST` e `TGFIDST` (Apuração de Divergências de ICMS-ST).

### Registros gerados

| **Registro** | **Descrição** |
| --- | --- |
| `C195` | Complemento do Registro Analítico - Observações do Lançamento Fiscal (códigos 01, 1B, 04 e 55). |
| `C197` | Outras Obrigações Tributárias, Ajustes e Informações provenientes de Documento Fiscal. |
| `C855` | Observações do lançamento fiscal (código 59). |
| `C857` | Outras obrigações tributárias, ajustes e informações de valores provenientes de documento fiscal. |
| `C895` | Observações do lançamento fiscal (código 59). |
| `C897` | Outras obrigações tributárias, ajustes e informações de valores provenientes de documento fiscal. |
| `D195` | Observações do lançamento (códigos 07, 08, 8B, 09, 10, 11, 26, 27, 57 e 67). |
| `D197` | Outras obrigações tributárias, ajustes e informações de valores provenientes do documento fiscal. |

**ℹ️ Nota**

Em versões anteriores à 4.17, esta aba se chama **Ajustes de Documentos (EFD C195/C197 - D195/D197)**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#sumario)

---

## Aba Ajustes de Apuração ICMS/ICMS ST

As informações inseridas nesta aba populam a tela [Ajuste da Apuração de ICMS e ICMS ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116153).

![Imagem 3: As informações inseridas nesta aba populam a tela Ajuste da Apuração de ICMS e ICMS ST .](https://ajuda.sankhya.com.br/hc/article_attachments/13642375290007)

### Campos

- **Tipo Ajuste** — informe os últimos 4 dígitos do código do ajuste.
- **Código Ajuste** — atende à legislação do estado de Pernambuco (PE) em relação ao Sintegra; deve ser preenchido conforme as regras dos campos 05 e 06 do **Registro Tipo 88 - Subtipo 77 - Detalhe 00**.
- **UF** — define a Unidade da Federação do destinatário da NF-e a ser buscada. Em branco, todas as notas vêm conforme os filtros dos demais campos.
- **Número Processo** — número do processo quando o ajuste tem origem em processo. Até 2022 permite até 15 caracteres; a partir de 2023, até 60 caracteres.
- **Origem Processo** — preenchido quando existe processo relacionado, com as opções **Sefaz**, **Justiça Federal**, **Justiça Estadual** e **Outros**.
- **Observação Padrão** — vínculo com a observação criada previamente na tela **Observações para Notas**.
- **Tipo Imposto** — o imposto vinculado ao ajuste: **0 - ICMS** ou **1 - ICMS ST**.
- **Indicador de Sub-Apuração** — preenchido quando o ajuste faz parte do registro `1923` da EFD ICMS/IPI.
- **Registro do Ajuste na DIME SC** — permite gerar estornos de crédito nos itens **60 - Outros Estornos de Crédito** e **65 - Estorno de Crédito da Entrada em Decorrência da Utilização de Crédito Presumido**. Ao selecionar uma opção, o sistema soma os valores do campo **Valor do Ajuste** e apresenta a soma no item 60 ou 65 do quadro 25 da DIME SC.
- **Agrupar registros em um único ajuste?** — permite gerar um único ajuste para várias notas ou um ajuste para cada nota.
- **Observação** — campo para incluir informações além da Observação Padrão.
- **Descrição do Processo** — inserida quando o ajuste está vinculado a um processo.
- **Fórmula Valor Ajuste** — fórmula cujo resultado preenche o campo **Valor do Ajuste**.

#### Tipo Apuração

**O que faz:** define a natureza do ajuste e influencia a formação do código, pois cada opção representa o quarto dígito do código. Opções: **0 - Outros débitos**, **1 - Estorno de créditos**, **2 - Outros créditos**, **3 - Estorno de débitos**, **4 - Deduções do imposto apurado** e **5 - Débito especial**.

**Impacto no sistema:** no SPED Fiscal, os ajustes com quarta posição **5** aparecem nos registros `E111` e `E220`; o valor é totalizado no campo **Débitos Especiais** do registro `E110` e no campo `DEB_ESP_ST` do registro `E210`.

#### Inserir Ajuste Por

**O que faz:** possibilita gerar um único ajuste para a nota inteira ou vincular um ajuste para cada item, com as opções **Item**, **Nota** e **Referência**.

**Como funciona:** se optar por **Nota** e informar o campo **Produto** na aba Filtros, o filtro por produto não tem efeito, pois o agrupamento passa a ser somente por nota. Para filtrar por produto, selecione a opção **Item**.

**Configurações relacionadas:** as tabelas aceitas nas fórmulas variam conforme a opção. Em **Item**: `TGFITTE`, `TGFPRO`, `TSIEMP`, `TGFTOP` e `TGFDIN` (ICMS, ICMS ST e IPI). Em **Nota**: `TGFCAB`, `TSIEMP`, `TGFTOP` e os campos `VLRSUBSTANT`, `BASESUBSTITANT`, `VLRICMSANT`, `BASESTANT`, `BASESTFCPINTANT` e `VLRSTFCPINTANT`.

![Imagem 4: Configurações relacionadas: as tabelas aceitas nas fórmulas variam conforme a opção. Em Item : TGFITTE , TGFPRO ,…](https://ajuda.sankhya.com.br/hc/article_attachments/13642416568087)
![Imagem 5: Configurações relacionadas: as tabelas aceitas nas fórmulas variam conforme a opção. Em Item : TGFITTE , TGFPRO ,…](https://ajuda.sankhya.com.br/hc/article_attachments/13642475471511)

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#sumario)

---

## Aba Filtros

Defina nesta aba os filtros pertinentes à busca dos documentos que serão vinculados aos ajustes. Caso as variáveis pré-estabelecidas não atendam à necessidade, é possível criar um **filtro personalizado** por meio de uma consulta em comandos SQL, para especificar melhor quais documentos devem ser vinculados ao ajuste.

![Imagem 6: Defina nesta aba os filtros pertinentes à busca dos documentos que serão vinculados aos ajustes. Caso as variáveis…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007795401)

**ℹ️ Nota**

Para conhecer os detalhes das opções do campo **Tributação**, acesse o artigo [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110693), aba Geral.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#sumario)

---

## Botões da tela

- **Validar Filtros/Fórmulas** — localizado na parte superior da tela, valida os filtros avançados e as fórmulas criadas, garantindo que tudo está estruturalmente de acordo com as regras aceitas pela rotina. Ao acionar, exibe um pop-up de mesmo nome com os campos obrigatórios **Empresa** e **Período**. Se a validação não for realizada, o campo **Status** fica como **Pendente** e a regra não é executada na geração do livro.

  ![Imagem 7: Validar Filtros/Fórmulas — localizado na parte superior da tela, valida os filtros avançados e as fórmulas criadas,…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007626002)

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#sumario)

---

## Executando a rotina

Para que o ajuste seja efetuado, gere o livro na tela [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953). Após a execução, verifique se as informações foram populadas nas telas **Cadastro Livro ICMS/IPI** (aba EFD C195/C197/C595/C597 - D195/D197) e **Ajuste da Apuração de ICMS e ICMS ST**.

**⚠️ Atenção**

Quando se tratar de **Notas de Transferência**, configure os ajustes na ordem correta para que as informações apareçam nos registros C195/C197 e D195/D197 do SPED Fiscal: primeiro realize, nesta tela, o ajuste de saída por transferência da empresa que emite a nota e, em seguida, o ajuste de entrada para a empresa que recebe. Depois, na tela Geração ICMS/IPI, gere o Livro Fiscal de Saída da empresa emitente e só então o Livro Fiscal de Entrada da empresa que recebe.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#sumario)

---

## Apuração automática do FECP (Rio de Janeiro)

No estado do Rio de Janeiro, conforme a Resolução SEFAZ nº 987/2016, a apuração do FECP toma como referência a base de cálculo do ICMS e do ICMS ST. Para automatizar essa apuração:

1. No Painel Principal, selecione em **Tipo de Configuração** a opção **Ajustes de Apuração de ICMS/ICMS ST** e em **Origem do Ajuste** a opção **Nota**.
2. Na aba Ajustes de Apuração ICMS/ICMS ST, no campo **Tipo Apuração**, indique **Deduções do imposto apurado**.
3. No campo **Tipo Imposto**, indique **ICMS**.
4. Marque **Agrupar registros em um único ajuste?**.
5. Em **Inserir Ajuste Por**, selecione **Referência**.
6. Informe a **Fórmula Valor Ajuste** conforme abaixo.

```
CASE WHEN ((CASE WHEN ITE.CODCFO =5000 AND ITE.CODCFO<6000 0="0" then="THEN" else="ELSE" -="-" when="WHEN">=1000 AND ITE.CODCFO<2000 0="0" then="THEN" else="ELSE"><> 0 THEN ((CASE WHEN ITE.CODCFO =5000 AND ITE.CODCFO<6000 0="0" then="THEN" else="ELSE" -="-" when="WHEN">=1000 AND ITE.CODCFO<2000 0="0" then="THEN" else="ELSE" end="END">
```

Após criar o registro, valide a fórmula pelo botão **Validar Filtros/Fórmulas** para que o campo **Status** passe de **Pendente** para **Liberado**. Em seguida, realize a Geração ICMS/IPI e verifique a geração do ajuste na tela Ajuste da Apuração de ICMS e ICMS ST.

**⚠️ Atenção**

Com **Inserir Ajuste Por** na opção **Referência**, não é possível usar em conjunto o campo **Origem do Ajuste** igual a **Financeiro** nem a marcação **Utiliza doc. relacionado de outra referência**. Se usados em conjunto, o sistema exibe "Inserir Ajuste Por 'Referência' não pode ser marcado em conjunto com a origem igual a 'Financeiro'" ou "Inserir Ajuste Por 'Referência' não pode ser marcado em conjunto 'Utiliza doc. relacionado de outra referência:' igual a 'Sim'".

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593-Tela-Configura%C3%A7%C3%B5es-de-Ajustes-de-Apura%C3%A7%C3%A3o#sumario)

---

## Pontos de atenção

- A marcação **Utiliza doc. relacionado de outra referência** só é habilitada quando o **Tipo de Configuração** é **2 - Ajustes de Apuração de ICMS/ICMS ST**.
- Com **Origem do Ajuste** igual a **Financeiro**, as fórmulas aceitam apenas as tabelas `TGFFIN` e `TGFTOP`.
- As tabelas aceitas nas fórmulas da aba Ajustes de Apuração mudam conforme o **Inserir Ajuste Por** (Item ou Nota).
- Ajustes com quarta posição **5** no código caem nos registros `E111`/`E220` e totalizam em `E110` (Débitos Especiais) e `E210` (`DEB_ESP_ST`).
- Enquanto o campo **Status** estiver como **Pendente**, a regra não é executada na geração do livro — valide sempre pelo botão **Validar Filtros/Fórmulas**.

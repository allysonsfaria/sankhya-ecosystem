---
id: "23459567355543"
titulo: "Cadastro de Benefícios -  cBenef Código de  Benefício Fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/23459567355543-Cadastro-de-Benef%C3%ADcios-cBenef-C%C3%B3digo-de-Benef%C3%ADcio-Fiscal"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:48:17Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "NF-e", "Impostos", "Documentos Eletrônicos"]
---

# Cadastro de Benefícios -  cBenef Código de  Benefício Fiscal

Esse artigo trata-se das principais configurações, melhores práticas e soluções relacionadas ao cBenef - Código de Benefícios Fiscal. É um campo utilizado na Nota Fiscal eletrônica (NF-e) e na Nota Fiscal de Consumidor eletrônica (NFC-e), **para indicar que há incentivos fiscais em uma determinada operação**, como carga tributária menor por determinado período ou diminuição, e até isenção de alguns impostos.

O cadastro do benefício deve estar 100% igual a nota, se houver qualquer divergência entre o cadastro do benefício e o cadastros que se encontram na nota, então o benefício pode não ser levado. 

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/23459567349527)SOLUÇÃO:**

![Imagem 2: Acesse a tela Preferências da Empresa (Comercial » Preferências » Empresa)](https://ajuda.sankhya.com.br/hc/article_attachments/23938232629911) Acesse a tela **Preferências da Empresa** (Comercial » Preferências » Empresa)

●Aba **"Documentos Eletrônicos",** sub-aba **"NF-e/NFC-e",** sub-aba **"NF-e"** a opção: **“Considerar benefícios ao alterar item da nota?”**: deve estar **ligada**

● Aba Documentos Eletrônicos, sub-aba NF-e/NFC-e, sub-aba Geral: campo **"Ambiente NF-e/NFC-e"** **não pode** estar preenchido com a opção **"Não usa"**.

![Imagem 3: Acesse a tela Tipo de Operação - TOP (Comercial > Arquivo > Cadastros >Tipo de Operação - TOP)](https://ajuda.sankhya.com.br/hc/article_attachments/23938249046679) Acesse a tela **Tipo de Operação - TOP** (Comercial > Arquivo > Cadastros >Tipo de Operação - TOP)

● Aba **"NF-e/NFC-e/CF-e",** campo **"NF-e"**: deve estar selecionado com as seguintes opções: **Normal, Complementar, Ajuste e Devolução**
● Aba NF-e/NFC-e/CF-e, campo **"Modelo do Documento"**: deve estar selecionado com as seguintes opções: **55-Nota Fiscal Eletrônica ou 65-Nota Fiscal Eletrônica de Venda a Consumidor**
● Aba **"Impressão",** campo **“Base de Numeração”** deve estar preenchido com as opções: **Venda ou Devolução de Venda.**

![Imagem 4: Acesse a tela " Cadastro Benefícios" ( Livros Fiscais » Arquivos » Cadastro Benefícios)](https://ajuda.sankhya.com.br/hc/article_attachments/29423448147479) Acesse a tela **"Cadastro Benefícios"** (Livros Fiscais » Arquivos » Cadastro Benefícios)

Existem 3 principais campos iniciais que são **prioritários** sobre os demais:
    **1. Código da Empresa;**
    **2. Finalidade da Operação;**
    **3. UF do Destinatário;**

Caso esses 3 campos estejam preenchidos de forma igual para mais de um cadastro de benefício então o sistema partirá para validação dos demais campos da tela, sendo eles;

● **Classificação de ICMS:** O sistema não permite o lançamento de uma nota onde o Cadastro da TOP e o Cadastro do Parceiro estejam com o campo "Classificação ICMS" um apontando para o outro.

● **Simples Nacional:** Se o Parceiro for **optante pelo Simples Nacional**, o sistema grava essa informação e ela deve estar habilitada no Cadastro do Benefício para o sistema considerar o código criado;

● **Operação interestadual:** O sistema valida se a UF da empresa da nota, é diferente da UF do cadastro do parceiro da nota.

**Observação:** se o Parceiro for de um estado diferente da Empresa (operação interestadual) então no cadastro do benefício a marcação "Operação interestadual" **deve** estar ativada mesmo que no campo UF do Destinatário contenha a UF do estado do parceiro.

● **UF do Destinatário:** Sistema pega a UF do parceiro da nota (CODPARC);

● **Tributação:** O sistema armazena o CST do item da nota. Ou seja, se no Cadastro do Benefício for um CST e na nota houver um CST diferente, então o benefício **não será levado.**

● **Grupo de ICMS 1 e 2:** quando preenchido o sistema buscará produtos que tenham esse grupo em seu cadastro.

● **Levar benefício nulo para o XML da NF-e:** esse campo deve ser marcado quando marcado a tag no XML não deverá ter o código, mas o mesmo pode ser destacado na Central e no DANFE.

● **Filtro Personalizado:** é utilizado quando nenhum dos campos da tela atende ao processo da empresa. Esse campo deve ser usado com cautela, pois a criação de um filtro pode afetar os demais cadastros. Também server para distinguir o benefício, onde pode-se colocar a condição para ser usado somente por  determinado Parceiro ou TOP e/ou não ser usado por Parceiro ou TOP.

#### Outros cadastros envolvidos que podem afetar no processamento do cBenef:

● Tela: **"Preferências da Empresa",** aba Documentos Eletrônicos, sub-aba NF-e/NFC-e sub-aba  NF-e, a opção: **“Atualização do cód. do benefício no faturamento pelo produto:”** deve ser ativada quando no pedido há um código de benefício e no momento do faturamento o benefício da nota será diferente do pedido.

● Tela: **"Produtos"**(Configurações » Cadastros » Produtos » Produtos), aba **"Impostos",** o campo **“Cód. Benefício Fiscal na UF”**deve estar preenchido nos produtos escolhidos. **Observação:**caso o código esteja menor que o tamanho padrão de caracteres, preencha com zeros a esquerda até o tamanho padrão.

● **Parâmetros:**

**UFPER8CTAGCBENE - UFs permitem o envio de 8 caracteres na tag cBenef:** Serão incluídas no campo "Texto", as UFs que devem preencher com 8 caracteres a tag

**ATUALFINFAT - Atualiza finalidade da operação no faturamento:** Afeta a finalidade da operação e pode afetar no processamento do cbenef.

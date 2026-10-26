---
id: "39374918377111"
titulo: "Como Cadastrar Alíquotas de IBS e CBS sem a Opção Empresa Zero"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39374918377111-Como-Cadastrar-Al%C3%ADquotas-de-IBS-e-CBS-sem-a-Op%C3%A7%C3%A3o-Empresa-Zero"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-14T20:04:55Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "Artigo criado KCS", "Alíquotas de CBS", "Alíquotas de IBS", "Fiscal/Contábil - KCS"]
---

# Como Cadastrar Alíquotas de IBS e CBS sem a Opção Empresa Zero

Durante o cadastro de alíquotas nas telas **“Alíquotas de IBS”** e **“Alíquotas de CBS”** (Livros Fiscais » Cadastros), alguns usuários identificaram que a opção **“Empresa 0”** não está disponível para seleção no campo **“Empresa do Cadastro”**, apesar de essa configuração ter sido apresentada em webinars e treinamentos oficiais.

Essa indisponibilidade pode gerar dúvidas sobre como realizar o cadastro de alíquotas que devem ser aplicadas de forma **genérica**, ou seja, sem vínculo com uma empresa específica.

### Solução para Cadastro Genérico de Alíquotas

Para realizar o cadastro de alíquotas de forma genérica, aplicável a todas as empresas do sistema, **não é necessário** selecionar a opção **"Empresa 0"**. O procedimento correto consiste em **deixar o campo "Empresa do Cadastro" em branco**, sem preencher nenhum valor.

Ao manter o campo vazio, o sistema interpreta que aquela configuração de alíquota deve ser aplicada de forma universal, sem restrição a uma empresa específica. Este comportamento substitui a necessidade de utilizar a **"Empresa 0"** e garante que a alíquota cadastrada seja válida para todas as empresas cadastradas no ERP.

### Quando Preencher o Campo Empresa

O campo **"Empresa do Cadastro"** deve ser preenchido apenas quando houver a necessidade de criar uma alíquota específica para uma determinada empresa. Neste caso, selecione a empresa desejada no campo, e a configuração será aplicada exclusivamente a ela.

Esta abordagem permite maior flexibilidade na gestão das alíquotas, possibilitando tanto configurações genéricas quanto específicas, conforme a necessidade de cada operação fiscal.

### Estrutura do Cadastro de Alíquotas

O cadastro de alíquotas de **IBS** e **CBS** está organizado em duas abas principais: **"Identificação"** e **"Tributação"**. Na aba **"Identificação"**, dentro da seção **"Dados da Empresa"**, encontra-se o campo **"Empresa do Cadastro"**, que pode ser deixado em branco para aplicação genérica ou preenchido com uma empresa específica.

Além do campo empresa, a aba **"Identificação"** também permite configurar outros parâmetros importantes, como **"Regime Tributário da Empresa"**, **"CNAE da Empresa"**, **"NCM do Produto"**, **"NBS do Serviço"**, **"UF Destino"**, **"Município de Destino"**, **"Finalidade da Operação"** e **"Tipo de Operação"**.

Já na aba **"Tributação"**, são configurados os dados tributários propriamente ditos, incluindo **"Código da Situação Tributária (CST)"**, **"Código de Classificação Tributária"**, alíquotas de referência, alíquotas efetivas, reduções, diferimentos e valores presumidos.

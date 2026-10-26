---
id: "26555446175639"
titulo: "Registro P100 do EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26555446175639-Registro-P100-do-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:41:30Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "CFOP", "EFD Contribuições", "Registro P100 do EFD Contribuições", "registros P100 ou P200", "P100"]
---

# Registro P100 do EFD Contribuições

Neste artigo serão apresentados os detalhes da geração do **registro P100 do EFD Contribuições**, e suas configurações.

#### **(1)** Conceito (Guia Prático)

Este registro tem o objetivo de identificar o estabelecimento da pessoa jurídica a que se referem as operações informadas neste bloco. **Só devem ser escriturados no Registro P010 os estabelecimentos que efetivamente tenham obtido receitas sujeitas à incidência da Contribuição Previdenciária sobre a Receita Bruta.** O estabelecimento que não realizou operações passíveis de registro nesse bloco, no período da escrituração, não deve ser identificado no Registro P010.
Para cada estabelecimento cadastrado em “P010”, deve ser informado nos registros de nível inferior (Registros Filho P100 e/ou P110) as informações necessárias para a apuração da Contribuição Previdenciária sobre Receitas.

#### **(1)** Dentro da aplicação, é possível subdividir o registro em três frentes:

**(2)** **Geração por meio de documentos da tela "Cadastro Livro ICMS/IPI" com origem:** Complemento, Estoque e Complemento;

(2)**Geração por meio de documentos presentes na tela "Cadastro Livro ISS"**;

(2)** Geração por meio de documentos da tela "Cadastro Livro ICMS/IPI", porém com o campo "Origem" igual a "Redução Z";**

**Observação:** independente da origem do documento, devem ser observadas as configurações apontadas no seguinte artigo: [Configurações iniciais do bloco P](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es#geraodoblocop)

Ainda é importante que, na tela **"Empresa"**(Caminho: Comercial » Preferências » Empresa), aba **"EFD - Escrituração Fiscal Digital",** posicionado na seção de **"EFD Contribuições",** o registro **"P010"** esteja marcado. Na mesma tela, também devem estar **marcados os registros P100 ou P200**.

#### **(1)** Detalhes das regras para cada frente

**(2)Geração por meio de documentos da tela "Cadastro Livro ICMS/IPI" com origem: Complemento, Estoque e Complemento:**

- Na tela Cadastro Livro ICMS/IPI, o campo **"Data de Movimento"** deve estar dentro do período de geração do TXT;
- O item do documento em questão, **não** pode ser um **serviço**, mas se for, o modelo do documento deve estar entre os seguintes: 7, 8, 9, 10, 11, 26, 27, 57, 67;
- No cadastro do CFOP levado ao livro fiscal, o campo **"Receita bruta p/EFD Contribuições"** deve estar diferente de **"Não afeta"**.

(2)**Geração por meio de documentos presentes na tela "Cadastro Livro ISS";**

- O campo Data do Movimento deve estar dentro do período de geração do TXT;
- O campo Origem deve estar como "Estoque";
- O item do documento em questão deve ser obrigatoriamente um serviço;

(2)**Geração por meio de documentos da tela "Cadastro Livro ICMS/IPI", porém com o campo "Origem" igual a "Redução Z";**

- Na tela Cadastro Livro ICMS/IPI, o campo Data de Movimento deve estar dentro do período de geração do TXT;
- O campo Origem deve estar como Redução Z;
- O item/produto do documento não pode ser um **serviço** e nem estar com o campo **"Usado Como"** igual a: Revenda (por fórmula) e Matéria-prima;
- No cadastro do CFOP levado ao livro fiscal, o campo Receita bruta p/EFD Contribuições deve estar diferente de Não afeta;
- A **"Data de Negociação"**, do cabeçalho do documento, deve ser igual à Data de Documento presente no livro fiscal.

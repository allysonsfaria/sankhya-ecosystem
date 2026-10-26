---
id: "31031737058839"
titulo: "Reoneração da folha: o que muda e como configurar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31031737058839-Reonera%C3%A7%C3%A3o-da-folha-o-que-muda-e-como-configurar"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Tributação da folha"
atualizado_em: "2026-09-27T14:22:46Z"
rotulos: ["Configuração", "Atualização", "Impostos", "eSocial", "Folha de Pagamento", "Registro Fiscal", "Reoneração da folha de pagamento", "alíquota da desoneração", "alíquota da CPP", "Desoneração da Folha", "Integralmente Substituída", "Parcialmente Substituída"]
---

# Reoneração da folha: o que muda e como configurar

Em **31 de dezembro de 2024**, foi implementada uma **atualização importante sobre as regras para a apuração da reoneração da folha de pagamento.**

A desoneração substitui a contribuição previdenciária patronal de 20% (CPP) sobre a folha de pagamento por uma alíquota menor, calculada com base na receita bruta da empresa.

**A partir de 2025, inicia-se uma fase de transição para a reoneração completa, que será concluída em 2028.** **Durante essa fase, as alíquotas serão compostas por duas partes:** **a alíquota da desoneração e a alíquota da CPP.**

As alíquotas serão ajustadas da seguinte forma:

- **2025**: 80% da desoneração e 25% da CPP
- **2026**: 60% da desoneração e 50% da CPP
- **2027**: 40% da desoneração e 75% da CPP
- **2028**: Fim da desoneração e CPP de 20%.

Para que o processo seja feito corretamente dentro do sistema, e que seja possível enviar as informações ao eSocial e gerar o resumo de folha corretamente, siga os passos abaixo para cada situação:

**![Imagem 1: Atenção: Para que o Resumo de Folha seja gerado corretamente, é necessário que o Módulo Pessoal esteja atualizado, na…](https://ajuda.sankhya.com.br/hc/article_attachments/31110959998871) Atenção:** Para que o Resumo de Folha seja gerado corretamente, é necessário que o Módulo Pessoal esteja atualizado, na versão **5.26.3** ou posterior.

### Folha Desonerada Integralmente

Na tela **Empresas** do Pessoal+ (Configurações > Cadastros > Pessoal > Empresas), verifique e ajuste os seguintes dados conforme a necessidade:

- Na aba **Informações Fiscais**, o campo **Indicativo Desoneração da folha** deve estar preenchido como **Empresa enquadrada nos critérios da legislação**.

![Imagem 2: Na aba Informações Fiscais , o campo Indicativo Desoneração da folha deve estar preenchido como Empresa enquadrada nos…](https://ajuda.sankhya.com.br/hc/article_attachments/31352244517143)

Na tela **Registro Fiscal** (Pessoal+ » Cadastros » Registro Fiscal), verifique e ajuste os seguintes dados conforme a necessidade:

- Na aba **Geral** o campo **Indicativo de substituição da Contribuição Previd. Patronal**precisa ser preenchido com a opção **1 - Integralmente Substituída**.

![Imagem 3: Na aba Geral o campo Indicativo de substituição da Contribuição Previd. Patronal precisa ser preenchido com a opção 1 -…](https://ajuda.sankhya.com.br/hc/article_attachments/31395562595607)

- Na aba **Desoneração da Folha**, o campo **Percentual da Receita Bruta para INSS** deve ser preenchido com **100%**, o sistema realiza automaticamente a verificação e aplicação da alíquota de reoneração conforme as regras vigentes.

![Imagem 4: Na aba Desoneração da Folha , o campo Percentual da Receita Bruta para INSS deve ser preenchido com 100% , o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/31395537643543)

### Folha Desonerada Parcialmente

Na tela Empresas do Pessoal+ (Configurações > Cadastros > Pessoal > Empresas), verifique e ajuste os seguintes dados conforme a necessidade:

- Na aba **Informações Fiscais**, o campo **Indicativo de substituição da Contribuição Previd. Patronal** deve estar preenchido como **Empresa enquadrada nos critérios da legislação**.

![Imagem 5: Na aba Informações Fiscais , o campo Indicativo de substituição da Contribuição Previd. Patronal deve estar preenchido…](https://ajuda.sankhya.com.br/hc/article_attachments/31352244517143)

Na tela **Registro Fiscal** (Pessoal+ » Cadastros » Registro Fiscal), verifique e ajuste os seguintes dados conforme a necessidade:

- Na aba **Geral** o campo **Indicativo de substituição da Contribuição Previd. Patronal**precisa ser preenchido com a opção **2 - Parcialmente Substituída**.

![Imagem 6: Na aba Geral o campo Indicativo de substituição da Contribuição Previd. Patronal precisa ser preenchido com a opção 2 -…](https://ajuda.sankhya.com.br/hc/article_attachments/31395537644183)

- Na aba **Desoneração da Folha**, o campo **Percentual da Receita Bruta para INSS** deve ser preenchido conforme a porcentagem desonerada. Por exemplo, se 60% da folha for desonerada, o campo Percentual da Receita Bruta para INSS deverá ser preenchido com esse valor.

![Imagem 7: Na aba Desoneração da Folha , o campo Percentual da Receita Bruta para INSS deve ser preenchido conforme a porcentagem…](https://ajuda.sankhya.com.br/hc/article_attachments/31111062976919)

**Exemplo de cálculo**:

A base de **R$ 100.000,00** será dividida em **60% de desoneração** e **40% de oneração**. Dessa forma, o valor da contribuição patronal será de **R$ 11.000,00**.

O cálculo é feito conforme abaixo:

![Imagem 8: O cálculo é feito conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/31031737057303)

(1)** Por que a base de INSS sobre o 13º salário não faz mais parte para o cálculo do patronal?**

Foi estabelecido um regime de transição para a Contribuição Previdenciária sobre a Receita Bruta (CPRB), previsto nos artigos 7º e 8º da Lei n.º 12.546/2011. Esse regime define o processo de desoneração e reoneração gradual da folha de pagamento até o ano de 2027.

**A desoneração sobre o 13º salário será de 100%, ou seja, a isenção será total sobre os valores referentes ao 13º salário.**

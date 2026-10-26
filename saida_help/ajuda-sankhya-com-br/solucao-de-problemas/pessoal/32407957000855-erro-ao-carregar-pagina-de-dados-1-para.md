---
id: "32407957000855"
titulo: "Erro ao carregar página de dados 1 para Funcionário. ORA-01722: número inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32407957000855-Erro-ao-carregar-p%C3%A1gina-de-dados-1-para-Funcion%C3%A1rio-ORA-01722-n%C3%BAmero-inv%C3%A1lido"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-03T13:18:21Z"
rotulos: ["Configuração Funcionários", "Tipo de Rescisão", "Cadastro", "Código de Afastamento", "Erro ao carregar página de dados 1 para Funcionário", "Configuração de Funcionários", "ORA-01722", "número inválido", "Pessoal+", "Erro"]
---

# Erro ao carregar página de dados 1 para Funcionário. ORA-01722: número inválido

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32552604842903) **MENSAGEM:**

Erro ao carregar página de dados 1 para Funcionário.

ORA-01722: número inválido

 

**SITUAÇÃO:**

Ao tentar acessar a tela de funcionários, é exibida a mensagem acima.

**SOLUÇÃO:**

Para corrigir o problema, siga os passos abaixo:

![Imagem 2: Na Tela "Código de Afastamento" (Pessoal+ » Cadastros » Código de Afastamento) , identifique o código de afastamento…](https://ajuda.sankhya.com.br/hc/article_attachments/32536336059543) Na Tela **"Código de Afastamento"** (Pessoal+ » Cadastros » Código de Afastamento), identifique o código de afastamento que contém letras no campo **CODAFAST**. 

![Imagem 3: Após a identificação, verifique se existe algum Tipo de Rescisão (Pessoal+ » Cadastros » Tipo de Rescisão) que utilizou…](https://ajuda.sankhya.com.br/hc/article_attachments/32536336061975)Após a identificação, verifique se existe algum **Tipo de Rescisão** (Pessoal+ » Cadastros » Tipo de Rescisão) que utilizou este código de letras, pois será necessário ajustar.

![Imagem 4: Após ajustar o tipo de rescisão, utilizando apenas o código numérico correto, exclua o código de afastamento que contém…](https://ajuda.sankhya.com.br/hc/article_attachments/32536297617815)Após ajustar o tipo de rescisão, utilizando apenas o código numérico correto, exclua o código de afastamento que contém letras.  

Feita a correção, o acesso à tela ''**Configuração de Funcionários''** será realizado sem a exibição de mensagens de erro.

**CAUSA:**

O erro está relacionado a tabela TFPAFA, na tela Código de Afastamento. 

O sistema tenta interpretar o conteúdo do campo **CODAFAST** como um valor numérico, porém foi identificado um valor inválido, com letras como. **Exemplo:S , J**. 

Essa mensagem indica que está sendo feita uma tentativa de conversão numérica na **TFPFUN** na tela Configuração Funcionários sobre um campo que contém **letras**, o que não é permitido, pois exige valores numéricos.

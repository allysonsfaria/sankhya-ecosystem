---
id: "16842127409047"
titulo: "Erro 303 - Não foi localizado o contrato de trabalho do trabalhador CPF: 'x' e Categoria: 'x'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16842127409047-Erro-303-N%C3%A3o-foi-localizado-o-contrato-de-trabalho-do-trabalhador-CPF-x-e-Categoria-x"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:17:56Z"
rotulos: ["Contrato", "eSocial", "Erro 303", "Configuração Funcionários", "Corrigir divergências em matrícula categoria ou CPF", "Contrato de trabalho não localizado", "Ajustar dados e reenviar eventos", "Erro", "Artigo atualizado KCS", "Sankhya RH - KCS", "Central de Projetos"]
---

# Erro 303 - Não foi localizado o contrato de trabalho do trabalhador CPF: 'x' e Categoria: 'x'

[303] Não foi localizado o contrato de trabalho do trabalhador CPF: 'X', Matrícula: 'X' e Categoria: Desconhecida.

[304] Não existe um contrato de trabalho para o CPF: 'X', Matrícula: 'X'  ou este encontra-se encerrado na data do evento.

### SITUAÇÃO

Ao tentar transmitir o evento **"S-2399"** (Trabalhador Sem Vínculo de Emprego/Estatutário - Término) para o eSocial, o sistema retorna os erros 303 e 304, indicando que não foi localizado um contrato de trabalho ativo para o trabalhador na data do evento.

### SOLUÇÃO

Para resolver este erro, verifique as seguintes situações:

**Situação 1: Evento S-2300 não enviado ao eSocial**

**(1)** Verifique se o evento **"S-2300"** (Trabalhador Sem Vínculo de Emprego/Estatutário - Início) foi enviado ao eSocial.

**(2)** Caso não tenha sido enviado, gere e transmita o evento **"S-2300"** antes de enviar o **"S-2399"**.

**(3)** Após a confirmação do envio do **"S-2300"**, gere e envie o evento **"S-2399"**.

**Situação 2: Evento S-2300 enviado ao eSocial**

**(1)** Verifique se o evento **"S-2300"** (Trabalhador Sem Vínculo de Emprego/Estatutário - Início) foi enviado ao eSocial e com qual matricula ele foi enviado.

**(2)**Confira se a matricula enviada é a mesma que consta no sistema nos campos Matricula e/ou Matrícula Alternativa na tela **Configuração Funcionários** (Configurações » Cadastros » Pessoal » Configuração Funcionários)

**(3)** Se estiver diferente é necessário ajustar o campo Matrícula Alternativa incluindo o matricula que consta no e-Social. 

**(4)** Faça uma geração geral e depois tente enviar novamente o evento.

### CAUSA

Os erros 303 e 304 ocorrem quando:

- O evento **"S-2300"** não foi enviado previamente ao eSocial, sendo necessário cadastrar o contrato de trabalho antes de encerrá-lo.
- O contrato de trabalho já se encontra **e-Social** com matricula diferente do sistema.

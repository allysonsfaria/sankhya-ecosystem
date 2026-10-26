---
id: "33712966580631"
titulo: "Erro 553 - Grupo \"Informações de desconto do empréstimo em folha' não deve ser preenchido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33712966580631-Erro-553-Grupo-Informa%C3%A7%C3%B5es-de-desconto-do-empr%C3%A9stimo-em-folha-n%C3%A3o-deve-ser-preenchido"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-18T19:54:52Z"
rotulos: ["Configuração", "eSocial", "Folha de Pagamento", "Erro 553", "Central do eSocial", "não deve ser preenchido", "Grupo \"Informações de desconto do empréstimo em folha\"", "Erro"]
---

# Erro 553 - Grupo "Informações de desconto do empréstimo em folha' não deve ser preenchido

**MENSAGEM**

Erro 553 - Grupo "Informações de desconto do empréstimo em folha" não deve ser preenchido.

**SITUAÇÃO**

Esta mensagem de erro é apresentada ao tentar realizar o envio do evento **S-1010** (Rubrica) pela **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial).

**SOLUÇÃO**

Para corrigir o problema, siga os passos abaixo:

**(1)** Acesse a **"Central do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e gere o evento **S-1010** para a rubrica **DESCONTO CRÉDITO TRABALHADOR**.

**(2)** Ao enviar o evento, desmarque a opção **"Utilizar a data de início padrão do sistema"**, conforme indicado na imagem abaixo.

![Imagem 1: (2) Ao enviar o evento, desmarque a opção "Utilizar a data de início padrão do sistema" , conforme indicado na imagem…](https://ajuda.sankhya.com.br/hc/article_attachments/33713144636695)

**(3)** Informe a referência **05/2025** no campo correspondente.

![Imagem 2: (3) Informe a referência 05/2025 no campo correspondente.](https://ajuda.sankhya.com.br/hc/article_attachments/33713144638615)

**(4)** Envie o evento com a data de validade **05/2025** para corrigir o problema.

**CAUSA**

O erro ocorre porque o início do envio da informação do **Crédito do Trabalhador** ao eSocial iniciou na referência **05/2025**, e o sistema precisa que esta rubrica seja enviada com a data de validade correspondente.

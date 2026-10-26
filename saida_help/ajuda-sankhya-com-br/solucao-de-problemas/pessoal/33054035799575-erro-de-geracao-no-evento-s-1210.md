---
id: "33054035799575"
titulo: "Erro de geração no evento S-1210"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33054035799575-Erro-de-gera%C3%A7%C3%A3o-no-evento-S-1210"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:20:06Z"
rotulos: ["Configuração", "eSocial", "Central do eSocial", "ORA:25134: Valor de dados fora da faixa", "Código ANS", "Erro de geração no evento S-1210", "Plano de Saúde", "Erro"]
---

# Erro de geração no evento S-1210

**MENSAGEM:**

 ORA:25134: Valor de dados fora da faixa.

**SITUAÇÃO:**

Ao realizar a geração no evento S-1210 na tela **''Central do eSocial''** (Pessoal+» Rotinas Folha» Central do eSocial) ocorre o erro ORA:25134: Valor de dados fora da faixa.

![Imagem 1: Ao realizar a geração no evento S-1210 na tela ''Central do eSocial'' (Pessoal+» Rotinas Folha» Central do eSocial)…](https://ajuda.sankhya.com.br/hc/article_attachments/33054035795479)

**CAUSA:**

**(1)**Código ANS Inválido no Cadastro de Plano de Saúde:

O erro ocorre na tela **“Plano de Saúde”** (Pessoal+ » Cadastros » Plano de Saúde), quando o campo **"Reg. Ag. Nac. Saúde"** é preenchido com um valor que ultrapassa 6 caracteres.

Conforme as normativas da Agência Nacional de Saúde Suplementar **(ANS)** e os requisitos técnicos do **eSocial**, esse campo deve conter **exatamente 6 dígitos numéricos**, correspondentes a um **código de operadora válido** e registrado na ANS.

O preenchimento com um código inválido ou fora do padrão estabelecido compromete a integridade das informações enviadas, podendo causar **rejeições nos eventos S-1210 do eSocial**. Isso impacta diretamente a regularidade das obrigações acessórias da empresa e pode gerar inconsistências nos registros transmitidos.

**SOLUÇÃO:**

Certifique-se de validar o código junto ao cadastro oficial da ANS antes de inseri-lo no sistema. Garanta também que o campo "Reg. Ag. Nac. Saúde" contenha apenas números e **tenha exatamente 6 dígitos**, conforme exigido pelo layout do eSocial.

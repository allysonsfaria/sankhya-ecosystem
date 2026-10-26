---
id: "36223230303767"
titulo: "IMOB_E00042 - Para usar projeto no lançamento de depreciação, é necessário informar um projeto no departamento do bem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36223230303767-IMOB-E00042-Para-usar-projeto-no-lan%C3%A7amento-de-deprecia%C3%A7%C3%A3o-%C3%A9-necess%C3%A1rio-informar-um-projeto-no-departamento-do-bem"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:23:24Z"
rotulos: ["Configuração", "Imobilizado", "Projeto", "Depreciação", "Geração de Lote de Depreciação", "Erro", "Lançamento de Depreciação", "Departamento do bem", "IMOB_E00042"]
---

# IMOB_E00042 - Para usar projeto no lançamento de depreciação, é necessário informar um projeto no departamento do bem

**MENSAGEM:**

[IMOB\_E00042] Para usar projeto no lançamento de depreciação, é necessário informar um projeto no departamento do bem.

**SOLUÇÃO:**

**(1)** Acesse a tela [**''Departamentos'**'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610254-Departamentos) (Pessoal+ » Recrutamento e Seleção » Cadastros) vinculado ao bem.

**(2)** No campo **''Projeto''** informe o projeto correto para o processamento da rotina.

![Imagem 1: (2) No campo ''Projeto'' informe o projeto correto para o processamento da rotina.](https://ajuda.sankhya.com.br/hc/article_attachments/36335241559447)![Imagem 2: (2) No campo ''Projeto'' informe o projeto correto para o processamento da rotina.](https://ajuda.sankhya.com.br/hc/article_attachments/36335241559831)

**(3)** Após salvar o projeto no departamento, execute novamente a geração do lote de depreciação.

**CAUSA:**

A mensagem ocorre porque a empresa está configurada para utilizar **Projetos** na depreciação e a rotina também foi executada com essa opção ativa.

Entretanto, **o Departamento vinculado ao bem não possui um Projeto informado**, impedindo o processamento.

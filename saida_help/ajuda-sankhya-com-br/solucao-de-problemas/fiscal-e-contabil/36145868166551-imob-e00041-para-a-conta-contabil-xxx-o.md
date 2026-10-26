---
id: "36145868166551"
titulo: "IMOB_E00041 - Para a conta contábil XXX o projeto é obrigatório"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36145868166551-IMOB-E00041-Para-a-conta-cont%C3%A1bil-XXX-o-projeto-%C3%A9-obrigat%C3%B3rio"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:23:43Z"
rotulos: ["Produtos", "Configuração", "Contas", "Imobilizado", "Projeto", "Geração de Lote de Depreciação", "Conta Contábil", "Projeto é obrigatório", "Usar Projeto", "IMOB_E00041"]
---

# IMOB_E00041 - Para a conta contábil XXX o projeto é obrigatório

**MENSAGEM**:

[IMOB\_E00041] Para a conta contábil XXX o projeto é obrigatório

**SOLUÇÃO**:

**(1)** Acesse a tela [**''Geração de Lote de Depreciação''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001593622-Gera%C3%A7%C3%A3o-de-Lote-de-Deprecia%C3%A7%C3%A3o) (Imobilizado » Rotinas).

**(2)** Habilite a opção **''Usar Projeto?''** e salve.

![Imagem 1: (2) Habilite a opção ''Usar Projeto?'' e salve.](https://ajuda.sankhya.com.br/hc/article_attachments/36410274236311)

**CAUSA**:

O erro ocorre porque as contas contábeis vinculadas aos bens na tela **''Produtos''** (Comercial » Configuração » Cadastro » Produtos) estão configuradas com a opção **“Projeto obrigatório”**.

Quando essa marcação existe, o sistema exige a informação de um Projeto.

Se a configuração indicada na Solução estiver desativada, o sistema não permite prosseguir e exibe a mensagem de erro.

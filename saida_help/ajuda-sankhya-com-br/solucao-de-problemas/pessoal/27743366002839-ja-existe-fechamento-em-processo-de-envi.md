---
id: "27743366002839"
titulo: "Já existe fechamento em processo de envio, não permitido novo fechamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27743366002839-J%C3%A1-existe-fechamento-em-processo-de-envio-n%C3%A3o-permitido-novo-fechamento"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:18:48Z"
rotulos: ["Fechamento", "eSocial", "Central do eSocial", "não permitido novo fechamento", "Já existe fechamento em processo de envio", "Erro", "S-1299"]
---

# Já existe fechamento em processo de envio, não permitido novo fechamento

**MENSAGEM:**

Já existe fechamento em processo de envio, não permitido novo fechamento.

**SITUAÇÃO:**

Ao tentar realizar o Fechamento da referência eSocial através da rotina:  **Pessoal+ » Rotinas Folha » Central do eSocial » Finalização**.

**CAUSA:**

**Causa 1:**
Pode ser que o S-1299 - Fechamento dos Eventos Periódicos esteja ainda em processamento, pois há eventos não finalizados no Console Sanesocial preso, impedindo a finalização do evento S-1299.

**Causa 2:**

Ou pode ser que tenha realizado o envio do S-1299 - Fechamento e, logo em seguida, realizou o envio do  S-1298 - Reabertura dos Eventos Periódicos, na mesma sequência.

**SOLUÇÃO:**

**Para Causa 1:** realize a liberação da fila com o processo indicado no Artigo: [Cancelar envio preso e Cancelar eventos não finalizados San esocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/9605763382935-Cancelar-envio-preso-e-Cancelar-eventos-n%C3%A3o-finalizados-San-esocial)

(1)**Após este processo de cancelar os eventos presos, retorne ao card de Acompanhamento e verifique se o evento finalizou o processamento de envio.**

**Para Causa 2:** realize o cancelamento do Envio através do Console Sanesocial no botão **“Cancelar Envio”**.

![Imagem 1: Para Causa 2: realize o cancelamento do Envio através do Console Sanesocial no botão “Cancelar Envio” .](https://ajuda.sankhya.com.br/hc/article_attachments/27743373838999)

![Imagem 2: Para Causa 2: realize o cancelamento do Envio através do Console Sanesocial no botão “Cancelar Envio” .](https://ajuda.sankhya.com.br/hc/article_attachments/27743373841687)

(1)** Após este processo de cancelamento, faça o processo de fechamento com envio do S-1299.**

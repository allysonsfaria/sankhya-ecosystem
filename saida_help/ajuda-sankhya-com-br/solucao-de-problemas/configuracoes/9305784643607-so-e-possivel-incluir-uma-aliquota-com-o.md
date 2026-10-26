---
id: "9305784643607"
titulo: "Só é possível incluir uma alíquota com os dados já existentes se o parâmetro \"PODEDUPALIQICMS\" estiver ligado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9305784643607-S%C3%B3-%C3%A9-poss%C3%ADvel-incluir-uma-al%C3%ADquota-com-os-dados-j%C3%A1-existentes-se-o-par%C3%A2metro-PODEDUPALIQICMS-estiver-ligado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:08:52Z"
rotulos: ["Alíquotas", "Configuração", "Fiscal", "ICMS", "Preferências", "CORE_E02108", "Habilitação de Duplicação de Alíquota", "Erro"]
---

# Só é possível incluir uma alíquota com os dados já existentes se o parâmetro "PODEDUPALIQICMS" estiver ligado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18666706725399) MENSAGEM:**

[CORE\_E02108] Só é possível incluir uma alíquota com os dados já existentes se o parâmetro "PODEDUPALIQICMS" estiver ligado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18666706737175) SITUAÇÃO:**

Ao incluir em todos os estados, o CST 41, alíquota 0% para a TOP retorno de conserto a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18666735905815) CAUSA:**

Tentar duplicar uma alíquota.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18666706752023) SOLUÇÃO:**

Habilite o parâmetro **PODEDUPALIQICMS** na tela **Preferências** (Configurações » Avançado » Preferências):

![Imagem 5: Habilite o parâmetro PODEDUPALIQICMS na tela Preferências (Configurações » Avançado » Preferências):](https://ajuda.sankhya.com.br/hc/article_attachments/9305777362455)

Com o parâmetro **"Permite duplicar cad. de tributação alíquota ICMS? - PODEDUPALIQICMS"** ativo, quando for realizada a duplicação de uma alíquota, todos os dados pertinentes à ela serão reproduzidos também na nova alíquota gerada, tais como, Tributação, Alíquota, Redução da Base etc.

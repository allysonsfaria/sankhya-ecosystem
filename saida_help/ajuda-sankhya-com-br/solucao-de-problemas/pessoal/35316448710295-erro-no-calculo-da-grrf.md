---
id: "35316448710295"
titulo: "Erro no cálculo da GRRF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35316448710295-Erro-no-c%C3%A1lculo-da-GRRF"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:20:56Z"
rotulos: ["Configuração", "Eventos", "Folha", "Geração de Guias", "GRRF", "FGTS", "Erro", "Erro no cálculo da GRRF", "GRRF - Guia de Recolhimento Rescisório do FGTS", "Guia de Recolhimento Rescisório do FGTS", "Artigo atualizado KCS", "Sankhya RH - KCS"]
---

# Erro no cálculo da GRRF

**MENSAGEM**

Divergência entre os valores da multa rescisória apresentados na GRRF (Guia de Recolhimento Rescisório do FGTS) gerada pelo sistema Sankhya e os valores constantes no FGTS Digital.

**SITUAÇÃO**

Ao emitir a GRRF através da tela **"Geração de Guias"** (Pessoal+ » Rotinas Folha » Geração de Guias), identifica-se que o valor apresentado no campo 31 não corresponde ao cálculo correto de 8% do FGTS informado no campo 26, gerando divergência nos valores da guia.

**SOLUÇÃO**

**(1)** Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos).

**(2)** Localize o evento que está causando a divergência no campo 31 da GRRF.

**(3)** Verifique a configuração do campo **"Identificação"** do evento.

![Imagem 1: (1) Acesse a tela "Eventos" (Pessoal+ » Cadastros » Eventos). (2) Localize o evento que está causando a divergência no…](https://ajuda.sankhya.com.br/hc/article_attachments/35629470409623)

**(4)** **Caso seja um evento padrão do sistema**, conforme orientado, altere ao valor do campo Identificação  para **"0 - Sem identificação"**.

**(5)** Salve as alterações realizadas no evento.

**(6)** Acesse novamente a tela **"Geração de Guias"** (Pessoal+ » Rotinas Folha » Geração de Guias) e emita uma nova GRRF para verificar a correção do campo 31.

**CAUSA**

A divergência ocorre porque o evento estava configurado com o campo **"Identificação"** definido como **"102 – Evento FGTS"**. Esta identificação possui vínculo direto com a geração da guia do FGTS e corresponde especificamente ao evento de valor do FGTS calculado, fazendo com que o sistema inclua valores adicionais no campo 31, resultando na divergência observada.

---
id: "35834304653719"
titulo: "não gerado quando difere do CR configurado na integração financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35834304653719-n%C3%A3o-gerado-quando-difere-do-CR-configurado-na-integra%C3%A7%C3%A3o-financeira"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:21:13Z"
rotulos: ["Configuração", "Rateio", "Movimentação Financeira", "Centro de Resultado", "Preferências", "Financeiro", "não gerado", "quando", "configurado", "na integração financeira", "CR", "difere"]
---

# não gerado quando difere do CR configurado na integração financeira

**SITUAÇÃO:**

Ao gerar a integração financeira, o sistema não preenche automaticamente a aba **''Rateio''** com o **Centro de Resultado (CR)** do departamento do funcionário quando este é diferente do CR definido na configuração da integração.

**SOLUÇÃO:**

O parâmetro “**Permite rateio para único CR/Projeto – FPRATEIOUNICO**” deve ser habilitado quando houver necessidade de gerar rateio para um único Centro de Resultado (CR), especialmente em situações em que o CR do funcionário seja diferente do CR configurado na integração financeira.

**Para ativar o parâmetro:**

- Acesse a tela **''Preferências''** (Configurações» Avançado);
- Localize o parâmetro FPRATEIOUNICO;
- Ative-o conforme demonstrado na imagem abaixo.

![Imagem 1: Ative-o conforme demonstrado na imagem abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/36310899970583)

**CAUSA:**

O rateio não é gerado para um único Centro de Resultado (CR) porque, por padrão, o sistema só processa o rateio quando existem lançamentos para mais de um CR na mesma integração.

Além disso, o CR do funcionário é diferente do CR configurado na integração financeira, e o parâmetro FPRATEIOUNICO não está habilitado, o que impede a geração do rateio em situações com apenas um CR.

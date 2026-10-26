---
id: "39339588706071"
titulo: "Erro no Cálculo de Férias com Valor em Dobro no Pagamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39339588706071-Erro-no-C%C3%A1lculo-de-F%C3%A9rias-com-Valor-em-Dobro-no-Pagamento"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:44Z"
rotulos: ["Configuração", "Eventos", "Folha de Pagamento", "Erro", "Artigo criado KCS", "Sankhya RH - KCS", "Recisão"]
---

# Erro no Cálculo de Férias com Valor em Dobro no Pagamento

**MENSAGEM**

O sistema calcula o evento **"225 - FERIAS PROP INDENIZADAS API** **"** em duplicidade, resultando em pagamento dobrado de férias no recibo do colaborador.

**SITUAÇÃO**

Ao processar o cálculo de rescisão ou férias, o valor do evento aparece duplicado no recibo do funcionário, gerando um pagamento incorreto e superior ao devido.

**SOLUÇÃO**

Para corrigir o cálculo em duplicidade, siga os passos abaixo:

**(1)** Acesse a tela **"Regra de Cálculo"** (Pessoal+ » Cadastros » Regras de Cálculo) e localize o aviso prévio.

**(2)** Desmarque o campo **"Considerar reflexo nas férias por período aquisitivo"** nas configurações do evento.

![Imagem 1: Salve as alterações realizadas no cadastro da Regra de cálculo.](https://ajuda.sankhya.com.br/hc/article_attachments/41423582570775)
**(3)** Salve as alterações realizadas no cadastro da Regra de cálculo.

**(4)** Exclua o cálculo de férias ou rescisão que apresentou o erro.

**(5)** Processe novamente o cálculo para o colaborador afetado.

**(6)** Verifique no recibo se o valor do evento está sendo calculado corretamente, sem duplicidade.

**CAUSA**

O erro ocorre quando o campo **"Considerar reflexo nas férias por período aquisitivo"** está marcado no cadastro do evento. Esta configuração faz com que o sistema calcule o valor das férias duas vezes: uma no processamento normal e outra considerando o reflexo por período aquisitivo, resultando na duplicidade do pagamento.

A marcação inadequada deste campo é a principal causa do cálculo em dobro, especialmente em eventos relacionados a férias proporcionais indenizadas em processos de rescisão.

---
id: "360044110934"
titulo: "Não é permitido o envio de mais de um evento para o mesmo contribuinte, num mesmo período de apuração para um mesmo estabelecimento e prestador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110934-N%C3%A3o-%C3%A9-permitido-o-envio-de-mais-de-um-evento-para-o-mesmo-contribuinte-num-mesmo-per%C3%ADodo-de-apura%C3%A7%C3%A3o-para-um-mesmo-estabelecimento-e-prestador"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:51Z"
rotulos: ["Parceiro", "Impostos", "EFD", "Alíquotas de ISS", "Identifique documentos com impostos diferentes e filtre lançamentos duplicados.", "Não é permitido enviar mais de um evento para o mesmo contribuinte no mesmo período.", "Considere retificação ou ajuste com a contabilidade antes de retransmitir.", "Documentos Eletrônicos", "Reinf"]
---

# Não é permitido o envio de mais de um evento para o mesmo contribuinte, num mesmo período de apuração para um mesmo estabelecimento e prestador

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16996957798167) MENSAGEM:**

MS1028 - Não é permitido o envio de mais de um evento para o mesmo contribuinte, num mesmo período de apuração para um mesmo estabelecimento e prestador, exceto se for para retificação de um evento enviado anteriormente ou se o evento anterior tiver sido excluído. Localização:Registro: evtServTom - XPATH: /Reinf/evtServTom

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16996965476119) SITUAÇÃO:**

Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16996965481239) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Identifique para um mesmo parceiro, documentos com incidência de impostos diferentes.](https://ajuda.sankhya.com.br/hc/article_attachments/16996957806999) Identifique para um mesmo parceiro, documentos com incidência de impostos diferentes.

![Imagem 5: Acesse: Livros Fiscais » Conexão » Reinf » EFD - Reinf Aba: "R2010-Retenção Contribuição Serviços Tomados"](https://ajuda.sankhya.com.br/hc/article_attachments/16996957810967) Acesse: Livros Fiscais » Conexão » Reinf » EFD - Reinf
Aba: **"R2010-Retenção Contribuição Serviços Tomados"**

- Através desta aba, pode ser feito um filtro utilizando os campos da grade para identificar 2 (dois) ou mais lançamentos para o mesmo CNPJ/Parceiro ou extrair um relatório em Excel.
- Também é possível gerar um relatório, através do botão **"Relatório"**, no painel principal da tela e auditar o evento R2010 para identificar os registros duplicados.

![Imagem 6: Após identificar os lançamentos, considere transmitir o evento de Retificação ou verificar com a contabilidade sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/16996965495063) Após identificar os lançamentos, considere transmitir o evento de Retificação ou verificar com a contabilidade sobre a(s) nota(s) do mesmo parceiro, com incidência de imposto diferente e tomar as providências de acordo com a solução repassada pelo Contador.

![Imagem 7: Após os ajustes, transmita novamente o arquivo.](https://ajuda.sankhya.com.br/hc/article_attachments/16996957818391) Após os ajustes, transmita novamente o arquivo.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16996965501719)CAUSA:**

Ocorre quando existe um lançamento para o mesmo parceiro, com informações de Alíquotas de impostos com percentuais (%) diferentes no período. **Exemplo:** uma Nota de serviço com incidência de INSS 3,5% e outra nota com 11% para o mesmo parceiro.

---
id: "360043062253"
titulo: "Data-Hora de Emissão posterior ao horário de recebimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043062253-Data-Hora-de-Emiss%C3%A3o-posterior-ao-hor%C3%A1rio-de-recebimento"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:09Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "Impostos", "703", "Rejeição por Data-Hora", "Impactos do Horário de Verão", "Ajuste de Servidor Necessário", "Erro", "Documentos Eletrônicos"]
---

# Data-Hora de Emissão posterior ao horário de recebimento

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16473951668119) MENSAGEM:**

[703-Rejeição]: Data-Hora de Emissão posterior ao horário de recebimento.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16473936110487) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Verifique, com a área de TI da empresa, se o horário do servidor do Banco de Dados está com a hora adiantada. Verifique…](https://ajuda.sankhya.com.br/hc/article_attachments/16473936111767) Verifique, com a área de TI da empresa, se o horário do servidor do Banco de Dados está com a hora adiantada. Verifique o fuso horário local e ajuste a Data/Hora do servidor.

![Imagem 4: Acesse a NF-e e verifique os campos de " Data do Cabeçalho" , " Data de Negociação" , " Data de Ent./Saída" , " Data de…](https://ajuda.sankhya.com.br/hc/article_attachments/16473951673239) Acesse a NF-e e verifique os campos de "**Data do Cabeçalho"**, "**Data de Negociação"**, "**Data de Ent./Saída"**, "**Data de Movimento"** e "**Data de Faturamento"**.

Verifique se a Data de Movimento está com a mesma data, das Data de Negociação e Data de Faturamento.

**![Imagem 5: CAUSAS:](https://ajuda.sankhya.com.br/hc/article_attachments/16473951678615) CAUSAS:**

![Imagem 6: Quando uma NF-e/NFC-e é emitida com Data/Hora de Emissão 2018-05-19T08:30:00-03:00 e na SEFAZ quando recebeu o…](https://ajuda.sankhya.com.br/hc/article_attachments/16473936111767) Quando uma NF-e/NFC-e é emitida com Data/Hora de Emissão 2018-05-19T08:30:00-03:00  e na SEFAZ quando recebeu o documento era  2018-05-19T08:00:00-03:00, então ocorre a rejeição.

![Imagem 7: Quando emite uma NF-e/NFC-e durante o horário de verão, para Sefaz SP (São Paulo), que sofreu mudança em seu horário.…](https://ajuda.sankhya.com.br/hc/article_attachments/16473951673239) Quando emite uma NF-e/NFC-e durante o horário de verão, para Sefaz SP (São Paulo), que sofreu mudança em seu horário. Na NF-e/NFC-e, foi informada data-hora de emissão igual a "2018-10-17T10:00:00-03:00" e na Sefaz, com o horário de verão, o GMT passa de "-03:00" para "-02:00". No momento da recepção da NF-e/NFC-e, a data-hora da Sefaz era igual a "2018-10-17T10:00:00-02:00". 

Pela diferença entre o GMT informado na NF-e/NFC-e e o servidor da Sefaz, o documento será rejeitado.

**![Imagem 8: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16473951683351) OBSERVAÇÕES:**

**(1)** É comum durante o horário de Verão Brasileiro² esta rejeição ocorrer com maior frequência, pois ocorre ajustes nos horários dos Servidores da SEFAZ, porém os clientes se esquecem de ajustar o horário do Servidor de Banco de Dados.

**(1)** O horário de verão foi aplicado por decreto nas regiões Sul, Sudeste e Centro-Oeste, desta forma os estados afetados serão: Distrito Federal, Espírito Santo, Goiás, Minas Gerais, Mato Grosso, Mato Grosso do Sul, Paraná, Rio de Janeiro, Rio Grande do Sul, Santa Catarina e São Paulo.

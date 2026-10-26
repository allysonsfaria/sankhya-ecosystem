---
id: "360044617513"
titulo: "Não existem Informações do Contribuinte vigente na data do evento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617513-N%C3%A3o-existem-Informa%C3%A7%C3%B5es-do-Contribuinte-vigente-na-data-do-evento"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:49Z"
rotulos: ["Configuração", "EFD", "Preferências", "Informações do Contribuinte faltando", "Verifique registros e datas do evento R1000.", "Atualize datas e reenvie R1000", "Erro", "Reinf", "R1000"]
---

# Não existem Informações do Contribuinte vigente na data do evento

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16981810079767) MENSAGEM:**

[MS1009]: Não existem Informações do Contribuinte vigente na data do evento. Localização:Registro: evtServTom - XPATH: /Reinf/evtServTom

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16981810081303) SITUAÇÃO:**

Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16981810083351)SOLUÇÃO:**

![Imagem 4: Consulte na referência atual, ou em referências anteriores da empresa, o último registro do evento R1000 finalizado;](https://ajuda.sankhya.com.br/hc/article_attachments/16981810088215) Consulte na referência atual, ou em referências anteriores da empresa, o último registro do evento R1000 finalizado;

![Imagem 5: Verifique o intervalo entre a Dt. Inicial da Vigência e Dt. Final da Vigência. Caso esteja fora da referência atual é…](https://ajuda.sankhya.com.br/hc/article_attachments/16981810089239) Verifique o intervalo entre a Dt. Inicial da Vigência e Dt. Final da Vigência. Caso esteja fora da referência atual é necessário o envio de um evento de alteração do registro R1000;

![Imagem 6: Este evento de alteração do registro R1000 pode ser gerado a partir da alteração das datas de início e fim da validade;](https://ajuda.sankhya.com.br/hc/article_attachments/16981810089879) Este evento de alteração do registro R1000 pode ser gerado a partir da alteração das datas de início e fim da validade;

![Imagem 7: Para correção, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16981818869399) Para correção, siga os passos abaixo:

**(1)** Acesse: Comercial » Preferências » Empresa
Aba: **"EFD-Escrituração Fiscal Digital"**
Tipo de Escrituração: EFD Reinf

Campo **"Data Validade Inicial Reinf":** informe data posterior a registrada no Dt. Final da Vigência o último evento R1000 com status finalizado.

**Exemplo:**

Caso o ultimo evento R1000 com status finalizado para a empresa esteja com o Dt. Final da Vigência igual a '31/07/2018', informar no campo Data Validade Inicial Reinf das preferências da empresa a data '01/08/2018'.

Campo **"Data Validade Final Reinf":** deixar vazio

Isso fará com que o sistema gere um registro de alteração para o evento R1000, fazendo com que a Dt. Inicial de Vigência e Dt. Final da Vigência fiquem compatíveis com referência atual.

Transmita novamente o R1000.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16981818871831) CAUSA:**

O evento R1000 é enviado apenas uma vez, quando ocorrer alguma alteração nos registros o R1000 é enviado novamente com o Tipo de Envio Alteração.
Pode ocorrer de ter enviado as informações do período anterior e estar preenchido Data Inicial da Vigência e Data Final da Vigência, com isso os dados constará na Receita(R1000) fechado.

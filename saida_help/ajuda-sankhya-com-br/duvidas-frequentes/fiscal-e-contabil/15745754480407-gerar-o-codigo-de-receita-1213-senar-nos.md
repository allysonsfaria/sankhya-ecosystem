---
id: "15745754480407"
titulo: "Gerar o código de receita 1213 (SENAR) nos totalizadores da EFD-REINF (R-5001/R-5011), a serem enviados à DCTFWEB"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15745754480407-Gerar-o-c%C3%B3digo-de-receita-1213-SENAR-nos-totalizadores-da-EFD-REINF-R-5001-R-5011-a-serem-enviados-%C3%A0-DCTFWEB"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-09-16T18:44:49Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "Folha de Pagamento", "Totalizadores EFD-REINF enviados à DCTFWEB", "Tag \"S\" para apuração folha retorno via SEFAZ", "Eventos R-2010 a R-2060 geram R-5001 e R-5011 retorno de informações", "DCTFWeb", "EFD-REINF"]
---

# Gerar o código de receita 1213 (SENAR) nos totalizadores da EFD-REINF (R-5001/R-5011), a serem enviados à DCTFWEB

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16968225616407) SITUAÇÃO:**

Gerar o código de receita 1213 (SENAR) nos totalizadores da EFD-REINF (R-5001/R-5011), a serem enviados à DCTFWEB

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16968225617943) SOLUÇÃO:**

A operação dentro do Sankhya não tem mudança no REINF quanto a isso.

Foi enviada a tag que indica que a apuração é sobre a folha de pagamento com o conteúdo "S". O retorno do código 1213 é por meio da própria SEFAZ no arquivo de retorno.

**![Imagem 3: OBSERVAÇÃO DO GUIA PRÁTICO:](https://ajuda.sankhya.com.br/hc/article_attachments/16968225618967) OBSERVAÇÃO DO GUIA PRÁTICO:**

Os eventos periódicos são os eventos R-2010 ao R-2060.

Para cada um destes eventos enviados teremos um Evento R-5001, que é um evento de retorno demonstrando se há aviso ou erro nos arquivos enviados. Após o envio dos eventos periódicos e sua finalização sem erros, será enviado o Evento de Retorno R-5011, que é o totalizador das bases e impostos enviados nos eventos. Os valores de impostos totalizados neste evento estarão disponibilizados na DCTF Web. Ou seja, não é um evento a ser enviado, são informações de retorno.

![Imagem 4: Para cada um destes eventos enviados teremos um Evento R-5001, que é um evento de retorno demonstrando se há aviso ou…](https://ajuda.sankhya.com.br/hc/article_attachments/17126842307479)

Ou seja, não é um evento a ser enviado, são informações de retorno.

![Imagem 5: Ou seja, não é um evento a ser enviado, são informações de retorno.](https://ajuda.sankhya.com.br/hc/article_attachments/16969501048215)

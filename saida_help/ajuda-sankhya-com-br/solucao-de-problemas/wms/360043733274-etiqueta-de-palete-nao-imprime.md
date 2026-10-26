---
id: "360043733274"
titulo: "Etiqueta de Palete não imprime"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043733274-Etiqueta-de-Palete-n%C3%A3o-imprime"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:59:21Z"
rotulos: ["#criadoRoger", "#RevisadoWellington", "Configuração", "Impressão", "Relatórios", "WMS", "Preferências", "Falha na geração do IDPalete ao enviar para o Recebimento", "Comunicação inadequada entre o WMS do SankhyaW e o MGEWMS", "Configurar o endereço do servidor SankhyaW nas preferências avançadas", "Squad WMS"]
---

# Etiqueta de Palete não imprime

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17175456588951) SITUAÇÃO:**

Sistema não estava gerando o IDPalete ao gerar enviar para o Recebimento.
(Geração do IDPalete automática ligada por parâmetro-WMSUSAIDPALETE).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17175476453911) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/17175456595223) Acesse: Configurações » Avançado » Preferências

Parâmetro:  **"URLSANKHYAW- Endereço do servidor SankhyaW"**: informe no campo Texto o endereço+porta do SankhyaW

Ex: http://192.168.1.29:8080

Com isso, o MGEWMS (Delphi) conseguirá comunicar com o SankhyaW para a correta impressão.

![Imagem 4: Acesse: MGEWMS>>Menu>>Relatórios>>Etiquetas de Paletização e efetue a impressão da etiqueta.](https://ajuda.sankhya.com.br/hc/article_attachments/17175476464279) Acesse: MGEWMS>>Menu>>Relatórios>>Etiquetas de Paletização e efetue a impressão da etiqueta.

**![Imagem 5: CAUSA](https://ajuda.sankhya.com.br/hc/article_attachments/17175476466455) CAUSA**

Quando não há a correta comunicação do WMS do SankhyaW com MGEWMS para impressão de Etiquetas de Paletização.

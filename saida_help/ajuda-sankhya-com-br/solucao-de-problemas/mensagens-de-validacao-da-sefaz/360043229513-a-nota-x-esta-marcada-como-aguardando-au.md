---
id: "360043229513"
titulo: "A nota 'X' está marcada como \"Aguardando autorização\" no sistema. Porém a SEFAZ considera como \"Denegada\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043229513-A-nota-X-est%C3%A1-marcada-como-Aguardando-autoriza%C3%A7%C3%A3o-no-sistema-Por%C3%A9m-a-SEFAZ-considera-como-Denegada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:16Z"
rotulos: ["ERRONF", "#PUBLIFER", "Configuração", "NF-e", "SEFAZ", "TOP", "Situação da nota", "Inconsistência na situação.", "Atualizar para \"Denegada\"", "Erro", "Documentos Eletrônicos"]
---

# A nota 'X' está marcada como "Aguardando autorização" no sistema. Porém a SEFAZ considera como "Denegada"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16087307274007) MENSAGEM:**

A nota 'X' está marcada como "Aguardando autorização" no sistema. Porém a SEFAZ considera como "Denegada".
Deseja atualizar a situação da nota?

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16087307278743) SOLUÇÃO:**

![Imagem 3: Ao " Buscar Autorização " de uma NF-e, quando essa foi Denegada pela SEFAZ, será apresentada a mensagem acima. Nesse…](https://ajuda.sankhya.com.br/hc/article_attachments/16087277683479) Ao "**Buscar Autorização**" de uma NF-e, quando essa foi Denegada pela SEFAZ, será apresentada a mensagem acima. Nesse momento deve optar por 'SIM' e validar se o campo "**Status NF-e**" foi devidamente atualizado para 'DENEGADA.

- NF-e com status 'DENEGADA' não pode ser excluída e/ou CANCELADA, seu registro deve ser mantido dessa forma em seu sistema.
- Caso a regularização fiscal aconteça, uma nova NF-e deve ser emitida.
- Os itens da nota passam a não atualizar estoque e os financeiros relacionados à nota são removidos.
- Para mais informações sobre esse status verifique o artigo: [Nota fiscal eletrônica Denegada - Saiba Mais !](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043229553)

Caso ao clicar em 'SIM' a atualização de status não aconteça, verifique se as configurações necessárias foram realizadas:

![Imagem 4: Vincular no cadastro da Top utilizada na emissão da respectiva NF-e um 'Tipo de Operação NF-e DENEGADA', conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/16087307286551) Vincular no cadastro da Top utilizada na emissão da respectiva NF-e um 'Tipo de Operação NF-e DENEGADA', conforme detalhado abaixo:

- Tela **"[Tipos de Operação -TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: Comercial/Arquivo/Cadastros)
- Aba:**"NF-e/NFC-e"**

**Tipo Operação NF-e Denegada**: A TOP informada aqui irá sobrepor as TOPS informadas no parâmetro **"TOPNFEDENEG"**. Isto será necessário quando a operação da NF-e for diferente das operações das TOPS informadas neste parâmetro (normalmente TOPS de Venda, Compra, Devoluções etc.).

![Imagem 5: IMPORTANTE :](https://ajuda.sankhya.com.br/hc/article_attachments/17874316029463) **IMPORTANTE:**

- A TOP Denegada a ser vinculada no campo mencionado acima, deve ter o mesmo **'Tipo de Movimento'** da TOP utilizada no lançamento. Exemplo: Se emitida uma NF-e de Devolução de Compra e essa for denegada pela SEFAZ, cadastre uma 'Top Denegada' com o Tipo de movimento DEVOLUÇÃO DE COMPRA.
- Caso não possua essa TOP configurada, valide se existe um "padrão" com tipo de movimento 'Venda' devidamente cadastrado, duplicando a mesma e ajustando o tipo de movimento conforme desejado. Certifique-se que esse cadastro padrão foi realizado e validado junto a um consultor de sua Unidade/Franquia e encontra-se de acordo com o esperado.

![Imagem 6: Realizada a configuração mencionada acima, busque uma nova autorização da nota, certificando-se que o status foi…](https://ajuda.sankhya.com.br/hc/article_attachments/16087277689367) Realizada a configuração mencionada acima, busque uma nova autorização da nota, certificando-se que o status foi devidamente atualizado.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16087277692951) CAUSA:**

Ao 'Buscar Autorização' de uma NF-e, quando essa foi Denegada pela SEFAZ, será apresentada a mensagem.

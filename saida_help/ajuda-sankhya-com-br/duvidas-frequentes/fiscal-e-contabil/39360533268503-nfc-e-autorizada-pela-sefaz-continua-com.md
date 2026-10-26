---
id: "39360533268503"
titulo: "NFC-e autorizada pela SEFAZ continua com status pendente no Portal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39360533268503-NFC-e-autorizada-pela-SEFAZ-continua-com-status-pendente-no-Portal"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-10-15T20:13:18Z"
rotulos: ["Fiscal", "Ocorrências", "SEFAZ", "NFC-e", "Erro", "Artigo criado KCS", "CVE - KCS", "Documentos Eletrônicos"]
---

# NFC-e autorizada pela SEFAZ continua com status pendente no Portal

**Situação**

Ao realizar a emissão de uma NFC-e, o documento continua com o **Status NF-e** pendente (por exemplo, **Enviada** ou **Aguardando autorização**) na tela **"Portal de Vendas"** (Comercial » Rotinas » Portal de Vendas), mesmo após ter sido devidamente autorizado pela SEFAZ.

**Solução**

Para regularizar a situação, siga os passos abaixo:

Acesse a tela **"Portal de Vendas"** (Comercial » Rotinas » Portal de Vendas). Se a empresa usa o **"Portal de Caixa"** (Comercial » Consulta » Portal de Caixa), os passos são os mesmos.
 Selecione a nota fiscal que apresenta a pendência (uma nota por vez).
 Clique no botão **NFC-e** e selecione a opção **Consulta situação atual da nota**.
 Aguarde o processamento da consulta. Se a SEFAZ confirmar que a nota está autorizada, o sistema exibe a mensagem **Status da nota desatualizado**, com a situação da nota no sistema e na SEFAZ. Confirme para atualizar a situação da nota.
 Caso o status permaneça pendente, verifique a resposta da SEFAZ exibida na consulta e as ocorrências da nota em **Outras Opções » Ver acompanhamentos**. Se a SEFAZ informar que a nota não consta na base de dados dela (código 217), a NFC-e não foi autorizada: o sistema muda o status para **Aguardando correção**, e a nota precisa ser corrigida e enviada novamente.
 Se o erro persistir, verifique a conectividade com a SEFAZ pela opção **NFC-e » Consulta do status do serviço**.

**(7)** Atualize a tela e confirme que o **Status NF-e** da nota passou para **Aprovada**.

**Causa**

O sistema só atualiza a situação da NFC-e quando recebe a resposta (retorno) da SEFAZ. Se essa resposta não chega ao sistema durante o envio (por exemplo, por queda de conexão ou demora na resposta), a nota fica com o último status gravado, mesmo já estando autorizada na SEFAZ. A opção **Consulta situação atual da nota** busca a situação diretamente na SEFAZ e permite atualizar o status no sistema.

---
id: "14815631387671"
titulo: "ORA-20101: Ordem de carga 6 usada na nota de Nro Único: 5157 está fechada e não pode ser alterada. ORA-06512: em \"SDETESTE4.TRG_INC_UPD_TGFCAB_ORD\", line 167 ORA-04088: erro durante a execução do gatilho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14815631387671-ORA-20101-Ordem-de-carga-6-usada-na-nota-de-Nro-%C3%9Anico-5157-est%C3%A1-fechada-e-n%C3%A3o-pode-ser-alterada-ORA-06512-em-SDETESTE4-TRG-INC-UPD-TGFCAB-ORD-line-167-ORA-04088-erro-durante-a-execu%C3%A7%C3%A3o-do-gatilho"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:57:58Z"
rotulos: ["Configuração", "Ordem de Serviço", "ORA-06512", "NFS-e", "Uso de Ordem de Carga Fechada em Novas Notas", "Erro"]
---

# ORA-20101: Ordem de carga 6 usada na nota de Nro Único: 5157 está fechada e não pode ser alterada. ORA-06512: em "SDETESTE4.TRG_INC_UPD_TGFCAB_ORD", line 167 ORA-04088: erro durante a execução do gatilho

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16638201061655) MENSAGEM:**

[ORA-20101]: Ordem de carga 6 usada na nota de Nro Único: 5157 está fechada e não pode ser alterada.

[ORA-06512]: em "SDETESTE4.TRG\_INC\_UPD\_TGFCAB\_ORD", line 167

[ORA-04088]: erro durante a execução do gatilho 'SDETESTE4.TRG\_INC\_UPD\_TGFCAB\_ORD'

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16638209843095) CAUSA:**

Ocorre ao tentar alterar utilizar uma ordem de carga fechada em um novo pedido ou nota quando o parâmetro ALTOCFECFORMOC está desabilitado.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16638209840791) SOLUÇÃO:**

Para utilizar uma ordem de carga fechada em novas notas/pedidos, ative o parâmetro **"ALTOCFECFORMOC"**.

![Imagem 4: Para utilizar uma ordem de carga fechada em novas notas/pedidos, ative o parâmetro " ALTOCFECFORMOC" .](https://ajuda.sankhya.com.br/hc/article_attachments/14815613116951)

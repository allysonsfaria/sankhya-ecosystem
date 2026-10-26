---
id: "360044213993"
titulo: "A TOP da Baixa deve ser informada. Financeiro de Nro Único: XXXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044213993-A-TOP-da-Baixa-deve-ser-informada-Financeiro-de-Nro-%C3%9Anico-XXXXX"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:45Z"
rotulos: ["#criadoRoger", "#Revisadoclaudio", "Configuração", "Movimentação Financeira", "TOP", "Preferências", "Financeiro", "ORA-20101", "Configurar parâmetros específicos", "Parâmetros de devolução não configurados", "TOP da Baixa não informada"]
---

# A TOP da Baixa deve ser informada. Financeiro de Nro Único: XXXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17291148395287) MENSAGEM:**

[ORA-20101]: A TOP da Baixa deve ser informada. Financeiro de Nro Único: XXXXX.
[ORA-06512]: em "NOMEBANCO.TRG\_UPT\_TGFFIN", line 585
[ORA-04088]: erro durante a execução do gatilho 'NOMEBANCO.TRG\_UPT\_TGFFIN'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17291148405271) SOLUÇÃO:**

Para correção, siga  os passos abaixo:

![Imagem 3: Acesse o cadastro de Parâmetros em: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/17291133552023) Acesse o cadastro de Parâmetros em: Configurações » Avançado » Preferências

Informe em cada parâmetro o código da Top de Baixa para Receita e Despesa, respectivamente. Para que no processo de compensação de devolução o sistema efetua as devidas baixas nos títulos em aberto.

- **"TOPBAIRECDEV-TOP baixa da receita na compensação de devolução":** parâmetro para registrar o código da TOP que será gravada no título de receita gerado pela devolução de compras;

- **"TOPBAIDESPDEV -TOP baixa da despesa na compensação de devolução":** parâmetro para registrar o código da TOP que será gravada no título de despesa gerado pela devolução de vendas.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17291133554327) CAUSA:**

- Ocorre quando não estão devidamente configurados os parâmetros de Top de compensação de devolução de compras e devolução de vendas;
- Aceita-se somente 1 (um) código de Top em cada parâmetro;
- As TOPs devem ser de Recebimento (Tipo de Movimento - R-Recebimento)  e Pagamento (Tipo de Movimento = G-Pagamento)

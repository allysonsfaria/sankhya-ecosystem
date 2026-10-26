---
id: "7117486338711"
titulo: "Visualização de boletos não gerada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7117486338711-Visualiza%C3%A7%C3%A3o-de-boletos-n%C3%A3o-gerada"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:14:57Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Boleto", "Financeiro", "CORE_E01374", "Revise configurações de emissão e movimentação financeira", "[CORE_E01374] Boleto não gerado", "Emissão de boleto não configurada", "Erro"]
---

# Visualização de boletos não gerada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16490370346519)  MENSAGEM:**

[CORE\_E01374] Visualização de boletos não gerada!

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16490370348183) CAUSA:**

Mensagem apresentada quando a emissão de boleto não está devidamente configurada e não permite a visualização do respectivo boleto.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16490312063895) SOLUÇÃO:**

Revise as configurações abaixo, de acordo com o lançamento efetuado, e caso algum deles não seja respeitado, a mensagem será apresentada na tentativa de visualização do boleto:

![Imagem 4: Acesse a tela: "Contas" (Caminho de acesso: Configurações » Cadastros » Bancários » Contas):](https://ajuda.sankhya.com.br/hc/article_attachments/16490312065303) Acesse a tela: **"Contas"** (Caminho de acesso: Configurações » Cadastros » Bancários » Contas):

Aba: **"Boleto(s)/Duplicatas"**

- Emite: marcado
- Modelo, configure em: '**Financeiro » Relatórios » Modelos de Boleto(s)**', um que seja padrão ou personalizado e vincule em '**Configurações » Avançado » Modelos de Nota Fiscal/Duplicatas/Boleto(s)**', para ser informado neste campo

![Imagem 5: Acesse a rotina "Movimentação Financeira" (Caminho de acesso: Financeiro » Rotinas » Movimentação Financeira):](https://ajuda.sankhya.com.br/hc/article_attachments/16490411528983) Acesse a rotina **"Movimentação Financeira"** (Caminho de acesso: Financeiro » Rotinas » Movimentação Financeira):

- Certifique-se que o(s) titulo(s) não estejam Baixados. Campo: "Data de Baixa" e **"Valor de Baixa"**  preenchidos e **"Data de Vencimento"** não seja igual data de negociação.

![Imagem 6: Após os ajustes, considere efetuar a impressão do boleto novamente](https://ajuda.sankhya.com.br/hc/article_attachments/16490411532311) Após os ajustes, considere efetuar a impressão do boleto novamente

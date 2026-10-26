---
id: "360043712474"
titulo: "A data de entrada e saída deve ser informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043712474-A-data-de-entrada-e-sa%C3%ADda-deve-ser-informada"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:41Z"
rotulos: ["#PUBLIFER", "CORE_E05556", "Configuração", "Movimentação Financeira", "Preferências", "Financeiro", "CORE_E05555", "Data Entrada/Saída", "Desative Parâmetro", "Atualização Recomendada", "Erro"]
---

# A data de entrada e saída deve ser informada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16199203171351) MENSAGEM:**

[CORE\_E05556]  A data de entrada e saída deve ser informada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199196695447)SOLUÇÃO:**

![Imagem 3: Para clientes que não trabalham com o módulo 'Orçamentário' (Controle Orçamentário e Metas) o parâmetro abaixo deverá…](https://ajuda.sankhya.com.br/hc/article_attachments/16199203175959) Para clientes que não trabalham com o módulo 'Orçamentário' (Controle Orçamentário e Metas) o parâmetro abaixo deverá estar desligado:

- Tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Configurações » Avançado » Preferências)
  Chave **"UTIORCDTENTSAI - Utiliza orçamento por data de entrada e saída"**

![Imagem 4: Tela " Preferências " ( Configurações » Avançado » Preferências ) Chave "UTIORCDTENTSAI - Utiliza orçamento por data de…](https://ajuda.sankhya.com.br/hc/article_attachments/14503356368535)

![Imagem 5: Desligado o parâmetro, prossiga com o lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16199196702359) Desligado o parâmetro, prossiga com o lançamento.

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17855350289943) IMPORTANTE:**

Caso trabalhe com o módulo Controle Orçamentário e Metas e a respectiva rotina não possua o campo "**Dt.Entrada/Saída"** para preenchimento, recomendamos a atualização do sistema para versão 3.31b143 ou superior. Se após atualizações o problema persistir, acione o Service Desk Sankhya para análises.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16199203184791) CAUSA:**

Mensagem apresentada ao salvar determinado lançamento financeiro no sistema, quando não informado valor para o campo Dt.Entrada/Saída e parâmetro UTIORCDTENTSAI: Ligado.

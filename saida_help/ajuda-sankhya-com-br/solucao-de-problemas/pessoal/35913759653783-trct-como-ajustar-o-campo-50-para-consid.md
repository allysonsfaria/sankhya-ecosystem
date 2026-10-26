---
id: "35913759653783"
titulo: "TRCT: Como Ajustar o Campo 50 para Considerar Faltas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35913759653783-TRCT-Como-Ajustar-o-Campo-50-para-Considerar-Faltas"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-18T19:53:38Z"
rotulos: ["Configuração", "Eventos", "Folha", "Faltas", "Erro", "DSR", "Campo", "Como", "50", "TRCT", "Ajustar", "Considerar"]
---

# TRCT: Como Ajustar o Campo 50 para Considerar Faltas

**SITUAÇÃO:**

Ao gerar a TRCT de um colaborador desligado, o campo 50 (“Saldo de DIASTRAB/Dias Salário”) não está deduzindo corretamente as faltas registradas.

**SOLUÇÃO:**

Para corrigir o comportamento apresentado, ajuste a ''**Regra de Cálculo''** (Pessoal+» Cadastros): 

(1)** Inclua os eventos de faltas no TRCT:**

- Abra a Regra de Cálculo, na aba ''**TRCT''**, e subaba ''**Eventos'';**
- Localize o código ''**50 - Saldo de DIASTRAB/dias Salário (líquido de FALTASDIA/faltas e DSR)'';**
- Inclua os eventos de ''**faltas''** e ''**DSR sobre faltas''** na configuração.

[GIF animado: Imagem 1: Configure os eventos de desconto e faltas na TRCT:](https://ajuda.sankhya.com.br/hc/article_attachments/35913917467799)

**(2)** **Configure os eventos de desconto e faltas na TRCT:**

- Lista de eventos de faltas;
- Lista de eventos de desconto DSR;

![Imagem 2: Lista de eventos de desconto DSR;](https://ajuda.sankhya.com.br/hc/article_attachments/36183226761623)

**CAUSA:**

O comportamento ocorre devido à ausência de configuração dos eventos de faltas e DSR na Regra de Cálculo da TRCT. Sem esses eventos configurados, o sistema não realiza a dedução correta das faltas no cálculo do saldo de dias trabalhados.

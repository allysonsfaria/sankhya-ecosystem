---
id: "15743203960599"
titulo: "Campos do registro 0111 EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15743203960599-Campos-do-registro-0111-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:56:20Z"
rotulos: ["Configuração", "Impostos", "CFOP", "Valores do registro 0111", "Configurações específicas necessárias", "Regras por tipo de receita", "EFD Contribuições", "Alíquotas de CBS"]
---

# Campos do registro 0111 EFD Contribuições

(3)** SOLUÇÃO:**

Como o sistema constrói os valores do 0111, que em suma, são os valores contábeis das vendas presentes no livro fiscal:
 
Regras de cada valor que é construído na query que monta o registro:

- Receita Bruta Não-Cumulativa - Tributada no Mercado Interno >> CFOP no livro deve estar entre 5000 e 6999 mas não podem ser os CFOP's 5551 e 6551, e existir na tabela de impostos da nota, linha de PIS/COFINS e estar com CST's entre: 01,02,03 e 05 e alíquotas 1,65 e 7,60.

- Receita Bruta Não-Cumulativa – Não Tributada no Mercado Interno (Vendas com suspensão, alíquota zero, isenção e sem incidência das contribuições) >>   CFOP no livro deve estar entre 5000 e 6999 mas não podem ser os CFOP's 5551 e 6551, e existir na tabela de impostos da nota, linha de PIS/COFINS e estar com CST's entre: 04,05,06,07,08,09 e 49, e estar com a configuração como "Incidência exclusivamente no regime não-cumulativo" ou "Incidência nos regimes não cumulativo e cumulativo" nas preferências da empresa (Comercial), na Aba Regime de Apuração da Contrib. Social e Aprop. Crédito no campo **"Incidência tributária",** e no campo**"Método de apropriação de créditos comuns"**deve estar marcado com a opção**"Método de rateio proporcional (Receita Bruta)".**

- Receita Bruta Não-Cumulativa – Exportação >> CFOP no livro deve estar entre 7000 e 7999,  e existir na tabela de impostos da nota, linha de PIS/COFINS, e estar com a configuração como "Incidência exclusivamente no regime não-cumulativo" ou "Incidência nos regimes não-cumulativo e cumulativo" nas preferências da empresa (Comercial), na Aba Regime de Apuração da Contrib. Social e Aprop. Crédito no campo **"Incidência tributária",** e no campo**"Método de apropriação de créditos comuns"**deve estar marcado com a opção**"Método de rateio proporcional (Receita Bruta)".**

- Receita Bruta Cumulativa >> CFOP no livro deve estar entre 5000 e 6999,  e existir na tabela de impostos da nota, linha de PIS/COFINS com alíquotas 1,65 e 3,00, e com valores de PIS/COFINS maiores que zero, estar com as seguintes marcações: "Incidência exclusivamente no regime cumulativo" ou "Incidência nos regimes não-cumulativo e cumulativo"**,** e no campo**"Método de apropriação de créditos comuns"**deve estar marcado com a opção**"Método de rateio proporcional (Receita Bruta)".**

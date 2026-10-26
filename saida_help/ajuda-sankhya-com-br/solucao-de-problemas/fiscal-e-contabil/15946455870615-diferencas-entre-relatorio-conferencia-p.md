---
id: "15946455870615"
titulo: "Diferenças entre relatório conferência PIS/COFINS e registro 0111 EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15946455870615-Diferen%C3%A7as-entre-relat%C3%B3rio-confer%C3%AAncia-PIS-COFINS-e-registro-0111-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:55:48Z"
rotulos: ["Conferência", "Relatórios", "Impostos", "EFD Contribuições", "Totalizar CST 06 PDF", "Filtrar notas prestação", "Diferença CSTs EFD", "PIS/COFINS"]
---

# Diferenças entre relatório conferência PIS/COFINS e registro 0111 EFD Contribuições

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16912808297751) SOLUÇÃO:**

Na geração no relatório de conferência, quando o sistema constrói as saídas para o CST 06, é filtrando as notas de serviços que são do tipo 'prestação', as notas de saídas de produto que estão no livro como origem 'estoque' e as notas com CST exatamente igual a 06, serão totalizadas no PDF, na seção do CST correspondente.
 
Já na geração do 0111, o sistema ao construir o campo "Receita Bruta Não-Cumulativa – Não Tributada no Mercado Interno" ele busca além da CST 06, várias outras CST's como as seguintes: 04,05,06,07,08,09 e 49 o que vai causar diferenças entre os campos do EFD Contribuições e relatório de conferência PIS/COFINS, por se mais abrangente que a regra do relatório.

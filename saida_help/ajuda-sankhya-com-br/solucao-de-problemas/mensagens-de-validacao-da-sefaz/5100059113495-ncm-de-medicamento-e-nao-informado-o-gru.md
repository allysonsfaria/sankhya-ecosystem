---
id: "5100059113495"
titulo: "NCM de medicamento e não informado o grupo de medicamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5100059113495-NCM-de-medicamento-e-n%C3%A3o-informado-o-grupo-de-medicamento"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:18:11Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "NF-e", "XML", "SEFAZ", "#validadoRaiane", "#validadoMarcia", "Rejeição 840: Grupo de Medicamento Faltando"]
---

# NCM de medicamento e não informado o grupo de medicamento

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16348381432215) MENSAGEM:**

Rejeição 840 - NCM de medicamento e não informado o grupo de medicamento.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16348397643159) CAUSA:**

Este erro ocorre devido as novas regras de validação da Nota Técnica 2021.004, que é a validação sobre o  GRUPO MED, ou seja, grupo de medicamento no XML.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16348397645463) SOLUÇÃO:**

Os medicamentos são classificados nos NCMs que começam com 3001, 3002, 3003, 3004, 3005 e 3006.

![Imagem 4: Os medicamentos são classificados nos NCMs que começam com 3001, 3002, 3003, 3004, 3005 e 3006.](https://ajuda.sankhya.com.br/hc/article_attachments/15776088610711)

Para gerar as tags de Medicamento no XML, consulte o artigo:

- [Quais as configurações para gerar as TAG de Medicamento no XML?](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000927421-Quais-as-configura%C3%A7%C3%B5es-para-gerar-as-TAG-de-Medicamento-no-XML-)

O texto da NT traz a seguinte instrução:

2.2.1. Criação da Regra de Validação K01-10 Regra de validação para obrigar o preenchimento do grupo de medicamento (campo: med.) quando o código NCM do produto for de medicamento (NCMs que começam com 3001, 3002, 3003, 3004, 3005 e 3006).

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16348397649047) OBSERVAÇÃO:**

Se o produto não for medicamente altere o NCM para diferente de 3001, 3002, 3003, 3004, 3005 e 3006.

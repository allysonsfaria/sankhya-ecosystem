---
id: "34278159731351"
titulo: "Divergência entre a linha digitável gerada pelo banco e a registrada no Sankhya? Saiba como resolver"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34278159731351-Diverg%C3%AAncia-entre-a-linha-digit%C3%A1vel-gerada-pelo-banco-e-a-registrada-no-Sankhya-Saiba-como-resolver"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-08-14T16:27:43Z"
rotulos: ["Configuração", "Contas", "Financeiro", "Bancário", "API", "Passos para resolver", "Razão do erro", "Detalhe do erro", "gerada pelo banco", "registrada no Sankhya", "adequação para que a geração dos dados", "API do Banco Sicredi", "Divergência entre a linha digitável", "versões 4.34b154 ou 4.35b119 do Sankhya", "Artigo atualizado KCS", "Financeiro - KCS", "Sicredi"]
---

# Divergência entre a linha digitável gerada pelo banco e a registrada no Sankhya? Saiba como resolver

A partir das**versões 4.34b154 ou 4.35b119 do Sankhya**, foi implementada uma adequação para que a geração dos dados via **API do Banco Sicredi funcione corretamente**.

Para que a **linha digitável e o "Nosso Número"**sejam gerados de forma correta, siga os passos abaixo:

**(1)**  Acesse a tela **"Contas"** (Configurações » Cadastros » Bancários » Contas) e localize a conta utilizada para integração com o Sicredi.

**(2)**  Na **"Aba Cadastros"**, preencha corretamente o campo **"Número do Beneficiário"**.

![Imagem 1: (1) Acesse a tela "Contas" (Configurações » Cadastros » Bancários » Contas) e localize a conta utilizada para…](https://ajuda.sankhya.com.br/hc/article_attachments/34278149142423)

**(3)**  Verifique se os demais dados bancários estão corretos e alinhados entre o sistema Sankhya e o cadastro no Banco Sicredi:

| Campo no Banco Sicredi | Campo correspondente no Sankhya |
| --- | --- |
| Agência | Agência |
| Conta Bancária | Conta Bancária (com dígito verificador - DV) |
| Modalidade | Modalidade |
| Posto | Convênio |
| Carteira | Carteira |
| Código do Beneficiário | Número Beneficiário |

**(4)**  Sempre que houver divergência na linha digitável, revise todos os campos acima e compare com as informações disponibilizadas pelo Banco Sicredi.

**CAUSA**

O erro ocorre por duas causas principais: 
1) Configuração ativa do parâmetro **"Usar geração de linha digitável" e "Usar geração do nosso número"** que interfere na API; 
 2) Divergências entre as informações cadastrais inseridas no sistema e os registros no Banco Sicredi.

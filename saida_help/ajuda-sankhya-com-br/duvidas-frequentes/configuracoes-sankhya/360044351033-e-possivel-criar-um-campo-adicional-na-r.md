---
id: "360044351033"
titulo: "É possivel criar um campo adicional na Rotina de Liberação de Limites (TSILIB)?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044351033-%C3%89-possivel-criar-um-campo-adicional-na-Rotina-de-Libera%C3%A7%C3%A3o-de-Limites-TSILIB"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:58:00Z"
rotulos: ["Configuração", "Liberação de Limites", "Dicionário de Dados", "Financeiro", "Adição de Campo na Rotina de Liberação de Limites", "TSILIB"]
---

# É possivel criar um campo adicional na Rotina de Liberação de Limites (TSILIB)?

**(1)** Sim, é possível criar um campo adicional na tabela de liberação de limites, veja abaixo a correta configuração:

![Imagem 1: Acesse: Configurações » Avançado » Dicionário de Dados](https://ajuda.sankhya.com.br/hc/article_attachments/16839671092503) Acesse: Configurações » Avançado » Dicionário de Dados

- Inclua um novo campo na tabela **VSILIB**
- Campo do tipo 'Texto', apresentação 'Padrão', 'Visível no grid de pesquisa' e 'Campo Calculado'.
- Adicione uma das expressões a seguir de acordo com a necessidade:

**Exemplo 1:** para apresentar a descrição do tipo de negociação 
#type.sql# SELECT TPV.DESCRTIPVENDA FROM TGFTPV TPV, TGFCAB CAB WHERE CAB.NUNOTA = VSILIB.NUNOTA AND CAB.CODTIPVENDA = TPV.CODTIPVENDA AND CAB.DHTIPVENDA = TPV.DHALTER 

**Exemplo 2:** para apresentar o código do tipo de negociação 
#type.sql# SELECT TPV.CODTIPVENDA FROM TGFTPV TPV, TGFCAB CAB WHERE CAB.NUNOTA = VSILIB.NUNOTA AND CAB.CODTIPVENDA = TPV.CODTIPVENDA AND CAB.DHTIPVENDA = TPV.DHALTER

- Botão » Outras Opções - Reiniciar a unidade de dados

![Imagem 2: Acesse: Configurações » Avançado » Liberação de Limites](https://ajuda.sankhya.com.br/hc/article_attachments/16839668125975) Acesse: Configurações » Avançado » Liberação de Limites

Botão: **"Configuração de Grade"**

- Configure a grade adicionando o novo campo criado.

[GIF animado: Imagem 3: - Configure a grade adicionando o novo campo criado.](https://ajuda.sankhya.com.br/hc/article_attachments/360062094294)

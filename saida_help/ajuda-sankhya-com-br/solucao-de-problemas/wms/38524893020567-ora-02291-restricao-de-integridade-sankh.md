---
id: "38524893020567"
titulo: "ORA-02291: restrição de integridade (SANKHYA.FK_TGWCOIVAL_TG_WCOI) violada – chave mãe não localizada."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38524893020567-ORA-02291-restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGWCOIVAL-TG-WCOI-violada-chave-m%C3%A3e-n%C3%A3o-localizada"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:01:30Z"
rotulos: ["Conferência", "Configuração", "Estoque", "Preferências", "Passos para resolver", "Detalhe do erro", "Erro", "Utiliza recontagem cumulativa na conf. entrada", "Lote/data de validade", "Múltiplas datas de validade", "USARECCUMCONENT", "Recontagem de entrada"]
---

# ORA-02291: restrição de integridade (SANKHYA.FK_TGWCOIVAL_TG_WCOI) violada – chave mãe não localizada.

**MENSAGEM**

ORA-02291: restrição de integridade (SANKHYA.FK\_TGWCOIVAL\_TG\_WCOI) violada – chave mãe não localizada.

**SITUAÇÃO**

Ao finalizar a recontagem de entrada, quando o produto possui mais de um lote/data de validade.

**SOLUÇÃO**

**(1)** Acesse a tela **''Preferências''** (Configurações » Avançado » Preferências).

**(2)** Busque pelo parâmetro **"USARECCUMCONENT-Utiliza recontagem cumulativa na conf. entrada.''**

**(3)** Habilite o parâmetro para permitir que um mesmo produto seja recontado mais de uma vez antes da finalização da conferência.

- Quando o parâmetro estiver desabilitado, o coletor permitirá que cada produto seja recontado apenas uma única vez para envio e conclusão da recontagem.

**CAUSA**

O erro ocorre quando o parâmetro “USARECCUMCONENT – Utiliza recontagem cumulativa na conferência de entrada” não está habilitado, pois, nessa condição, o sistema permite que o produto seja recontado apenas uma única vez.

Como consequência, não é possível informar múltiplas datas de validade ou lotes para o mesmo produto durante a conferência.

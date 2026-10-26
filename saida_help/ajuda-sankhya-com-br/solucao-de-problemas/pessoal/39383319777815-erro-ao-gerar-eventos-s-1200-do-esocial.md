---
id: "39383319777815"
titulo: "Erro ao gerar eventos S-1200 do eSocial [ORA-00001] Restrição exclusiva (PK_TFPS1200) violada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39383319777815-Erro-ao-gerar-eventos-S-1200-do-eSocial-ORA-00001-Restri%C3%A7%C3%A3o-exclusiva-PK-TFPS1200-violada"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-06T19:35:36Z"
rotulos: ["Fiscal", "Admissão", "eSocial", "Configuração Funcionários", "Central do eSocial", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro ao gerar eventos S-1200 do eSocial [ORA-00001] Restrição exclusiva (PK_TFPS1200) violada

**MENSAGEM**

[ORA-00001] Restrição exclusiva (CMRPRD.PK\_TFPS1200) violada

**SITUAÇÃO**

Ao tentar gerar os eventos **"S-1200"** (Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social) do **"eSocial"** para a competência de janeiro, o sistema apresenta erro indicando violação de restrição exclusiva na tabela.

**SOLUÇÃO**

Para corrigir o erro, siga os passos abaixo:

**(1)** Verifique se há duplicação de cadastros do funcionário na mesma empresa. Acesse a tela "Funcionários" (Configurações » Cadastros » Pessoal » Configuração Funcionários) e confirme se o colaborador possui mais de um vínculo cadastrado.

**(2)** Caso identifique cadastros duplicados, verifique se ambos estão com as informações completas e consistentes, incluindo o campo "Situação no eSocial" configurado de forma equivalente entre eles.

**(3)** Se o cadastro do autônomo estiver parametrizado como "Não sujeito à admissão", ajuste essa configuração para permitir o envio do evento "S-2300" (Admissão).

**(4)** Realize uma nova geração dos eventos na "Central do eSocial" (Central do eSocial Pessoal+ » Rotinas Folha » Central do eSocial).

 **(5)** Envie primeiro o evento "S-2300" e, na sequência, efetue o envio das folhas "S-1200".

 **(6)** Valide se os eventos foram recepcionados com sucesso no "Portal do eSocial".

**CAUSA**

O erro ocorre devido à duplicação de recibos **"S-1200"** na base de dados, geralmente causada por:

- Funcionário com cadastros duplicados na mesma empresa sem as devidas parametrizações no **"eSocial"**.
- Recibos perdidos durante o processamento, possivelmente em decorrência de lentidão no sistema ou no processamento do **"eSocial"**.
- Cadastro do funcionário autônomo parametrizado incorretamente como **"Não sujeito à admissão"**, impedindo o envio adequado dos eventos.

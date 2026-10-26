---
id: "18047968893335"
titulo: "E0101[eSocial/evtTabEstab/infoEstab/alteracao/dadosEstab/infoCaepf/tpCaepf] Elemento obrigatório estoque vazio."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18047968893335-E0101-eSocial-evtTabEstab-infoEstab-alteracao-dadosEstab-infoCaepf-tpCaepf-Elemento-obrigat%C3%B3rio-estoque-vazio"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:18:09Z"
rotulos: ["Configuração", "Estoque", "eSocial", "E0101", "Central do eSocial", "Erro E0101: tpCaepf", "Corrigir tipo de inscrição", "Configuração do S-1005", "Erro"]
---

# E0101[eSocial/evtTabEstab/infoEstab/alteracao/dadosEstab/infoCaepf/tpCaepf] Elemento obrigatório estoque vazio.

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18047968878743) MENSAGEM:**

E0101 [eSocial/evtTabEstab/infoEstab/alteracao/dadosEstab/infoCaepf/tpCaepf] Elemento obrigatório estão vazio. Reveja o manual ou a Documentação do sistema.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18047960259351) SITUAÇÃO:**

Foi identificado que S-1005 estava puxando o CPF do responsável pela empresa, no entanto o registro fiscal demostrava o tipo de inscrição como CAEPF.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18047976023063) SOLUÇÃO:**

Acesse a tela **Preferências** Configurações » Avançado » Preferências, informe a chave do parâmetro **FPENVOBRA1005 - Enviar obras cadastradas como lotação no S-1005** e ligue o mesmo.

![Imagem 4: Acesse a tela Preferências Configurações » Avançado » Preferências , informe a chave do parâmetro FPENVOBRA1005 -…](https://ajuda.sankhya.com.br/hc/article_attachments/18047869873303)

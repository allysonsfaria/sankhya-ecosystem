---
id: "9144499962775"
titulo: "Nota XXXX já foi enviada mas o resultado ainda não foi obtido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9144499962775-Nota-XXXX-j%C3%A1-foi-enviada-mas-o-resultado-ainda-n%C3%A3o-foi-obtido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:10:09Z"
rotulos: ["Configuração", "Impostos", "CORE_E00547", "Prefeituras", "NFS-e", "resuma esse texto com um titulo e um conjunto de 3 palavras chaves :", "Erro"]
---

# Nota XXXX já foi enviada mas o resultado ainda não foi obtido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19276632494103) MENSAGEM:**

[CORE\_E00547] Nota XXXX já foi enviada mas o resultado ainda não foi obtido. Favor utilizar a opção Buscar autorização.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19276632496279) SITUAÇÃO:**

Ao tentar emitir uma NFS-e a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19276632497175) CAUSA:**

Ocorre ao emitir nota RPS.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19276592897431) SOLUÇÃO:**

- Verifique se o serviço está devidamente configurado para reter ISS.

![Imagem 5: Verifique se o serviço está devidamente configurado para reter ISS.](https://ajuda.sankhya.com.br/hc/article_attachments/9143899036055)

Em casos de emissão como RPS, verifique alguns pontos:

1. A nota será negada por limite de tentativa, não sairá da API, e será emitida em ambiente de Homologação com o sequencial zero:
2. A série informada no cadastro da empresa está incorreta, enviando **NF-e** deve ser **1;**
3. **Para emissões no ambiente de produção, libere o RPS na prefeitura.**

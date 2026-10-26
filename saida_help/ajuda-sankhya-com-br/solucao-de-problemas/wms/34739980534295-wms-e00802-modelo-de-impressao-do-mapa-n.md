---
id: "34739980534295"
titulo: "WMS_E00802: Modelo de impressão do mapa não foi configurado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34739980534295-WMS-E00802-Modelo-de-impress%C3%A3o-do-mapa-n%C3%A3o-foi-configurado"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:26:46Z"
rotulos: ["Configuração", "Relatórios", "WMS", "Estoque", "Preferências", "Mapa de Separação Manual", "WMS_E00802 - Modelo de impressão do mapa não foi configurado", "RELMAPSEPMANPED", "WMS_E00802", "Modelo de impressão do mapa não foi configurado"]
---

# WMS_E00802: Modelo de impressão do mapa não foi configurado

**MENSAGEM**

[WMS\_E00802] O modelo de impressão do mapa não foi configurado.

**SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta **gerar um mapa de separação** no sistema WMS, mas o relatório de separação manual não foi devidamente configurado no parâmetro correspondente.

**SOLUÇÃO**

**(1)** Acesse o **Sankhya Place** e selecione a aba **"Pacotes"**.

**(2)** Pesquise por **"Mapa de Separação Manual"** e instale o pacote.

**(3)** Acesse a tela **"Relatórios Formatados"** (Configurações » Avançado » Relatórios Formatados).

**(4)** Pesquise o relatório **"Mapa de Separação Manual"** baixado do Place e anote o número do relatório.

**(5)** Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências).

**(6)** Busque pelo parâmetro **"RELMAPSEPMANPED"** e informe o número do relatório anotado no passo 4.

**CAUSA**

A mensagem é exibida porque o **parâmetro "RELMAPSEPMANPED"** não possui um relatório de separação manual configurado, impedindo a geração do mapa de separação no sistema WMS.

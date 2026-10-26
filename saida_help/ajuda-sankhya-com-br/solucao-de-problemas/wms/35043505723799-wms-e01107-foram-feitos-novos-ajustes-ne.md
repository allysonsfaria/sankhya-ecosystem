---
id: "35043505723799"
titulo: "WMS_E01107: foram feitos novos ajustes neste inventário. O ajuste só pode ser desfeito após desfazer os ajustes mais recentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35043505723799-WMS-E01107-foram-feitos-novos-ajustes-neste-invent%C3%A1rio-O-ajuste-s%C3%B3-pode-ser-desfeito-ap%C3%B3s-desfazer-os-ajustes-mais-recentes"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:26:07Z"
rotulos: ["WMS", "Histórico de Ajuste de Estoque", "Estoque", "Erro", "Foram feitos novos ajustes neste inventário", "inventário", "WMS_E01107", "O ajuste só pode ser desfeito após desfazer os ajustes mais recentes"]
---

# WMS_E01107: foram feitos novos ajustes neste inventário. O ajuste só pode ser desfeito após desfazer os ajustes mais recentes

**MENSAGEM**

[WMS\_E01107] Foram feitos novos ajustes neste inventário. O ajuste só pode ser desfeito após desfazer os ajustes mais recentes.

**SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta **desfazer um ajuste de inventário** que possui **ajustes posteriores** vinculados ao mesmo inventário no sistema WMS.

**SOLUÇÃO**

**(1)** Acesse a tela **"Histórico de Ajuste de Estoque"** (WMS » Inventário » Histórico de Ajuste de Estoque).

**(2)** Identifique o **inventário** que está tentando desfazer o ajuste.

**(3)** Valide o **número de ajuste** vinculado ao inventário.

**(4)** Verifique se existem **ajustes posteriores** gerados para o mesmo inventário.

**(5)** Desfaça primeiro o **ajuste mais recente** gerado.

**(6)** Continue desfazendo os ajustes na **sequência inversa** até chegar ao ajuste desejado.

**CAUSA**

A mensagem é exibida porque existem **múltiplos ajustes** gerados para o mesmo inventário posteriormente ao ajuste que está sendo desfeito. O sistema exige que os ajustes sejam desfeitos em **ordem cronológica inversa** para manter a integridade dos dados de estoque.

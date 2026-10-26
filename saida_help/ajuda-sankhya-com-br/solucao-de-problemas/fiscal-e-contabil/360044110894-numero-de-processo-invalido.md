---
id: "360044110894"
titulo: "Número de processo inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110894-N%C3%BAmero-de-processo-inv%C3%A1lido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:54Z"
rotulos: ["Configuração", "Fiscal", "SEFAZ", "MS1196", "Número de processo inválido devido a pontos ou traços", "Ajuste o campo \"Nro. do Processo\" removendo pontos e traços", "Transmita novamente o Reinf após ajustes.", "Erro", "EFD-REINF"]
---

# Número de processo inválido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16334603679383) MENSAGEM:**

[MS1196]: Número de processo inválido.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16334588879383) SITUAÇÃO:**

Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16334588881175) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Livros Fiscais » Arquivos » Processos Administrativos Judiciais](https://ajuda.sankhya.com.br/hc/article_attachments/16334603699479) Acesse: Livros Fiscais » Arquivos » Processos Administrativos Judiciais

- Campo **"Nro. do Processo"**: ajuste o valor nesse campo, retirando .(ponto) e -(traços).

Exemplo:

De: 922-41.2012.4.01.3303

Para: **00009224120124013303**

Salve o registro.

![Imagem 5: Após os ajustes, transmita novamente o Reinf.](https://ajuda.sankhya.com.br/hc/article_attachments/16334603701527) Após os ajustes, transmita novamente o Reinf.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16334588889879) CAUSA:**

Ocorre quando o Nro do processo está informado um valor inválido, geralmente .(ponto), -(traços), que invalidam o campo.

---
id: "4406422486679"
titulo: "Solução do erro: Número de processo inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4406422486679-Solu%C3%A7%C3%A3o-do-erro-N%C3%BAmero-de-processo-inv%C3%A1lido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:22:20Z"
rotulos: ["Configuração", "EFD", "#BaseantigaJiva", "Mensagem: Número de processo inválido [MS1196].", "Solução: Remova pontos e traços do campo \"Nro. do Processo\" e salve.", "Causa: Erro ocorre devido a formatação inválida do número do processo.", "Erro", "Documentos Eletrônicos", "Reinf"]
---

# Solução do erro: Número de processo inválido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16428965625367) MENSAGEM:**

[MS1196]: Número de processo inválido

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16428965628439) SOLUÇÃO:**

Para correção seguir os passos abaixo:

![Imagem 3: Acesse a tela " Processos Administrativos Judiciais " (Caminho de acesso: Livros Fiscais » Arquivos » Processos…](https://ajuda.sankhya.com.br/hc/article_attachments/16428965630615) Acesse a tela "**[Processos Administrativos Judiciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608094)"** (Caminho de acesso: Livros Fiscais » Arquivos » Processos Administrativos Judiciais)

Campo: "**Nro. do Processo"**: Ajuste o valor nesse campo, retirando .(ponto) e -(traços)

Exemplo:

De:922-41.2012.4.01.3303

Para: **00009224120124013303**

Salve o registro.

![Imagem 4: Salve o registro.](https://ajuda.sankhya.com.br/hc/article_attachments/14627894546455)

**(2)** Após os ajustes, transmita novamente o Reinf.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16428949870359) CAUSA:**

Ao transmitir as informações do R2010 do EFD-Reinf, ocorre o erro. Acontece quando o número do processo está informado com um valor inválido, geralmente .(ponto), -(traços), que invalida o campo.

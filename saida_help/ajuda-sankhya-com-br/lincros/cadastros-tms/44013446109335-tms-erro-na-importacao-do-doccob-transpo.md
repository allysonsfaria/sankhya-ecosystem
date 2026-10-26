---
id: "44013446109335"
titulo: "[TMS] - Erro na Importação do DOCCOB: Transportadora sem Padrão EDI Definido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013446109335--TMS-Erro-na-Importa%C3%A7%C3%A3o-do-DOCCOB-Transportadora-sem-Padr%C3%A3o-EDI-Definido"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:58:00Z"
rotulos: ["sync_hc", "lincros", "sync_hash_0db23fd831fb", "lincros_13432430"]
---

# [TMS] - Erro na Importação do DOCCOB: Transportadora sem Padrão EDI Definido

**1 - Problema Relatado pelo Cliente**: O cliente relatou que a transportadora não está importando o DOCCOB e que o sistema apresenta o erro: "A transportadora "x" sem padrão EDI definido". O cliente solicitou orientações para solucionar o problema.

![Imagem 1: 1 - Problema Relatado pelo Cliente : O cliente relatou que a transportadora não está importando o DOCCOB e que o…](https://ajuda.sankhya.com.br/hc/article_attachments/44013422632087)

## 2 - Passo a Passo para Resolver o Problema:

1. ## Acessar o Cadastro da Transportadora

   - No menu principal do TMS, navegue até:
     Cadastros Gerais > Transportadoras > Transportadora Empresa > Cadastro
2. ## Localizar a Transportadora

   - Na tela de cadastro, localize a transportadora usando os filtros disponíveis (CNPJ ou Nome).
   - CLique no código da transportadora para abrir a tela de edição da mesma
3. ## Definir o Padrão EDI

   - Na tela de cadastro da transportadora, localize o campo "EDI Padrão".
   - ![Imagem 2: Na tela de cadastro da transportadora, localize o campo "EDI Padrão".](https://ajuda.sankhya.com.br/hc/article_attachments/44013467221143)
   - Selecione o padrão EDI correto utilizado pela transportadora (geralmente EDI Padrão Proceda 3.0 (Com CONEMB) ou EDI Padrão Proceda 3.0a (Com CONEMB) ou Padrão Proceda 5.0 (Com CONEMB 3.1)).
4. ## Salvar as Alterações

   - Após definir o padrão EDI, clique em "Salvar" para confirmar as alterações.
5. ## Importar o Arquivo EDI Novamente

   - Acesse o menu de importação:
     Operacional > Importação > EDI > Importação
   - ![Imagem 3: Acesse o menu de importação: Operacional > Importação > EDI > Importação](https://ajuda.sankhya.com.br/hc/article_attachments/44013453227799)
   - Realize a importação do arquivo EDI novamente.

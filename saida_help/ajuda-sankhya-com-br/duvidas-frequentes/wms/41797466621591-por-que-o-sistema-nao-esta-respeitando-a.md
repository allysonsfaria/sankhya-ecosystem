---
id: "41797466621591"
titulo: "Por que o sistema não está respeitando a área de armazenagem configurada e não está sugerindo o armazenamento no endereço vinculado a essa área?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41797466621591-Por-que-o-sistema-n%C3%A3o-est%C3%A1-respeitando-a-%C3%A1rea-de-armazenagem-configurada-e-n%C3%A3o-est%C3%A1-sugerindo-o-armazenamento-no-endere%C3%A7o-vinculado-a-essa-%C3%A1rea"
trilha: "Dúvidas Frequentes > WMS"
atualizado_em: "2026-10-07T21:09:57Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Configuração de Armazenagem", "Endereços Vazios", "Completar Endereços", "WMS - KCS", "Prioriza pulmões vinculados ao produto", "Armazenagem"]
---

# Por que o sistema não está respeitando a área de armazenagem configurada e não está sugerindo o armazenamento no endereço vinculado a essa área?

Para que o sistema entenda que deve gerar tarefas para os pulmões vinculados à área de armazenagem do grupo do produto, é necessário marcar a opção **“Prioriza pulmões vinculados ao produto”** nas opções **“Endereços vazios”**, **“Completar endereços”** e **“UMA”**, caso estejam ativas dentro da regra padrão de armazenagem, na rotina **''Configuração de Armazenagem''** (WMS » Rotinas » Configuração de Armazenagem).

Isso ocorre porque a área de armazenagem é considerada pelo sistema apenas para geração de tarefas direcionadas a endereços de armazenagem do tipo pulmão.

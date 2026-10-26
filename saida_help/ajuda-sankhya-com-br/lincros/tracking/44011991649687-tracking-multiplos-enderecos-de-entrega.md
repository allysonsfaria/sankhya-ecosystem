---
id: "44011991649687"
titulo: "[Tracking] - Múltiplos Endereços de Entrega"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011991649687--Tracking-M%C3%BAltiplos-Endere%C3%A7os-de-Entrega"
trilha: "Lincros > Tracking"
atualizado_em: "2026-10-05T19:16:03Z"
rotulos: ["sync_hc", "lincros", "lincros_13434637", "sync_hash_a84b955cd50b"]
---

# [Tracking] - Múltiplos Endereços de Entrega

**Menu**: Tracking > Cadastros > Cadastros de Clientes

**Objetivo**: A partir da versão **4.19** do Tracking[,](https://lincros.movidesk.com/kb/article/250073/tracking-versao-419?menuId=6325-65828-250073&ticketId=&q=),) foi disponibilizada a melhoria Possibilitar que o ponto de interesse do cliente seja atualizado com base na entrega. Com ela, passa a ser possível associar mais de um endereço de entrega em um cliente no Tracking.
Com este artigo, vamos compreender este funcionamento.

**Considerações**:

- Esta funcionalidade está disponível à partir da versão **4.19** do Tracking (Release Notes: <https://lincros.movidesk.com/kb/article/250073/tracking-versao-419?menuId=6325-65828-250073&ticketId=&q=>[)](https://lincros.movidesk.com/kb/article/250073/tracking-versao-419?menuId=6325-65828-250073&ticketId=&q=),)

Sempre que recebermos um endereço para um cliente na integração de uma rota, que seja diferente do endereço já registrado no cadastro dentro do Tracking, este endereço será **ADICIONADO** no campo 'Locais de Entrega' dentro do cadastro do cliente, e o lacre de ponto de interesse será aberto.

O Tracking irá verificar se esse novo endereço está fora ou dentro do raio do cliente. Caso esteja dentro, o endereço que veio na entrega será ignorado e o endereço atual permanecerá no cadastro. Caso esteja fora do raio do cliente, será criado um novo local de entrega.

A cada novo endereço/local de entrega cadastrado, o ponto de interesse será deslacrado, e será necessário que a equipe de monitoramento valide o endereço e lacre o ponto de interesse novamente, caso necessário.

![Imagem 1: A cada novo endereço/local de entrega cadastrado, o ponto de interesse será deslacrado, e será necessário que a equipe…](https://ajuda.sankhya.com.br/hc/article_attachments/44011978056855)

Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos.

---
id: "25761385774999"
titulo: "Saiba mais sobre 'Completar endereços' e 'Endereços vazios' para o campo Preferir Endereços como 'Maior proximidade do Picking'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25761385774999-Saiba-mais-sobre-Completar-endere%C3%A7os-e-Endere%C3%A7os-vazios-para-o-campo-Preferir-Endere%C3%A7os-como-Maior-proximidade-do-Picking"
trilha: "Dúvidas Frequentes > WMS"
atualizado_em: "2026-07-22T14:44:36Z"
rotulos: ["Configuração", "WMS", "Estoque", "Preferências", "Completar endereços", "Endereços vazios", "Maior proximidade do Picking", "Armazenagem"]
---

# Saiba mais sobre 'Completar endereços' e 'Endereços vazios' para o campo Preferir Endereços como 'Maior proximidade do Picking'

Para funcionamento correto da regra de armazenagem com a marcação 'Maior proximidade do picking', é necessário utilizar o campo **"Ordem"** da rotina **"Endereço de armazenamento"**(Caminho: WMS » Cadastros » Endereço de Armazenamento) de todos os endereço, para definir a maior proximidade do endereço pulmão com o endereço de picking. Pois, o sistema valida a distância entre endereços para identificar o pulmão mais próximo do picking através da ordem nos endereços de armazenamento.

**Exemplo:**
 
**Endereço de picking:** campo ordem 155.
 
**'Maior proximidade do picking':** endereço pulmão que possui ordem mais próximo como um endereço pulmão cadastrado campo ordem 156.

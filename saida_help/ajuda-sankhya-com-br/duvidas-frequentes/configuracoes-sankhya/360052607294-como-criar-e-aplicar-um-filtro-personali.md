---
id: "360052607294"
titulo: "Como criar e aplicar um filtro personalizado de consulta de OS de maneira assertiva"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052607294-Como-criar-e-aplicar-um-filtro-personalizado-de-consulta-de-OS-de-maneira-assertiva"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:29:04Z"
rotulos: ["Configuração", "Consulta", "Filtro", "Ordem de Serviço", "#AGUARDANDOVALIDAÇÃO", "#formatadoroger", "Filtros Personalizados para Consulta de OS"]
---

# Como criar e aplicar um filtro personalizado de consulta de OS de maneira assertiva

#### Neste artigo, vamos auxiliar na criação; manutenção e uso de um filtro para dinamizar a consulta na tela de 'Consulta de OS'.

Visando encontrar com palavras-chave o que se busca, tanto na Descrição(Cabeçalho da OS), quanto nas(Soluções), Sub-itens da OS.

**Vejamos**:

- Acesse a tela > Consulta de OS > Clique no botão para criar Filtro
- De um nome ao filtro
- Clique em 'Modo Avançado'
- Copie o filtro abaixo e cole: [Exemplo de filtro]

UPPER(ItemOrdemServico.DESCSERV) LIKE UPPER('%?%') OR
UPPER(ItemOrdemServico.SOLUCAO) LIKE UPPER('%?%')

- Salve o novo filtro, volte para a tela de Consulta de OS, selecione o filtro criado e clique em Aplicar.

**Dica**: Para usar combinações de palavras, frases, mensagens de erros, pode-se usar o carácter %, como separador, exemplo:

Problema: **%icms%C100%**
Solução: **%icms%C100%**

[GIF animado: Imagem 1: Problema: %icms%C100% Solução: %icms%C100%](https://ajuda.sankhya.com.br/hc/article_attachments/360089682293)

 Demais detalhes de como refinar a consulta, utilizando os filtros rápidos, executantes, acesse o Ajuda desta Rotina.

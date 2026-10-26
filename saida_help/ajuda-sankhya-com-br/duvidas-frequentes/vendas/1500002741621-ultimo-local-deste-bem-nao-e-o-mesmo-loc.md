---
id: "1500002741621"
titulo: "Último Local deste Bem não é o mesmo Local informado no item da nota. Saiba mais! "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002741621-%C3%9Altimo-Local-deste-Bem-n%C3%A3o-%C3%A9-o-mesmo-Local-informado-no-item-da-nota-Saiba-mais"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-09-23T12:44:22Z"
rotulos: ["Configuração", "NF-e", "Estoque", "não apagar", "#publicadoHyago", "CORE_E06241", "Erro"]
---

# Último Local deste Bem não é o mesmo Local informado no item da nota. Saiba mais! 

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16304527390103) MENSAGEM**:

Produto: XXXX Bem: XXXXX         
[CORE\_E06241] Último Local deste Bem não é o mesmo Local informado no item da nota.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16304527394967) SOLUÇÃO:**

Na confirmação de uma nota de venda para bens do imobilizado existe uma validação do local de saída (TGFITE) com o último local de movimentação do bem (TCIIBE). Quando o local é diferente e a data de aquisição do bem for menor que o parâmetro **"DTINICVALLOCBEM"**, que é uma data, o sistema faz a validação, porém permite confirmar a nota.

**"DTINICVALLOCBEM - Data de Início da Validação do Local do Bem"**

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16304527399191) CAUSA:**

Nota de entrada (compra) do bem com local diferente do local da  nota em que o bem esta saindo (venda).

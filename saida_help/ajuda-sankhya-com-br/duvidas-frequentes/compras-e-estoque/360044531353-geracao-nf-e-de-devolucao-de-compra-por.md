---
id: "360044531353"
titulo: "Geração NF-e de devolução de compra por empresas não contribuintes do IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044531353-Gera%C3%A7%C3%A3o-NF-e-de-devolu%C3%A7%C3%A3o-de-compra-por-empresas-n%C3%A3o-contribuintes-do-IPI"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T15:55:22Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "IPI", "Impostos", "TOP", "Nota de Compra", "Destaque de IPI", "Ajustes de Configuração"]
---

# Geração NF-e de devolução de compra por empresas não contribuintes do IPI

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17004564426519) SOLUÇÃO:**

Para correção, siga as orientações abaixo:

![Imagem 2: Acesse: Comercial » Consulta » Portal de Compras >>Nota de COMPRA (Com IPI Destacado)](https://ajuda.sankhya.com.br/hc/article_attachments/17004564429463) Acesse: Comercial » Consulta » Portal de Compras >>Nota de COMPRA [Com IPI Destacado]

A Nota de Entrada deve estar registrada no sistema com os IPI devidamente calculados e destacados em campos próprios.

![Imagem 3: Acesse: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/17004535205143) Acesse: Comercial » Preferências » Empresa

- Aba: **"Propriedades"**
- Campo **"Trabalha com IPI?":** desmarcado
- Código Sit. Trib. IPI Saída [(-1)-Não sujeita ao IPI]

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/17004535206679) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Aba **"Impressão",** Campo **"NF-e":** devolução
- TOP de Devolução de Compra [E-Devolução de Compra]
- Aba: **"Impostos"**
- Campo **"Calculo de ICMS, IPI, ISS":** Não Calcula e digita
- **"Tem IPI":** marcado
- **"Somar IPI ao total da nota":** marcado
- **"Código Sit.Trib.IPI Saída":** - 1 Não Sujeito ao IPI
- **"Somar ST ao total da nota":** quando se tratar de uma devolução que há calculo ST, com CST que incide/destaca esse imposto

![Imagem 5: Acesse: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/17004535210135) Acesse: Configurações » Cadastros » Produtos » Produtos

- Aba: **"Impostos"**
- Campo **"Tem IPI na Venda":** desmarcado

![Imagem 6: Acesse: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/17004564445847) Acesse: Configurações » Cadastros » Parceiros

- Aba: **"Fiscal"**
- Campo **"Tem IPI":** marcado

![Imagem 7: Acesse: Comercial » Consulta » Portal de Compras Pesquise pela Nota de Compra, selecione-a, depois clique no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/17004564450967) Acesse: Comercial » Consulta » Portal de Compras
Pesquise pela Nota de Compra, selecione-a, depois clique no botão **"Devolv./Estor"**.

![Imagem 8: Selecione a TOP de Devolução de Compra, ajustada conforme instruções no item 3. Verifique nos itens a incidência do CST…](https://ajuda.sankhya.com.br/hc/article_attachments/17004564453015) Selecione a TOP de Devolução de Compra, ajustada conforme instruções no item 3. Verifique nos itens a incidência do CST de IPI, Base de IPI/Aliq. de IPI e Valor de IPI e no rodapé as informações de Base e Valor de IPI.

- Ao gerar a nota de devolução neste formato, o sistema trata o IPI destacado na nota de devolução como IPI de devolução e não como IPI normal.
- No item da nota, a tag <vIPI> será gerada com valor zero e a tag <vIPIDevolv> passa a ser gerada, somando o IPI ao total da nota.

**![Imagem 9: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17004564459159) IMPORTANTE:**

Caso seja necessário que os valores de IPI sejam gerados na**tag <vOutro>**, quando a nota de origem os possuir, marque a opção abaixo no 'Tipo de Operação' utilizado na respectiva devolução:

- Tela **"Tipos de Operação - TOP'** (Caminho de acesso: Comercial » Arquivo » Cadastros)
- Aba **"Impostos**", campo **"Devolver sem destacar IPI".**

Realizada a marcação acima, refaça o lançamento de devolução.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17004564465303)CAUSA:**

A empresa **não** trabalha com IPI e recebe uma nota de entrada com IPI em alguns itens, não permitindo o destaque nos campos próprios do IPI, sendo necessário a geração dos valores no grupo de tributos devolvidos do XML .

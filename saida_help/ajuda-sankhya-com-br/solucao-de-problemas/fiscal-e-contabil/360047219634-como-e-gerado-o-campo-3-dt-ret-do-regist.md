---
id: "360047219634"
titulo: "Como é gerado o Campo 3 - DT_RET do Registro F600  - EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360047219634-Como-%C3%A9-gerado-o-Campo-3-DT-RET-do-Registro-F600-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:31:58Z"
rotulos: ["Configuração", "Fiscal", "Movimentação Financeira", "Impostos", "avulsa", "NFS-e", "EFD Contribuições", "Preenchimento dependente de impostos retidos", "Detalhes específicos por tipo de imposto", "Destaque na NFS-e"]
---

# Como é gerado o Campo 3 - DT_RET do Registro F600  - EFD Contribuições

**(1)** Condições para preenchimento deste campo:

- **Se** os impostos forem retidos na nota, será considerada a data de negociação, para preenchimento do DT\_RET;
- **Se** os impostos forem retidos no financeiro, sempre será considerada a data da baixa.

**(1)** Configurações dos impostos retidos:

![Imagem 1: Na tela "Impostos" (Caminho de acesso: Configurações » Cadastros » Impostos) , configure cada imposto individualmente…](https://ajuda.sankhya.com.br/hc/article_attachments/16532006422295) Na tela **"Impostos"** (Caminho de acesso: Configurações » Cadastros » Impostos), configure cada imposto individualmente (não pode configurar o PCC como 'Outros', deve ser configurado PIS, depois COFINS, depois o CSLL);

![Imagem 2: Para destaque na nota e retenção no financeiro, as abas "Parceiro" , "TOP" e "Empresa" da tela " Impostos" , devem…](https://ajuda.sankhya.com.br/hc/article_attachments/16532035509655) Para destaque na nota e retenção no financeiro, as abas **"Parceiro"**, **"TOP"** e **"Empresa"** da tela "**Impostos"**, devem estar da seguinte forma:

- Na Nota = Já Incluso
- No Financeiro Origem Financeiro = Nenhum
- No Financeiro Origem Estoque = Subtrair

![Imagem 3: Ligue o parâmetro "DESTIMPNRETIDO - Destacar impostos federais na NFS-e mesmo quando não retidos" :](https://ajuda.sankhya.com.br/hc/article_attachments/16532006426903) Ligue o parâmetro **"DESTIMPNRETIDO - Destacar impostos federais na NFS-e mesmo quando não retidos"**:

![Imagem 4: Ligue o parâmetro "DESTIMPNRETIDO - Destacar impostos federais na NFS-e mesmo quando não retidos" :](https://ajuda.sankhya.com.br/hc/article_attachments/15604131575575)

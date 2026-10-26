---
id: "30787634799511"
titulo: "Ao gerar a nota de remessa o sistema não atualiza o 'Cód. de Benefício Fiscal na UF' automaticamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30787634799511-Ao-gerar-a-nota-de-remessa-o-sistema-n%C3%A3o-atualiza-o-C%C3%B3d-de-Benef%C3%ADcio-Fiscal-na-UF-automaticamente"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:34:43Z"
rotulos: ["Configuração", "NF-e", "Atualização", "Impostos", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Ao gerar a nota de remessa", "sistema não busca o 'Cód. de Benefício Fiscal na UF'", "automaticamente", "Documentos Eletrônicos"]
---

# Ao gerar a nota de remessa o sistema não atualiza o 'Cód. de Benefício Fiscal na UF' automaticamente

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30788814155287) **SITUAÇÃO:**

1. Ao confirmar uma nota de vendas que tem a top configurada para gerar remessa, o Cód. de Benefício Fiscal na UF não é atualizado automaticamente, se alterar o item o valor é calculado.

![Imagem 2: Ao confirmar uma nota de vendas que tem a top configurada para gerar remessa, o Cód. de Benefício Fiscal na UF não é…](https://ajuda.sankhya.com.br/hc/article_attachments/30788773556631)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30787634794391)SOLUÇÃO:**

Acesse a tela **"Empresa"**  (Comercial > Preferências > Empresa), vá até a aba **"Documentos eletrônicos",** depois clique na sub aba **"NFe/NFC-e"**, em seguida escolha a sub aba **"NF-e"** e marque a opção:

- **"Atualização Cód. Beneficio no Faturamento pelo Produto":** Sempre Atualizar

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30787633531927)CAUSA:**

Esse problema acontece porque o campo Atualização do cód. do benefício no faturamento pelo produto está configurado para Não Atualizar nas preferências da Empresa.

Ainda que a remessa não esteja sendo gerada pelo processo de faturamento, o campo Atualização do cód. do benefício no faturamento pelo produto tem o mesmo comportamento. Para mais informações, acesse: [Cadastro de Benefícios - cBenef Código de Benefício Fiscal – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/23459567355543-Cadastro-de-Benef%C3%ADcios-cBenef-C%C3%B3digo-de-Benef%C3%ADcio-Fiscal)

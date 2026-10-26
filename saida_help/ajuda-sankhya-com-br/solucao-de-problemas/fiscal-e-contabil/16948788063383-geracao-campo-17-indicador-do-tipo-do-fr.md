---
id: "16948788063383"
titulo: "Geração campo 17 \"Indicador do tipo do frete\" no D100 (EFD-ICMS/IPI e EFD CONTRIBUIÇÕES)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16948788063383-Gera%C3%A7%C3%A3o-campo-17-Indicador-do-tipo-do-frete-no-D100-EFD-ICMS-IPI-e-EFD-CONTRIBUI%C3%87%C3%95ES"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:54:09Z"
rotulos: ["CT-e", "Configuração", "Fiscal", "NF-e", "EFD", "Financeiro", "EFD Contribuições", "Origem e Entrada: Campo frete = 1", "Frete Zero: Campo frete = 9", "Parceiro Não Satisfeito: Campo frete = 2"]
---

# Geração campo 17 "Indicador do tipo do frete" no D100 (EFD-ICMS/IPI e EFD CONTRIBUIÇÕES)

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16948802517271)SOLUÇÃO:**

Para as seguintes versões de layout:

- EFD-ICMS/IPI, versão de layout 5 ou superior
- EFD CONTRIBUIÇÕES, versão de layout 2 ou superior

O sistema tem o seguinte comportamento para construção do Tipo de Frete (Apresentando em forma hierárquica):

**(1)** Se a origem for financeira, o campo fica = 1

**(1)** Se for uma entrada, também será = 1

**(1)** Se o valor do frete estiver com valor 0, fica = 9

**(1)** Se o parceiro do CT-E for igual ao destinatário, fica = 1

**(1)** Se o parceiro da nota for igual remetente = 0

**(1)** E se nenhuma das condições acima forem satisfeitas, o sistema vai lançar a opção 2 no campo 17   (Indicador do tipo do frete) do registro D100 dos EFD's.

---
id: "7066461017239"
titulo: "Geração do Registro F550 - EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7066461017239-Gera%C3%A7%C3%A3o-do-Registro-F550-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:15:17Z"
rotulos: ["Configuração", "Impostos", "Estoque", "Financeiro", "EFD Contribuições", "Validação Documentos Receita", "Registro F550 Lucro Presumido", "Configuração EFD Contribuições"]
---

# Geração do Registro F550 - EFD Contribuições

Será abordado nesse artigo algumas informações pertinentes à geração do registro F550.

"Registro específico para a pessoa jurídica submetida ao regime de apuração com base no lucro presumido, optante
pela apuração da contribuição para o PIS/Pasep e da COFINS pelo regime de competência, conforme previsto na Lei
nº 9.718, de 1998.

Este registro tem por objetivo representar a escrituração e tratamento fiscal das receitas auferidas no período,
independente de seu recebimento ou não, segmentado por Código de Situação Tributária - CST, do PIS/Pasep e da
Cofins. (Fonte: Guia Prático)"

#### Veja as configurações:

**Preferências da Empresa:**
Aba **"EFD - Escrituração Fiscal Digital"**:
Campo **"Tipo de Escrituração"** marcado como **"EFD CONTRIBUIÇÕES"**.
Na aba **"Blocos e Registros"**, ajuste na seção **"Bloco"** o bloco F e na seção **"Registros"** configure:

**F001**
**F010**
**F550**
**F560**
**F990**

![Imagem 1: F001 F010 F550 F560 F990](https://ajuda.sankhya.com.br/hc/article_attachments/16488751189911)

Aba **"Regime de Apuração da Contrib. Social e Aprop. Crédito"**:
Campos:
**"Dt.Inicial Regime"**: deve ter uma configuração que abranja o período de geração do EFD CONTRIBUIÇÕES.
**"Incidência tributária"**: Incidência Exclusivamente no regime cumulativo;
**"Lucro Presumido/Critério Apuração"**: Regime de competência - Escrituração consolidada registro F550;

![Imagem 2: Aba "Regime de Apuração da Contrib. Social e Aprop. Crédito" : Campos: "Dt.Inicial Regime" : deve ter uma configuração…](https://ajuda.sankhya.com.br/hc/article_attachments/16488751193111)

Agora confira a análise de algumas validações para a geração dos documentos no F550, tanto com origem Estoque, quanto com origem Financeira:

![Imagem 3: Deve se tratar de documentos geradores de Receitas;](https://ajuda.sankhya.com.br/hc/article_attachments/16488751195927) Deve se tratar de documentos geradores de Receitas;

![Imagem 4: Não pode ser título de "Provisão" financeira, no caso, deve ser título de receita;](https://ajuda.sankhya.com.br/hc/article_attachments/16488751197719) Não pode ser título de "Provisão" financeira, no caso, deve ser título de receita;

![Imagem 5: A TOP deve estar marcada para calcular PIS/COFINS;](https://ajuda.sankhya.com.br/hc/article_attachments/16488705065111) A TOP deve estar marcada para calcular PIS/COFINS;

![Imagem 6: Para documentos financeiros com origem financeira, no cadastro de Natureza, o regime "Regime (EFD PIS/COFINS)" deve…](https://ajuda.sankhya.com.br/hc/article_attachments/16488705068183) Para documentos financeiros com origem financeira, no cadastro de Natureza, o regime **"Regime (EFD  PIS/COFINS)"** deve estar com uma das seguintes opções:
Regime de Competência (Dt.Negociação)
Regime de Competência (Dt.Entrada/Saída)

![Imagem 7: Para documentos com origem "Estoque" é obrigatório a presença de "Financeiro" vinculado à nota, e esse financeiro deve…](https://ajuda.sankhya.com.br/hc/article_attachments/16488705070487) Para documentos com origem "Estoque" é obrigatório a presença de "Financeiro" vinculado à nota, e esse financeiro deve estar devidamente configurado no campo "Regime (EFD PIS/COFINS)".

![Imagem 8: Para documentos com origem "Estoque" é obrigatório a presença de "Financeiro" vinculado à nota, e esse financeiro deve…](https://ajuda.sankhya.com.br/hc/article_attachments/16488751206935)

**Observações:**

**(1)** A aba **"Natureza x PIS/COFINS x Empresa"** da tela **"Naturezas de Receitas e Despesas"** só é observada para a geração de documento Financeiros com origem Financeira.

**(1)** Os documentos com origem "Estoque" não observam o rateio para a geração do F550, pegando apenas as informações presentes na tela: grade de itens> botão outras opções > consultar/alterar dados dos impostos dos itens proporcional.

**(1)** Se na nota houver diferença de CST entre o PIS/COFINS para cada item (situação que já se trata de um erro, pois deve ser o mesmo CST entre PIS/COFINS para cada item), o sistema vai acabar gerando o F550 em duplicidade para os documentos gerados, e deve então ser ajustado essa informação na nota.

**(1)** Títulos financeiros de destino em processo de Renegociação não serão gerados no registro, apenas as origens da renegociação.

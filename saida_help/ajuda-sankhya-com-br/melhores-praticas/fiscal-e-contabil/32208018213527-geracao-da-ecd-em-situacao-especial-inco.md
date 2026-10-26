---
id: "32208018213527"
titulo: "Geração da ECD em situação especial - Incorporação/ Incorporadora"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32208018213527-Gera%C3%A7%C3%A3o-da-ECD-em-situa%C3%A7%C3%A3o-especial-Incorpora%C3%A7%C3%A3o-Incorporadora"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:31:53Z"
rotulos: ["Configuração", "Empresa", "ECD", "Fiscal", "incorporação cisão fusão ou extinção", "ECD - Escrituração Contábil Digital", "Geração de arquivo - ECD", "Geração da ECD em situação especial - Incorporação/ Incorporadora", "ECD para o mesmo CNPJ", "naturezas diferentes de escrituração", "Situação Especial"]
---

# Geração da ECD em situação especial - Incorporação/ Incorporadora

Em situações especiais, como **incorporação, cisão, fusão ou extinção**, **deverá ser transmitido mais de uma ECD para o mesmo CNPJ no mesmo ano-calendário. No entanto, cada uma deve ter naturezas diferentes de escrituração** e obedecer regras específicas.

![Imagem 1: Em situações especiais, como incorporação, cisão, fusão ou extinção , deverá ser transmitido mais de uma ECD para o…](https://ajuda.sankhya.com.br/hc/article_attachments/32481121676055)

![Imagem 2: Em situações especiais, como incorporação, cisão, fusão ou extinção , deverá ser transmitido mais de uma ECD para o…](https://ajuda.sankhya.com.br/hc/article_attachments/32481121676951)

### Exemplo prático: Incorporação em 15/07/2024

#### **(1)** Arquivo 1

**(2)**Os **campos de situação especial e data do evento** no registro 0000 devem estar preenchidos corretamente na empresa incorporadora. Para isso, acesse a tela **"Empresa"**(Contabilidade » Preferências » Empresa), vá até a aba **"ECD - Escrituração Contábil Digital"**, em seguida, sub-aba **"Situação Especial"**e informe a data e a situação especial.

![Imagem 3: (2) Os campos de situação especial e data do evento no registro 0000 devem estar preenchidos corretamente na empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/32481121678103)

**(2)**Depois, vá até a tela **"Geração de arquivo - ECD"** (Contabilidade » Conexão » ECD » Geração de Arquivo - ECD) e informe a data. **Importante destacar que a data limite deve ser a data em que aconteceu a situação especial.**

**(2)**Em seguida, no campo **"Indicador de sit. início do período"** informe opção **"0 - Normal ( Início do primeiro dia do ano)".**

![Imagem 4: (2) Em seguida, no campo "Indicador de sit. início do período" informe opção "0 - Normal ( Início do primeiro dia do…](https://ajuda.sankhya.com.br/hc/article_attachments/32481114536215)

|0000|LECD|01012023|15072023|EMPRESA TESTE|11111111000199|AM||3534401|99999|3|0|0|0||0|0||N|N|0|0|1|

Campo 11 – Situação Especial: 3 (corresponde a incorporação no período)

Campo 12 – Indicador de Situação no Início do Período: 0 (Normal)

#### **(1)** Arquivo 2

**(2)** Para geração do arquivo 2, não se informa a situação especial nas preferências da empresa. Informe somente na tela Geração de arquivo - ECD. **Atente-se para que a data inicial do arquivo 2 seja o primeiro dia posterior ao final da geração do arquivo 1** (por exemplo, como o arquivo 1 tinha data final 15/07/2024, a data inicial do arquivo 2 será 16/07/2024).

**(2)**E no campo Indicador de sit. início do períodos selecione a opção **"2 - Resultante de cisão/ fusão ou remanescente de cisão, ou realizou incorporação"**

![Imagem 5: (2) E no campo Indicador de sit. início do períodos selecione a opção "2 - Resultante de cisão/ fusão ou remanescente…](https://ajuda.sankhya.com.br/hc/article_attachments/32481121680663)

Campo 11 – Não há situação especial no período.

Campo 12 – Indicador de Situação no Início do Período: 2 (Resultante de cisão)

|0000|LECD|16072023|31122023|EMPRESA TESTE|11111111000199|AM||3534401|99999||2|0|0||0|0||N|N|0|0|1|

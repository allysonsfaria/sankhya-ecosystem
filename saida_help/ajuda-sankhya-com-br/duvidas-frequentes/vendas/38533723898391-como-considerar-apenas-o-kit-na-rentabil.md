---
id: "38533723898391"
titulo: "Como Considerar Apenas o Kit na Rentabilidade?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38533723898391-Como-Considerar-Apenas-o-Kit-na-Rentabilidade"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:01:26Z"
rotulos: ["Produtos", "Custos", "Configuração", "TOP", "considerar apenas o kit na rentabilidade", "rentabilidade", "kit"]
---

# Como Considerar Apenas o Kit na Rentabilidade?

Para que o cálculo de rentabilidade considere apenas o valor do kit e descarte os componentes individuais, é necessário realizar configurações específicas no parâmetro **"Considera Kit na TOP para Rentabilidade - CONSKITTOPGOL"** e no **"Tipo de Operação (TOP)"** utilizado na movimentação.

Esta configuração garante que o sistema calcule corretamente o faturamento e o Custo da Mercadoria Vendida (CMV) na análise de rentabilidade, evitando distorções nos valores quando produtos são vendidos como kits.

### Ativação do Parâmetro CONSKITTOPGOL

O primeiro passo é **ativar o parâmetro** **"Considera Kit na TOP para Rentabilidade - CONSKITTOPGOL"**. Este parâmetro influencia diretamente o cálculo do faturamento na rentabilidade, garantindo que o sistema considere os valores corretos quando trabalha com produtos do tipo kit.

Quando o **CONSKITTOPGOL** está desligado, o sistema pode calcular o faturamento incorretamente, considerando valores com casas decimais adicionais que distorcem a análise de rentabilidade.

### Configuração do Tipo de Operação

Após ativar o parâmetro, acesse o **"Tipo de Operação (TOP)"** (Comercial » Arquivo » Cadastros) utilizado na movimentação que deseja analisar na rentabilidade e realize a seguinte configuração:

**(1)**  Acesse a aba **"Impressão"** do Tipo de Operação. 

**(2)**  Localize o campo **"Kit/Componentes - Impressão e Livro Fiscal"**. 

**(3)**  Selecione a opção **"Kit"** neste campo. 

Com esta configuração, o sistema considerará apenas o custo do kit na rentabilidade. **Lembrando que é obrigatório existir linhas de custo para o Kit**.

### Impacto nas Notas Fiscais

É importante destacar que **esta configuração é histórica**, ou seja, ela afetará apenas as notas fiscais emitidas após a alteração. As notas já emitidas anteriormente manterão o comportamento da configuração que estava vigente no momento de sua emissão.

Portanto, ao analisar a rentabilidade, verifique se as notas foram emitidas com a configuração correta. Notas antigas podem apresentar valores diferentes dependendo de como o campo **"Kit/Componentes - Impressão e Livro Fiscal"** estava configurado na TOP utilizada.

### Diferenças entre as Opções de Configuração

O campo **"Kit/Componentes - Impressão e Livro Fiscal"** oferece três opções de configuração, cada uma com comportamento específico no cálculo da rentabilidade:

- **"Kit"**: Considera apenas o valor do kit. O CMV será zerado se o kit não tiver custo cadastrado, desconsiderando os componentes.
- **"Componentes"**: Considera apenas os componentes individuais. O sistema soma o custo de cada componente no CMV.
- **"Kit e Componentes"**: Considera tanto o kit quanto seus componentes. O CMV será maior, pois inclui todos os custos envolvidos.

Escolha a opção que melhor se adequa à forma como sua empresa gerencia os custos e analisa a rentabilidade dos produtos vendidos como kits.

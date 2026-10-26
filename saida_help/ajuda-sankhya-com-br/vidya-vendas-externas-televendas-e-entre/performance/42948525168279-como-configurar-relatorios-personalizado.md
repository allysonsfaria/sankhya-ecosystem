---
id: "42948525168279"
titulo: "Como configurar relatórios personalizados no Vidya Force"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948525168279-Como-configurar-relat%C3%B3rios-personalizados-no-Vidya-Force"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Performance"
atualizado_em: "2026-08-24T16:41:30Z"
rotulos: ["sync_hc", "vidya", "vidya_476110", "sync_hash_8f318bf4ba92"]
---

# Como configurar relatórios personalizados no Vidya Force

## 📊 Disponibilizando Relatórios no Vidya Force

### 🔍 Acesso aos Relatórios Formatados

Acesse o Sankhya e localize a tela de **Relatórios Formatados**.

Nesta tela, é possível cadastrar e gerenciar relatórios que poderão ser disponibilizados tanto em outras telas do sistema quanto no aplicativo **Vidya Force**.

![Imagem 1: Nesta tela, é possível cadastrar e gerenciar relatórios que poderão ser disponibilizados tanto em outras telas do…](https://ajuda.sankhya.com.br/hc/article_attachments/42956871908503)

##

### ➕ Vinculando o Relatório ao Vidya Force

Após confirmar que o relatório desejado já está cadastrado:

1. Acesse a tela de **Configurações - Vidya Force**
2. Navegue até a aba **Relatórios Formatados**
3. Clique no botão **➕ (Adicionar)**
4. Selecione o relatório desejado na lista

   ![Imagem 2: Selecione o relatório desejado na lista](https://ajuda.sankhya.com.br/hc/article_attachments/42956872343191)

Após a seleção, será exibida a opção para definir **em qual contexto/tela o relatório será disponibilizado** dentro do aplicativo.

![Imagem 3: Após a seleção, será exibida a opção para definir em qual contexto/tela o relatório será disponibilizado dentro do…](https://ajuda.sankhya.com.br/hc/article_attachments/42956845203479)

### 📱 Exibição no Aplicativo

No aplicativo Vidya Force, os relatórios configurados estarão disponíveis na **nova tela inicial (Home)**, dentro do botão:

**“Relatórios”**

![Imagem 4: “Relatórios”](https://ajuda.sankhya.com.br/hc/article_attachments/42956888227479)

## ⚙️ Parâmetros Obrigatórios por Tipo de Relatório

Para que o relatório funcione corretamente no aplicativo, é essencial respeitar o padrão de nomenclatura dos parâmetros, conforme o tipo de informação:

- **Relatórios de Parceiros**
  → Parâmetro obrigatório: `P_CODPARC`
- **Relatórios de Usuários/Vendedores**
  → Parâmetro obrigatório: `P_CODVEND`
- **Relatórios de Vendas (Pedidos/Notas)**
  → Parâmetro obrigatório: `PK_NUNOTA`

📌 **Importante:**
O funcionamento do relatório no app depende diretamente da correspondência exata desses parâmetros. Caso estejam divergentes, o relatório não será carregado corretamente.

## 🛠️ Configuração no IReport

Ao utilizar o IReport para construção do relatório, é obrigatório garantir que os parâmetros estejam consistentes em dois pontos:

- Na **query SQL**
- No **cadastro do parâmetro dentro do layout do relatório**

Ou seja, o nome do parâmetro deve ser idêntico em ambas as configurações, respeitando exatamente a nomenclatura esperada pelo sistema.

![Imagem 5: Ou seja, o nome do parâmetro deve ser idêntico em ambas as configurações, respeitando exatamente a nomenclatura…](https://ajuda.sankhya.com.br/hc/article_attachments/42956912999319)

![Imagem 6: Ou seja, o nome do parâmetro deve ser idêntico em ambas as configurações, respeitando exatamente a nomenclatura…](https://ajuda.sankhya.com.br/hc/article_attachments/42956888701079)

## 🔧 Diretrizes Técnicas para Configuração de Relatórios Personalizados

Para garantir o correto funcionamento dos relatórios personalizados integrados aos aplicativos da Vidya, é indispensável seguir as diretrizes técnicas abaixo durante a implementação.

### 📌 Tipagem Obrigatória de Parâmetros

Todos os parâmetros numéricos utilizados no relatório devem ser definidos obrigatoriamente como:

```
java.math.BigDecimal
```

**Justificativa técnica:**
A camada de integração entre os aplicativos Vidya e o Sankhya foi projetada para trabalhar com o tipo `java.math.BigDecimal` na manipulação de valores numéricos. A utilização de outros tipos, como `Integer`, `Long` ou `Double`, pode gerar incompatibilidades na conversão de dados, resultando em:

- Falhas na execução do relatório
- Retorno de dados inconsistentes
- Erros silenciosos difíceis de diagnosticar

### ⚠️ Restrição no Uso de Usuário Logado

Não deve ser utilizada, em hipótese alguma, a procedure nativa:

```
STP_GET_CODUSULOGADO
```

**Motivo técnico:**
Quando o relatório é executado via aplicativos da Vidya, a autenticação no Sankhya ocorre por meio de um **usuário técnico de integração**, e não pelo usuário final que está utilizando o aplicativo.

Na prática, isso significa que a procedure sempre retornará o mesmo usuário (usuário Vidya), independentemente de quem esteja acessando o relatório.

---
id: "28557088871575"
titulo: "Configurações para calcular o Antidumping"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28557088871575-Configura%C3%A7%C3%B5es-para-calcular-o-Antidumping"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T14:37:49Z"
rotulos: ["Produtos", "Configuração", "Importação", "Impostos", "Antidumping", "Configurações para calcular o Antidumping", "Comércio Exterior"]
---

# Configurações para calcular o Antidumping

### 1. Cálculo do Antidumping

#### 1.1 Cadastro de produtos

Configurações> Cadastros > Produtos
No registro de produtos, foi incorporada a seção **“Antidumping"**, para cadastrar as informações para o sistema calcular o Antidumping.

![Imagem 1: Configurações> Cadastros > Produtos No registro de produtos, foi incorporada a seção “Antidumping" , para cadastrar as…](https://ajuda.sankhya.com.br/hc/article_attachments/28557088865559)

Para cadastrar um percentual de **“Antidumping”** clique em **"Incluir"**. Existem duas fórmulas de cálculo para o Antidumping, sendo a primeira por País e Percentual ou a forma por Parceiro e valor fixo.

#### 1.2 Cálculo por País e Percentual

**(1)** **Cód. País:** busque o país previamente cadastrado no cadastro de Países do sistema.

**(1)** **% Antidumping:** informe a porcentagem que deve ser adicionada ao valor do produto de Antidumping, conforme a legislação brasileira.

![Imagem 2: (1) % Antidumping: informe a porcentagem que deve ser adicionada ao valor do produto de Antidumping, conforme a…](https://ajuda.sankhya.com.br/hc/article_attachments/28557061229207)

###

#### 1.3 Cálculo por Parceiro e valor fixo

**(1)Cód. País:** busque o país previamente cadastrado no cadastro de Países do sistema;

**(1)** **Valor Fixo (US$):** coloque o valor Fixo conforme a legislação para calcular o Antidumping;

**(1)** **Unidade de medida:** escolha qual unidade de medida será multiplicada pelo valor fixo;

**(1)** **Cód. Parceiro:** busque qual parceiro será vinculado a essa regra.

**Observação:** quando o cálculo de antidumping de valor fixo for baseado no peso líquido e a unidade do produto diferir da cadastrada na guia Antidumping, ative o parâmetro **IMP\_CALCPESOLIQ**.

![Imagem 3: Observação: quando o cálculo de antidumping de valor fixo for baseado no peso líquido e a unidade do produto diferir da…](https://ajuda.sankhya.com.br/hc/article_attachments/28557061231639)

#### 1.4 Portal de Importação

Comércio Exterior > Rotinas
Com base na seção Antidumping do cadastro de produtos, ao criar um processo de importação que inclua um produto sujeito a medidas Antidumping, o SOP realizará uma análise do país associado ao endereço registrado do parceiro vinculado ao processo de importação e calculará o adicional de Antidumping correspondente, preenchendo automaticamente o campo **"Vlr. Antidumping"** com o valor calculado.

**![Imagem 4: Atenção: o sistema faz o seguinte cálculo: (Vlr. Fixo USD / Tonelada) * Peso Líquido Produto = VlrUsd / UN](https://ajuda.sankhya.com.br/hc/article_attachments/28557088869015) Atenção:** o sistema faz o seguinte cálculo:
(Vlr. Fixo USD / Tonelada) \* Peso Líquido Produto = VlrUsd / UN

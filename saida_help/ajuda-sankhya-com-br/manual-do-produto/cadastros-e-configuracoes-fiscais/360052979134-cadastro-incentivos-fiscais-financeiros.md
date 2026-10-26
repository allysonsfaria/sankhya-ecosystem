---
id: "360052979134"
titulo: "Cadastro Incentivos Fiscais/Financeiros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052979134-Cadastro-Incentivos-Fiscais-Financeiros"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Cadastros e Configurações Fiscais"
atualizado_em: "2026-09-15T14:02:24Z"
rotulos: ["Configuração", "Livros Fiscais", "Impostos", "EFD", "br.com.sankhya.mgeliv.cad.IncentivosFiscaisFinanc", "Campos principais: Número único decreto empresa", "Configurações adicionais: Natureza percentual de incentivo", "Cadastro de Incentivos Fiscais: Detalhes e procedimentos", "PRODEPE", "Incentivos Fiscais"]
---

# Cadastro Incentivos Fiscais/Financeiros

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313119360791) Módulo: Livros Fiscais > Arquivos      ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42313119364247) Versão disponível: a partir da 4.5
```

---

Na tela de Cadastro Incentivos Fiscais/Financeiros, você irá cadastrar os benefícios do PRODEPE referentes aos Registros 1930 e 1960 vinculando os benefícios aos produtos da empresa especificada.

![Imagem 3: Na tela de Cadastro Incentivos Fiscais/Financeiros , você irá cadastrar os benefícios do PRODEPE referentes aos…](https://ajuda.sankhya.com.br/hc/article_attachments/4424791004567)

Assim, no **"Painel Principal"** da tela teremos:

No campo **"Nro. Único"**, insira o Número Único do benefício.

**Observação:** referente ao Nro Único, destacamos que se o sistema encontrar mais de um decreto para um determinado produto, o decreto selecionado será aquele que possuir o maior número no campo acima.

Insira em **"Número do Decreto"** o número referente ao decreto que será cadastrado.

No campo **"Cód. Empresa"**, cadastre a empresa do benefício.

**Nota:** apenas uma empresa pode ser vinculada por benefício, se este for válido também para outra empresa, você deve duplicar o registro. Se esse campo ficar vazio, o benefício valerá para todas as empresas.

Você irá informar em **"Data Inicio Validade"** o início da vigência do decreto.

No campo **"Indicador de enquadramento"** informe o enquadramento do registro, de acordo com as opções abaixo:

- 0-Operações não incentivadas;
- 1-Indústria (crédito presumido);
- 3-Importação (diferimento/crédito presumido);
- 4-Central de distribuição (entradas/saídas);
- 5-Comércio atacadista - sistemática especial da Lei nº 14.721/2012

Defina em **"Indicador de Natureza"**, a natureza que abrange o registro. Você poderá selecionar:

- 0-Ampliação;
- 1-Ampliação com nova linha;
- 2-Implantação;
- 3-Isonomia;
- 4-Manutenção;
- 5-Migração;
- 6-Prorrogação;
- 7-Renovação;
- 8-Revitalização;
- 9-Outros.

Insira no campo **"Indicador de Cobrança de ICMS Mínimo"** se o Registro terá indicador ou não.

Em **"Percentual de Incentivo do item"** insira o percentual de incentivo.

Selecione no campo **"Indicador de Sub-Apuração"** o tipo de sub-apuração que o registro pertence.

Quando a marcação **"Considera a validação entre CFOP e Produto"** estiver habilitada, o sistema irá considerar as informações cadastradas nas telas [CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714) e [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), para compor o Item Variável - 03.

Informe no campo **"Índice de recolhimento da central de distribuição"**, o índice de recolhimento da central de distribuição que será gerado no registro 1980. 

A marcação **"Considerar a validação entre CFOP e Produto para geração do registro C177?"** fará o sistema levar em consideração as configurações dos campos **"Tipo de Operação PRODEPE"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714-CFOP#abageral) da tela [CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714-CFOP) e **"Cód. Apur. Inc. PRODEPE/FUNCRESCE"** da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), de forma que, caso as opções **"Operação não incentivada"** e **"Sem incentivo"** forem definidas, o registro C177 será gerado se o campo **"Cód. do Produto Sem incentivo"** da sub-aba [Prodepe](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI-#sub-abaprodepe) da tela [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI-) estiver vazio.

Ao habilitar a marcação **"Considerar a validação entre CFOP e Produto para geração do registro 1960?"**, o sistema irá considerar as configurações dos campos Tipo de Operação PRODEPE (aba Geral da tela CFOP) e Cód. Apur. Inc. PRODEPE/FUNCRESCE (aba Impostos do Cadastro de Produtos)  para a geração dos valores incentivados e não incentivados do registro 1960 do EFD Fiscal. Dessa forma, quando as opções **"Operações Incentivadas"** e **"Com incentivo"** dos campos aqui informados forem respectivamente selecionadas, o campo **"Saídas incentivadas de PI"** da aba **"1001"** localizado na tela EFD - Fiscal ICMS/IPI será preenchido; porém, se as opções **"Operação Não Incentivada"** e **"Sem incentivo"** forem respectivamente configuradas, o campo **"Saídas não incentivadas de PI"** também da aba 1001 que será preenchido.

**Observação:** o registro 1960 será gerado na tela EFD - Fiscal ICMS/IPI somente se a opção **"1-Indústria (crédito presumido)"** do campo Indicador de Enquadramento dessa tela for selecionado.

Defina no campo **"Custo para Importações-base"**, o tipo de custo que será gerado no Registro 1975, conforme as opções abaixo:

- Médio com ICMS;
- Médio sem ICMS;
- Gerencial;
- Reposição.

#### Aba Produtos

Na aba **"Produtos"**, cadastre os produtos que serão vinculados ao benefício que você estará inserindo nesta tela.

Apenas os produtos que estiverem cadastrados com os campos **"Cód. Apur. Inc. PRODEPE/FUNCRESCE"** e **"Indicador Esp. Inc. PRODEPE/FUNCRESCE"** (tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos)) selecionados com a opção **"Com incentivos"**, serão exibidos nesta tela.

No campo **“Alíquota incidente s/ Importações-base”**, selecione o percentual de alíquota incidente sobre importações-base que será gerado no Registro 1975, de acordo com as opções abaixo:

- 03,50%;
- 06,00%;
- 08,00%;
- 10,00%.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052979134-Cadastro-Incentivos-Fiscais-Financeiros#top)

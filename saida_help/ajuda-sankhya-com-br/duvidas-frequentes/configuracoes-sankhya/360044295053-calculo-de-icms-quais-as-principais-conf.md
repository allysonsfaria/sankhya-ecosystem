---
id: "360044295053"
titulo: "Cálculo de ICMS: Quais as principais configurações no sistema? "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044295053-C%C3%A1lculo-de-ICMS-Quais-as-principais-configura%C3%A7%C3%B5es-no-sistema"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:58:55Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "ICMS", "Impostos", "TOP", "Configurações Essenciais para o Cálculo de ICMS"]
---

# Cálculo de ICMS: Quais as principais configurações no sistema? 

(1)** ICMS - Imposto sobre Operações relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual** **e Intermunicipal e de Comunicação:** imposto não cumulativo que incide sobre as operações relativas à circulação de mercadorias e prestações de serviços de transporte interestadual e intermunicipal e de comunicação. De competência dos Estados e do Distrito Federal, conforme previsto no art. 155, II, da Constituição de 1988, apresenta-se como uma das principais fontes de recursos financeiros para a consecução das ações governamentais.

![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17325817709463) **SOLUÇÃO:**

Configurações necessárias para o calculo básico de ICMS, sem exceções:

**![Imagem 2: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17325817724439) IMPORTANTE:**

Abaixo serão listadas as configurações principais, desconsiderando processos específicos e exceções. Recomenda-se que toda e qualquer configuração seja realizada por um usuário certificado na utilização do sistema, que conheça os impactos dessas parametrizações. Lembramos que o Service Desk não realiza tais configurações, e havendo necessidade um Consultor de sua Franquia deverá ser acionado para apoio.

![Imagem 3: Acesse: Preferências da Empresa: (Caminho de acesso: Comercial Preferências » Empresa )](https://ajuda.sankhya.com.br/hc/article_attachments/17325810156311) Acesse: Preferências da Empresa:  (Caminho de acesso: Comercial  Preferências » Empresa)

- Aba **"Propriedades",** campo **"Calcular ICMS":**marcado

![Imagem 4: Aba "Propriedades", campo "Calcular ICMS": marcado](https://ajuda.sankhya.com.br/hc/article_attachments/17325817742743)

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17325810184343) OBSERVAÇÃO:**

Se tiver casos com IPI também e o mesmo somar a base do ICMS, marque a opção: **"IPI Incide no ICMS"**, desta mesma tela.

![Imagem 6: Cadastro da TOP: tela "Tipos de Operação - TOP" (Caminho de acesso: Comercial » Arquivo » Cadastros)](https://ajuda.sankhya.com.br/hc/article_attachments/17325817766551) Cadastro da TOP: tela **"Tipos de Operação - TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros)

Aba **"Imposto"**, configure os seguintes campos:

- **"Cálculo de ICMS, IPI e ISS"**, defina uma das opções abaixo:
  - **Calcula e não digita**: o sistema calculará os impostos conforme as configurações previamente realizadas e não deixará digitá-los na nota. Recomendada para geração de notas de Venda e Devolução.
  - **Calcula e digita:** o sistema calculará os impostos conforme as configurações previamente efetuadas e permitirá alterá-las na nota. Esta opção é utilizada para validar Notas de Compras, pois estas nem sempre apresentam o cálculo correto e algumas vezes a diferença é apenas de arredondamento de valores. Nos casos de erro, o contador deverá notificar a empresa fornecedora sobre a diferença.

- Marque o campo **"Tem ICMS"**.
- Verifique a opção **"Classificação ICMS"**: como padrão recomenda-se **"Usar do parceiro"**

![Imagem 7: Verifique a opção "Classificação ICMS" : como padrão recomenda-se "Usar do parceiro"](https://ajuda.sankhya.com.br/hc/article_attachments/17325817777687)

![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17325810184343) **OBSERVAÇÃO:**

Se tiver casos com IPI também e o mesmo somar a base do ICMS, marque a opção: IPI Incide no ICMS, desta mesma tela. 

![Imagem 9: Se tiver casos com IPI também e o mesmo somar a base do ICMS, marque a opção: IPI Incide no ICMS , desta mesma tela.](https://ajuda.sankhya.com.br/hc/article_attachments/17325810229399)

**![Imagem 10: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17325810184343)OBSERVAÇÃO:**

Para calcular e gerar CFOP na nota, a top tem que atualizar Livros Fiscais e terá que configurar as CFOP's para dentro e fora do Estado para entrada ou saída na aba **"Livros fiscais"; 

![Imagem 11: Para calcular e gerar CFOP na nota, a top tem que atualizar Livros Fiscais e terá que configurar as CFOP's para dentro…](https://ajuda.sankhya.com.br/hc/article_attachments/17325817821719)**

![Imagem 12: Cadastro de parceiros (Caminho de acesso: Configurações » Cadastros » Parceiros ):](https://ajuda.sankhya.com.br/hc/article_attachments/17325817833751) Cadastro de parceiros (Caminho de acesso: Configurações » Cadastros » Parceiros):

- Aba **"Fiscal"**: configure os campos **"Classificação ICMS"** (em Operações para **Compra/Revenda**, como **Revendedor**, ou a classificação que corresponder ao seu parceiro de negócios)

![Imagem 13: Aba "Fiscal" : configure os campos "Classificação ICMS" (em Operações para Compra/Revenda , como Revendedor , ou a…](https://ajuda.sankhya.com.br/hc/article_attachments/17325810290583)

- Endereços: observe a Unidade Federativa - UF (estado do parceiro). Este cadastro é importante para determinar qual regra para Cálculo de ICMS o sistema irá utilizar.

![Imagem 14: Endereços: observe a Unidade Federativa - UF (estado do parceiro). Este cadastro é importante para determinar qual…](https://ajuda.sankhya.com.br/hc/article_attachments/17325817879575)

![Imagem 15: O BSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17325810184343)**OBSERVAÇÃO:**

Se tiver casos com IPI também e o mesmo somar a base do ICMS tem que marcar a opção: IPI Incide no ICMS, desta mesma tela.

![Imagem 16: Cadastro de produtos (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos) :](https://ajuda.sankhya.com.br/hc/article_attachments/17325817899159) Cadastro de produtos (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos):

- Aba **"Impostos"**, marque o campo **"Calcular ICMS"**

![Imagem 17: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17325810184343)**OBSERVAÇÃO:**

Caso utilize impostos por empresa (Parâmetro **"EMPPRODIMPOST"** ligado), observe as mesmas marcações por empresa na aba **"Impostos / Informações por empresa".**

![Imagem 18: Caso utilize impostos por empresa (Parâmetro " EMPPRODIMPOST" ligado), observe as mesmas marcações por empresa na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/17325817933847)

![Imagem 19: Cadastro das 'Alíquotas de ICMS' (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS):](https://ajuda.sankhya.com.br/hc/article_attachments/17325810383383) Cadastro das 'Alíquotas de ICMS' (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS):

- Considerando uma venda em que a empresa emissora seja de Minas Gerais e o cliente também de Minas Gerais, configure as hierarquias de MG (Origem) para MG (Destino). Selecione ainda na árvore hierárquica, do lado esquerdo da tela, a opção **sem exceção**.

![Imagem 20: Considerando uma venda em que a empresa emissora seja de Minas Gerais e o cliente também de Minas Gerais, configure as…](https://ajuda.sankhya.com.br/hc/article_attachments/17325817962007)

![Imagem 21: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17325810184343)**OBSERVAÇÃO:**

Sempre verifique/configure as prioridades desta tela, em outras opções .

![Imagem 22: Sempre verifique/configure as prioridades desta tela, em outras opções .](https://ajuda.sankhya.com.br/hc/article_attachments/17325810407063)

![Imagem 23: Sempre verifique/configure as prioridades desta tela, em outras opções .](https://ajuda.sankhya.com.br/hc/article_attachments/13136505125783)

![Imagem 24: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17325810184343)**OBSERVAÇÃO:**

Caso o sistema não calcule os Impostos(ICMS/ST/IPI) para alguns produtos e ao verificar toda a configuração de Cálculo dos impostos constatar que tudo está certo, verifique se os produtos são "Matérias Primas/Uso Consumo", configuração do Cadastro de produto "Usado como:".

Para cálculo de impostos destes produtos, observe o **"CALCIMPMP"** (Configurações >> Avançando >> Preferências), este parâmetro deve ser ligado.

Parâmetro **"Proporcionalizar base ICMS calculada por fórmula? - PROPFORBASEICMS"** para itens que possuem ICMS com fórmula vinculada será necessário ligar este parâmetro. Com ele ligado a base de ICMS será proporcionalizada por fórmula.

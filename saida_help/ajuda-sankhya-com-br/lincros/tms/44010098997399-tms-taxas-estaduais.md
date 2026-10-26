---
id: "44010098997399"
titulo: "[TMS] - Taxas Estaduais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010098997399--TMS-Taxas-Estaduais"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T18:30:22Z"
rotulos: ["sync_hc", "lincros", "lincros_13432087", "sync_hash_978a7efbfe6b"]
---

# [TMS] - Taxas Estaduais

**Menu**: Cadastros gerais > Configurações da empresa > Taxas > Taxas estaduais
**Objetivo**: Cadastrar um valor de ICMS, PIS e COFINS para uma determinada região e transportadora.

**Considerações:** Ter conhecimentos dos valores de impostos a serem informados, uma vez que após alterado todos os cálculos de frete para a região e transportadora informado será afetado.
**Taxas Estaduais**

Para iniciar o cadastro, acesse o menu Cadastros gerais > Configurações da empresa > Taxas > Taxas estaduais e clique no botão 'Novo'

![Imagem 1: Menu : Cadastros gerais > Configurações da empresa > Taxas > Taxas estaduais Objetivo : Cadastrar um valor de ICMS, PIS…](https://ajuda.sankhya.com.br/hc/article_attachments/44010099202967)

Ao clicar no botão 'Novo' você será redirecionado para a aba 'Edição de taxa', são campos obrigatórios: Estado de origem e Estado de destino

**Aba Cadastro**A aba Cadastro possui os seguintes campos:

- **Estado de origem:** Estado de origem do cadastro.
- **Estado de destino**: Estado de destino do cadastro.
- **Código fiscal de operação:** Código fiscal da operação que está sendo feito.
- **ICMS:** Valor de ICMS.
- **ICMS não contribuinte:** Valor de ICMS não contribuinte.
- **ICMS aéreo**: Valor de ICMS para operação aérea.
- **Calcular ICMS no pedágio:** Caso precise desse cálculo deixe a caixa marcada, caso não, desmarque-a**.**
- **Calcula ICMS CIF:** Caso precise desse cálculo deixe a caixa marcada, caso não, desmarque-a**.**
- **Calcula ICMS FOB:** Caso precise desse cálculo deixe a caixa marcada, caso não, desmarque-a.
- **Desconto na alíquota de ICMS:** Valor que será usado para desconto da alíquota de ICMS.
- **PIS**: Valor do PIS.
- **COFINS**: Valor do COFINS.

Após clicar no botão 'Salvar' duas abas novas serão criadas, a aba 'Restrições' e 'Histórico'

![Imagem 2: Após clicar no botão 'Salvar' duas abas novas serão criadas, a aba 'Restrições' e 'Histórico'](https://ajuda.sankhya.com.br/hc/article_attachments/44010106723095)

**Aba Restrição**Nessa aba nova será possível criar restrições para o uso da taxa estadual, que pode ser restrita por produto e ou transportadora.

![Imagem 3: Aba Restrição Nessa aba nova será possível criar restrições para o uso da taxa estadual, que pode ser restrita por…](https://ajuda.sankhya.com.br/hc/article_attachments/44010121463703)

Dentro do campo restrições de produto ao apertar no botão 'Adicionar' será aberta uma nova tela com alguns campo, onde o único obrigatório é o de produto.

![Imagem 4: Dentro do campo restrições de produto ao apertar no botão 'Adicionar' será aberta uma nova tela com alguns campo, onde…](https://ajuda.sankhya.com.br/hc/article_attachments/44010116804375)

os demais campos são;

- **ICMS**: Valor de ICMS.
- **ICMS aéreo**: Valor de ICMS aéreo.
- **ICMS aéreo não contribuinte**: Valor de ICMS aéreo para não contribuinte.
- **Calcular ICMS no pedágio:** Caso precise desse cálculo deixe a caixa marcada, caso não, desmarque-a**.**
- **Calcula ICMS CIF:** Caso precise desse cálculo deixe a caixa marcada, caso não, desmarque-a**.**
- **Calcula ICMS FOB:** Caso precise desse cálculo deixe a caixa marcada, caso não, desmarque-a.
- **Desconto na alíquota de ICMS:** Valor que será usado para desconto da alíquota de ICMS.
- **PIS**: Valor do PIS.
- **COFINS**: Valor do COFINS.

Dentro do campo restrições de transportadora ao apertar no botão 'Adicionar' será aberta uma nova tela com alguns campo, onde o único obrigatório é o de transportadora.

![Imagem 5: Dentro do campo restrições de transportadora ao apertar no botão 'Adicionar' será aberta uma nova tela com alguns…](https://ajuda.sankhya.com.br/hc/article_attachments/44010121816855)

os demais campos são:

- **ICMS**: Valor de ICMS.
- **ICMS aéreo**: Valor de ICMS aéreo.
- **ICMS aéreo não contribuinte**: Valor de ICMS aéreo para não contribuinte.
- **Calcular ICMS no pedágio:** Caso precise desse cálculo deixe a caixa marcada, caso não, desmarque-a**.**
- **Calcula ICMS CIF:** Caso precise desse cálculo deixe a caixa marcada, caso não, desmarque-a**.**
- **Calcula ICMS FOB:** Caso precise desse cálculo deixe a caixa marcada, caso não, desmarque-a.
- **Desconto na alíquota de ICMS:** Valor que será usado para desconto da alíquota de ICMS.
- **PIS**: Valor do PIS.
- **COFINS**: Valor do COFINS.

**IBS e CBS (Reforma Tributária):** desde a versão TMS v4.159, esta tela também possui uma aba **IBS/CBS**, com campos próprios de alíquota e retenção para os novos tributos, além de vigência específica. Se um CT-e ou pré-conhecimento estiver com o cálculo de IBS/CBS divergente ou zerado, confira primeiro se a alíquota está cadastrada nessa aba para o estado de origem/destino da rota (ou na tela equivalente de Taxas Municipais). Também é necessário que o componente correspondente esteja com o checkbox "Calcular IBS/CBS" marcado na Tabela de Frete da transportadora (Cadastros Gerais > Transportadoras > Negociações > Tabelas de Frete) — sem essa marcação, o valor não entra na base de cálculo mesmo com a alíquota cadastrada aqui.

**Componentes IBS, CBS, IBS Destacado e CBS Destacado:** a versão v4.159 criou quatro componentes padrão de frete (Cadastros gerais > Configurações da empresa > Componentes de frete): **IBS**, **CBS**, **IBS Destacado** e **CBS Destacado**. O cálculo usa as alíquotas configuradas em Taxas Estaduais e Municipais. Nos componentes "Destacado", o valor do imposto é **adicionado ao total do frete sem compor a base de cálculo** dos tributos. Ao usar um componente Destacado, recalcule o pré-conhecimento e confira a aba Movimentos.

**Somar IBS/CBS ao total do frete na Cotação Spot:** os checkboxes que definem se o valor de IBS e CBS é somado ao total do frete ficam no cadastro **Transportadora - Empresa** e se aplicam à Cotação Spot. Eles não estão na Tabela de Frete.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"

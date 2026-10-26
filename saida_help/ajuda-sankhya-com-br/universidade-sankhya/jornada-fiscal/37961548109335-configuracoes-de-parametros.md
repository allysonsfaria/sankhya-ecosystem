---
id: "37961548109335"
titulo: "Configurações de parâmetros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37961548109335-Configura%C3%A7%C3%B5es-de-par%C3%A2metros"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-07-22T14:03:27Z"
rotulos: ["Configuração", "Fiscal", "ICMS", "Impostos", "Preferências", "ERP Sankhya"]
---

# Configurações de parâmetros

## Preferências

Antes de iniciar o passo a passo, lembre-se que os parâmetros desta tela determinam como o ERP Sankhya irá calcular o ICMS e suas variações nas operações da empresa.

Como essas chaves influenciam diretamente a base de cálculo, as alíquotas e o destaque do imposto nas notas fiscais, revise e ajuste cada parâmetro de acordo com a realidade da empresa. Assim, o sistema aplicará corretamente as regras fiscais e evitará erros no cálculo.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela **“Preferências”**
   **Menu:** Configurações » Avançado » Preferências

- Digite o parâmetro no campo **“Chave ou Descrição e tecle ENTER”** e pressione **ENTER** para carregar as informações;
- No lado direito da tela, será exibida a chave com as configurações correspondentes. Caso seja necessário alterá-las, faça as modificações e salve para confirmar;
- Clique no botão **"Salvar"** para concluir a alteração.

#### Parâmetros

- **CALCIMPMP - Calcular Impostos para Matéria Prima**
  Habilite caso o “usado como” do produto esteja configurado como matéria prima.
- **COPIAIMPCALCDIG - Movimentos p/ copiar impostos TOP Calcula Digita**
  Determina qual tipo de movimento da operação que copiará impostos quando a TOP estiver configurada como "Calcula e Digita".
- **EMPPRODIMPOST - Usa imposto de produtos por empresa**
  Quando ligado, a aba “Impostos/Informações por Empresa” será apresentada. Os campos dessa aba têm prioridade na busca das configurações do ICMS, ISS e IPI.
- **ENDICMS - Endereço para ICMS**
  Indica em qual cadastro a UF será consultada para o cálculo do ICMS e suas variações.
- **USENDENTREGA -** **Usa endereço de entrega dos contatos** 
  Se habilitado, o sistema irá considerar a UF vinculado ao endereço do contato do parceiro para definir origem e destino no cálculo do imposto.
- **VALPARTSNUNICA - Valida partilha do Simples Nac. mesmo sendo única -** Ligado
- **HABFORMASREPRED - Habilitar formas alternativas de repasse de ICMS -** Ligado
- **VALUSOPRODNCM - Não validar NCM para produtos Usados como -** I,C,0,S,3
- **UFNFESEMCEST - UFs que devem ter XML de NF-e sem o CEST** 
  Informe as siglas dos estados separados por vírgula. Essa configuração indica que a tag CEST não será impressa no XML das notas das empresas pertencentes às UF's informadas no parâmetro.
- **CFOPAQUSERVDEN - CFOP de aquisição de serviço dentro do estado** e **CFOPAQUSERVFOR - CFOP de aquisição — de serviço fora do estado**
  Os parâmetros são globais, ou seja, as configurações serão validadas de forma prioritária em relação aos demais relacionados a CFOP. Quando informados valores nestes, as notas de serviços emitidas terão o CFOP atualizados com base nos parâmetros. Para que seja considerado o cadastro da TOP para obtenção do CFOP, os parâmetros deverão permanecer vazios.
- **CALCIE - Calc.ICMS p/prod.c/'ST compra qdo inter-estadual?** - Ligado
- **AVISACODTRIBERR - Avisar qdo Prod.marcado subst.trib.e conf.s/subs?** - Ligado
- **USATABSTPARC - Usa tabela para base de ST no cadastro de parceiro** - Desligado
- **STIPIEMBDESC - ST e IPI embutido como desconto no item da nota -** Desligado
- **MOMCALCDIFALIQ - Momento do cálculo do diferencial de alíquota** - Na central e recálculo no livro
- **CODOBSGARANTIDO - Código da observação para o garantido integral**: Preencher com o código da Observação
- **CODIMPGARANTIDO - Código do imposto para o garantido integral**: Preencher com o código do Imposto
- **TIPTITGNREST - Tipo de Título p/indicar GNRE p/S.T.**
  Configure esse parâmetro com o tipo de título que será usado para gerar a GNRE. Não poderá conter o mesmo título do “Garantido Integral". No caso da compra, esse parâmetro não pode ser igual ao tipo de título informando na aba “parcelas”, do Tipo de Negociação, criado para parcela que contenha a fórmula.
- **UFDESTNFEBENFIS - UFs destino NF-e com benefício fiscal para DIFAL**
  Informe a sigla de cada UF da SEFAZ de destino (separada por vírgula), que esteja amparada por benefícios fiscais. Ou seja, a alíquota interestadual é igual a zero nessas operações. Essa condição se aplica aos seguintes CST"s: 40, 41, 50, 51, ou 60.
- **HABFORMASREPRED - Habilitar formas alternativas de repasse de ICMS**: Ligado. 
  Com esse parâmetro ligado, será disponibilizado na tela ‘Alíquota de ICMS” o campo “**Forma de repasse Desoneração”**.
- **UFDEDREPICMSIRF - UF que permite deduzir vlr repasse ICMS da BC IRRF**: Ligado. 
  Com esse parâmetro ligado durante a emissão da nota com desoneração de ICMS e retenção de IR, o valor do repasse será deduzido da base de cálculo do IRRF.
- **SUFRAMABASERED - Repasse SUFRAMA p/ base ST com redução base ICMS**: Ligado. 
  Com esse parâmetro ligado, a base será considerada sem redução para o cálculo do percentual de repasse SUFRAMA.
- **GERIMPOSTO - Gerar impostos (ISS, INSS, IRF) no financeiro:** Quando ligado, a dedução dos impostos retidos irá ocorrer diretamente na movimentação financeira, no momento da baixa.
- **CONSIMPRETNOTA - Considerar impostos retidos no valor da nota:** Quando ligado, a dedução dos impostos retidos irá ocorrer na nota e será abatido do valor total da nota.
- **CALCMENSALNOTA - Calcular Imposto c/Base Mensal na Nota**

Ligado, se o cálculo for por base mensal com registro na nota. Nesse caso, o valor da nota fica líquido.

- **CALCMENSALREC - Calc. Imp. de Base Mensal p/ Receitas no Financeiro**

Ligado, se o cálculo for por base mensal com registro no financeiro. Nesse caso, o valor da nota fica bruto. 

- **CFGALIQSERVPROD - Permite configuração aliquota por serviço/produto**: Ligado.
- **TEMFUNRURAL - Calcular Funrural no lugar de INSS:** Ligue o parâmetro, para que no lugar do INSS seja calculado o FUNRURAL
- **VLRCALCINSS** - **Valor líquido p/ retenção de INSS**: indique o valor a partir do qual será registrado o cálculo do Funrural.
- **RETEMINSS** - **Retém INSS**: Ligado.
- **ENTIPISEMDESC - Entrada c/Base IPI sem Desconto** e **SAIIPISEMDESC - Saída c/Base IPI sem Desconto;**

Quando ligados, a BC do IPI será calculada, desconsiderando o valor de desconto concedido no lançamento.

- **PADCSTIPITOPNCD - Padrão CST.IPI pela TOP com não Calcula e Digita;**

Quando ligado e a TOP configurada como Não Calcula e Digita, caso o sistema não consiga calcular a CST de IPI conforme a hierarquia, por padrão será utilizada a CST definida na TOP.

- **INCLUIALIPISCOF - Incluir impostos simultâneos (PIS/COFINS)?**
  Ao cadastrar uma alíquota de PIS, o sistema permite o cadastro simultâneo de uma alíquota de COFINS, o que agiliza o processo.

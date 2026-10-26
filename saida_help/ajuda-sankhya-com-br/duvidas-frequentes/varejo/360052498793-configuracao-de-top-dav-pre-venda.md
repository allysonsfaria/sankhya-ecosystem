---
id: "360052498793"
titulo: "Configuração de TOP DAV/Pré venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052498793-Configura%C3%A7%C3%A3o-de-TOP-DAV-Pr%C3%A9-venda"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T15:29:47Z"
rotulos: ["Configuração", "Fast Service", "TOP", "Vendas", "Estoque", "Financeiro", "Cupom Fiscal: Receita real baixar estoque controle de numeração", "Pré-venda: Configuração TOP atualizar financeiro reservar estoque", "DAV: Pedido de venda atualizar financeiro calcular impostos"]
---

# Configuração de TOP DAV/Pré venda

| - Nesse documento serão apresentadas as configurações básicas para **Pré-venda** e **DAV** no FAST Service, considerando um processo padrão. - Ressaltamos que toda e qualquer configuração deverá respeitar especificações do processo definido em sua empresa, e dessa forma, validado com um consultor de sua Franquia/Filial. |
| --- |

### Vendas Balcão (Cupons Fiscais):

- **Pré-Venda: (para a modalidade Pré-Venda)**

Tipos de Operações TOP:

1. O tipo de movimento para essa TOP é "Venda";
2. Informar o numero da TOP criada no parâmetro CODTOPPREVENDA,
3. Deve atualizar financeiro com uma provisão receita,
4. Deve reservar o estoque das mercadorias,
5. A nota fica pendente;
6. Configurar o campo "Usar como Preço" com a opção "Preço de Venda",
7. Não deve atualizar livros fiscais, mas a CFOP deve ser informada: 5102 e 6102;
8. Deve calcular impostos incidentes sobre os produtos (ICMS, ST, PIS e COFINS)
9. Deve ser cadastrado um Controle de Numeração com a série igual a 'PV'. Para isto, a Base de Numeração desta TOP deve ser igual a "Venda".

- **Pedido de venda DAV: (para a venda Não-Concomitante):**

1. O Tipo de Movimento para essa TOP é "Pedido de Venda";
2. Deve atualizar financeiro com uma provisão de receita,
3. Não deve permitir alteração após a confirmação,
4. Configurar o campo "Usar como Preço" com a opção "Preço de Venda",
5. Não deve atualizar livros fiscais, pois o DAV não deve ser escriturado;
6. Deve calcular impostos incidentes sobre os produtos (ICMS e ST)
7. Configurar para esta TOP a Base de Numeração igual a "DAV cupom fiscal".
8. Após a confirmação do pedido, o próximo passo no processo de vendas é o faturamento do Pedido, para emissão do Cupom Fiscal. Assim é necessário informar a TOP de "Venda Cupom Fiscal" no campo "TOP de Faturamento", ou realizar a configuração de uma restrição para que a única TOP de destino permitida seja a TOP de "Venda Cupom Fiscal".

- **Cadastre a Top** **Venda Cupom Fiscal: (para a venda Concomitante)**

1. O tipo de movimento para essa TOP é "Venda";
2. Deve atualizar financeiro com uma receita real, pois se trata de um direito real obtido através da venda das mercadorias registrada em documento fiscal;
3. Deve baixar o estoque das mercadorias, pois o produto antes disponível no estoque será entregue ao cliente;
4. Não deve permitir alteração após a confirmação, para evitar que o registro do Cupom Fiscal no sistema seja diferente do Cupom Fiscal emitido e entregue ao cliente;
5. Deve Atualizar o Apoio a Decisão, para que os lançamentos realizados com esta TOP sejam considerados na análise das Vendas do período;
6. Para emissão de Cupons Fiscais a opção “TOP de Cupom Fiscal” deve estar marcada;
7. Configurar o campo "Usar como Preço" com a opção "Preço de Venda", pois o valor unitário a ser praticado nas vendas é o Preço de Venda calculado pelo sistema, a exemplo das demais operações deste processo;
8. Não deve atualizar livros fiscais, pois a atualização dos Livros será realizada a partir da Redução Z, e não individualmente a partir de cada Cupom Fiscal;
9. Deve calcular impostos incidentes sobre os produtos (ICMS, ST, PIS e COFINS) para que a empresa realize a emissão do cupom com todos os impostos incidentes na operação;
10. Para que o sistema permita a emissão de Cupons Fiscais e seu registro no sistema, deve ser cadastrado um Controle de Numeração com a série igual a 'CF'. Para isto, a Base de Numeração desta TOP deve ser igual a "Venda". Para permitir a informação da série, deve ser definido o Tipo de Numeração igual a "Empresa/Série", além de cadastrar no "Controle de Numeração" uma linha para a empresa 1 com a série "CF", que será utilizada nos lançamentos de Cupons Fiscais. Nos lançamentos realizados com esta TOP, o usuário deverá se lembrar de utilizar a série "CF".

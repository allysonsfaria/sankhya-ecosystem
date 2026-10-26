---
id: "4413642741399"
titulo: "Geração do Registro 0500 no arquivo EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4413642741399-Gera%C3%A7%C3%A3o-do-Registro-0500-no-arquivo-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-08-10T19:58:26Z"
rotulos: ["Configuração", "Impostos", "Contabilização", "Natureza", "Plano de Contas", "EFD Contribuições", "Pesquisa Conta Contábil", "Configuração Plano Contas", "Geração EFD Contribuições"]
---

# Geração do Registro 0500 no arquivo EFD Contribuições

### Formas de busca da Conta Contábil

Existem duas formas de se realizar a pesquisa da Conta Contábil, sendo que uma empresa só poderá ter uma definição de busca configurada.

Na tela Empresa (Comercial>Preferências), aba EFD - Escrituração Fiscal Digital, selecionar no campo 'Tipo de Escrituração': 'EFD Contribuições' e no campo 'Tipo da Conta Contábil' definir se a busca será por: 

**(1)** Cadastros; ou

**(1)** Contabilização.

![Imagem 1: (1) Contabilização.](https://ajuda.sankhya.com.br/hc/article_attachments/16199399441047)

### Cadastros

Optando-se pela opção "Cadastros", realize a configuração da Conta Contábil para EFD. 

Na geração do arquivo do EFD Contribuições, o sistema segue uma ordem de análise para efetuar a busca do código que foi vinculado ao campo "Conta Contábil para EFD". 

Veja abaixo a sequência de análise:

![Imagem 2: Produto > Cadastro de Produtos, aba "Impostos / Informações por empresa";](https://ajuda.sankhya.com.br/hc/article_attachments/16199399442327) Produto > Cadastro de Produtos, aba "Impostos / Informações por empresa";

Serviço > Cadastro de Serviços, aba Configurações por Empresa;

![Imagem 3: Produto > Cadastro de Produtos, aba "Impostos";](https://ajuda.sankhya.com.br/hc/article_attachments/16199405878807) Produto > Cadastro de Produtos, aba "Impostos";

Serviço > Cadastro de Serviços, aba Impostos;

![Imagem 4: Cadastro de Grupos de Produtos/Serviços, aba "Impostos por Empresa";](https://ajuda.sankhya.com.br/hc/article_attachments/16199405883671) Cadastro de Grupos de Produtos/Serviços, aba "Impostos por Empresa";

![Imagem 5: Cadastro de Grupos de Produtos/Serviços, aba "Geral";](https://ajuda.sankhya.com.br/hc/article_attachments/16199399448599) Cadastro de Grupos de Produtos/Serviços, aba "Geral";

![Imagem 6: Cadastros de Tipo de Operação - TOP, aba Impostos.](https://ajuda.sankhya.com.br/hc/article_attachments/16199405894167) Cadastros de Tipo de Operação - TOP, aba Impostos.

Para os registros referentes aos financeiros, como por exemplo F100, F500, F525, F500, a hierarquia seguirá a seguinte ordem:

![Imagem 7: Cadastro de Natureza de Receitas e Despesas, aba "PIS/COFINS";](https://ajuda.sankhya.com.br/hc/article_attachments/16199399442327) Cadastro de Natureza de Receitas e Despesas, aba "PIS/COFINS";

![Imagem 8: Cadastros de Tipo de Operação - TOP, aba Impostos.](https://ajuda.sankhya.com.br/hc/article_attachments/16199405878807) Cadastros de Tipo de Operação - TOP, aba Impostos.

Os registros referentes ao imobilizado, como por exemplo F120, F130, a seguinte ordem de hierarquia será:

![Imagem 9: Cadastro de Produtos, aba "Impostos";](https://ajuda.sankhya.com.br/hc/article_attachments/16199399442327) Cadastro de Produtos, aba "Impostos";

![Imagem 10: Cadastros de Tipo de Operação - TOP, aba Impostos.](https://ajuda.sankhya.com.br/hc/article_attachments/16199405878807) Cadastros de Tipo de Operação - TOP, aba Impostos.

### Contabilização

Adotando a opção "Contabilização", na geração do registro o sistema verificará na contabilização do documento em questão, ordenando primeiramente pelo lançamento na contabilidade de maior valor para a conta configurada no determinado grupo de "Natureza para EFD" definido.

A determinação da conta a ser gerada no arquivo, será conforme a movimentação do registro em foco. De forma que, o sistema localizará na contabilização dos determinados registros as contas contábeis configuradas com a natureza para EFD.

**(1)** Para os registros referentes aos movimentos de Estoque que foram contabilizadas pela contabilização do Estoque ou do Livro (TCBINT.ORIGEM = 'E' ou ‘L’);

**(1)** Para os registros referentes aos movimentos do Financeiro que foram contabilizadas pela contabilização do Financeiro, Baixa, Movimentação Bancária, Renegociação e Juros (TCBINT.ORIGEM = F', 'B', 'M', 'R', 'J’);

**(1)** Para os registros referentes as movimentações do Imobilizado, a busca da conta será conforme a Contabilização que ocorreu no Produto ou no Bem em questão.

### Plano de Contas

Na tela do Plano de Contas (Contabilidade>Cadastros), aba **"Geral"**, foi criado o campo **"Natureza para EFD",** no qual para a conta a ser gerada no arquivo, se faz necessário a configuração da Natureza. 

![Imagem 11: Na tela do Plano de Contas (Contabilidade>Cadastros), aba "Geral" , foi criado o campo "Natureza para EFD", no qual…](https://ajuda.sankhya.com.br/hc/article_attachments/16199399455383)

**(1)** Foram criadas 13 Naturezas para EFD, sendo elas:

01- Receita de vendas, Receitas prestação serviços, Receitas financeiras, Receitas não operacionais;

02- Receitas de vendas não tributadas;

03- Receita de Fretes, Receita de transportes rodoviário de cargas;

04- Custos de Produtos/Serviços prestados por pessoa jurídica;

05- Custos com transportes;

06- Despesas Diversas;

07- Despesas de fretes contratados e despesas de comercialização;

08- Estoques, Matéria prima e material de embalagem;

09- Aquisições de bens para revenda, aquisições de insumos para industrialização;

10- Encargos de depreciação do período, encargos de amortização do período, etc;

11- Máquinas e Equipamentos do Ativo Imobilizado, ativo fixo, etc;

12- Despesas de Aplicações Financeiras; Despesas Financeiras (Juros/Multas);

13- Receitas de Aplicações Financeiras; Receitas Financeiras (Juros/Multas).

**(1)** Para os registros **'A170', 'C170', 'C191', 'C195', 'C396', 'C481', 'C485', 'C501', 'C505', 'F100\_NOTA', 'F100\_FINANCEIRO'**

Lista de Naturezas utilizadas para busca da Conta Contábil:

01- Receita de vendas, Receitas prestação serviços, Receitas financeiras, Receitas não operacionais;

02- Receitas de vendas não tributadas;

03- Receita de Fretes, Receita de transportes rodoviário de cargas;

04- Custos de Produtos/Serviços prestados por pessoa jurídica;

06- Despesas Diversas;

07- Despesas de fretes contratados e despesas de comercialização;

08- Estoques, Matéria prima e material de embalagem;

09- Aquisições de bens para revenda, aquisições de insumos para industrialização.

**(1)** Para os registros **'C175', 'C181', 'C185', 'C381', 'C385', 'C491', 'C495', 'C810', 'C870'**

Lista de Naturezas utilizadas para busca da Conta Contábil:

01- Receita de vendas, Receitas prestação serviços, Receitas financeiras, Receitas não operacionais.

02- Receitas de vendas não tributadas.

**(1)** Para os registros 'D100', 'D101', 'D105'

Lista de Naturezas utilizadas para busca da Conta Contábil:

03- Receita de Fretes, Receita de transportes rodoviário de cargas.

05- Custos com transportes;

06- Despesas Diversas;

07- Despesas de fretes contratados e despesas de comercialização;

08- Estoques, Matéria prima e material de embalagem;

09- Aquisições de bens para revenda, aquisições de insumos para industrialização.

11- Máquinas e Equipamentos do Ativo Imobilizado, ativo fixo, etc.

**(1)** Para os registros **'D201', 'D205', 'D601', 'D605'**

Lista de Naturezas utilizadas para busca da Conta Contábil:

03- Receita de Fretes, Receita de transportes rodoviário de cargas.

**(1)** Para os registros  **'D501', 'D505'**

Lista de Naturezas utilizadas para busca da Conta Contábil:

06- Despesas Diversas;

07- Despesas de fretes contratados e despesas de comercialização;

**(1)** Para os registros  **'F500', 'F510', 'F525', 'F550', 'F560', '1900'**

Lista de Naturezas utilizadas para busca da Conta Contábil:

01- Receita de vendas, Receitas prestação serviços, Receitas financeiras, Receitas não operacionais.

02- Receitas de vendas não tributadas.

03- Receita de Fretes, Receita de transportes rodoviário de cargas.

**(1)** Para os registros  **'F100\_MULTA', 'F100\_JURO', 'F100\_DESCONTO'**

Lista de Naturezas utilizadas para busca da Conta Contábil:

01- Receita de vendas, Receitas prestação serviços, Receitas financeiras, Receitas não operacionais.

02- Receitas de vendas não tributadas.

06- Despesas Diversas;

07- Despesas de fretes contratados e despesas de comercialização;

12- Despesas de Aplicações Financeiras; Despesas Financeiras (Juros/Multas).

13- Receitas de Aplicações Financeiras; Receitas Financeiras (Juros/Multas).

**Observação:** Informe a conta contábil que será gerada no Registro F130 no campo **"Conta Contábil para EFD"** (tela Cadastro de Produtos, aba Impostos).

O registro 0500 será gerado conforme a configuração do [Cadastro de Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116393-Plano-de-Contas) da Empresa que estiver gerando [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es). Caso sejam gerados os registros das filiais no arquivo, também será gerado o plano de contas das filiais.

Só serão geradas as contas contábeis que foram geradas nos registros do arquivo.

### Geração do Registro 0600

Esse registro só será gerado para as empresas que realizam a busca da conta contábil pela "Contabilização". Sendo que a contabilização dos movimentos deverá ser por Centro de Resultado.

Para as empresas que efetuam a geração da conta contábil de forma fixa, não será gerado este registro.

###

### Observações Importantes

![Imagem 12: Os registros que apresentarem a conta contábil sem configuração, serão gravados no log de erro, ao gerar o arquivo.](https://ajuda.sankhya.com.br/hc/article_attachments/16199399442327) Os registros que apresentarem a conta contábil sem configuração, serão gravados no log de erro, ao gerar o arquivo. 

 O arquivo de log tem o mesmo nome do arquivo gerado, porém sua extensão é ".erro". Veja um exemplo:

"REGISTRO: A170. NUNOTA: 475701. SEQUENCIA: 1. ORIGEM: E. Conta Contábil está vazia.".

Deste modo, deve-se acessar o registro em questão e verificar a contabilização do documento de origem. Como também, analisar as configurações que foram definidas na busca da conta contábil.

![Imagem 13: Na geração da conta contábil nos registros EFD - Contribuições , deve-se informar o código da Conta Contábil credora ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16199405878807) Na geração da conta contábil nos registros EFD - Contribuições, deve-se informar o código da Conta Contábil credora ou devedora principal. Tem-se como conta principal aquela que recebeu maior valor na contabilização da operação.

![Imagem 14: Será enviado no arquivo EFD - Contribuições o plano de contas da empresa, somente daquelas contas que obtiveram…](https://ajuda.sankhya.com.br/hc/article_attachments/16199405883671) Será enviado no arquivo EFD - Contribuições o plano de contas da empresa, somente daquelas contas que obtiveram registros no arquivo. Assim, as empresas que entregam o ECD - Escrituração Contábil Digital devem informar as mesmas contas contábeis de forma que seja enviado o mesmo plano de contas.

![Imagem 15: Na geração do EFD Contribuições, quando se tratar de uma empresa com várias filiais, o sistema irá verificar se cada…](https://ajuda.sankhya.com.br/hc/article_attachments/16199399448599) Na geração do EFD Contribuições, quando se tratar de uma empresa com várias filiais, o sistema irá verificar se cada filial está configurada com o mesmo Tipo de Conta Contábil para EFD da matriz. Caso não estejam, será emitida a seguinte mensagem:

"As empresas filiais da matriz X não possuem a mesma configuração para o campo Tipo da Conta Contábil para EFD e isso poderá impedir que o sistema busque corretamente as contas do arquivo. Deseja continuar?"

Optando-se por sim, dá-se continuidade na geração mantendo o risco de ocorrer a busca incorreta das contas. Ao indicar que não se deseja continuar, será necessário padronizar nas Preferências da Empresa, aba **"EFD – Escrituração Fiscal Digital"**, a configuração do campo **"Tipo de Conta Contábil para EFD"** para todas as filiais.

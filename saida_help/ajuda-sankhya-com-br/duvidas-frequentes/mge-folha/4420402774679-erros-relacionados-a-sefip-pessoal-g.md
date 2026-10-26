---
id: "4420402774679"
titulo: "Erros relacionados à SEFIP  - Pessoal G"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4420402774679-Erros-relacionados-%C3%A0-SEFIP-Pessoal-G"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:36:33Z"
rotulos: ["Ocorrências", "Pessoal", "#validadoAnaLucia", "Folha de Pagamento", "SEFIP", "Configuração Funcionários", "Erro na variável \"varRecolComplementar\"", "SEFIP sem dados a processar", "Autônomo não na SEFIP", "Erro"]
---

# Erros relacionados à SEFIP  - Pessoal G

#### ![Imagem 1: Erro na atualização da variável "varRecolComplementar"](https://ajuda.sankhya.com.br/hc/article_attachments/42310326376215) Erro na atualização da variável "varRecolComplementar"

Erro ocorre ao gerar o arquivo SEFIP: **Conexão > Arquivo para Sefip > Processamento**

**Possível Solução**:

Use o layout da Sefip. Caso não saiba como fazer, siga as orientações do artigo abaixo:

[Como baixar e importar Layout's de Conexão (RAIS, SEFIP, DIRF-Pessoa Física, CAGED, GRRF) para o MGEPessoal? – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043729794-Como-baixar-e-importar-Layout-s-de-Conex%C3%A3o-RAIS-SEFIP-DIRF-Pessoa-F%C3%ADsica-CAGED-GRRF-para-o-MGEPessoal-)

#### ![Imagem 2: Já existe o mesmo PIS/PASEP/CI cadastrado com Código de Ocorrência que exige Múltiplos Vínculos](https://ajuda.sankhya.com.br/hc/article_attachments/42310326378263) Já existe o mesmo PIS/PASEP/CI cadastrado com Código de Ocorrência que exige Múltiplos Vínculos

Ocorre quando o funcionário é demitido e contratado no mesmo mês.

**Exemplo:** o Jovem aprendiz  passou a CLT, neste caso ele é levado duas vezes no arquivo sendo que nas duas deve estar com um múltiplo vinculo = 05, na aba **"Admissão"** dados p/FGTS campo **"Tabela"** ocorrência FGTS. 

**Possível Solução**:

Realize o ajuste no cadastro do empregado.

![Imagem 3: Realize o ajuste no cadastro do empregado.](https://ajuda.sankhya.com.br/hc/article_attachments/15751430769943)

#### ![Imagem 4: Cliente questiona diferença no valor INSS entre SEFIP e Resumo:](https://ajuda.sankhya.com.br/hc/article_attachments/42310326379031) Cliente questiona diferença no valor INSS entre SEFIP e Resumo:

Nestes casos, o erro geralmente está em algum evento ou funcionário com base incorreta, para conferência o Usuário tem que gerar o resumo da Folha e o arquivo SEFIP RE e confrontar cada funcionário verificando as bases de cálculo para identificar em qual ocorre a diferença para a devida tratativa do SD. 

#### ![Imagem 5: Ao gerar a SEFIP apresenta mensagem "Não existem dados a serem processados"](https://ajuda.sankhya.com.br/hc/article_attachments/42310326380183) Ao gerar a SEFIP apresenta mensagem "Não existem dados a serem processados"

**Possível Solução**:

**(1)** Essa mensagem está relacionada ao cadastro do funcionário, no qual provavelmente deve faltar alguma informação de dados cadastrais, como dados pessoais ou de endereço.

**(1)** Falta de confirmação do cálculo.

####

#### ![Imagem 6: Base de Cálculo 13º Salário Previdência Social](https://ajuda.sankhya.com.br/hc/article_attachments/42310326380695) Base de Cálculo 13º Salário Previdência Social

Referente à competência do movimento deve ser informada para trabalhadores com movimentação definitiva (exceto rescisão por justa causa por iniciativa do empregador) dentro do mês competência. 

Este erro ocorre pois quando se tem cálculo de 13° salário na rescisão e o funcionário tem menos de 15 dias trabalhados no ano, **(ocorre mais no mês de janeiro ou em situações de afastamento)** ou em casos nos quais o funcionário foi admitido no mês e no mesmo mês foi desligado com menos de 15 dias e tem pagamento de 13º salário. Neste caso, deve-se analisar o cálculo da rescisão, se realmente é devida a verba proveniente do 13º salário. 

**Observação:** como paliativo é usual pagar tudo junto com a remuneração sem 13° salário.

Isso é ajustado dentro do app SEFIP, devido a SEFIP não reconhecer a  verba de 13° sem o funcionário ter 15 dias ou mais . A orientação acima  pode ser passada como opção, porém deixando claro que **não se trata de erro do sistema e sim como a SEFIP entende o evento.**

#### ![Imagem 7: Remuneração Base de Cálculo da Contribuição Previdenciária só deve ser informada quando houver movimentação por O1, O2…](https://ajuda.sankhya.com.br/hc/article_attachments/42310342259863) Remuneração Base de Cálculo da Contribuição Previdenciária só deve ser informada quando houver movimentação por O1, O2 , R, Z2, Z3 e Z4 ou Registro Complementar para FGTS.

Esse erro ocorre quando o funcionário tem alguma situação de afastamento e não leva o registro 32 referente aos dados da movimentação, normalmente ocorre quando o usuário está gerando a SEFIP de uma referência específica em outra referência.

**Possível Solução**:

Neste caso, alterando a referência do menu arquivo > empresas resolve.

![Imagem 8: Neste caso, alterando a referência do menu arquivo > empresas resolve.](https://ajuda.sankhya.com.br/hc/article_attachments/15751573828375)

#### ![Imagem 9: Autônomo não está indo para SEFIP](https://ajuda.sankhya.com.br/hc/article_attachments/42310342261143) Autônomo não está indo para SEFIP

Na maioria das vezes está relacionado ao cadastro do Autônomo.

**Possível Solução**:

Serão necessárias algumas conferências:

**(1)** Na aba **"Admissão"** > Dados Gerais, preencha o campo **"Vínculo"** com a opção Autônomo.

![Imagem 10: (1) Na aba "Admissão" > Dados Gerais, preencha o campo "Vínculo" com a opção Autônomo.](https://ajuda.sankhya.com.br/hc/article_attachments/15751619310103)

**(1)** Na aba Admissão > Dados p/ FGTS, preencha o campo **"Tabela de categoria FGTS"** com a opção correta de acordo com o tipo de acordo.

![Imagem 11: (1) Na aba Admissão > Dados p/ FGTS, preencha o campo "Tabela de categoria FGTS" com a opção correta de acordo com o…](https://ajuda.sankhya.com.br/hc/article_attachments/15751599041559)

Estando correto, analise a aba **"Histórico"**, ainda na tela de funcionários, se o histórico gravado referente a essa competência ficou com os dados corretos:

![Imagem 12: Estando correto, analise a aba "Histórico" , ainda na tela de funcionários, se o histórico gravado referente a essa…](https://ajuda.sankhya.com.br/hc/article_attachments/15751644766615)

Caso tenha gravado alguma informação incorreta, ajuste a tabela **TFPHFU,** pois após gravada a informação não é possível alterar.

#### ![Imagem 13: Erro SEFIP 100304 - Dedução do salário-maternidade só pode ser informada a partir da competência 09/2013, quando tiver…](https://ajuda.sankhya.com.br/hc/article_attachments/42310326385047) Erro SEFIP 100304 - Dedução do salário-maternidade só pode ser informada a partir da competência 09/2013, quando tiver pelo menos um trabalhador com movimentação Q1 ou Q3. Para competências anteriores à 06/2000 a data de movimentação deve ser anterior à 20/11/1999.

Erro muito comum e está relacionado ao cadastro do menu lançamento/registro de ocorrências que devem ser analisadas as informações da ocorrência da funcionária com afastamento por licença gestante. Pois este erro ocorre quando existe informações de valores de licença gestante no arquivo e não há funcionária com dados de movimentação para essa situação.

**Possível Solução**:

Verifique na tela de **"Cadastro de Funcionário"**, aba **"Afastamento"**, se a funcionária está como afastada no sistema, pois só irá gerar a movimentação se estiver afastada

![Imagem 14: Verifique na tela de "Cadastro de Funcionário" , aba "Afastamento" , se a funcionária está como afastada no sistema,…](https://ajuda.sankhya.com.br/hc/article_attachments/15751757303191)

#### ![Imagem 15: Não gera a SEFIP complementar](https://ajuda.sankhya.com.br/hc/article_attachments/42310342264087) Não gera a SEFIP complementar

Primeiro, confira se a folha complementar dissídio está confirmada, verificando o resumo da folha ou a tabela TFPFOL com TIPFOLHA = 'O' gravada. Em seguida, na tela de processamento SEFIP informe o cod recolhimento = 650 e o código sindicato. 

#### ![Imagem 16: 320500 Tipo de Inscrição do Tomador/Obra difere do campo correspondente do Registro 20. Preencher o campo com Tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/42310326389527) 320500 Tipo de Inscrição do Tomador/Obra difere do campo correspondente do Registro 20. Preencher o campo com Tipo de Inscrição do Tomador/Obra igual ao campo correspondente do Registro 20 anterior.

Erro muito comum e está relacionado ao movimento de Tomadores de serviço quando o Cliente gerar a SEFIP com cod movimentação = 150 ou 155.

**Possível Solução**:

Para identificar o erro o usuário deverá avaliar:

**(1)** Na tela Avançado > Registro fiscal campo **"Inscrição"**:

![Imagem 17: (1) Na tela Avançado > Registro fiscal campo "Inscrição" :](https://ajuda.sankhya.com.br/hc/article_attachments/15751779586711)

**(1)** Em seguida, o menu Arquivo > empresas campo **"Reg. Fiscal Apro/Guia"** se está coerente com o cadastro Fiscal:

![Imagem 18: (1) Em seguida, o menu Arquivo > empresas campo "Reg. Fiscal Apro/Guia" se está coerente com o cadastro Fiscal:](https://ajuda.sankhya.com.br/hc/article_attachments/15751804982551)

**(1)** No menu Arquivo > Parceiros, verifique se o parceiro referente ao Tomador está com cod inscrição CEI correto:

![Imagem 19: (1) No menu Arquivo > Parceiros, verifique se o parceiro referente ao Tomador está com cod inscrição CEI correto:](https://ajuda.sankhya.com.br/hc/article_attachments/15751790031639)

**(1)** Em seguida, localize um funcionário que tenha alocação em tomador, pelo menu Lançamento > Movimentação de tomadores de serviço e analise se a alocação está correta.

![Imagem 20: (1) Em seguida, localize um funcionário que tenha alocação em tomador, pelo menu Lançamento > Movimentação de tomadores…](https://ajuda.sankhya.com.br/hc/article_attachments/12632080101911)

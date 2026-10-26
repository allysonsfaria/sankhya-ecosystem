---
id: "4412602452887"
titulo: "Conﬁgurações para o evento R2060 da EFD-Reinf (CPRB)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4412602452887-Con%EF%AC%81gura%C3%A7%C3%B5es-para-o-evento-R2060-da-EFD-Reinf-CPRB"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-08-17T14:42:46Z"
rotulos: ["Alíquotas", "Configuração", "Impostos", "EFD", "#validadoLauraPerez", "Configurações Necessárias", "Procedimentos para Registros", "EFD-Reinf e Evento R-2060", "Reinf", "CPRB"]
---

# Conﬁgurações para o evento R2060 da EFD-Reinf (CPRB)

### ![Imagem 1: Introdução](https://ajuda.sankhya.com.br/hc/article_attachments/16172361338903) Introdução

Considere que uma empresa privada de **“Tecnologia de Informação e Tecnologia da** **Informação** **e** **Comunicação”** está obrigada, desde 01 de janeiro do corrente ano, a entregar a Escrituração Fiscal Digital de Retenções e Outras Informações Fiscais (EFD-Reinf), que é um dos módulos do Sistema Público de Escrituração Digital - SPED.

Ela presta serviço de **“Análise** **e** **Desenvolvimento** **de** **Sistemas”** para os seus parceiros, um deles é a empresa **“FOX Varejo e Eletrônicos Ltda”**, e este serviço está sujeito a retenção da Contribuição Previdenciária sobre a Receita Bruta (CPRB), a uma alíquota de **“4,5%”** conforme “**Tabela 5.1.1 Contribuição Previdência sobre a Receita Bruta”,** disponível no [site](http://sped.rfb.gov.br/arquivo/show/1684) do SPED.

Além da prestação de serviços, ela comercializa equipamentos e suprimentos de informática. Um dos produtos mais vendidos é o **“Teclado para computadores”**, que é bastante solicitado pelo seu parceiro **“TECLOG Escola Proﬁssionalizante Ltda”**. A atividade de Comércio varejista especializado em equipamentos e suprimentos de informática é sujeita à CPRB, por este motivo, a empresa deve realizar a retenção desta contribuição, a uma alíquota de **“2,5%”**.

Esta retenção diz respeito ao evento **“R-2060 - Contribuição Previdenciária sobre a Receita** **Bruta** **-** **CPRB”** da Reinf, referente a desoneração da Folha, onde as empresas começaram a ter a Contribuição Previdenciária calculada sobre a Receita Bruta, e não mais pela Folha de Pagamento – conforme Medida Provisória 540/2011, convertida na Lei 12.546/2011.

Com base nestas informações, vejamos a seguir as conﬁgurações necessárias para geração deste evento.

### Imagem 2: Conﬁgurações para o evento R2060 da EFD-Reinf (CPRB) Conﬁgurações para o evento R2060 da EFD-Reinf (CPRB)

Além das conﬁgurações essenciais, para gerar o Evento R2060 da EFD-Reinf daremos atenção especial, às **“Preferências da Empresa”**, aos cadastros de **“Cód. Atividades** **Produtos** **e** **Serviços** **p/** **CPRB”**, **“Produtos”** e **“Serviços”**.

**2.1 Comercial » Preferências » Empresa**

Acesse a tela **"Empresa".**

**2.1.1 Aba EFD- Reinf**

Na aba **‘EFD** **-** **Reinf’** efetua-se parte das conﬁgurações dos eventos pertinentes a geração da EFD-Reinf. A marque a opção **“Desoneração** **da** **Folha** **-** **CPRB**”, já que a empresa realiza a Contribuição Previdenciária sobre a Receita Bruta (CPRB), como apresentado em nosso case exemplo.

![Imagem 3: Na aba ‘EFD - Reinf’ efetua-se parte das conﬁgurações dos eventos pertinentes a geração da EFD-Reinf. A marque a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/16172361360407)

Clique em **"salvar".**

**2.1.2 Aba Reintegra Previdência**

As conﬁgurações da aba **‘Reintegra** **Previdência’** tem o objetivo de identiﬁcar a alíquota e demais informações da Contribuição Previdenciária sobre a Receita Bruta (CPRB) para geração do **Evento** **R-2060** da EFD-Reinf.

Esta aba possibilita a inserção de apenas um código e uma alíquota. Deste modo, para empresas que tem mais de uma alíquota, como nosso exemplo, faz-se necessária a utilização da tela **“Cód. Atividades Produtos e Serviços p/** **CPRB”**, que veremos em seguida.

Assim sendo, não se realiza nenhuma conﬁguração nesta aba.

| **Saiba mais:**  A Contribuição Previdenciária sobre a Receita Bruta (CPRB) é uma contribuição social de natureza tributária destinada a custear a previdência social e de competência da União Federal. Incide sobre a receita bruta de empresas que atendem aos parâmetros deﬁnidos pela Lei 12.546, relacionados a atividades, setores e produtos especíﬁcos. A tabela com as informações pertinentes aos códigos, alíquotas e descrição de atividades está disponível no [Portal do Sistema](http://sped.rfb.gov.br/arquivo/show/2773) [Público de Escrituração Digital.](http://sped.rfb.gov.br/arquivo/show/2773) |
| --- |

####

#### 2.2 Comercial » Arquivo » Cadastros » Cód. Atividades Produtos e Serviços p/ CPRB

Acesse a tela **“Cod.** **Atividades** **Produtos** **e** **Serviços** **p/** **CPRB”**. Esta rotina permite efetuar a inserção dos dados para a geração do **Evento** **R-2060** da EFD-Reinf. Clique em **“Novo”** para cadastrar a primeira atividade, que é a prestação de serviço de **“Análise** **e** **Desenvolvimento** **de** **Sistemas”**. Em **“Cód.** **Atividade** **(Prest.** **Serviços** **e** **Produtos)”** preencha com o código do serviço prestado **“00000025”**.

![Imagem 4: Acesse a tela “Cod. Atividades Produtos e Serviços p/ CPRB” . Esta rotina permite efetuar a inserção dos dados para a…](https://ajuda.sankhya.com.br/hc/article_attachments/16172374100759)

No campo **“Data** **Inicial”** informe a data de início de validade da alíquota sobre o referido Código de Atividade.

![Imagem 5: No campo “Data Inicial” informe a data de início de validade da alíquota sobre o referido Código de Atividade.](https://ajuda.sankhya.com.br/hc/article_attachments/16172374106391)

Deixe o campo **“Data** **Final”** sem informação, pois este se refere ao término da vigência da atividade e da alíquota de tributação da previdência.

![Imagem 6: Deixe o campo “Data Final” sem informação, pois este se refere ao término da vigência da atividade e da alíquota de…](https://ajuda.sankhya.com.br/hc/article_attachments/16172374112279)

No campo **"Código** **de** **Recolhimento",** preencha com o código **“2991”** utilizado como código de pagamento da CPRB para emissão da guia e geração da DCTF.

![Imagem 7: No campo "Código de Recolhimento", preencha com o código “2991” utilizado como código de pagamento da CPRB para emissão…](https://ajuda.sankhya.com.br/hc/article_attachments/16172374122519)

| **Saiba mais:**  Existem dois códigos de arrecadação especíﬁcos para o pagamento por meio de DARF da CPRB, que são: 2985 - Contribuição Previdenciária Sobre Receita Bruta - Art. 7º da Lei 12.546/2011; e 2991 - Contribuição Previdenciária Sobre Receita Bruta - Art. 8º da Lei 12.546/2011. |
| --- |

Em **"Alíquota"** preencha com o percentual aplicável à empresa, de acordo com sua atividade. Para ilustrar, informe **“4,5%”**.

![Imagem 8: Em "Alíquota" preencha com o percentual aplicável à empresa, de acordo com sua atividade. Para ilustrar, informe “4,5%”…](https://ajuda.sankhya.com.br/hc/article_attachments/16172361389719)

E por último, no campo **“Desc.** **Atividade** **(Prest.** **Serviços** **e** **Produtos)”** informe a descrição da atividade como “**Assessoria** **e** **Consultoria** **em** **Informática”**.

![Imagem 9: E por último, no campo “Desc. Atividade (Prest. Serviços e Produtos)” informe a descrição da atividade como “…](https://ajuda.sankhya.com.br/hc/article_attachments/16172374131991)

Clique em **“Salvar”**. Novamente, clique **“Novo”** para cadastrar a atividade **“Comércio** **varejista** **especializado** **de** **equipamentos** **e** **suprimentos** **de** **informática”**. Em **“Cód.** **Atividade** **(Prest.** **Serviços** **e** **Produtos)”** preencha com o código da atividade **“00100040”**.

![Imagem 10: Clique em “Salvar” . Novamente, clique “Novo” para cadastrar a atividade “Comércio varejista especializado de…](https://ajuda.sankhya.com.br/hc/article_attachments/16172374137495)

No campo **“Data** **Inicial”** informe a data de início de validade da alíquota sobre o referido Código de Atividade.

![Imagem 11: No campo “Data Inicial” informe a data de início de validade da alíquota sobre o referido Código de Atividade.](https://ajuda.sankhya.com.br/hc/article_attachments/16172374141975)

Deixe o campo **“Data** **Final”** sem informação, pois este se refere ao término da vigência da atividade e da alíquota de tributação da previdência.

![Imagem 12: Deixe o campo “Data Final” sem informação, pois este se refere ao término da vigência da atividade e da alíquota de…](https://ajuda.sankhya.com.br/hc/article_attachments/16172361413527)

No campo **"Código** **de** **Recolhimento"** preencha com o código **“2991”** utilizado como código de pagamento.

![Imagem 13: No campo "Código de Recolhimento" preencha com o código “2991” utilizado como código de pagamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16172374152727)

Em **"Alíquota",** preencha com o percentual aplicável à empresa, de acordo com sua atividade. Para ilustrar, informe **“2,5%”**.

![Imagem 14: Em "Alíquota", preencha com o percentual aplicável à empresa, de acordo com sua atividade. Para ilustrar, informe…](https://ajuda.sankhya.com.br/hc/article_attachments/16172361432855)

E por último, no campo **“Desc.** **Atividade** **(Prest.** **Serviços** **e** **Produtos)”** informe a descrição desta atividade como **“Comércio** **varejista** **especializado** **de** **equipamentos** **e** **suprimentos** **de** **informática”**.

![Imagem 15: E por último, no campo “Desc. Atividade (Prest. Serviços e Produtos)” informe a descrição desta atividade como…](https://ajuda.sankhya.com.br/hc/article_attachments/16172374163607)

Clique em **"salvar".**

#### 2.3 Conﬁgurações » Cadastros » Produtos » Serviços

Acesse a tela de **“Serviço”** e localize o serviço **“Análise e Desenvolvimento de** **Sistemas”**.

**2.3.1 Aba impostos**

Na aba **"Impostos"**, marque **"Enquadrado** **no** **Reintegra/Prev."** para indicar que este serviço será inserido na geração do evento R-2060.

![Imagem 16: Na aba "Impostos" , marque "Enquadrado no Reintegra/Prev." para indicar que este serviço será inserido na geração do…](https://ajuda.sankhya.com.br/hc/article_attachments/16172361445911)

Aponte, no campo **"Cód. Atividade CPRB (Reintegra/Prev.)",** o código da atividade deste serviço, cadastrado na tela **“Cód. Atividades Produtos e** **Serviços** **p/** **CPRB”**.

![Imagem 17: Aponte, no campo "Cód. Atividade CPRB (Reintegra/Prev.)", o código da atividade deste serviço, cadastrado na tela “Cód.…](https://ajuda.sankhya.com.br/hc/article_attachments/16172590333847)

####

#### 2.4 Conﬁgurações » Cadastros » Produtos

Acesse a tela de **“Produtos”** e localize o produto **“Teclado** **para** **Computadores”.**

**2.4.1 Aba Geral**

Na aba **"Geral"**, no campo **“NCM”,** veriﬁque se o código para este produto, “**84716052”,** está devidamente conﬁgurado.

![Imagem 18: Na aba " Geral" , no campo “NCM”, veriﬁque se o código para este produto, “ 84716052”, está devidamente conﬁgurado.](https://ajuda.sankhya.com.br/hc/article_attachments/16172590341655)

**2.4.2. Aba impostos**

Na aba ‘Impostos’, marque **"Enquadrado no Reintegra/Prev.",** para indicar que este produto será inserido na geração do evento R-2060.

![Imagem 19: Na aba ‘Impostos’, marque "Enquadrado no Reintegra/Prev.", para indicar que este produto será inserido na geração do…](https://ajuda.sankhya.com.br/hc/article_attachments/16172590348695)

Aponte, no campo **"Cód.** **Atividade** **CPRB** **(Reintegra/Prev.)",** o código da atividade relacionada a este produto.

![Imagem 20: Aponte, no campo "Cód. Atividade CPRB (Reintegra/Prev.)", o código da atividade relacionada a este produto.](https://ajuda.sankhya.com.br/hc/article_attachments/16172590360215)

| **Importante:**  Quando este campo encontrar-se sem informação, o sistema irá buscá-la no campo “NCM” do cadastro do produto. |
| --- |

Clique em **"Salvar".**

#### 2.5 Comercial » Arquivo » Cadastros » CFOP

Acesse a tela de **“CFOP”**. Nesta tela, deve-se conﬁgurar as CFOPs elencadas para gerar as informações para o evento R-2060. O campo **“Receita Bruta p/ EFD Contribuições”** indica o comportamento do cálculo da Receita Bruta sobre o tipo de operação. Tem-se neste campo as seguintes opções:

**(1)** “**Somar”**, para aqueles CFOPs que geram Receita Bruta;

**(1)** “**Subtrair”**, para aqueles CFOPs que diminuem a Receita Bruta;

**(1)** “**Não** **afetar”**, para os demais CFOPs.

![Imagem 21: (1) “ Não afetar” , para os demais CFOPs.](https://ajuda.sankhya.com.br/hc/article_attachments/16172589941783)

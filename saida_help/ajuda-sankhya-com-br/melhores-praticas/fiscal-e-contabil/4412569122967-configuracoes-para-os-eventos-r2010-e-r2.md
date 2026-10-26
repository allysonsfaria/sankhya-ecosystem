---
id: "4412569122967"
titulo: "Configurações para os eventos R2010 e R2020 da EFD-Reinf (Serviços)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4412569122967-Configura%C3%A7%C3%B5es-para-os-eventos-R2010-e-R2020-da-EFD-Reinf-Servi%C3%A7os"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:20:49Z"
rotulos: ["Configuração", "Construção Civil", "Serviços", "Impostos", "INSS", "#validadoLauraPerez", "Evento R-2010: Serviços Tomados", "Evento R-2020: Serviços Prestados", "Configurações de Serviços", "EFD-REINF"]
---

# Configurações para os eventos R2010 e R2020 da EFD-Reinf (Serviços)

## ![Imagem 1: Introdução](https://ajuda.sankhya.com.br/hc/article_attachments/16175106402199) Introdução

Para efeitos de ilustração, considere que uma empresa contratou um parceiro do ramo de construção civil para execução de determinado serviço no 2º andar do seu prédio, que encontra-se em reforma. Por se tratar de um serviço com cessão de mão de obra, ele tem incidência de INSS, calculado com alíquota de 11%, que deve ser retido na nota fiscal. Como o serviço executado coloca o trabalhador em exposição a agentes nocivos à sua saúde, o mesmo tem incidência adicional de INSS, com uma alíquota de 2%, e contribui para efeitos de aposentadoria especial de 25 anos.

Esta retenção é tratada no evento **“R-2010** **-** **Retenção** **Contribuição** **Previdência** **-** **Serviços** **Tomados”**, que comporta as informações relativas aos serviços contratados, realizados mediante cessão de mão de obra ou empreitada, com as correspondentes informações sobre as retenções previdenciárias.

Considere que esta mesma empresa também presta um serviço executado mediante cessão de mão-de-obra, sobre o qual o valor do INSS deve ser retido a uma alíquota de 11% na nota fiscal. Por se tratar também de uma atividade com exposição a agente nocivo, o mesmo tem incidência adicional de INSS, com uma alíquota de 2%, para efeitos de aposentadoria especial de 25 anos.

Esta retenção é tratada no evento **“R-2020 - Retenção Contribuição Previdência - Serviços** **Prestados”**, onde são apresentadas as informações sobre a retenção referente aos serviços prestados pela empresa com cessão de mão de obra ou empreitada, sobre os quais é calculada a retenção do INSS.

Com base nestas informações, para a geração e entrega destes eventos, além das configurações básicas para a entrega da Reinf, vejamos a seguir as configurações específicas relacionadas aos mesmos, que são realizadas nos cadastros de **“Lista** **de** **Serviços”**, **“Serviço”**, **“Parceiros”** e **“Impostos”**.

## ![Imagem 2: Configurações para os eventos R2010 e R2020 da EFD-Reinf](https://ajuda.sankhya.com.br/hc/article_attachments/16175107660439) Configurações para os eventos R2010 e R2020 da EFD-Reinf

### 2.1 Comercial » Arquivos » Cadastros » Lista de Serviços

Acesse a tela **“Lista de Serviços”** e localize o serviço **“07.02 - Execução, por administração...”.** Acione o campo **“Exige Cód. da Obra”** para que o serviço seja utilizado numa obra específica.

![Imagem 3: Acesse a tela “Lista de Serviços” e localize o serviço “07.02 - Execução, por administração...”. Acione o campo “Exige…](https://ajuda.sankhya.com.br/hc/article_attachments/16175107669527)

Clique em **“Salvar”**.

### 2.2 Configurações » Cadastros » Produtos » Serviço

#### 2.2.1 Serviço tomado

Acesse a tela de **“Serviço”** e localize o serviço **“Serviço** **Limpeza de** **Vidros”**.

**2.2.1.1 Aba impostos**

Na aba **‘Impostos’**, configure o campo **“Tipo** **de** **INSS** **Especial”** com a opção **“INSS 25 anos”**, pois estamos tratando de uma atividade com exposição a agente nocivo.

![Imagem 4: Na aba ‘Impostos’ , configure o campo “Tipo de INSS Especial” com a opção “INSS 25 anos” , pois estamos tratando de uma…](https://ajuda.sankhya.com.br/hc/article_attachments/16175106418583)

Informe no campo **“%** **INSS** **Especial”** o percentual de **“2%”**.

![Imagem 5: Informe no campo “% INSS Especial” o percentual de “2%” .](https://ajuda.sankhya.com.br/hc/article_attachments/16175106424727)

No campo **“Tipo** **de** **Serviço”** deve se indicar a classificação da cessão de mão de obra pertinente. Para o nosso exemplo, vamos usar a opção **“702 -** **Execução, por administração, empreitada ou subempreitada, de obras de** **construção civil, hidráulica ou elétrica e de outras obras semelhantes,** **inclusive sondagem, perfuração de poços, escavação, drenagem e irrigação,** **terraplanagem,** **pavimentação,** **conc”**.

![Imagem 6: No campo “Tipo de Serviço” deve se indicar a classificação da cessão de mão de obra pertinente. Para o nosso exemplo,…](https://ajuda.sankhya.com.br/hc/article_attachments/16175106428439)

Configure o campo **“CNAE”** com o código correspondente ao serviço.

![Imagem 7: Configure o campo “CNAE” com o código correspondente ao serviço.](https://ajuda.sankhya.com.br/hc/article_attachments/16175107699479)

No campo **“Classificação** **Cessão** **M.** **d.** **Obra”** indique a opção aplicável**.**

![Imagem 8: No campo “Classificação Cessão M. d. Obra” indique a opção aplicável .](https://ajuda.sankhya.com.br/hc/article_attachments/16175107703063)

Como no nosso exemplo o serviço contrato foi para a execução de parte de uma obra, aponte, no campo **“Obra de Construção Civil”**, a opção **“2 -** **Empreitada** **Parcial”.** Clique em **“Salvar”**.

| **Importante:**  Estas mesmas configurações do cadastro de ‘Serviço’, para os serviços tomados, são aplicadas para os serviços prestados.  A diferença entre os dois é que o evento R-2020 - Retenção Contribuição - Previdenciária - Serviços Prestados se dá pelas retenções de INSS sobre os serviços prestados com a cessão de mão de obra ou empreitada. Por isto, estes eventos se diferenciam somente se o serviço é compra (tomado) ou venda (prestado). |
| --- |

#### 2.2.2 Serviço prestado

Na tela de **“Serviço”**, localize o serviço prestado pela empresa.

**2.2.2.1 Aba impostos**

Na aba **‘Impostos’**, marque o campo **“Tipo de INSS Especial”** com a opção **“INSS 25 anos”**, pois estamos tratando de uma atividade com exposição ao agente nocivo, da mesma forma que fizemos para o serviço contratado.

![Imagem 9: Na aba ‘Impostos’ , marque o campo “Tipo de INSS Especial” com a opção “INSS 25 anos” , pois estamos tratando de uma…](https://ajuda.sankhya.com.br/hc/article_attachments/16175107708951)

Informe no campo **“%** **INSS** **Especial”** o percentual de **“2%”.**

![Imagem 10: Informe no campo “% INSS Especial” o percentual de “2%”.](https://ajuda.sankhya.com.br/hc/article_attachments/16175106448151)

No campo **“Tipo** **de** **Serviço”** indique a classificação da cessão de mão de obra pertinente. Neste caso, vamos usar a opção **“702 - Execução,** **por** **administração,** **empreitada** **ou** **subempreitada,** **de obras de** **construção civil, hidráulica ou elétrica e de outras obras semelhantes,** **inclusive sondagem, perfuração de poços, escavação, drenagem e** **irrigação,** **terraplanagem,** **pavimentação,** **conc”**.

![Imagem 11: No campo “Tipo de Serviço” indique a classificação da cessão de mão de obra pertinente. Neste caso, vamos usar a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/16175107719575)

Configure o campo **“CNAE”** com o código correspondente ao serviço prestado.

![Imagem 12: Configure o campo “CNAE” com o código correspondente ao serviço prestado.](https://ajuda.sankhya.com.br/hc/article_attachments/16175106458775)

Configure o campo **“Classificação** **Cessão** **M.** **d.** **Obra”** com a opção relacionada ao serviço.

![Imagem 13: Configure o campo “Classificação Cessão M. d. Obra” com a opção relacionada ao serviço.](https://ajuda.sankhya.com.br/hc/article_attachments/16175107732631)

Aponte, no campo **“Obra** **de** **Construção** **Civil”,** que trata-se de uma “**Empreitada** **Parcial”** em função da execução de uma única parte da obra.

![Imagem 14: Aponte, no campo “Obra de Construção Civil”, que trata-se de uma “ Empreitada Parcial” em função da execução de uma…](https://ajuda.sankhya.com.br/hc/article_attachments/16175106470935)

Clique em **“Salvar”**.
